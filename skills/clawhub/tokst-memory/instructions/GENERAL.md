# TokST — General Agent Instructions

TokST is a persistent memory system. Use the MCP tools to read and write memory.

## Session Start

```
TOKST_AGENT=1 tokst context --limit 20 --json
```

Always load context before responding.

## Search

```
TOKST_AGENT=1 tokst search "<query>" [--search-mode auto|keyword|semantic|hybrid] [--type <type>] [--tags a,b] [--atlas-id <id>] [--limit <n>] --json
```

Search before repeating decisions or recommendations.

## Store

```
TOKST_AGENT=1 tokst remember "<content>" --type <type> [--tags a,b] [--source-type human|agent] [--source <name>] [--atlas-id <id>] [--file <path> ...] --json
```

| Type | When |
|------|------|
| `fact` | Stable facts |
| `decision` | Chosen plans |
| `preference` | User preferences |
| `task` | Open actions |
| `architecture` | Design decisions |
| `note` | General context |

### File attachments

```
tokst remember "Diagram" --type architecture --file diagram.png --json   # attach on create
tokst memory attach mem_xxxxx --file report.pdf --json                   # attach to existing
tokst memory download mem_xxxxx --out ./files --json                     # download attachments
```

## Session protocol

Use a Session for multi-step work, a context boundary, or a handoff:

```
TOKST_AGENT=1 tokst session start --task "<task>" --json
TOKST_AGENT=1 tokst session capture --session <ses-id> "<confirmed finding>" --kind decision --json
TOKST_AGENT=1 tokst session checkpoint --session <ses-id> "<progress and next action>" --json
TOKST_AGENT=1 tokst session finalize --session <ses-id> "<completed work>" --json
```

Capture confirmed long-term information only. Keep credentials, raw reasoning,
and transient tool output in the current runtime context. Use `--full` only for
the complete response and `--stdin` for delayed input pipes.
