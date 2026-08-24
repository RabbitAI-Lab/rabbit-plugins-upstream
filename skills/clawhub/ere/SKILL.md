---
name: ere
description: >-
  Editorial Refinement Engine — transforma texto gerado por LLMs em conteúdo
  editorialmente refinado: mais natural, menos previsível, com variação de
  ritmo, léxico, estrutura e estilo. Preserva fatos, entidades e citações.
  Alternativa com mais profundidade que o humanizer tradicional.
version: 1.3.0
author: Gabi (Hermes Agent) + Rickk Barbosa
license: MIT
platforms: [linux, darwin]
tags: [editorial, refinement, writing, humanization, text-quality]
metadata:
  hermes:
    tags: [editorial, refinement, writing, humanization, text-quality]
    category: productivity
    related_skills: []
    requires_toolsets: [terminal]
  openclaw:
    os: [linux, darwin]
    requires:
      bins: [python3]
      optional_bins: []
    install:
      pip: null
---

# ERE — Editorial Refinement Engine

Transforma texto de IA em conteúdo editorial profissional — sem fabricar fatos,
sem perder informações, sem soar como "texto de robô".

## Diferença do humanizer tradicional

| Humanizer (blader/humanizer) | ERE |
|---|---|
| Remove 33 padrões de "AI writing" | Aplica motores editoriais: estilo, ritmo, léxico, estrutura |
| Foco: não parecer IA | Foco: qualidade editorial + legibilidade + naturalidade |
| Única passagem | Pipeline com análise quantitativa |
| Sem perfil editorial | 5 perfis: default, technical, corporate, creative, minimal |

## Quando usar

- "Refina este texto" / "Melhora a qualidade editorial deste artigo"
- "Humaniza este conteúdo mantendo os fatos"
- "Aplica perfil jornalístico neste texto técnico"
- "ERE: refina com perfil creative nível 75"

## Quando NÃO usar

- Tradução (use ferramenta de tradução)
- Correção gramatical simples (use corretor ortográfico)
- Geração de conteúdo do zero (use o modelo base)
- Textos que dependem de formatação exata (código, tabelas, JSON)

## Como usar

### Invocação básica

```
ERE: refina este texto com perfil default
[cole o texto aqui]
```

### Com perfil e nível

```
ERE: perfil technical, nível 40
[texto técnico]
```

### Com análise de qualidade

```
ERE: refina e analisa
[texto]
```

## Pipeline de Refinamento

Quando o ERE é invocado, siga este pipeline em sequência:

### 1. PRESERVAÇÃO (Fact Preservation)

**ANTES de qualquer transformação**, identifique e congele:

- **Entidades nomeadas:** pessoas, empresas, produtos, locais
- **Números e datas:** valores, percentuais, anos, horários
- **Citações literais:** texto entre aspas, falas atribuídas
- **Termos técnicos:** siglas, jargão do domínio

**Regra:** estas informações NÃO podem ser alteradas, parafraseadas ou omitidas.
Se aparecerem no texto original, devem aparecer idênticas no texto refinado.

### 2. ESTILO (Style Selector)

Ajuste o registro conforme o perfil:

| Perfil | Registro | Exemplo de tom |
|--------|----------|----------------|
| default (journalistic) | Neutro-profissional | "O projeto foi lançado em março" |
| technical | Objetivo-técnico | "A API retorna HTTP 200 com payload JSON" |
| corporate | Formal-empresarial | "A organização implementou a iniciativa" |
| creative | Expressivo-envolvente | "Março trouxe o projeto à vida" |
| minimal | Direto-enxuto | "Projeto lançado em março" |

### 3. ESTRUTURA (Structure Engine)

- Varie a abertura: não comece sempre com sujeito + verbo
- Alterne entre parágrafos descritivos e analíticos
- Se o original tem 3 parágrafos de background, condense em 1-2
- Se o original pula direto para detalhes sem contexto, adicione 1 frase de abertura
- Respeite o `paragraph_size` do perfil

### 4. RITMO (Rhythm Engine)

