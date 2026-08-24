# ERE — Editorial Refinement Engine

Skill de refinamento editorial para Claude Code / Codex. Transforma texto
gerado por LLMs em prosa editorial de qualidade, preservando fatos,
entidades e citações.

## Como usar

Ao receber um pedido de refinamento ("refina este texto", "humaniza",
"aplica perfil editorial"), siga o pipeline de 9 etapas documentado em
`SKILL.md`:

1. **Preservação** — congele entidades, números, datas e citações antes de tudo
2. **Estilo** — ajuste o registro ao perfil (default/technical/corporate/creative/minimal)
3. **Estrutura** — varie abertura e organização dos parágrafos
4. **Ritmo** — varie o comprimento das frases
5. **Léxico** — remova clichês de IA e repetições
6. **Conectores** — varie e reduza densidade
7. **Introdução** — varie o padrão de abertura
8. **Contexto** — enriqueça apenas com conhecimento geral indiscutível
9. **Revisão** — audite contra o original

## Regras de ouro

1. NUNCA invente fatos, dados, citações ou referências.
2. NUNCA omita informação factual do original.
3. NUNCA altere entidades, números ou datas.
4. SEMPRE varie ritmo, léxico, conectores e estrutura.
5. O resultado deve parecer escrito por um bom editor humano.

## Perfis

| Perfil | Nível | Uso |
|--------|-------|-----|
| default | 60 | Artigos, blog posts |
| technical | 40 | Documentação, tutoriais, specs |
| corporate | 50 | Comunicados, relatórios |
| creative | 75 | Storytelling, marketing |
| minimal | 25 | Resumos, notas, bullets |

## Análise quantitativa (opcional)

```bash
python3 scripts/ere.py analyze arquivo.txt      # métricas de qualidade
python3 scripts/ere.py diff original.txt refinado.txt  # comparação
python3 scripts/ere.py profile technical         # inspeciona perfil
```

Requires Python 3.10+ (stdlib only). Documento de arquitetura completo em
`references/ERE.md`; catálogo de padrões de IA em `references/patterns.md`;
princípios dos clássicos de escrita (Gopen & Swan, Strunk & White, Othon
Garcia) em `references/writing-principles.md` — consulte ao refinar
estrutura, clareza, precisão ou argumentação. Para texto em português,
consulte também `references/portuguese-writing-principles.md` (ordem de
colocação, colocação pronominal, regência, gerúndio, vícios de linguagem).
