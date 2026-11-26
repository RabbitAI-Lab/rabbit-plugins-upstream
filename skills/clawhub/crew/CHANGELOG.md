# Changelog

## 1.3.3 — 2026-11-26

- The crew / sub-agent / direct-call comparison is now a Markdown table with ★ ratings and short notes.

## 1.3.2 — 2026-11-26

- README, README.en and SKILL.md: when to use crew, a sub-agent or direct `codex exec` calls, with a rating table.

## 1.3.1 — 2026-11-26

- `watch [--nudge]`: finds members stopped at their prompt after a connection error and, with `--nudge`, tells each to resume its registered task. `board` reads a wider pane tail for the busy state.

## 1.3.0 — 2026-11-26

- `board [--text]`: every member's state (busy / idle / offline, read from the pane) with its current and scheduled tasks.
- `board` reads the model shown in each Codex pane and flags it when it differs from the configured one (`⚠ 模型被换了`).
- `task --now/--next/--done/--clear-next [--for NAME]`: members record their own tasks in `<project>/.crew/tasks.json`; main may record for others.

## 1.2.1 — 2026-11-25

- Point-to-point messaging documented: any member may `send` to any member directly, including members of another group with `--dir <their project>`.
- Cross-group `send` now names the sender as `<group>/<member>` and appends how to reply (`crew send --dir <sender project> --to <member>`), instead of `guest`.

## 1.2.0 — 2026-11-24

- `quota`: remaining quota for Codex (session logs), Claude Code (`/usage` cache, refreshed in a hidden terminal) and agy (its own status-line data). Local reads only; `CREW_NO_QUOTA=1` turns them off.
- `advise --task <type>`: recommends a model from quota, a leaderboard snapshot and personal preferences, with reasons.
- `rankings`: status / show / import / schema for `~/.config/crew/rankings.json`; the main agent refreshes it from arena.ai when older than 30 days.
- Personal preferences in `~/.config/crew/roles.json` (task → preferred models, thresholds, Claude menu).
- `models` shows remaining quota per option and lists only installed CLIs; `spawn` warns when the chosen model's quota is below 20%.
- `doctor`: checks dependencies, model lists, quota sources and config.
- Leaderboard matching compares dotted versions correctly (4.6 < 5) and never lets an older model stand in for the one an alias starts.
- agy menu no longer hides any family; the menu is simply each CLI's first two models.
- Bilingual: English + Chinese description, an English overview at the top of SKILL.md (agents reply in the user's language), full English README (`README.en.md`).
- Scope stated plainly: macOS + iTerm2; Claude Code, Codex and agy.
- ClawHub metadata (`metadata.openclaw`), permissions and privacy section, MIT-0 license.

Verified with Claude Code 2.1.331, codex-cli 0.172.0, agy 1.5.16 on macOS (python3 3.9 and 3.13).