- **Varie o comprimento das frases.** Se o original tem 5 frases de ~20 palavras,
  produza algo como: 8, 22, 5, 18, 12 palavras
- Quebre períodos muito longos (>40 palavras em pt-BR, >35 em en)
- Una fragmentos muito curtos consecutivos se soarem telegráficos
- Evite mais de 3 frases com mesma estrutura sintática em sequência
- Alvo: desvio padrão entre 5 e 12 palavras (medido pelo `ere.py analyze`)

### 5. LÉXICO (Lexical Engine)

- **Substitua palavras repetidas** em parágrafo próximo (distância < 50 palavras)
- **Elimine clichês de IA:**
  - "é importante notar que" → remova ou use "note que"
  - "desempenha um papel fundamental" → "é essencial para"
  - "no mundo de hoje" / "no cenário atual" → remova
  - "vale ressaltar" / "cabe destacar" → remova
  - "não apenas... mas também" → simplifique
  - "através de" (quando não é movimento físico) → "por meio de" ou "com"
  - "enquanto" repetido como conector → varie com "ao passo que", "já", "por outro lado"
- **Vocabulário:** use o campo `verbosity` do perfil para calibrar
  - low: vocabulário enxuto, sem floreios
  - high: vocabulário rico, com sinônimos precisos

### 6. CONECTORES (Connector Engine)

- **Varie conectores.** Se o original usa "além disso" 3 vezes, use "também",
  "ainda", "ademais", "some-se a isso"
- **Reduza densidade.** Muitos conectores tornam o texto mecânico.
  Alvo: 1 conector a cada 3-4 frases (verificado pelo `ere.py analyze`)
- **Evite:** "primeiramente... segundamente... finalmente" (mecânico)
  Prefira transições implícitas por sentido

### 7. INTRODUÇÃO (Intro Generator)

- Varie o padrão de abertura:
  - **Fato:** "Em março de 2026, o projeto atingiu 10 mil usuários"
  - **Pergunta:** "O que acontece quando uma ferramenta open source atinge maturidade?"
  - **Cena:** "Era uma manhã de deploy quando o alerta disparou"
  - **Contraste:** "Enquanto o mercado apostava em IA proprietária, a equipe foi na direção oposta"
  - **Direto:** "O projeto foi lançado. Os resultados surpreenderam."
- A abertura deve corresponder ao perfil (creative usa mais variação; technical é mais direto)

### 8. CONTEXTO (Context Engine)

- Se o perfil tem `context: true`, enriqueça com informações implícitas no próprio texto
- **NUNCA invente fatos, dados, citações ou referências externas**
- Use apenas informações que já estão no texto ou são de conhecimento geral
  e indiscutível (ex: "São Paulo é a maior cidade do Brasil")
- Exemplo: se o texto menciona "Docker", pode adicionar "a plataforma de
  containers" como aposição — isso é conhecimento geral, não invenção

### 9. REVISÃO (AI Auditor)

Após o refinamento, verifique:

- [ ] Nomes, números e datas estão idênticos ao original?
- [ ] Citações literais não foram parafraseadas?
- [ ] Nenhuma informação foi adicionada que não estava no original?
- [ ] Não há repetição de palavras em parágrafos adjacentes?
- [ ] As frases variam em comprimento?
- [ ] O texto não contém clichês de IA?
- [ ] O tom corresponde ao perfil solicitado?

## Análise Quantitativa

Após gerar o texto refinado, execute o helper para métricas:

```bash
# Salvar original e refinado
echo "$ORIGINAL" > /tmp/ere_original.txt
echo "$REFINED" > /tmp/ere_refined.txt

# Analisar
python3 scripts/ere.py analyze /tmp/ere_refined.txt
python3 scripts/ere.py diff /tmp/ere_original.txt /tmp/ere_refined.txt
```

### Interpretação dos scores

| Score | Significado |
|-------|-------------|
| 90-100 | Excelente — pronto para publicação |
| 75-89 | Bom — pequenas melhorias possíveis |
| 60-74 | Regular — revisar ritmo e léxico |
| <60 | Insatisfatório — reaplicar refinamento |

