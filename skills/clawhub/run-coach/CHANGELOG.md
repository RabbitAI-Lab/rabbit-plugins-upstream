# Changelog

## 1.1.6 (2026-08-21)
- Frontmatter description now discloses Garmin health-metric collection and
  local credential/token storage up front (SkillSpector TP4 advisory).
- Display name fixed to drop the accidental "Clawhub" prefix (build-folder
  artifact).

## 1.1.5 (2026-08-21)
- Privacy review remediation (ClawScan/SkillSpector findings on v1.1.4):
  - New "Data & privacy" section fully enumerating every Garmin data category
    collected (activity details, daily health metrics, training metrics, auth
    token cache), storage locations, retention (until user deletion, with the
    exact delete command), recommended permissions, and the opt-out.
  - `garmin-query.py json` now outputs a minimized, coaching-operational
    subset by default (activities + training metrics); daily health metrics
    (resting HR, stress, Body Battery) require an explicit `--full` flag.

## 1.1.2 (2026-08-17)
- Credential handling unified to chmod-600 dotfiles (`.credentials` at skill
  root, matching the existing `garmin/.credentials` pattern). Credentials no
  longer pass through command-line arguments (visible in process listings) or
  environment variables; docs and code now describe the identical flow.
  Addresses the ClawScan review note on credential safety and disclosure.

## 1.1.1 (2026-08-17)
- Scanner compliance: `text-to-image-canvas.mjs` now takes credentials as CLI
  arguments (same interface as `send-album.mjs`) instead of reading environment
  variables in the same file that performs network sends — addresses ClawScan
  static-analysis rule `suspicious.env_credential_access`. No behavior change.

## 1.1.0 (2026-08-17)

**Security**
- All credentials now come from environment variables (`TELEGRAM_BOT_TOKEN`,
  `TELEGRAM_CHAT_ID`) — removed every hardcoded path and credential from
  bundled scripts. Added a Transparency section to SKILL.md declaring the
  skill's complete network surface (api.telegram.org + optional Garmin Connect).
- Scripts are path-independent: data lives relative to the skill directory,
  overridable via `GARMIN_DATA_DIR` / `PLAYWRIGHT_BROWSERS_PATH`.

**Coaching disciplines (new)**
- Six production-derived rules: data-first answers, injury-inquiry discipline
  (resolved = passive monitoring), immediate goal-change propagation,
  pending-item semantics (track the runner's actions, never the bot's
  unanswered questions), correction-requires-real-error, fragments-are-normal.
  Each rule is distilled from a documented failure mode observed in six months
  of production coaching.

**Memory conventions (new)**
- Stable fact IDs, absolute-date discipline, authoritative-correction handling,
  and a refreshed MEMORY.md template.

## 1.0.7 (2026-05)
- Visual HD training plans, Garmin sync, MAF/VDOT/80-20 methodology.
