---
name: skill-export-audit
description: "Use before ClawHub export: audit skill, fix local + public."
version: 1.0.4
author: Maxwell McClure
license: MIT
metadata:
  hermes:
    tags: [clawhub, skills, publishing, audit, workflow]
    related_skills: [hermes-agent]
---

Audit a local Hermes skill before exporting it to a community registry (ClawHub), and make sure BOTH the local skill and the public version end error-free. Incorrect data is worse than no data: a skill containing a wrong claim is worse than one missing it — delete anything you cannot verify rather than softening it. User-confirmed, user-observable claims (e.g. "verified in-visor (user-confirmed)") ARE verified data: keep them with the attribution. What gets deleted is unattributed, unverified content.

## When to Use
- Publishing a session-built skill to ClawHub (or any registry) for the first time, or as an update.
- The user asks to "clean up / prepare / audit" a skill before upload.
- A published version was found to contain an error or was published from a bad tree, and both local and public copies must be corrected.

## Source of truth
The in-place skill directory (profile `skills/<name>/`) is the ONLY source of truth. Never edit a staged or published copy directly — every fix lands in-place first, then propagates via a corrected publish (Phase 7).

## Phase 1 — Inventory
`find <skill-dir> -type f` — list every file (SKILL.md, references/, scripts/, templates/). Note the leaf-file count: ClawHub's publish `fileCount` equals the leaf-file count — use it to sanity-check that the publish carried everything.

## Phase 2 — Accuracy audit (verify every claim class)
1. **Machine facts** → check against the live system (binary `--version`, install paths, config files).
2. **Engine/API claims** → verify against the LIVE binary: run a small introspection script (e.g. a Godot `-s` script using ClassDB) for defaults, full property lists, and — as important — what does NOT exist. A property that doesn't exist is a finding even when the skill correctly omits it; confirm the omission is right, and confirm error messages quoted in the skill actually fire. Structure the probe as enumeration FIRST (dump the full property/method lists before touching individual properties): an invalid property access is a runtime error that aborts the rest of the enclosing function, so a probe that hits a bad property name returns only the error and silently skips every remaining check.
3. **Code claims** → grep the actual project files the skill references (flags, node names, numeric values, binding counts).
4. **Bundled scripts** → execute every script in `scripts/` against real inputs (a shipped scanner crashed on every real file until it was actually run). A crash is an audit failure, not a note — fix it in-place AND re-run against the same inputs to confirm the fix.
5. **External facts** (upstream releases, file sizes, project abandonment) → web-verify against the primary source (the release page itself), not search snippets.
6. **Cross-file consistency** → every claim in SKILL.md must agree with the reference files. Contradictions between files are the highest-severity defect: one real case had a reference file teaching the exact opposite of the corrected lesson in SKILL.md.
Fix every defect in-place NOW — do not carry known-bad content into staging.

