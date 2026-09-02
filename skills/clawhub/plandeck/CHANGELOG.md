# Changelog

All notable changes to Plandeck are recorded here. The format follows Keep a
Changelog, and versions follow semantic versioning.

## [0.3.0] (2026-07-14)

### Added
- Mission journal in `.plandeck/journal.ndjson` for observed plan loads, card additions and removals, effective column changes, status changes, receipt fingerprints, archive lifecycle events, and doctor restores.
- Last-known-good snapshots with Windows-safe compact timestamps and retention of the newest 20 changed plan versions.
- `plandeck journal` with timestamp filtering, entry limits, human output, and JSON output.
- `plandeck doctor` for health reports, snapshot diffs, and explicit atomic restore to `plan.yaml`, with replaced content preserved in `plan.yaml.corrupt`.
- `GET /<slug>/api/journal` on each live board.
- Actor attribution through `--actor` or `PLANDECK_ACTOR` for board, next, archive, and doctor observations.
- Stable `stateHash` output from `plandeck next --json`, plus `next --since <hash>` for low-cost unchanged polling.

### Changed
- `NEXT.md` now includes the newest five journal events in chronological order under `Since you left`.
- `NEXT.md`, plan restore, corruption backup, and last-state cache writes now use atomic replacement. Immutable snapshot files use exclusive creation.
- Continuity failures warn once and do not block board, next, or archive operations.
- The Windows-safe test entrypoint now runs 62 `node:test` checks with no child-process isolation and no new dependencies.

## [0.2.1] (2026-07-14)

### Added
- Verified temporary hub breadcrumbs, which let later commands discover a hub on a fallback or ephemeral port.
- Observed velocity from completion history when no configured rate exists. Derivation requires three dated completions across at least one day, and ETA output reports its basis.
- One-day aging for blocked cards, an mtime-based note cache, and completion-check warnings for orphan or missing note files.

### Changed
- Unestimated cards count as one point in both progress rollups and critical-path calculations.
- `plandeck archive` removes only completed card line ranges from `plan.yaml`, preserves surrounding formatting and comments, replaces each output file atomically, and refuses an id already present in `archive.yaml`.
- Hub mutation endpoints require JSON and an approved loopback Host header.

### Fixed
- Every occupied port-ladder rung is checked for a compatible hub before another port is tried.
- A note file that disappears during a rebuild no longer removes a healthy board, and an idempotent registration cannot return an evicted record.
- Hub done counts now include archived cards, and the hub live indicator reflects the SSE connection state.
- Unchanged `NEXT.md` content no longer triggers another file write.
- Oversized registration bodies return 413 and close their connection without leaving unread bytes for a later request.
- A plan with no live or archived cards now reports that it has no cards instead of reporting completion.

## [0.2.0] (2026-07-14)

### Added
- Multi-board hub with one root index, collision-safe board paths, hub-level live updates, explicit unregister support, and cleanup when a plan disappears.
- `plandeck archive`, which moves completed cards into `archive.yaml` and appends on repeat runs.
- Archived card count in the board header and archived progress metadata in the board payload.

### Changed
- A second board process registers with an existing Plandeck hub on the requested port. Non-Plandeck listeners still trigger the port ladder.
- Archived card IDs satisfy dependencies, and their points remain in done and total progress.
- The board watcher refreshes `NEXT.md` after every valid plan change.
- Parse errors retain and serve the last good board state with a visible stale-state warning.

### Fixed
- Removed plans now release their watcher and SSE clients instead of remaining in the live board registry.
- Completion checks no longer report archived dependencies as dangling.

## [0.1.0] (2026-07-12)

First release. Private while the visual layer is verified.

### Added
- Deterministic planning engine with no AI in it: topological ready detection (cycle guarded), the critical path as the longest points weighted dependency chain, honest progress rollups, and a single tie broken next action pointer.
- Live Kanban board server (`plandeck board`) with SSE live reload, six lanes, a gold critical path, a progress ring, and a "do this next" banner. Zero dependencies.
- Completion gate (`plandeck check`) that exits non zero on a structural error and reports COMPLETE only when the plan is clean and every card is done.
- Cache safe re entry breadcrumb (`plandeck next`, `--write` emits `NEXT.md`) so an agent knows its one move after a `/clear`.
- `plandeck init` scaffolding, plan templates, four role agent prompts (scout, worker, judge, pm), and a runnable ten card sample plan with a real dependency graph.
- Windows safe port ladder that falls back when 41747 lands in a reserved range.

### Credits
- Grows out of planning-with-files (MIT): durable, crash proof plans on disk plus a deterministic completion gate. The board server, the YAML reader, the intelligence layer, and the rendering are Plandeck's own. See NOTICE.
