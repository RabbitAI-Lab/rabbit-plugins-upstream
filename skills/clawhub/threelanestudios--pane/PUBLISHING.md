# Publishing this skill

Matt runs these himself — this file is a reference, not something the agent
should execute unattended.

## One-time setup

```bash
npm i -g clawhub
clawhub login
clawhub whoami
```

## First publish

```bash
clawhub skill publish ./pane \
  --slug pane \
  --name "Pane" \
  --version 1.0.0 \
  --changelog "Initial release: conversational note/task/project ops via chat sessions, session/chat/sync REST operations"
```

Org-scoped target (if publishing under the Three Lane Studios org handle):

```bash
clawhub skill publish ./pane \
  --slug @ThreeLaneStudios/pane \
  --name "Pane" \
  --version 1.0.0 \
  --changelog "Initial release: conversational note/task/project ops via chat sessions, session/chat/sync REST operations"
```

Dry-run first if the CLI supports it, to confirm the publish plan before
uploading:

```bash
clawhub skill publish ./pane --dry-run
```

## Subsequent versions

```bash
clawhub skill publish ./pane --version 1.1.0 \
  --changelog "Describe what changed"
```

## Tag management

```bash
clawhub skill publish ./pane --version 1.0.0 --tags latest
```

## Consumer-side testing (before/after publish)

```bash
openclaw skills search "pane"
openclaw skills verify pane
openclaw skills install pane
openclaw skills install pane --version 1.0.0
```

## Notes

- `clawhub skill publish` reads `SKILL.md` frontmatter (`name`, `description`,
  `version`, `metadata.openclaw.*`) — keep `requires.env` in sync with any
  new env vars referenced in the body, or the security scanner will flag a
  declared-vs-used mismatch.
- All ClawHub skills publish under MIT-0. No per-skill license override.
- `export CLAWHUB_DISABLE_TELEMETRY=1` to suppress install-event reporting
  during testing.
- v1 scope note: the Pane Gateway does not expose direct note/task/project
  CRUD REST routes. If/when `src-gateway/src/routes/` gains
  `/v1/notes`/`/v1/projects`/`/v1/tasks` routes mirroring
  `get_pane_tools()`, update `SKILL.md` and `references/gateway-api.md`
  accordingly and bump the minor version.
