# GTM Coach changelog

The full Skill bundle uses one Semantic Version. A release covers `SKILL.md`, stage modules, project-type modules, channel modules, schemas, and API guidance.

## 1.3.0 — 2026-09-15

### Added

- Persist the full Skill bundle into the **current agent’s** skills folder (Cursor, Claude Code, Codex, WorkBuddy/CodeBuddy) so later chats can invoke GTM Coach in natural language.
- Shared workspace `.gtm/` remains the only project memory. Switching agents reuses the plan; the new host still needs its own skill install.
- Description triggers for weekly GTM, CMO board, traffic/growth, this week, and resume `.gtm` (English, for cross-agent routing).

### Changed

- Session engine starts with persist-if-missing, then resume `.gtm/plan.json` (never re-init when a plan exists).
- Skill refresh also overwrites this host’s persisted skills copy. Tokens never go in a skills folder.

### Guardrails

- `.cursor/skills/` is not visible to Codex, Claude Code, or WorkBuddy. Install per host.
- Copy or symlink the whole `gtm-coach/` directory, not `SKILL.md` alone.

## 1.2.1 — 2026-09-15

### Changed

- One canonical CMO board template for every turn (stage, constraint, scored channels, this week).
- Evidence values match `plan.json`: `none` · `anecdote` · `pains_scored` · `waitlist` · `paying`.
- Auth header no longer uses HTML-like angle brackets, so published markdown keeps the token instructions.
- Bound `/status` returns `picture` hints (period, readiness, evidence) as a hypothesis. `status.next` no longer tells the agent to fetch `/leads`.
- Instrument counts (`leads_pending`, `replies_posted_7d`) may appear on the board; they are not ICP activation.
- First write copies `plan.example.json`. Load `reference.md` only then, or when schema/API changed.
- Write `.gtm/` at the workspace root for the bound project, even inside a monorepo.

### Guardrails

- Do not echo a pasted `nmagt_` key.
- Ask optional Nichestarter monitoring only after the board, never as the weekly task.

## 1.2.0 — 2026-09-15

### Changed

- Strategy turns now publish a professional CMO board: stage, evidence, constraint, and scored channels. The stage stays visible every turn.
- Load the stage SOP and project-type SOP for that board. Load a channel SOP only after the founder chooses to execute or inspect that channel.
- Reddit/Facebook: list NicheReach leads as clickable URLs only. Do not fetch post bodies. Do not draft comments. The founder opens the URL in the NicheReach Chrome extension.

### Guardrails

- A channel tutorial must not replace the GTM picture.
- `modules.primary_channel` stays empty until a dive.
- Community reply copy is owned by the extension, not the agent.

## 1.1.0 — 2026-09-15

### Added

- Post-value onboarding for users who started the Coach without a project key.
- One-time “Connect this project — free” prompt after the GTM picture and first useful output.
- Clear connection benefits: verified project context, exact project-type SOP, relevant monitoring data, NicheReach thread workflow, and optional NicheMatch handoff.
- Connection state to prevent repeated signup prompts.
- Intent-based Premium prompts only for continuous pain monitoring or NicheReach auto-discovery.

### Guardrails

- No signup interruption before first-run value.
- No claim that local GTM plans sync to the server.
- Declining or deferring connection never reduces the manual Coach.

## 1.0.0 — 2026-09-15

### Added

- Modular loading: one stage SOP, one project-type SOP, and one primary-channel SOP.
- Nine project-type playbooks for apps, services, media, digital products, communities, creators, brands, education, and marketplaces.
- Fourteen channel playbooks including direct outreach, communities, LinkedIn, X, short/long video, email, SEO, launches, events, guest content, partnerships, and paid acquisition.
- Project-scoped Nichestarter monitoring rules with no public-library fallback.
- Optional NicheReach discovery prompt and clickable-thread reply workflow.
- Weekly experiment tracking: hypothesis, meaningful metric, review trigger, and continue/change/stop decision.
- Cross-agent update protocol with automatic version check and approval before refresh.

## Version policy

- **PATCH** (`1.0.x`): compatible fixes, clarifications, and safety improvements.
- **MINOR** (`1.x.0`): backward-compatible modules, channels, capabilities, or API fields.
- **MAJOR** (`x.0.0`): breaking plan schema, workflow, security, or API behavior. Requires explicit migration approval.

Release notes never authorize external actions. New publishing, messaging, spending, or write capabilities remain preview-first and require founder approval.