## Perfis disponíveis

| Perfil | Nível padrão | Ideal para |
|--------|-------------|------------|
| `default` | 60 | Artigos, blog posts, conteúdo geral |
| `technical` | 40 | Documentação, tutoriais, specs |
| `corporate` | 50 | Comunicados, relatórios, apresentações |
| `creative` | 75 | Storytelling, marketing, opinião |
| `minimal` | 25 | Resumos, bullet points, notas |

Para usar: `ERE: perfil creative nível 80`

## Níveis de refinamento

| Nível | Efeito |
|-------|--------|
| 0-25 | Correções leves: ritmo, clichês, conectores repetidos |
| 25-50 | Reestruturação moderada: varia parágrafos, melhora léxico |
| 50-75 | Estilo editorial completo: intro, estrutura, contexto |
| 75-100 | Reescrita profunda: preserva apenas fatos e entidades |

## Regras de ouro

1. **NUNCA invente.** Sem fatos, dados, citações ou referências que não estejam no original.
2. **NUNCA omita.** Toda informação factual do original deve aparecer no refinado.
3. **NUNCA altere entidades.** Nomes, números, datas são sagrados.
4. **SEMPRE varie.** Ritmo, léxico, conectores, estrutura — a variação é o que torna o texto humano.
5. **O texto refinado deve ser indistinguível de um texto escrito por um bom editor humano** — não por uma IA tentando não parecer IA.

## Princípios dos clássicos de escrita

O ERE incorpora orientações de três obras de referência sobre refinamento de
escrita. O catálogo completo (46 princípios + checklist de anti-padrões,
organizados por categoria) está em `references/writing-principles.md`.
Fontes: **[GS]** *The Science of Scientific Writing* (Gopen & Swan),
**[SW]** *The Elements of Style* (Strunk & White), **[OG]** *Comunicação em
Prosa Moderna* (Othon M. Garcia).

### Mapeamento para o pipeline

| Etapa do pipeline | Princípios aplicáveis |
|---|---|
| 1. Preservação | F1, F2 (fatos vs. indícios; validade das declarações) |
| 2. Estilo | D1 (voz ativa), D2 (declarações positivas), D3 (segundo plano), C7 (substantivos/verbos), C6 (palavras simples) |
| 3. Estrutura | A1 (planejamento), A2 (parágrafo-unidade), A3 (tópico frasal), A4 (desenvolvimento), A5 (coerência), A7 (um desenho) |
| 4. Ritmo | B5 (uma unidade, um ponto), B8 (desdobrar períodos), E3 (fronteira de orações) |
| 5. Léxico | C2 (precisão), C3 (generalização+especificação), C4 (concreto), C5 (omitir palavras), C8 (qualificadores) |
| 6. Conectores | A5 (transição), E3 (pontuação de fronteira) |
| 7. Introdução | A3 (tópico frasal), B7 (contexto antes do novo) |
| 8. Contexto | C3 (especificação), B7 (contexto primeiro) |
| 9. Revisão | B2 (posição de ênfase), B3 (posição de tópico), B4 (dado-novo), F4 (falácias), F5 (lacunas lógicas) |

### Regras de ouro dos clássicos (as mais transformadoras)

