---
name: multi-channel-skill-publisher
description: |-
  Publish ONE skill to ALL agent-skill channels from a single source of truth: the ClawHub skill registry, a ClawHub bundle-plugin package, and a Claude Code plugin marketplace (plain GitHub repo). Use when the user wants to publish, release, rename, or version-bump a skill/plugin across registries, or asks how to package a skill as a Claude Code plugin or OpenClaw bundle plugin. Covers the SSOT/sync model against redundancy, exact manifests (plugin.json, marketplace.json, openclaw.plugin.json), known CLI bugs and their web-UI workarounds (rename, --name, display-name fallback), versioning pitfalls (permanent versions, highest-version-wins display name, web-UI version drift), how to pass the registry security scan, and publish gotchas (version must exceed live on BOTH namespaces, push before source-linked package publish, name-driven search).
---

# multi-channel-skill-publisher

Release one skill everywhere — without maintaining three diverging copies.

## The three channels

| Channel | What it is | Publish via |
|---|---|---|
| **ClawHub Skill** | searchable skill registry entry | web UI (most reliable) or `clawhub publish <dir> --slug <slug>` |
| **ClawHub Package** (bundle-plugin) | plugin package, source-linked to a GitHub commit | `clawhub package publish <abs-path> --family bundle-plugin …` |
| **Claude Code plugin** | installable via `/plugin` from a plain GitHub repo | just `git push` — the repo IS the marketplace |

## 0. Layout: one source of truth (SSOT)

Never hand-maintain copies. Canonical files live once, everything else is generated:

```
repo/
  SKILL.md            <- SSOT (canonical skill text; YAML frontmatter: name + description)
  skill.json          <- SSOT (registry metadata; THE version number lives here)
  sync.py             <- copies SSOT into every target + stamps the version everywhere
  clawhub-skill/      <- generated copy for clawhub publish
  plugin/                          <- the ONE plugin folder, served to BOTH plugin channels
    .claude-plugin/plugin.json     <- Claude Code manifest (name, displayName, version, …)
    openclaw.plugin.json           <- OpenClaw manifest, REQUIRED for bundle-plugin publish:
                                      {"id": "...", "name": "...", "version": "...", "configSchema": {}}
    skills/<name>/SKILL.md         <- generated from SSOT
    commands/<name>.md             <- optional slash command ($ARGUMENTS)
  .claude-plugin/marketplace.json  <- makes the repo its own Claude Code marketplace:
                                      {"name": "...", "owner": {...}, "plugins": [{"name": "...", "source": "./plugin"}]}
```

`sync.py` (concept): read version from `skill.json`, copy SKILL.md into `clawhub-skill/` and `plugin/skills/<name>/`, stamp the version into `plugin.json`, `marketplace.json`, `openclaw.plugin.json`. Run it after EVERY edit of the SSOT files.

## Release procedure

1. **Edit only the SSOT files** (SKILL.md, skill.json).
2. **Bump the version** in skill.json — it must be HIGHER than what is live on **both** namespaces:
   ```bash
   clawhub inspect <skill-slug>          # skill: Latest: x.y.z
   clawhub package explore <plugin-name> # package: [Bundle Plugin] version
   ```
3. **Sync:** `python3 sync.py`
4. **Commit + push** — MANDATORY before step 6 (the package publish links a commit SHA that must exist on GitHub):
   ```bash
   git add -A && git commit -m "Version -> <v>" && git push
   git rev-parse HEAD
   ```
   First release ever? Bootstrap repo + push in one step: `gh repo create <owner>/<repo> --public --source . --push`
5. **Publish the skill.** For a FRESH publish (new slug, no rename) the CLI works — use an ABSOLUTE path:
   ```bash
   clawhub publish "$(pwd)/clawhub-skill" --slug <skill-slug> --name "<Display Name>" --version <v>
   ```
   When a rename is involved or the CLI misbehaves, use the **web UI**:
   skill page → new version → **re-select the folder fresh** (browser caches the old selection) → type the display name EXACTLY into the name field → set version → publish.
6. **Publish the package (bundle-plugin)** — CLI works reliably here; use an ABSOLUTE path:
   ```bash
   clawhub package publish "$(pwd)/plugin" \
     --family bundle-plugin \
     --name <plugin-name> --display-name <DisplayName> \
     --version <v> \
     --host-targets claude-code \
     --source-repo <owner>/<repo> \
     --source-commit <HEAD-SHA> \
     --source-ref refs/heads/main \
     --source-path plugin
   ```
7. **Claude Code channel:** nothing to do — users install with
   `/plugin marketplace add <owner>/<repo>` → `/plugin install <plugin-name>@<marketplace-name>`.

## Verify

```bash
clawhub inspect <skill-slug>             # Latest == <v>
clawhub package explore <plugin-name>    # Bundle Plugin == <v>
```

