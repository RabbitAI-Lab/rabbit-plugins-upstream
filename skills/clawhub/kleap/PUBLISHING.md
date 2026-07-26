# Publishing to ClawHub — step by step (founder-only, do not run without OK)

**Nothing here has been run against the live registry.** Everything below was
verified locally (auth-free) with the official `clawhub` CLI **v0.23.1**
against this exact folder. Only the final `clawhub skill publish` (without
`--dry-run`) actually pushes anything — every command before it is read-only /
local. Where the CLI and its published docs (`docs/cli.md`) disagree, the
commands below stick to doc-listed flags; extras verified present in the
v0.23.1 CLI are called out separately.

## 0. Prerequisites

- Node ≥ 18.
- `npm i -g clawhub` (or `npx clawhub@latest ...` for every command below —
  no global install needed).
- A ClawHub account — created by the browser sign-in on first `clawhub login`.

## 1. Confirm the `kleap` slug is still free

```bash
npx clawhub search kleap
```
Checked 2026-07-03: **no results** — the `kleap` slug is free. Re-run this
immediately before publishing in case that's changed.

## 2. Log in (one-time per machine)

```bash
npx clawhub login
# opens a browser to authorize this machine; on a headless box use
# --no-browser (prints a verification URL to open elsewhere) or
# --token <token> to store an existing API token directly.
npx clawhub whoami
# confirms the logged-in handle
```

Decide **who publishes it**: your personal handle, or a shared `kleap`
publisher org (recommended, matches the project rather than one person):

```bash
npx clawhub publisher create kleap
# creates an org publisher you own; lets you publish as --owner kleap
# instead of your personal handle, and add teammates later.
```

## 3. Dry-run (already verified — safe, no network write, no login needed)

**The published slug derives from the folder name** when no override is
given (verified: this folder dry-runs as slug `kleap-openclaw-skill`; a copy
named `kleap/` dry-runs as slug `kleap`, display name `Kleap`). So publish
from a copy of this folder named `kleap`:

```bash
cp -r kleap-openclaw-skill kleap
npx clawhub skill publish ./kleap --dry-run --json
```

Verified output (run 2026-07-03 against this content):

```json
{
  "ok": true,
  "status": "would-publish",
  "slug": "kleap",
  "displayName": "Kleap",
  "version": "1.0.0",
  "latestVersion": null,
  "fileCount": 5
}
```

(`fileCount: 5` = `SKILL.md`, `references/recipes.md`,
`references/troubleshooting.md`, `README.md`, `PUBLISHING.md` — this file
ships too; it's founder-facing docs, harmless alongside. The CLI also prints
a `fingerprint` hash, omitted here because it changes with any content edit.)

This confirms: the frontmatter YAML parses, the slug resolution is right, and
the CLI accepts the folder as a valid skill — no ClawHub account is needed
for a dry-run, which is why it was safe to run without asking first.

## 4. Publish for real (REQUIRES EXPLICIT FOUNDER GO-AHEAD — do not run otherwise)

```bash
npx clawhub skill publish ./kleap --owner kleap
```

That's the whole command — slug `kleap` and display name `Kleap` come from
the folder name (step 3), the version defaults to `1.0.0`, and the tag
defaults to `latest`. Drop `--owner kleap` to publish under your personal
handle instead (then skip step 2's `publisher create`).

Optional flags — **not in `docs/cli.md`, but verified present in CLI
v0.23.1** (`clawhub skill publish --help`, and accepted by dry-run); if a
future CLI version rejects one, just drop it:

- `--slug kleap --name "Kleap"` — pin the slug/name explicitly instead of
  relying on the folder name (useful if you can't rename the folder).
- `--changelog "<text>"` — e.g.
  `"Initial release — create, edit, publish, and connect a domain for a live site via the kleap CLI (npx @eliottd/kleap)."`
- `--source-repo Kleap-co/kleap --source-path skill-openclaw` — provenance
  link back to the canonical repo; only set these **after** this folder is
  actually committed there at that path (see "Where should this folder
  live?" below); otherwise omit.

Re-publishing later: run the same command on the changed folder — the CLI
auto-bumps the next patch version (or pass `--version` explicitly);
unchanged content is skipped, not re-published. All ClawHub skills are
licensed `MIT-0` on publish, no exceptions — same posture as the
MIT-licensed `Kleap-co/kleap` CLI, nothing to add here.

## 5. Verify it landed

```bash
npx clawhub search kleap
npx clawhub inspect @kleap/kleap
# inspect fetches the published metadata + file list without installing.
# Replace @kleap with the actual publishing handle if it wasn't the org
# (i.e. @<your-handle>/kleap).
```

CLI v0.23.1 also has `clawhub skill verify kleap` ("verify a published skill
using ClawHub security evidence" — listed in `clawhub skill --help`, not in
`docs/cli.md`); worth running as an extra post-publish check if present in
your CLI version.

## Where should this folder live long-term?

Right now it's a standalone package in the scratchpad. Two reasonable
homes, founder's call:
- **Inside `Kleap-co/kleap`** as `skill-openclaw/` (keep it distinct from the
  existing `skill/` folder, which is the Claude/MCP-tool-call version — see
  `README.md` → "Relationship to the existing Claude skill"). Then the
  optional `--source-repo`/`--source-path` flags in step 4 link the listing
  to it, and future CLI releases can update both skills in the same commit.
- **A new standalone repo** (e.g. `Kleap-co/kleap-openclaw-skill`) if the
  team wants the OpenClaw listing to version independently of CLI releases.

Either works with the `clawhub skill publish` command above; only the
optional provenance flags change.
