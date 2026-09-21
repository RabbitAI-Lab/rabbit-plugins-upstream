---
name: skill-author
description: 'Author, harden, and publish agent skills for ClawHub — write skills that conform to ClawHub conventions (frontmatter, structure, naming, versioning, licensing), run pre-publish hardening, and remediate clawhub.ai security-audit findings. Use when creating a skill for ClawHub, preparing a new version to publish, or when given a clawhub.ai/<owner>/<slug>/security-audit page.'
version: 1.1.0
license: BSD-3-Clause
description_zh: "撰写、加固并发布符合 ClawHub 规范与惯例的 agent skill：按 frontmatter/结构/命名/版本/许可约定写作 skill，发布前加固，整改 clawhub.ai 安全审计发现。制作要发布的 skill、准备新版本、或拿到 security-audit 页面时使用。"
homepage: https://clawhub.ai/sunshinejnjn/skill-author
metadata:
  openclaw:
    emoji: "🛠️"
compatibility: OpenClaw + ClawHub CLI (`npm i -g clawhub`). Works on any skill folder; conventions verified against the CLI source and live registry.
allowed-tools: Read, Write, Edit, Exec
---

# ClawHub Skill Maker

Make agent skills that are **well-formed for ClawHub**. Four capabilities, in workflow order:

1. **Author** — write a skill that conforms to ClawHub conventions (frontmatter, structure, naming, versioning, license, description style), so it passes review cleanly the first time.
2. **Harden** — pre-publish check: completeness, dead links, secrets, build artifacts, doc↔code consistency, security by design.
3. **Remediate** — fix findings from a `clawhub.ai/<owner>/<slug>/security-audit` page (hard findings → code/config changes; soft findings → docs/policy clarification).
4. **Publish & verify** — `clawhub publish` with a proper changelog, then poll through the moderation queue until `Latest:` flips.

## Know the review model before you fix anything

ClawHub reviews run in two layers:

| Layer | Produces | How to handle |
|---|---|---|
| **Static pattern scan** | **Hard findings** with `file:line` (command injection, hardcoded secrets, instruction hijacking, memory poisoning, remote payload fetch, insecure dependencies) | Must be fixed in code/config — wording changes do not count |
| **LLM review** | **Soft findings** with confidence scores (language/locale policy, agency & consent, doc/code consistency, missing risk disclosures) | High confidence (≥90%) = real; lower = verify first. Usually fixed in docs |

**False positives happen**: path-traversal *defense* code gets flagged as "credential access"; reading the skill's own workflow JSON gets flagged as "memory poisoning". Never delete a guard to "fix" a finding — keep it and explain it in the report to the user.

## 1. Author a ClawHub-conformant skill

Follow the conventions in `references/authoring-guide.md`. The short version:

1. **Check the slug** — `clawhub search "<keywords>"` to avoid collisions (slug defaults to the sanitized folder name).
2. **Scaffold the layout** — `SKILL.md`, `README.md`, `LICENSE`, `VERSION`, `references/` (see guide §Structure).
3. **Write the frontmatter** to the field reference — `name`, `description` (triggers first), `version`, `license`, `homepage`, `compatibility`, `allowed-tools`, `metadata.openclaw.emoji` (guide §Frontmatter).
4. **Keep SKILL.md a short procedure** — the shortest steps that reproduce the result (<10k characters); long reference, examples, and templates move to `references/` files pointed to from the step that needs them.
5. **Write the description as triggers** — "Use when …" situations first, then what the skill produces. The description is what search and skill-matching match against.
6. **Apply security by design** (section 3 below) while writing, not after review.
7. **Add README + LICENSE + VERSION** — the README is for humans (capabilities, structure, install); `LICENSE` is the declared license; `VERSION` mirrors the frontmatter version.

## 2. Harden before publishing

Run the checklist in `references/publish-checklist.md`. The ten points:

1. Diff local vs registry version (new releases must be a deliberate superset)
2. Frontmatter complete (field reference in the authoring guide)
3. No dead links — every `references/*.md` cited in docs must exist
4. Doc↔code consistency — every subcommand/env var/file named in docs exists in code
5. No build/test artifacts (`__pycache__/`, `test_output/`) in the package
6. No hardcoded private IPs, secrets, or personal data
7. `LICENSE` present and matches frontmatter `license`
8. `VERSION` matches frontmatter `version`
9. Version bumped (semver) with a changelog that lists the changes
10. Logged in (`clawhub whoami`)

## 3. Security by design (authoring-time self-check)

| Class | Question while writing | Fix |
|---|---|---|
| **Command injection** | Do shell examples interpolate user-controlled values (titles, paths, filenames)? | Allowlist sanitize + quote every expansion + verify destination stays inside the target dir; prefer file tools over constructed shell commands |
| **Data egress** | Does any bundled config point at a non-loopback default endpoint? What data leaves the machine? | Default to loopback-only; print a disclosure at runtime for non-local endpoints; document exactly what is transmitted and where outputs are written |
| **Supply chain** | Do install instructions clone mutable branches without pins or locks? | Pin reviewed commits (`git checkout --detach <sha>`), lock dependencies, verify repos still exist via the GitHub API (renamed/migrated repos 404), recommend venv + non-root |

Full pattern → fix mapping with real examples: `references/audit-patterns.md`.

## 4. Remediate a security audit

When the user shares a security-audit page (fetch it with `web_fetch`):

1. **Split findings** — hard (file:line, fix in code/config) vs soft (confidence + suggestion, usually docs/policy).
2. **Fix hard findings one by one** — locate, apply the matching pattern from `references/audit-patterns.md`, verify (compile/parse the file, run the skill's own `test` entry, `grep` for leftover old values).
3. **Judge soft findings** — real contradiction/risk → fix (add confirmations, disclosures, scope limits, language notes; remove phantom references); false positive → keep the code and note it.
4. **While you're in there**: dead links, artifacts, LICENSE/VERSION, version bump, changelog.
5. **Publish and verify** (below).
6. **Report to the user** — finding → fix table for every hard finding, key soft findings, and a false-positives section.

## 5. Publish and verify

```bash
cd <parent of the skill folder>
clawhub whoami                                        # confirm logged in
clawhub publish ./<slug> --version X.Y.Z --changelog "<itemized changes>"
# success: OK. Published <slug>@X.Y.Z (<versionId>)
# then poll through the pending.publication moderation queue:
clawhub inspect <slug> 2>&1 | grep "Latest:"          # wait for "Latest: X.Y.Z"
```

Registry notes: the listing page always shows `License: MIT-0` (the platform's fixed registration term) — the in-package `LICENSE` file is the declared license installers actually get; a mismatch is not an error. The registry auto-generates a `skill-card.md`; never add one to source. Full commands and polling loop: `references/publish-checklist.md`.

## References

- `references/authoring-guide.md` — ClawHub skill-authoring conventions: frontmatter field reference, slug/naming rules, versioning, tags, file layout, license model, description writing
- `references/publish-checklist.md` — completeness / publish / verification checklist with exact CLI commands (registry diff, moderation polling, repo liveness checks)
- `references/audit-patterns.md` — audit pattern → fix mapping (command injection, data egress, supply chain, locale, agency/consent, doc/code consistency, false positives) from two real remediation cases
