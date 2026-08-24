# ERE — Editorial Refinement Engine

Skill multi-agente que transforma texto gerado por LLMs em conteúdo
editorialmente refinado. Compatível com **Hermes Agent**, **OpenClaw**,
**Claude Code** e **Codex**.

## O que faz

- **Preserva fatos:** entidades, números, datas e citações são congelados antes da transformação
- **Aplica motores editoriais:** estilo, estrutura, ritmo, léxico, conectores, introdução, contexto
- **Remove padrões de IA:** 33 padrões catalogados (clichês, repetições, linguagem mecânica)
- **Métricas quantitativas:** readability (Flesch), diff, composite quality score
- **5 perfis:** default (jornalístico), technical, corporate, creative, minimal

## Diferença do humanizer tradicional

O humanizer original foca em remover padrões de detecção de IA. O ERE vai além: aplica
técnicas editoriais reais (variação de ritmo, estrutura de parágrafos, riqueza lexical)
para produzir texto com qualidade de editor humano — não apenas "indetectável".

## Instalação

### Hermes Agent

```bash
cp -r ere/ ~/.hermes/skills/ere/
```

### OpenClaw

```bash
cp -r ere/ ~/.openclaw/skills/ere/
# ou empacote como .skill (tar.gz do diretório)
```

### Claude Code

```bash
mkdir -p .claude/skills/ere
cp -r ere/* .claude/skills/ere/
```

### Codex

```bash
mkdir -p .agents/skills/ere
cp -r ere/* .agents/skills/ere/
```

## Uso

```
ERE: refina este texto com perfil default
[texto]

ERE: perfil technical, nível 40
[texto técnico]

ERE: refina e analisa
[texto]
```

## Estrutura

```
ere/
├── SKILL.md                    # Instruções para o agente (dual-platform)
├── CLAUDE.md                   # Contexto para Claude Code / Codex
├── AGENTS.md                   # Regras de workspace
├── scripts/
│   └── ere.py                 # Análise quantitativa (stdlib)
├── profiles/
│   └── default.yaml            # Perfis editoriais (5 perfis)
├── references/
│   ├── patterns.md             # Catálogo de 33 padrões IA
│   ├── writing-principles.md   # Princípios dos clássicos (Gopen & Swan, Strunk & White, Othon Garcia)
│   ├── portuguese-writing-principles.md  # Regras do português pt-BR (Othon Garcia)
│   └── ERE.md                  # SDD original (referência)
├── manifest.json               # Metadados de distribuição
├── release.json                # Changelog de releases
└── README.md
```

## Requisitos

- Python 3.10+ (stdlib apenas — sem dependências externas)
- Qualquer harness de agente que suporte skills em Markdown

## Compatibilidade

| Agente | Arquivo de entrada |
|--------|--------------------|
| Hermes Agent | `SKILL.md` (metadata.hermes) |
| OpenClaw | `SKILL.md` (metadata.openclaw) |
| Claude Code | `SKILL.md` + `CLAUDE.md` |
| Codex | `SKILL.md` + `AGENTS.md` |

## Licença

MIT
