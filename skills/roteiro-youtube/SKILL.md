---
name: roteiro-youtube
description: Escreve, embala e revisa roteiros de vídeos longos de YouTube (de 8 a 40 minutos) em português falado, na voz do criador. Cobre todas as etapas — ideia e ângulo, título, conceito de thumbnail, abertura (primeiro minuto), estrutura em blocos, roteiro completo, revisão de roteiro pronto e leitura de retenção no Analytics. Use SEMPRE que a pessoa pedir roteiro, script, texto pra gravar, ideia de vídeo, título, thumb, gancho, intro, estrutura, outline, "isso dá vídeo?", "como eu começo esse vídeo", "revisa meu roteiro", "tá chato", "por que a retenção caiu", "o que gravar essa semana", mesmo que não diga "skill" nem "YouTube". Não é para Shorts, Reels ou TikTok de menos de 3 minutos, nem para edição, legenda ou thumbnail pronta em imagem.
---

# Roteiro para YouTube longo

Esta skill ajuda um criador a sair de uma ideia e chegar a um vídeo longo que as pessoas clicam e assistem até o fim: o pacote (título e thumb), a abertura, a estrutura e o texto falado, mais a revisão e a leitura dos números depois de publicar.

Ela não promete viralizar, não inventa experiência ou número e não decide se o assunto merece existir. O tema é do criador; o trabalho aqui é achar a forma mais clara, honesta e interessante de entregar esse tema.

## 1. Comece pelo perfil do canal

Um roteiro sem perfil sai genérico: soa como "conteúdo de IA", não como a pessoa. Por isso o primeiro passo é achar o perfil.

**Onde procurar, nesta ordem:**
1. Um arquivo `perfil-do-canal.md` na pasta de trabalho, nos arquivos do projeto ou anexado na conversa.
2. Informações sobre o canal já ditas nesta conversa.

**Se existir:** leia inteiro antes de qualquer coisa. Ele manda na voz, no público, nos formatos e nos números. Se algo nele contradiz esta skill, o perfil ganha, porque ele foi medido no canal da pessoa e esta skill é geral.

**Se não existir**, depende do pedido:
- Pedido completo (roteiro, planejamento) ou o primeiro uso: faça o **onboarding** — mande as perguntas de `references/perfil-do-canal-modelo.md` (seção "Perguntas do onboarding") numa mensagem só, monte o perfil com as respostas e entregue o arquivo. No Claude Code, salve como `perfil-do-canal.md` na pasta de trabalho. No Claude.ai, entregue o texto e diga para colocar nos arquivos do Projeto, assim ele vale para as próximas conversas.
- Pedido pequeno (títulos, uma abertura, revisar um trecho) ou a pessoa disse que quer rápido: siga com o perfil genérico do fim de `references/perfil-do-canal-modelo.md`, marque na entrega que usou o genérico e ofereça criar o perfil em uma linha.

O onboarding acontece uma vez. Depois, perfil existente nunca vira questionário de novo.

## 2. Teto e piso

Duas coisas diferentes decidem o resultado de um vídeo, e confundir as duas é o erro mais caro:

- **A embalagem define o teto.** Título, thumbnail e ângulo decidem quantas pessoas *podem* clicar. Nenhum roteiro recupera um teto baixo.
- **A retenção defende o teto.** Abertura, progressão e final decidem quanto desse público vira tempo assistido. Nenhuma retenção cria público que a embalagem não trouxe.

Por isso, trabalhe o pacote antes do texto, e todo roteiro sai com título e conceito de thumb junto. Eles fazem parte da entrega.

## 3. Descubra o que a pessoa quer, sem questionário

