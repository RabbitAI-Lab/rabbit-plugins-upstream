# Workspace Init — Execution Checklist

> Triggered by: "workspace init {name}", deep research request, or user teaches a procedure worth persisting.

## Input

- `{name}` — workspace name (used as directory name)
- `--type` — `project` (default), `research`, or `runbook`

## For type=project

1. Read source code or context at the relevant path
2. Create `memory/projects/{name}/`
3. Write `overview.md`:
   ```markdown
   # {name} — Overview
   > Created: {YYYY-MM-DD}

   ## What It Does
   ## Architecture
   ## Tech Stack
   ## Entry Points
   ## Configuration
   ```
4. Create empty `decisions.md` (append-only log of design decisions)
5. Add pointer to MEMORY.md `## Projects`:
   `- {name} | {one-line description} | memory/projects/{name}/`
6. Log to `memory/.lifecycle.log`

## For type=research

1. Create `memory/projects/{name}/`
2. Write `overview.md`: background, core questions, current status
3. Write `report.md`: full findings and analysis
4. Write `references.md`: sources with URLs or file paths
5. Add pointer to MEMORY.md `## Projects`
6. Log to `memory/.lifecycle.log`

## For type=runbook

1. Create `memory/projects/{name}/`
2. Write `runbook.md`: step-by-step procedure with prerequisites, commands, rollback steps, gotchas
3. Add pointer to MEMORY.md `## Projects`:
   `- {name} | {one-line description} | memory/projects/{name}/`
4. Log to `memory/.lifecycle.log`

## Output Structure

```
memory/projects/{name}/
├── overview.md          # Architecture or research background
├── runbook.md           # Step-by-step procedure (runbook type)
├── report.md            # Full findings (research type)
├── references.md        # Sources (research type)
└── decisions.md         # Design decisions (project type, append-only)
```

Not all files are required — create only what's needed for the workspace type. Files are living documents; update them as the project evolves.
