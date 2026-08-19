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

## Session End

Run `TOKST_AGENT=1 tokst context --limit 20 --json` for handoff. Add `--full`
when the complete existing response is required, and add `--stdin` for delayed
input pipes.