Right after publishing, `clawhub inspect` returns **"Skill is hidden by moderation (pending.publication)"** until the security scan clears — transient at first, NOT a failed publish. Poll every ~30 s instead of republishing. Similarly, `clawhub package inspect <name>` may say "Package not found" while `package explore` already lists it (indexing/moderation lag) — trust `explore` for existence.

If it STAYS hidden: your content likely tripped the scanner (see the security-scan gotchas). `clawhub unhide <slug> --yes` does NOT work — moderation hides are Forbidden for the owner ("contact a moderator"). Self-serve fix: clean the flagged content, bump, and publish a higher version; escalate to a moderator only if that doesn't surface it. Meanwhile the profile page shows the skill missing under "Skills" while the plugin twin is visible under "Plugins" — that asymmetry is the tell that moderation, not the publish, is the problem.

## Gotchas — CLI bugs & workarounds (each cost a real debugging session)

- **`clawhub rename` is broken:** it errors `newSlug required` even when the new slug IS provided. Rename via the **web UI** instead. And after a rename, CLI `publish` may still only match the **original** slug — another reason the web UI is the safer skill-publish path.
- **`--name` on `clawhub publish` (skill flow) can throw a server error** — observed on EXISTING/renamed skills; on a fresh first publish (CLI v0.9.0) it worked fine. If it errors: omitting it makes the display name fall back to the folder name (you get a skill literally called "Clawhub Skill"); fix by typing the display name **exactly** into the web UI name field.
- **Web-UI upload caches the folder selection.** After editing files, re-select the folder fresh or the scanner shows stale content. Sanity check: the file list/preview must show your newest files.
- **EVERY clawhub path argument must be absolute** — both `clawhub publish` (skill) and `clawhub package publish` error with `Path must be a folder` on a relative path. Always pass `"$(pwd)/<dir>"`.
- **After a failed publish the server rate-limits retries** (~45 s). Don't hammer; fix the cause, then retry once. Read errors (`inspect`, `package inspect`) carry the hint too — the `(reset in Ns)` suffix tells you how long to wait.

## Gotchas — registry behavior

- **ClawHub search is NAME-driven, not description-semantic.** Put the search tokens users will type into the skill *name/slug* (e.g. `known-error-fixes-database`), not only the description.
- **Skill and package namespaces are separate.** The same name can exist as both; `clawhub inspect <name>` may hit the skill entry — use `clawhub package inspect` / `package explore` for packages.
- **`--family code-plugin` requires a `package.json`** (it means a Node/code plugin, e.g. an MCP server). A skill bundle is `--family bundle-plugin`.
- **`bundle-plugin` requires `openclaw.plugin.json`** at the plugin root — minimal valid manifest: `{"id", "name", "version", "configSchema": {}}`. `hostTargets`/format do NOT go in the manifest; they are CLI flags (`--host-targets`, format auto-detects `claude` from `.claude-plugin/plugin.json`).
- **Downloads ≠ installs.** Registry download counters include fetch/crawler noise; treat installs and real usage signals as adoption truth.
- The Claude Code marketplace needs the repo to be **public**; a fresh `git push` is all a "release" takes on that channel.

## Gotchas — versioning bugs

- **Versions are permanent and the display name follows the HIGHEST version number.** A stray high version from CLI experiments hijacks the displayed name (and cannot be deleted); the only fix is publishing an even higher version. Never publish throwaway/test versions to your real slug.
- **"Version already exists" errors** mean the live version is >= yours. Check BOTH namespaces before bumping (skill and package are versioned independently — `clawhub inspect <skill-slug>` + `clawhub package explore <plugin-name>`).
- **Web-UI publishes bypass your repo → version drift.** Publishing (or auto-bumping) via the web UI updates the registry but NOT your local `skill.json`; the next repo-driven release then fails as "too low" or silently ships an older number. After ANY web-UI publish, write the live version back into the SSOT `skill.json` and run `sync.py`.
- **Keep ONE monotonic version across all channels.** The sync script must stamp the same number into `skill.json`, `plugin.json`, `marketplace.json`, and `openclaw.plugin.json` — hand-edited manifests drift apart within a release or two.

## Gotchas — passing the registry security scan

- **Never include consent-weakening phrasing in a skill** — any wording that tells the agent it may skip asking the user before acting. Scanners flag it as Description-Behavior Mismatch / Missing User Warnings. Phrase outbound actions **condition-based** instead: "report X once you have acted on it; contribute when all N criteria apply."
- **The string matcher does not know use from mention.** Quoting a forbidden phrase verbatim as a warning example puts that exact string in your skill — and gets IT flagged. Describe banned phrasings, never quote them. (The most plausible reason this very skill got moderation-hidden on its first publish while its plugin twin sailed through: the skill scan reads SKILL.md content, the package channel doesn't gate on it.)
- **Vague triggers get flagged** ("error", "stuck", "fix") and over-trigger. Use narrow, specific phrases ("recurring error", "seen this error before").
- **A scan "Pass" coexists with Medium findings** — those are advisory, not blocking. Read them, fix what's real, don't panic over the rest.
