# Contributing to Plandeck

Thanks for looking. Plandeck is small on purpose, and contributions that keep it
that way are the most welcome.

## Principles

- **Zero runtime dependencies.** The engine and the board server run on Node
  standard library only. A change that adds a dependency needs a strong reason.
- **The intelligence layer stays pure.** Everything in `scripts/lib/intelligence.mjs`
  is a deterministic function of the plan. No clock, no filesystem, no network,
  no model calls. That is what makes it testable and trustworthy after a `/clear`.
- **Honest claims only.** The README and SKILL.md describe what the code actually
  does. If you change behavior, update the docs in the same change.

## Getting started

```bash
git clone https://github.com/OthmanAdi/plandeck
cd plandeck
npm test                    # run the suite (62 tests, no framework)
node scripts/cli.mjs board examples/ship-onboarding-flow
```

## Before you open a PR

- Add or update a test in `test/` for any change to the brain. New non trivial
  logic leaves one runnable check behind.
- Keep prose free of dashes used as a pause (commas, colons, and parentheses do
  the job). Compound hyphens like "crash-proof" are fine.
- Run `npm test` and confirm it is green.

## Where things live

| Path | What |
|------|------|
| `scripts/lib/intelligence.mjs` | The pure brain: ready detection, critical path, rollups, next action. |
| `scripts/lib/deck.mjs` | The YAML reader and the plan normalizer. |
| `scripts/lib/journal.mjs` | The append-only transition journal and durable last-state cache. |
| `scripts/lib/snapshot.mjs` | Last-known-good snapshots and card diff summaries. |
| `scripts/lib/continuity.mjs` | The best-effort observation facade used by board, next, and archive. |
| `scripts/lib/render.mjs` | The board app (HTML, CSS, JS) and the NEXT breadcrumb. |
| `scripts/board.mjs` | The live server (HTTP, SSE, file watch). |
| `scripts/doctor.mjs` | Plan diagnosis and explicit snapshot restore. |
| `scripts/cli.mjs` | The `plandeck` command. |
| `test/` | The test suite. |

Bug reports with a small `plan.yaml` that reproduces the issue are gold.
