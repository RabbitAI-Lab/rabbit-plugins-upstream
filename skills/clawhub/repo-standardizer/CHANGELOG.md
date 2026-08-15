# Changelog

All notable changes to this project are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versions follow [SemVer](https://semver.org/).

## [Unreleased]

## [v0.2.7] - 2026-08-14

### Changed

- Surface-only positioning: SKILL.md description + intro, README (en + zh)
  tagline and Safety-by-design now state clearly that the skill polishes a
  repo's surface (labels, templates, CI configs, rulesets, docs) and never
  touches code logic; GitHub repo description updated with the same wording
- Repo moved from `programmingHLS` to `programmingWTF` (personal account, per
  Guiyu's call — consistent with ClawHub publisher identity); all path
  references updated (README badges/install/usage, issue-form config,
  SECURITY.md, AGENTS.md); old URL redirects automatically

## [v0.2.6] - 2026-08-14

### Changed

- Emoji policy relaxed: rating tiers (`rating:*` / `issue-rating:*`) are now
  the ONLY mandatory-emoji labels (clear low→high gradient); all other
  labels leave emoji to the agent's judgment
- Consistency rule added: within one dimension, either ALL labels carry an
  emoji or NONE do — never a mixed half-emoji dimension
- `templates/labels.json` baseline now ships plain names (no emoji) —
  `bug`, `P0`–`P3`, `status: *`, `dependencies`, `security`…; impact labels
  were already emoji-free, so every dimension is now consistent
- SKILL.md / LABELS.md / README (en + zh) wording updated to the new policy

## [v0.2.5] - 2026-08-13

### Changed

- description updated to reflect the fuller taxonomy: P0–P3 priority, impact
  severity, auto-close rules
- SKILL.md Module A: bot-label language exception — `r:*` / `clawsweeper:*` /
  `triage:*` / `close:*` names stay in the bot's language (automation matches
  literal names); only their description uses the user's language

## [v0.2.4] - 2026-08-13

### Added

- Preflight step 6: ask whether the repo has automation bots / AI writers
  (dependabot, Stale, ClawSweeper, AI coding agent…) — the answer decides
  whether the Governance / auto-close-rules labels are added at all, with the
  reasoning spelled out
- Module A Governance dimension now gated by Preflight step 6

## [v0.2.3] - 2026-08-13

### Added

- SKILL.md Module A: `Governance / auto-close rules` dimension — `r:*` and
  bot-state labels (`clawsweeper:*`, `triage:*`, `close:*`) are **signal
  labels, not categories**, only meaningful when a governance bot actually
  runs on the repo; skip them otherwise

## [v0.2.2] - 2026-08-13

### Changed

- Priority labels switched to `P0`–`P3` (OpenClaw convention; `P0` = emergency)
- Added `impact:` severity dimension — security / data-loss / availability /
  auth-provider / session-state / message-loss / ux-blocker / ux-friction
- SKILL.md Module A rewritten into a full dimension menu mirroring OpenClaw's
  official taxonomy — every dimension is opt-in ("add only if the repo needs
  it"), Type is the only mandatory one
- Label language rule: names + descriptions follow the user's chosen language
  (Preflight step 5)

## [v0.2.1] - 2026-08-13

### Changed

- Label taxonomy now uses emoji prefixes across **every** category (type,
  priority, status, team, rating) — not just rating tiers — so the whole set
  is scannable at a glance
- SKILL.md: emoji-prefix rule promoted from rating-only to the full taxonomy;
  Module A tables and examples updated
- SKILL.md description + README tagline rewritten for discoverability — adds
  `professionalize`, `tidy up`, `polish`, `emoji label taxonomy` trigger words

### Added

- `templates/labels.json`: emoji-prefixed baseline labels (🐛 ✨ 📚 ❓ 🙋 🌱
  🔴🟠🟡🟢 🧱🚧✅🎉🚫 📦 🔒)

## [v0.2.0] - 2026-08-11

### Changed

- Repositioned as an agent-agnostic skill (not OpenClaw-specific): works with
  any skills-enabled agent — Claude Code, Cursor, Copilot, OpenClaw, etc.
- README (en/zh): tagline now reads "A skill…" + agent-agnostic note;
  install section leads with the generic `npx skills add` path
- AGENTS.md / docs/ARCHITECTURE.md: dropped the "OpenClaw skill" self-description

## [v0.1.9] - 2026-08-11

### Fixed

- Release workflow: changelog regex now excludes the title date from the
  extracted release body

## [v0.1.8] - 2026-08-11

### Changed

- Release workflow: Release body now rendered from the `CHANGELOG.md` entry
  for the tag (modeled on OpenClaw official) instead of auto-generated notes
- SKILL.md: language preference asked up front (Preflight step 5) —
  `CONTRIBUTING.md` and PR template are written in the user-chosen language
- AGENTS.md: all commit messages, PR titles/bodies, and repo communication
  are in English

## [v0.1.7] - 2026-08-11

### Added

- `VISION.md`, `THIRD_PARTY_NOTICES.md`, `docs/ARCHITECTURE.md`
- SKILL.md Module F: VISION / THIRD_PARTY_NOTICES / ARCHITECTURE / CHANGELOG generation
- Templates: `VISION.md`, `CHANGELOG.md`

## [v0.1.6] - 2026-08-11

### Added

- Bilingual README: `README.md` (English, default) + `README.zh.md` (简体中文) with switcher line
- `AGENTS.md` + `CLAUDE.md` (symlink) — AI assistant guides (Telegraph style, modeled on OpenClaw official)
- SKILL.md Module F: README language workflow (ask which languages; ccmm-style switcher)
- SKILL.md Module G: AI assistant guides generation
- Templates: `AGENTS.md`, `CLAUDE.md`, `README.zh.md`

## [v0.1.5] - 2026-08-11

### Changed

- Commit style: `type(scope): description` in CONTRIBUTING (template + repo)

## [v0.1.4] - 2026-08-11

### Changed

- README title (drop emoji) — remote edit by Guiyu Li

## [v0.1.3] - 2026-08-11

### Added

- `CODE_OF_CONDUCT.md` (adapted from Contributor Covenant v2.1) + template
- SKILL.md Module F: CoC included in docs module

## [v0.1.2] - 2026-08-11

### Changed

- Rating-label rules: no verbatim copying of any repo's tier system; emoji/icons + gradient + `LABELS.md` documentation required
- OpenClaw official `rating:` tiers used as example only

### Added

- Template: `LABELS.md` (rating label documentation)

## [v0.1.1] - 2026-08-11

### Changed

- Label taxonomy: project-aware design (audience-based rating tiers, optional `team:*` labels, semantic diverse colors)
- `labels.json`: wontfix gray, added `status: ready to merge` / `status: merged` (greens)

## [v0.1.0] - 2026-08-11

### Added

- Initial release: SKILL.md + 15 templates (labels, issue forms, PR template, CI for Node/Python/Go/Rust, CODEOWNERS, CONTRIBUTING, SECURITY, README)
- Automated release workflow: `v*` tag → build standard skill zip → publish Release
- Repo self-standardized: 19 labels, issue forms, PR template, rulesets protecting `main`
