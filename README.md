# roteiro-youtube

Roteiros de YouTube longo em português, na **sua** voz. Do tema solto ao texto pronto para gravar: ângulo, título, ideia de thumbnail, abertura, estrutura em blocos, roteiro completo, revisão e leitura dos números depois de publicar.

## O que ele faz

| Você pede | Você recebe |
|---|---|
| "isso dá vídeo?" / "o que gravar essa semana" | 3 a 6 ângulos para o tema, o melhor e o porquê |
| "me dá títulos e thumb" | 8 a 12 títulos de tipos diferentes, 2 a 3 ideias de thumb e o pacote recomendado |
| "como eu começo esse vídeo?" | 3 aberturas escritas palavra por palavra e a recomendada |
| "escreve o roteiro sobre X" | título, thumb, abertura, blocos encadeados e fecho, com a duração estimada e o que conferir antes de gravar |
| "revisa meu roteiro" | o que está fazendo o público sair e os trechos já reescritos |
| "por que a retenção caiu?" | se o problema é o título e a thumb ou o roteiro, e o que testar no próximo vídeo |

Ele não inventa números, histórias pessoais nem resultados. O que precisa de fonte vem marcado como `[VERIFICAR]`.

## Primeiro passo: o perfil do seu canal

Na primeira vez, ele faz 8 perguntas rápidas sobre o seu canal: público, como você fala, vídeos que funcionaram e regras. Com as respostas, monta o `perfil-do-canal.md`, que deixa todos os roteiros com a sua cara. Dica: cole 2 ou 3 trechos de roteiros ou transcrições suas. É o que mais ajuda.

## Instalação

### Claude Code ou app do Claude no computador (versão completa)

A versão completa traz a skill, os comandos e dois revisores automáticos (checador de fatos e espectador leigo).

1. Abra o Claude Code (ou a aba Code do app do Claude) numa pasta só para o seu canal, por exemplo `Documentos/meu-canal`.
2. Digite:
   ```
   /plugin marketplace add paullabs/roteiro-youtube
   ```
3. Depois:
   ```
   /plugin install roteiro-youtube@roteiro-youtube
   ```
4. Crie o seu perfil:
   ```
   /roteiro-youtube:perfil
   ```

Comandos:
- `/roteiro-youtube:roteiro como sair do cheque especial`: escreve o roteiro completo.
- `/roteiro-youtube:revisar-roteiro meu-roteiro.md`: revisa um roteiro pronto.
- `/roteiro-youtube:perfil`: cria ou atualiza o perfil do canal.

Você não precisa dos comandos: pedir em português normal ("me dá títulos pra um vídeo sobre…") já ativa a skill.

### Claude no navegador ou no app (claude.ai)

1. Baixe o arquivo [`roteiro-youtube.zip`](https://github.com/paullabs/roteiro-youtube/releases/latest/download/roteiro-youtube.zip).
2. No Claude, vá em **Configurações → Capacidades → Skills** e clique em **Enviar skill**. Escolha o .zip.
3. Crie um **Projeto** chamado "Meu canal". Quando a skill montar o seu perfil, salve o texto como `perfil-do-canal.md` nos **arquivos do Projeto**. Assim ele vale para todas as conversas desse projeto.
4. Converse dentro do Projeto: "escreve o roteiro do meu próximo vídeo sobre…"

Nessa versão não tem os comandos nem os revisores automáticos; o próprio Claude faz as duas revisões dentro da conversa.

## Dicas

- Atualize o perfil a cada 10 vídeos publicados, com os números novos (CTR, retenção aos 30 s e 1 min). Peça: "atualiza meu perfil com esses números".
- Quer só uma parte? Peça só a parte: "só a abertura", "só os títulos". Ele não faz o roteiro inteiro se você não pediu.
- Já tem um texto seu? Mande junto. Ele preserva as frases que já soam como você.
- Se a sessão tiver busca na web, ele confere fatos e vê o que já existe sobre o tema no YouTube.

## O que tem dentro

```
skills/roteiro-youtube/
  SKILL.md                         o método e o fluxo
  references/
    perfil-do-canal-modelo.md      perguntas do onboarding e o modelo do perfil
    embalagem.md                   ângulos, títulos, thumbnail, V2
    abertura.md                    o primeiro minuto
    estrutura.md                   blocos em escada, formatos de vídeo, retenção, fecho
    voz-e-oralidade.md             texto falado, sem cara de IA
    pesquisa-e-fatos.md            checagem e pesquisa de demanda
    revisao-e-analytics.md         revisão e leitura dos números
  scripts/medir_roteiro.py         mede duração, frases longas, abertura e estrutura
agents/                            checador-de-fatos, espectador-leigo
commands/                          roteiro, revisar-roteiro, perfil
```

Feito por Paulo Labs.
