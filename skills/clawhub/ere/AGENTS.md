# AGENTS.md — ERE Workspace Rules

Este diretório contém a skill **ERE (Editorial Refinement Engine)** —
um pipeline de 9 etapas para transformar texto de LLM em prosa editorial
de qualidade, preservando fatos, entidades e citações.

## O que é este repositório

- `SKILL.md` — instruções completas do pipeline para o agente
- `scripts/ere.py` — análise quantitativa (stdlib Python, zero deps)
- `profiles/default.yaml` — 5 perfis editoriais configuráveis
- `references/patterns.md` — 33 padrões de "AI writing" a evitar
- `references/writing-principles.md` — princípios dos clássicos de escrita (Gopen & Swan, Strunk & White, Othon Garcia)
- `references/portuguese-writing-principles.md` — regras específicas do português pt-BR (Othon Garcia)
- `references/ERE.md` — SDD / documento de arquitetura
- `CLAUDE.md` — contexto para Claude Code / Codex
- `README.md` — documentação pública

## Regras ao usar esta skill

1. **Nunca altere os arquivos de referência sem necessidade** — são a fonte
   de calibração da skill.
2. **O script `ere.py` é read-only por design** (analisa, não modifica texto).
3. **Não armazene segredos** neste diretório. Se a skill for distribuída,
   credenciais entram via variáveis de ambiente, nunca em arquivos.
4. **Idioma:** o conteúdo da skill é pt-BR porque o alvo primário é texto
   em português; o pipeline também funciona para inglês.
5. Ao encontrar um bug no `ere.py`, corrija e adicione um caso de teste —
   nunca remova funcionalidade silenciosamente.

## Verificação rápida

```bash
python3 scripts/ere.py profile default   # deve imprimir JSON com o perfil
python3 scripts/ere.py analyze arquivo.txt  # métricas de qualidade
```

Ambos devem sair com exit code 0.