| Pedido | Modo | Entrega |
|---|---|---|
| tema solto, "isso dá vídeo?", "o que gravar" | Direção | 3–6 ângulos, o escolhido e o motivo |
| título, thumb, "como eu embalo isso" | Embalagem | 8–12 títulos em famílias diferentes, 2–3 conceitos de thumb, o pacote recomendado |
| abertura, gancho, intro | Abertura | 3 aberturas escritas palavra por palavra e a recomendada |
| planejar, estruturar, outline | Planejamento | pacote + mapa de blocos + o que precisa ser verificado |
| escrever, criar roteiro | Roteiro | pacote + texto completo pronto para gravar |
| revisar, corrigir, "tá chato" | Revisão | diagnóstico curto + trechos já corrigidos |
| números, curva de retenção, vídeo publicado | Performance | o que o dado mostra, hipóteses e o próximo teste |

Se pediram o roteiro completo, entregue tudo de uma vez. Não pare para aprovar título, ângulo ou estrutura: deixe essas decisões no topo da entrega, uma linha cada, para a pessoa redirecionar em segundos se quiser.

**Quando perguntar:** só quando a resposta muda um fato (algo pessoal que você não pode inventar, uma obrigação de patrocínio) e não dá para inferir nem pesquisar. No máximo uma pergunta, e continue o resto enquanto isso. Público, tom e duração vêm do perfil. Escopo ambíguo vira leque de ângulos com um escolhido, não pergunta.

## 4. Fluxo do roteiro completo

Leia só as referências que a etapa pede (tabela da seção 6). Um pedido pequeno deve continuar barato.

1. **Preservar.** Separe o que não muda (tema, intenção, fatos, pedidos explícitos), o que dá para adaptar (ângulo, ordem, exemplos, duração) e o que não pode ser inventado (números, resultados, experiências pessoais). Se a pessoa mandou texto, marque as frases que já soam como ela antes de reescrever qualquer coisa.
2. **Abrir o leque.** Escreva 3–6 ângulos do mesmo tema variando o eixo (público, promessa, formato, escopo, inimigo, momento). Escolha por demanda × credibilidade × capacidade de pagar a promessa. → `references/embalagem.md`
3. **Fechar o pacote.** Títulos em famílias diferentes, um escolhido, e um conceito de thumb que acrescenta ao título em vez de repetir. Teste: o roteiro paga isso cedo? Se não paga, baixe a promessa ou suba a entrega. → `references/embalagem.md`
4. **Verificar o que sustenta a promessa.** Pesquise só o que segura título, abertura, comparações e conclusão. Falta de prova bloqueia a frase, não o vídeo: qualifique, transforme em teste ou corte. → `references/pesquisa-e-fatos.md`
5. **Escolher o motor** (curso comprimido, explicação, demonstração, investigação, comparação, diagnóstico, história, desafio) e desenhar o **mapa de blocos** como escada: cada bloco resolve uma dúvida e cria a necessidade do próximo. → `references/estrutura.md`
6. **Escrever os blocos.** Primeiro a lógica, depois a fala. Cada bloco cumpre a maior parte de: necessidade → resposta → exemplo ou prova → o que isso muda → limite → gancho para o próximo. → `references/estrutura.md` e `references/voz-e-oralidade.md`
7. **Escrever a abertura por último.** Ela promete o que o vídeo entrega; escrita antes, promete o que você *acha* que vai entregar. → `references/abertura.md`
8. **Fechar.** O final junta as peças num resultado, decisão ou sistema — não é resumo. O pedido de inscrição vem depois da entrega, nunca antes.
9. **Medir.** Rode `python3 scripts/medir_roteiro.py roteiro.md --alertas` (caminho relativo à pasta desta skill; use `--ppm` com o ritmo do perfil). O script aponta pagamento atrasado, escopo pesado, frases longas, catálogo, percentuais sem fonte e CTA cedo. É alerta, não veredito.
10. **Revisar com outros olhos.** Se existirem os agentes `checador-de-fatos` e `espectador-leigo` (versão plugin), rode os dois em paralelo com o roteiro salvo em arquivo. Sem eles, faça as duas leituras você mesmo com `references/revisao-e-analytics.md`: primeiro como checador (cada número e nome tem fonte?), depois como alguém sem contexto que assiste distraído.
11. **Reparar.** No máximo duas passadas. Depois entregue a melhor versão e cite só os riscos que dependem da pessoa.

