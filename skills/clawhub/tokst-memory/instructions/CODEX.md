# TokST — Codex Instructions

You have access to TokST via MCP tools. Use it as your persistent memory across sessions.

## Session Start (mandatory)

At the start of EVERY conversation:

```
TOKST_AGENT=1 tokst context --limit 20 --json
```

This loads project context (facts, decisions, architecture, preferences, tasks, notes).
Do not skip this. Read the output before responding.

## Search Before Deciding

Before making any recommendation or decision:

```
TOKST_AGENT=1 tokst search "<natural language query>" --json
```

Frame the query with intent: "User wants to X — what have we decided before?"
Never repeat a recommendation without checking memory first.

## When to Store

Store automatically — do not ask permission:

- Facts about the user or project → `--type fact`
- Decisions made or plans chosen → `--type decision`
- User preferences or habits → `--type preference`
- Open tasks or next actions → `--type task`
- Architecture or design decisions → `--type architecture`
- General useful context → `--type note`

## Tag Convention

Always combine a domain tag with a type tag:

```json
"--tags project,tokst"
"--tags personal,preference"
"--tags work,architecture"
```

## Source Attribution

Always set `--source-type agent --source codex` when storing.
Use `--source <your-name>` consistently so memories are traceable.

## Auto-Routing

If you omit `atlasId`, TokST auto-routes the memory to the best matching
atlas based on keyword analysis of the content. You only need to specify
`--atlas-id` when you have a strong reason to target a specific atlas.

## Session protocol

Use a Session for multi-step work, a context boundary, or a handoff:

```
TOKST_AGENT=1 tokst session start --task "<task>" --json
TOKST_AGENT=1 tokst session capture --session <ses-id> "<confirmed finding>" --kind decision --json
TOKST_AGENT=1 tokst session checkpoint --session <ses-id> "<progress and next action>" --json
TOKST_AGENT=1 tokst session finalize --session <ses-id> "<completed work>" --json
```

Capture confirmed durable information only. Keep credentials, raw reasoning,
and transient tool output in the current runtime context.
