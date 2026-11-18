#!/usr/bin/env python3
"""Mede um roteiro de YouTube e emite alertas. Não emite veredito.

Mede o que a skill roteiro-youtube diz que importa: duração falada, carga
percebida na abertura, distância até o primeiro pagamento da promessa, ligação
entre blocos (escada x catálogo), frases longas demais para falar, alegações que
precisam de fonte e posição do pedido de inscrição. Nada aqui decide qualidade.

Uso:
    python3 medir_roteiro.py roteiro.md --alertas
    python3 medir_roteiro.py roteiro.md --ppm 175 --pretty
    python3 medir_roteiro.py roteiro.md --marcadores "tipo assim,olha só"
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-’'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]+|[^.!?]+$")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")

# Marcadores de fala conversacional. São sinal positivo, não filler:
# "só que" abre o próximo passo e "porque" preserva causalidade.
# Acrescente os do seu perfil com --marcadores. Ver references/voz-e-oralidade.md.
MARCADORES_DE_VOZ = [
    "só que", "porque", "por exemplo", "pensa", "você não precisa",
    "como se fosse", "ou seja", "repara", "olha", "imagina",
]
FRASE_LONGA = 30  # palavras

# Conectores que ligam um bloco ao anterior. Bloco sem nenhum é candidato a catálogo.
LIGACAO_RE = re.compile(
    r"\b(?:só que|porque|por isso|mas|agora que|com isso|então|aí|"
    r"e é por isso|acontece que|o problema (?:é|disso)|isso significa|"
    r"depois disso|a partir daí|só que aí)\b",
    re.I,
)

# Sinais de que o espectador recebeu algo concreto.
PAGAMENTO_RE = re.compile(
    r"\b(?:por exemplo|olha (?:só|aqui|isso)|repara|vou (?:te )?mostrar|"
    r"na prática|isso significa|a diferença é|funciona assim|pensa (?:num|numa|em)|"
    r"aqui (?:ó|está|tá)|veja|imagina|não é (?:um|uma|o|a)|ao invés de)\b",
    re.I,
)

# Escopo anunciado como profundidade, ex.: "30 conceitos".
ESCOPO_RE = re.compile(
    r"\b(\d+)\s+(conceitos?|n[ií]veis?|blocos?|passos?|etapas?|partes?|"
    r"ferramentas?|m[óo]dulos?|aulas?)\b",
    re.I,
)

# Custo unitário: o que faz o escopo parecer barato.
CUSTO_UNITARIO_RE = re.compile(
    r"\b(?:cada um[a]? (?:em|leva|dura|com)|menos de um minuto|"
    r"em menos de \w+|cada bloco|cada etapa (?:leva|dura)|um por vez)\b",
    re.I,
)

# Jargão aproximado: siglas e CamelCase. Heurística, não linguística.
JARGAO_RE = re.compile(r"\b(?:[A-Z]{2,}|[A-Z][a-z]+[A-Z][A-Za-z]*)\b")

# Radicais de hype: pegam "absurdo", "absurdas", "insana", "incríveis"...
SUPERLATIVOS = (
    "incr[ií]ve", "absurd", "revolucion[aá]ri", "insan", "inacredit[aá]ve",
    "impressionant", "sensaciona", "brutal", "gigantesc", "espetacular",
    "surrea", "bizarr", "explodir", "m[aá]gic",
)

# Frases com cara de texto gerado por IA ou de anúncio.
CLICHES = (
    "você sabia que", "neste vídeo", "nesse vídeo vamos", "prepare-se", "prepara que",
    "mergulhar", "no mundo de hoje", "nos dias de hoje", "é aqui que a mágica",
    "sem mais delongas", "fica até o final", "não se esqueça de",
)

CTA_PATTERNS = {
    "inscricao": re.compile(r"\b(?:se inscrev|inscreva-se|inscreva)\w*", re.I),
    "comentario": re.compile(r"\bcomenta\w*|deixa nos comentários", re.I),
    "link": re.compile(r"\blink\b|descrição|comentário fixado", re.I),
    "compra": re.compile(r"\b(?:compre|assine|contrate|aproveite)\b", re.I),
}
COMERCIAL_RE = re.compile(
    r"patrocin|parceir|cupom|desconto|assinatura|utm", re.I
)
PERCENTUAL_RE = re.compile(r"\b\d{1,3}\s?%", re.I)


FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
METADADO_RE = re.compile(r"^\s*[-*]?\s*\*\*[^*]+:\*\*.*$", re.M)
CITACAO_RE = re.compile(r"^\s*>.*$", re.M)
TEMPO_RE = re.compile(r"⏱️\s*[\d:]+", re.M)
# Indicações de tela e rubricas não são fala: "(tela: ...)", "[TELA ...]".
TELA_RE = re.compile(r"\((?:tela|imagem|corte|b-roll|broll|grafismo|texto na tela)[^)]*\)|\[(?:tela|imagem|corte|b-roll|broll|grafismo|sfx|m[uú]sica)[^\]]*\]", re.I)
MARCA_BLOCO_RE = re.compile(r"^\s*\[([^\]]{1,60})\]\s*$", re.M)


def limpar(text):
    """Remove frontmatter, metadados e avisos. Mede narração, não cabeçalho."""
    text = FRONTMATTER_RE.sub("", text)
    # formato de entrega da skill: cabeçalho --- narração --- verificações e fontes
    partes = re.split(r"^\s*---\s*$", text, flags=re.M)
    if len(partes) >= 3:
        text = max(partes[1:-1], key=len)
    text = METADADO_RE.sub("", text)
    text = CITACAO_RE.sub("", text)
    text = TEMPO_RE.sub("", text)
    text = TELA_RE.sub("", text)
    text = MARCA_BLOCO_RE.sub(lambda m: "## " + m.group(1), text)   # [BLOCO 1 — x] vira título de unidade
    return text


def indice(match, text, total):
    antes = len(WORD_RE.findall(text[: match.start()]))
    return {
        "termo": match.group(0).strip(),
        "palavra": antes + 1,
        "percentual": round((antes / max(total, 1)) * 100, 1),
    }


def analisar_abertura(text, janela):
    palavras = WORD_RE.findall(text)
    abertura = " ".join(palavras[:janela])
    escopos = [
        {"numero": int(m.group(1)), "unidade": m.group(2).lower()}
        for m in ESCOPO_RE.finditer(abertura)
    ]
    tem_custo = bool(CUSTO_UNITARIO_RE.search(abertura))
    primeiro_pagamento = PAGAMENTO_RE.search(abertura)
    corte = primeiro_pagamento.start() if primeiro_pagamento else len(abertura)
    jargao = sorted(set(JARGAO_RE.findall(abertura[:corte])))
    return {
        "janela_palavras": min(janela, len(palavras)),
        "escopo_declarado": escopos,
        "custo_unitario_declarado": tem_custo,
        "jargao_antes_do_primeiro_concreto": jargao,
        "pagamento_dentro_da_abertura": bool(primeiro_pagamento),
    }


def analisar_unidades(text):
    """Divide por headings; sem headings, por parágrafos duplos."""
    linhas = text.splitlines()
    unidades, atual, titulo = [], [], None
    for linha in linhas:
        h = HEADING_RE.match(linha.strip())
        if h:
            if atual or titulo:
                unidades.append((titulo, "\n".join(atual)))
            titulo, atual = h.group(1).strip(), []
        else:
            atual.append(linha)
    if atual or titulo:
        unidades.append((titulo, "\n".join(atual)))

    if len(unidades) <= 1:
        blocos = [b for b in re.split(r"\n\s*\n", text) if b.strip()]
        unidades = [(None, b) for b in blocos]

    sem_ligacao, detalhe = [], []
    ultima_anterior = ""
    for i, (titulo, corpo) in enumerate(unidades):
        frases_u = [s.strip() for s in SENTENCE_RE.findall(corpo) if s.strip()]
        primeira = frases_u[0] if frases_u else ""
        # ligado se a primeira frase retoma o anterior OU se o bloco anterior terminou abrindo este (gancho no fim)
        ligado = bool(LIGACAO_RE.search(primeira)) or bool(LIGACAO_RE.search(ultima_anterior)) or ultima_anterior.endswith("?")
        ultima_anterior = frases_u[-1] if frases_u else ""
        rotulo = titulo or (primeira[:48] + "…" if len(primeira) > 48 else primeira)
        detalhe.append({"unidade": i + 1, "rotulo": rotulo, "ligada_a_anterior": ligado})
        if i > 0 and not ligado:
            sem_ligacao.append(rotulo)
    return {
        "total": len(unidades),
        "sem_ligacao_com_anterior": sem_ligacao,
        "detalhe": detalhe,
    }


def analisar(text, wpm, janela):
    palavras = WORD_RE.findall(text)
    total = len(palavras)
    frases = [s.strip() for s in SENTENCE_RE.findall(text) if s.strip()]

    pagamentos = [indice(m, text, total) for m in PAGAMENTO_RE.finditer(text)]
    abertura = analisar_abertura(text, janela)
    unidades = analisar_unidades(text)

    marcadores = {}
    baixo = text.lower()
    for termo in MARCADORES_DE_VOZ:
        n = len(re.findall(rf"(?<!\w){re.escape(termo)}", baixo))
        if n:
            marcadores[termo] = n

    supers = {}
    for radical in SUPERLATIVOS:
        achados = re.findall(rf"(?<!\w){radical}\w*", baixo)
        for a_ in achados:
            supers[a_] = supers.get(a_, 0) + 1

    ctas = {
        nome: [indice(m, text, total) for m in padrao.finditer(text)]
        for nome, padrao in CTA_PATTERNS.items()
    }
    ctas = {k: v for k, v in ctas.items() if v}

    repetidos = Counter(
        w.lower() for w in palavras
        if len(w) >= 7 and w.lower() not in MARCADORES_DE_VOZ
    )
    frequentes = [
        {"termo": t, "quantidade": n}
        for t, n in repetidos.most_common(15) if n >= 5
    ]

    longas = [
        {"frase": f[:90] + ("…" if len(f) > 90 else ""), "palavras": len(WORD_RE.findall(f))}
        for f in frases if len(WORD_RE.findall(f)) > FRASE_LONGA
    ]
    cliches = {}
    for termo in CLICHES:
        n = baixo.count(termo)
        if n:
            cliches[termo] = n

    alertas = []
    if longas:
        alertas.append(
            f"{len(longas)} frase(s) com mais de {FRASE_LONGA} palavras — difíceis de "
            "falar e de entender ouvindo. Primeira: \"" + longas[0]["frase"] + "\""
        )
    if cliches:
        alertas.append("Frases de anúncio ou de IA: " + ", ".join(cliches))
    if not pagamentos:
        alertas.append(
            "Nenhum marcador de pagamento concreto encontrado. "
            "O texto pode estar só explicando."
        )
    elif total >= 800 and pagamentos[0]["percentual"] > 15:
        alertas.append(
            f"Primeiro pagamento concreto só aos {pagamentos[0]['percentual']}% "
            "do roteiro. Antecipe a primeira demonstração ou exemplo."
        )
    elif total < 800 and pagamentos[0]["palavra"] > 120:
        alertas.append(
            f"Primeiro pagamento concreto na palavra {pagamentos[0]['palavra']}. "
            "Em trecho curto isso é indicativo, não conclusão."
        )
    if abertura["escopo_declarado"] and not abertura["custo_unitario_declarado"]:
        n = abertura["escopo_declarado"][0]
        alertas.append(
            f"Escopo anunciado como profundidade ('{n['numero']} {n['unidade']}') "
            "sem custo unitário. Isso aumenta a carga percebida."
        )
    if len(abertura["jargao_antes_do_primeiro_concreto"]) >= 3:
        alertas.append(
            "Três ou mais termos técnicos antes do primeiro concreto na abertura: "
            + ", ".join(abertura["jargao_antes_do_primeiro_concreto"][:6])
        )
    if unidades["total"] >= 4:
        proporcao = len(unidades["sem_ligacao_com_anterior"]) / (unidades["total"] - 1)
        if proporcao >= 0.6:
            alertas.append(
                f"{len(unidades['sem_ligacao_com_anterior'])} de "
                f"{unidades['total'] - 1} unidades começam sem ligação com a "
                "anterior. Candidato a catálogo — confirme lendo se a ordem "
                "pode ser embaralhada sem perda. Ruidoso em transcrições com "
                "capítulos automáticos."
            )
    if sum(supers.values()) >= 2:
        alertas.append("Superlativos empilhados: " + ", ".join(supers))
    percentuais = [indice(m, text, total) for m in PERCENTUAL_RE.finditer(text)]
    if percentuais:
        alertas.append(
            "Percentuais no texto exigem fonte ou reformulação: "
            + ", ".join(p["termo"] for p in percentuais)
        )
    for nome, hits in ctas.items():
        cedo = hits and (hits[0]["percentual"] < 10 or (nome in ("inscricao", "comentario") and hits[0]["palavra"] <= 160))
        if cedo:
            alertas.append(
                f"CTA '{nome}' na palavra {hits[0]['palavra']} ({hits[0]['percentual']}%) — "
                "antes de entregar valor. Pedido de inscrição vai depois do conteúdo."
            )

    return {
        "palavras": total,
        "duracao_estimada_minutos": round(total / wpm, 2) if wpm else None,
        "duracao_estimada": (f"{int(total / wpm)}min{int(round((total / wpm % 1) * 60)):02d}s" if wpm else None),
        "ritmo_usado_ppm": wpm,
        "frases_longas": longas,
        "cliches": cliches,
        "frases": len(frases),
        "media_palavras_por_frase": round(total / max(len(frases), 1), 2),
        "perguntas": text.count("?"),
        "abertura": abertura,
        "primeiro_pagamento": pagamentos[0] if pagamentos else None,
        "pagamentos_totais": len(pagamentos),
        "pagamentos_por_mil_palavras": (
            round(len(pagamentos) / max(total, 1) * 1000, 1)
        ),
        "unidades": unidades,
        "marcadores_de_voz": marcadores,
        "superlativos": supers,
        "percentuais_sem_fonte": percentuais,
        "ctas": ctas,
        "mencoes_comerciais": [
            indice(m, text, total) for m in COMERCIAL_RE.finditer(text)
        ],
        "termos_frequentes": frequentes,
        "alertas": alertas,
        "observacao": (
            "Alertas mecânicos. Não determinam clareza, retenção, naturalidade "
            "nem qualidade do hook. Marcadores de voz são sinal positivo."
        ),
    }


def main():
    p = argparse.ArgumentParser(description="Mede roteiro sem emitir veredito.")
    p.add_argument("arquivo", type=Path)
    p.add_argument("--ppm", "--wpm", dest="wpm", type=float, default=160.0,
                   help="palavras por minuto de fala (perfil do canal; padrão 160)")
    p.add_argument("--marcadores", default="",
                   help="marcadores de voz do perfil, separados por vírgula")
    p.add_argument("--janela-abertura", type=int, default=200,
                   help="palavras consideradas como abertura")
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--alertas", action="store_true",
                   help="imprime só os alertas, em texto")
    a = p.parse_args()

    MARCADORES_DE_VOZ.extend(m.strip().lower() for m in a.marcadores.split(",") if m.strip())
    texto = limpar(a.arquivo.read_text(encoding="utf-8"))
    r = analisar(texto, a.wpm, a.janela_abertura)

    if a.alertas:
        print(f"{r['palavras']} palavras · ~{r['duracao_estimada']} falados a {int(a.wpm)} ppm")
        if not r["alertas"]:
            print("Sem alertas mecânicos.")
        for item in r["alertas"]:
            print(f"- {item}")
        return

    print(json.dumps(r, ensure_ascii=False, indent=2 if a.pretty else None))


if __name__ == "__main__":
    main()
