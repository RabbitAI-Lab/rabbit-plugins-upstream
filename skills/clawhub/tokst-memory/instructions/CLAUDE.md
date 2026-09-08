# TokST — Claude Instructions

TokST gives you persistent memory across Claude sessions via MCP tools.

## Mandatory: Load Context First

Every conversation must begin with the Agent-safe CLI mode:

```
TOKST_AGENT=1 tokst context --limit 20 --json
```

Read the output before responding. It contains facts, decisions, architecture,
preferences, tasks, and notes from previous sessions.

## Search Before Acting

Before making recommendations or decisions:

```
TOKST_AGENT=1 tokst search "<natural language query>" --json
```

Always frame the query with context about what you're trying to do.
Do not repeat what has already been decided.

## Storage Rules

Store silently — never ask for permission:

| Scenario | Type |
|----------|------|
| User facts, project facts | `--type fact` |
| Decisions, chosen plans | `--type decision` |
| Preferences, habits | `--type preference` |
| Open tasks, next actions | `--type task` |
| Design, architecture | `--type architecture` |
| General context | `--type note` |

## Tags

Combine a scope tag with a topic tag:

```
--tags project,name
--tags personal,preference
```

## Source

Always use `--source-type agent --source claude`.

## Auto-Routing

TokST auto-routes by content keywords. You can omit `atlasId` in most cases.
Use `--atlas-id <uuid>` only when targeting a specific atlas explicitly.

## Explicit Session recording

Use this protocol when the user requests an explicit Session record or an
existing integration requires it. Automatic memory collects connected Agent
work separately. A Session record never creates a formal Task by itself:

```
TOKST_AGENT=1 tokst session start --task "<task>" --json
TOKST_AGENT=1 tokst session capture --session <ses-id> "<confirmed finding>" --kind decision --json
TOKST_AGENT=1 tokst session checkpoint --session <ses-id> "<progress and next action>" --json
TOKST_AGENT=1 tokst session finalize --session <ses-id> "<completed work>" --json
```

Capture confirmed durable information only. Keep credentials, raw reasoning,
and transient tool output in the current runtime context. Use `--full` only for
the complete response and `--stdin` for delayed input pipes.
