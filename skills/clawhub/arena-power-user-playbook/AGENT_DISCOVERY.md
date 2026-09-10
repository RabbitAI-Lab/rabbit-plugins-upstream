# Agent Discovery

## What you can do with this skill

If you need to **choose an arena.ai mode** for a concrete task, **check
whether the leaderboard rotated** since a decision was made, **screen a
response** with measurable heuristics before escalating, **carry state
between chats** on a long Agent task, or **fall back to a cloud provider**
when arena.ai is degraded — this skill has an offline, machine-readable
command for each of those.

## When to load it

- "Which mode should I use for ...?" → `mode`
- "Has the leaderboard changed since X?" / "Is model Y still in the top N?" →
  `model-check` (with a fresh dump)
- "This reply looks weak" → `weak` (screening flags, not a verdict)
- "Continue this long task in a new chat" → `state next`
- "What keeps going wrong for me on arena?" → `stats report`

## When NOT to use it

- You need a live model recommendation **right now** — use the live picker or
  arena.ai/leaderboard/agent; this skill's snapshot is a dated baseline.
- You want a quality judgment of a response — this skill never makes one.
- You want a local-model fallback — this skill is cloud-only by design.

## Machine interface

`python3 scripts/arena_playbook.py <cmd> --help`; one summary line on stdout,
full JSON with `--out`; exit codes 0/1/2/3. No network, no dependencies,
python3 stdlib.

## Trust model

Claims are one of: sourced (dated, in references/), measured (script output),
or labeled heuristic. If a claim has none of those three markers, it is not in
this skill — that is the point.