1. **Sujeito seguido do verbo** [GS] — nada com mais de ~8-10 palavras entre eles; material interposto é lido como interrupção e perde importância.
2. **Posição de ênfase no fim** [GS][SW] — feche cada frase com a informação nova que merece destaque; nunca com verbo fraco ou anticlimático.
3. **Dado no início, novo no fim** [GS] — posição de tópico = informação já mencionada (liga para trás); posição de ênfase = novidade. É o "problema nº 1 da escrita profissional".
4. **Uma unidade, um ponto** [GS] — "frase longa demais" = mais candidatos a ênfase do que posições disponíveis. Divida ou crie posições secundárias (; e :).
5. **Desdobre períodos labirínticos** [OG] — >35-40 palavras ou 3+ subordinadas antes da principal = reescreva, não pontue.
6. **Aproxime termos relacionados** [OG][SW] — modificador longe do modificado gera ambiguidade; quando conflitar ênfase vs. clareza, a clareza vence.
7. **Toda generalização exige especificação** [OG] — declaração geral precisa de fato, dado, exemplo ou razão logo a seguir; tópico frasal + desenvolvimento é o padrão.
8. **Omita palavras desnecessárias** [SW] — "every word tell"; corte "a questão de saber se", "devido ao fato de que", qualificadores de enchimento (muito, bastante, meio).
9. **Declarações positivas** [SW] — diga o que é, não o que não é; elimine condicionais de hesitação (poderia, talvez) sem incerteza real.
10. **Clareza acima da forma** [OG] — elegância oca e fraseado bonito falseiam as ideias; se o sentido exigir releitura, reescreva.
11. **Ação no verbo** [GS] — "quem faz o quê?"; ação central escondida em nominalização ou verbo vazio perde as pistas estruturais.
12. **Fatos ≠ indícios** [OG] — evidência de indício pede "parece/provavelmente/sugere"; inferência apresentada como fato é falácia.

### Anti-padrões mais frequentes

- Comma splice e frase quebrada no meio de oração dependente [SW]
- Frase que termina com material fraco ocupando a posição de ênfase [GS]
- Informação nova estreando na posição de tópico [GS]
- Termos genéricos onde caberia palavra específica ("árvore" → "palmeira") [OG]
- Superlativos gratuitos e "um dos mais" [SW]
- Petição de princípio: a declaração usada como prova ("dizer a mesma coisa com outras palavras") [OG]
- Falsa causalidade: correlação tratada como causa [OG]
- Passiva sem agente quando o agente é conhecido [SW][GS]

## Português (pt-BR)

Refinar texto em português exige regras próprias da língua — ordem de
colocação, colocação pronominal, regência, gerúndio, vícios de linguagem.
O catálogo completo (33 princípios organizados em G/H/I/J/K + checklist de
anti-padrões pt-BR) está em `references/portuguese-writing-principles.md`,
extraído de *Comunicação em Prosa Moderna* (Othon M. Garcia).

### Regras de ouro do português

1. **Ordem direta é a norma; inversão só com propósito** [G1] — anteponha termo apenas para ênfase, clareza, ritmo ou eufonia; inversão gratuita soa empolada.
2. **Antepôs objeto/predicativo? Retome com pronome** [G2] — "o homem... fê-lo"; sem a retomada (torneio pleonástico), a inversão fica truncada.
3. **"E" nem sempre é adição** [G5] — falsa coordenação: causa → "porque", consequência → "por isso", oposição → "mas". Explicite a relação lógica.
4. **Período tenso: principal no fim para suspense; frouxo: principal primeiro para texto direto** [G3] — nunca alongue a prótase além da atenção do leitor.
5. **Frase de arrastão e ladainha são defeitos** [G7][G8] — "Então... mas aí... então..."; parágrafo amarrado por "e" — subordine e varie conectivos.
6. **Gerúndio: ação secundária, nunca adjetivo** [I1] — "tendo objeto próprio" → "com objeto próprio"; evite "vou estar fazendo".
7. **Anfibolia: o leitor precisa saber quem faz o quê** [J3] — "O pai viu o filho sair" é ambíguo; pronome com referente único.
8. **Pleonasmo vicioso é erro; intencional é ênfase** [J4] — corte "subir para cima", "planejamento prévio"; preserve "vi com meus próprios olhos" só com carga expressiva real.
9. **Preciosismo é vício, não virtude** [J5] — "óbito" → "morte"; se a palavra exige dicionário e há sinônimo comum, substitua.
10. **Cacofonia e eco quebram a leitura** [K1] — leia em voz alta: "boca dela", série de "ção".
11. **Colocação pronominal: norma culta sem artificialidade** [I5] — próclise após negativas/advérbios/relativos; ênclise em início; sem "me parece" em texto formal quando a norma pede atração.
12. **Carga valorativa contamina texto objetivo** [J8] — "burocrata" vs. "funcionário"; troque pelo termo neutro se o fato não sustenta o juízo.