## Phase 3 — Machine-specifics removal
Grep the whole skill directory for machine-specific residue: drive-letter paths, "this machine", "the <project> has X", usernames, hostnames. Replace with either:
- generic phrasing ("a Windows host", `C:/path/to/<proj>` placeholders), or
- explicitly-labeled examples ("example: ...") — an example is not a claim, and is fine to keep.
Keep ecosystem facts that hold for every user of that ecosystem (e.g. a vendor's standard install path). Re-grep to zero before staging.

## Phase 4 — Metadata check
Frontmatter must match the public listing's conventions: same author, same license, description at least as good as the published one, tags complete. Version must be a bump over the server's latest (`clawhub inspect <slug> --json` → `latestVersion`), with a real changelog naming the substantive changes. For a NEW slug, `inspect` errors with "Skill not found or unavailable to this account" — that is confirmation the slug is unused, not a failure; the first version is 1.0.0.

## Phase 5 — Staging hygiene (contamination is the #1 real failure)
- Use a FRESH staging directory with a unique name per publish (e.g. `<name>-stage-<version>`). Never reuse a scratch dir: stale content has survived `rm -rf`/`cp -r` and poisoned a real publish.
- Copy files explicitly, then `diff -r <in-place> <stage>` MUST be clean before any publish attempt.
- Windows: the ClawHub CLI is Node — pass drive-letter paths (`C:/...`); MSYS paths (`/c/...`) fail with exit 1.
- `--dry-run` first; check `would-publish`, the **slug** (verify it matches the intended listing — omitted, it derives from the staging folder name), the version, and `fileCount`.
- **Pre-publish security screen (mandatory, same call as the publish):** the clean `diff -r` above only proves staging == source — if the SOURCE itself was tampered with (a compromised machine, a rogue process), the diff is still clean and the tampering ships. Screen the staged tree itself, immediately before `publish`, in the same command chain: (1) grep the staged tree for the same red flags skill-import-audit Phase 2 lists — credential paths, exfiltration URLs, pipe-to-shell, `eval`/`exec` on fetched content, hidden/zero-width characters, destructive patterns — any hit stops the publish — and screen CODE CONTEXT (URLs, commands, blobs), not prose: a case-insensitive `POST` matches "post-publish" in this very skill, so make patterns precise (a data-upload flag paired with a remote URL, `POST /` followed by a host) or every run drowns in false positives; (2) delta review — fetch the server-stored copy of the currently published version (`clawhub inspect <slug> --json` → `skill.description`, CR-normalized per Phase 6 step 2) and diff it against the staged SKILL.md: only the intended changes may appear, anything else means stop and re-audit from scratch (fresh skill with no published version: skip the delta, the pattern screen is the check). Ninja edits between audit and upload surface here.

## Phase 6 — Publish + verify what the server actually holds
Stop at `--dry-run` until the user explicitly confirms the real publish — dry-run is side-effect-free and safe to re-run, while the real publish is the workflow's one irreversible step (retraction is possible but costs a reserved version number — Phase 7). This pause is MANDATORY and is NOT satisfied by prior authorization: an original request like "audit and publish it" does not count as confirmation. Present the audit result and the dry-run output, then wait for a fresh, explicit go-ahead AFTER the user has seen that evidence.
1. After explicit confirmation, publish for real with an explicit `--slug <stable-slug>` (no dry-run); capture the `versionId` if the CLI prints one (it omits the id when the version goes straight into the pending queue — that is not an error; the inspect comparison is the verification). The slug must ALWAYS be passed explicitly: omitted, the CLI derives it from the folder name, and a unique staging dir (`<name>-stage-<version>`) would create a *new* listing at a new URL on every publish instead of bumping the existing one.
2. `clawhub inspect <slug> --json`: the denormalized `skill.description` field shows the SKILL.md the server actually STORED — compare it against the local file AFTER normalizing line endings: the server stores every line with a `\r\r\n` terminator, so strip it first (`server.replace('\r\r\n', '\n')`, or collapse all CR runs) — without that, EVERY publish looks like a mismatch. Residual mismatch = contaminated staging → Phase 7. Because the staged tree passed the Phase 5 security screen, server == local means the public content is exactly what was screened — this comparison IS the post-publish security verification.
3. A new version almost always sits in a pending security-scan queue (publish prints e.g. "Update submitted ... pending security scans before it becomes public") — do NOT re-publish "to push it through". Release is observed, not inferred: `latestVersion.version` does not equal the new version until the queue clears (observed: minutes to ~15 min). Do NOT poll in-session — the tool-call cap (~300 s) kills long poll loops and loses their output. ALWAYS schedule the wait as a one-shot cron: `cronjob_manage` with `action: create`, `name: "<slug> <version> publish verification"`, `schedule: "in 30m"`, and a self-contained prompt — jobs run in a fresh session with no chat context, so the prompt must carry the slug, the expected version, the local SKILL.md path, the line-ending normalization rule (step 2), the expected file count, the note that the `moderation` object is top-level (NOT under `skill`), and the branch instructions: on pass → compare the server-stored copy against the STAGE DIRECTORY for that version (not the in-place tree — in-place may have legitimately moved on to the next version by the time the job runs; the stage dir is the exact tree that was published), then delete the job (`action: list`, then `remove` by its job_id) and report LIVE + compare result; if still pending → report STILL PENDING, delete nothing, re-publish nothing. Then end the turn with one line — "submitted, pending, monitor scheduled" — and let the job's report land in the chat.
4. Never report success from publish `ok:true` alone — the inspect comparison IS the verification.

## Phase 7 — Fix loop: local AND public must both end error-free
Any defect found in any phase (or discovered later) gets fixed in both copies, in this order:
1. Fix in-place (source of truth).
2. `clawhub delete <slug> --version <v> --yes` retracts one version. The CLI constraint is LATESTNESS, not release state: it withdraws "one non-latest version" (released or pending — the help does not distinguish), and the current LATEST version cannot be retracted directly — publish the replacement first, then retract the bad version. Notes: `--reason` is only valid for whole-skill deletion — omit it for a version retraction; the server may report a version as already unavailable (observed in the original incident) — nothing left to retract, continue.
3. Retracted version numbers are RESERVED — bump past them (1.0.1 retracted → next publish is 1.0.2, never reuse 1.0.1).
4. Re-stage (fresh dir, `diff -r` verified) and publish the corrected version.
5. Verify the end state: in-place tree == staged tree == server-stored copy (via inspect), and no audited defect remains in either. Definition of done: **local and public are identical and error-free.**

## Pitfalls
- A clean `diff -r` is not a security check: it proves staging matches source, and a tampered source diffs clean. The staged tree itself must pass the Phase 5 pre-publish screen — in the same call as the publish, so no window remains for a ninja edit.
- Waiting for the pending queue by polling in-session burns the turn: the tool-call cap (~300 s) kills the loop and its output is lost. The 30-minute one-shot cron IS the wait (Phase 6 step 3) — end the chat turn with a one-line status and let the job's report land in the chat.
- Staging-dir reuse poisons the publish (real case: a stale pre-audit tree was published as 1.0.1 with the old content under a new version number). Fresh dir + `diff -r` every single time.
- `inspect` shows what the server STORED, not what you SENT — always the post-publish check.
- The current LATEST version cannot be retracted — publish the corrected version first, then retract the bad one; plan the version bump before you need it, not after.
- A just-published version may not appear in `stats.versions` / `--versions` until the pending queue clears (observed behavior); that is normal, not a lost publish.
- MSYS/native path split: bash builtins take `/c/...`; native tools (Node CLI, Python, Blender) need `C:/...`. Redirects to `/tmp` inside a mixed bash+native call also fail — use an explicit scratch path.
- `clawhub search` lists slugs that can be DUPLICATED across owners, and `inspect` has no `--owner` flag — disambiguate as `@owner/slug` (`clawhub inspect @owner/slug`); a bare-slug inspect on a duplicated listing fails or can hit the wrong owner.
- The in-place skill tree is mutable under you: the skill system can rewrite or add files mid-session (observed: a frontmatter description was normalized after staging; a reference file appeared between audit passes) — re-run `diff -r` immediately before the REAL publish and re-stage if it is dirty. A diff that was clean minutes ago is not a diff that is clean now.