## 5. Formato da entrega

Para roteiro completo, use este formato:

```
Título: ...
Thumb: o que aparece na imagem + o que ela acrescenta ao título
Contrato: a pessoa entra com ___ e sai ___
Formato: [motor] · [N blocos] · ~[X] min falados (a [ppm] palavras por minuto)
Perfil: [nome do perfil usado | genérico]

---

[ABERTURA]
texto falado...

[BLOCO 1 — nome curto]
texto falado...
(tela: indicação visual, só quando ajuda)

...

[FECHO]
texto falado...

---

Verificar antes de gravar:
- [VERIFICAR: afirmação] — por quê
Fontes:
- ...
Alternativas: 2 títulos e 1 abertura reserva
```

O texto entre as marcações é só o que vai ser falado: sem "hook", "virada" ou "payoff" no meio da narração, sem relatório antes do roteiro. Fontes e observações ficam separadas do texto.

Na revisão: explique só os defeitos que mudam a decisão e já entregue os trechos corrigidos, lado a lado com o original quando ajudar.

## 6. Qual referência ler

| Vai mexer em | Leia |
|---|---|
| criar ou atualizar o perfil do canal | `references/perfil-do-canal-modelo.md` |
| ideia, ângulo, título, thumbnail, V2 de um vídeo | `references/embalagem.md` |
| primeiro minuto, gancho, contrato | `references/abertura.md` |
| mapa de blocos, motor, retenção no meio do vídeo, final | `references/estrutura.md` |
| escrever ou naturalizar o texto, voz, cortar cara de IA | `references/voz-e-oralidade.md` |
| fatos, números, ferramenta atual, pesquisa de demanda | `references/pesquisa-e-fatos.md` |
| revisar roteiro pronto, ler Analytics, vídeo publicado | `references/revisao-e-analytics.md` |

## 7. Portão antes de entregar um roteiro

Se algum item falhar, corrija antes de entregar. Avisar e entregar mesmo assim não conta.

1. Tem título e conceito de thumb, e a thumb acrescenta informação em vez de repetir o título.
2. O leque de ângulos foi aberto antes de escolher.
3. A primeira frase confirma o assunto e soa como a pessoa do perfil, não como anúncio.
4. O hook faz trabalho: abre uma tensão que o espectador não tinha quando clicou (não só confirma o clique).
5. A promessa finita (quantos blocos, quanto tempo, onde termina) aparece nos primeiros 30 segundos.
6. O primeiro pagamento da promessa chega dentro do primeiro minuto.
7. Nenhum número, resultado, teste ou história pessoal foi inventado; o que falta está marcado `[VERIFICAR]` ou `[CONFIRMAR]`.
8. Cada bloco depende do anterior; se a ordem pode ser embaralhada sem perda, é catálogo e precisa virar escada.
9. O final integra e paga a promessa do título.
10. O texto lido em voz alta não tropeça: frases curtas, uma ideia por frase, jargão explicado na mesma frase.
11. A duração estimada cabe na faixa do perfil; se não couber, a entrega diz onde crescer ou cortar (sem encher linguiça para bater a marca).

## 8. O que esta skill não faz

Ela falha se: recusar um tema que dá para consertar; fizer questionário quando o perfil já existe; inventar prova, número ou experiência pessoal; trocar uma abertura direta e natural por uma cena publicitária; entregar roteiro sem título e thumb; convergir no primeiro ângulo; corrigir texto quando o problema é a embalagem (ou o contrário); chamar um vídeo de bom ou ruim sem comparar com a média do próprio canal; transformar uma heurística daqui em lei contra o perfil medido da pessoa.