### Anti-padrões pt-BR mais frequentes

- Falsa coordenação: "e" escondendo causa/consequência/oposição [G5]
- Frase de arrastão: "Então... mas aí... então... aí..." [G7]
- Fragmento vicioso: gerúndio isolado por ponto por descuido [G10]
- Correlações quebradas: "não tanto... mas também" [H2]
- Solecismos: "haviam pessoas", "fazem cinco anos", "a gente vamos" [I3]
- Regência errada: "assistir o filme", "preferir X do que Y" [I4]
- Pleonasmo vicioso: "subir para cima", "entrar para dentro", "surpresa inesperada" [J4]
- Clichês: "vale ressaltar", "cabe destacar", "frio de rachar" [J6]
- Muletas retóricas: "no que tange a", "com vistas a", "faz-se mister" [J9]
- Cacofonia: "boca dela", "cada lado" [K1]

## Exemplo

### Entrada
```
O projeto de automação residencial foi desenvolvido pela equipe em 2025.
O projeto utiliza sensores IoT para monitorar o ambiente. Além disso,
o projeto conta com um aplicativo mobile para controle remoto. É importante
notar que o projeto foi premiado na feira de tecnologia. O projeto também
oferece integração com assistentes virtuais como Alexa e Google Home.
```

### Saída (perfil default, nível 60)
```
Premiado na feira de tecnologia de 2025, o projeto de automação residencial
nasceu com uma proposta ambiciosa: integrar sensores IoT, controle mobile
e assistentes virtuais em uma única plataforma.

A equipe desenvolveu um sistema que monitora o ambiente em tempo real
usando sensores conectados. O aplicativo mobile complementa a experiência
com controle remoto, enquanto a compatibilidade com Alexa e Google Home
elimina a fricção de aprender uma nova interface.

O resultado é uma casa que responde — sem que o morador precise pensar nisso.
```

### Métricas
- Original: 5 frases, ~11 palavras/frase (monótono)
- Refinado: 6 frases, comprimentos 8, 22, 18, 14, 17, 12 (variado)
- Palavra "projeto": 6x no original, 1x no refinado
- Flesch: 45 → 62

## Pitfalls

### YAML Parser: inline comments not stripped

The simple YAML subset parser in `ere.py` does NOT strip inline comments by default.
A value like `"journalistic  # comment"` will include the comment as part of the value.
This was fixed in v1.0.0 by adding `value.split("#")[0].strip()` after parsing.

### Profile not found: falls back to default

If the requested profile name doesn't exist in `profiles/default.yaml`, the loader
returns the `default` profile silently. Verify with `ere.py profile <name>` before using.

### pgpy not available on Python 3.13+

The `pgpy` library fails with `ModuleNotFoundError: No module named 'imghdr'` because
`imghdr` was removed from stdlib in Python 3.13. ERE uses only stdlib for this reason.

## Arquivos

| Arquivo | Função |
|---------|--------|
| `scripts/ere.py` | Análise quantitativa: readability, diff, quality score |
| `profiles/default.yaml` | Perfis editoriais: default, technical, corporate, creative, minimal |
| `references/patterns.md` | Catálogo de padrões de IA a evitar (33 padrões) |
| `references/writing-principles.md` | Princípios dos clássicos de escrita: 46 regras + anti-padrões (Gopen & Swan, Strunk & White, Othon Garcia) |
| `references/portuguese-writing-principles.md` | Português pt-BR: 33 regras da língua (ordem, colocação pronominal, regência, gerúndio, vícios) + anti-padrões (Othon Garcia) |
| `references/ERE.md` | Documento de arquitetura completo (SDD original) |

## Compatibilidade entre agentes

| Agente | Como carrega |
|--------|--------------|
| Hermes Agent | `SKILL.md` (metadata.hermes) |
| OpenClaw | `SKILL.md` (metadata.openclaw) |
| Claude Code | `.claude/skills/ere/SKILL.md` + `CLAUDE.md` |
| Codex | `.agents/skills/ere/SKILL.md` + `AGENTS.md` |
