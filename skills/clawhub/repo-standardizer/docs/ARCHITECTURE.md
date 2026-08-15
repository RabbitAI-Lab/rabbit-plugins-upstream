# Architecture

How the repo-standardizer skill is structured and how it applies a baseline
to a target repository.

## The product

`SKILL.md` is a skill: a set of instructions the agent follows to
standardize a GitHub repository. `templates/` are the concrete artifacts it
places into (or adapts for) the target repo.

There is no runtime code. The skill is executed by an AI agent using the
`gh` CLI and the GitHub REST API.

## Module pipeline

Each run follows: **Preflight → Plan → Apply → Verify**.

| Phase | What happens |
|---|---|
| Preflight | `gh auth status` (stop + guide if not logged in); detect repo type (`User`/`Organization`, `PUBLIC`/`PRIVATE`, archived/fork); audit current state (labels, `.github`, workflows, rulesets, docs); detect test framework |
| Plan | Show a dry-run table (create / update / skip); confirm destructive ops |
| Apply | Modules A–G, each idempotent (see below) |
| Verify | Re-query GitHub; report `applied / skipped / failed` |

## Modules

| Module | Scope | Idempotency mechanism |
|---|---|---|
| A — Labels | design-first taxonomy (type/priority/status/rating/team) | `GET /labels/{name}` → `POST` (create) or `PATCH` (update); no `PUT` endpoint exists |
| B — Issue forms | `.github/ISSUE_TEMPLATE/*.yml` + `config.yml` | diff before overwrite |
| C — PR template | `.github/PULL_REQUEST_TEMPLATE.md` | diff before overwrite |
| D — CI | `.github/workflows/ci.yml` from framework detection | only add if missing |
| E — Rulesets | branch protection on default branch | `POST` if name absent, else `PUT` full-replace (no `PATCH`) |
| F — Docs | README (+languages), CONTRIBUTING, SECURITY, CoC, LICENSE, CHANGELOG | copy from templates if missing; ask before overwriting |
| G — AI guides | `CLAUDE.md` / `AGENTS.md` | diff and fill gaps |

## Release pipeline

`.github/workflows/release-skill.yml`:

1. Trigger: push of a `v*` tag.
2. Build: `SKILL.md` + `templates/` are zipped (no top-level folder) into
   `repo-standardizer-<tag>.zip`.
3. Publish: `softprops/action-gh-release` creates the Release and attaches
   the zip.

Versioning is SemVer with a `v` prefix (`v0.1.6`); tag and zip share the
same name.

## Design constraints

- **Templates stay generic**: `OWNER/REPO` placeholders, never project-specific
  content — they are applied to other people's repositories.
- **Idempotency is a contract**: every module can run twice with the same
  result; user content is never clobbered.
- **API claims are tested**: command examples in `SKILL.md` are verified
  against the live GitHub API (several traps were found only by testing —
  see AGENTS.md "Verification").
- **Dual maintenance**: repository files and the live skill
  (`workspace/skills/repo-standardizer/`) must stay in sync.
