# skill-author — Author, Harden & Publish Skills for ClawHub

Turn an agent skill into a **ClawHub-ready, audit-passing** package. Four capabilities:

- **Author** — write a skill that conforms to ClawHub conventions (frontmatter, structure, naming, versioning, licensing), so it passes review cleanly the first time
- **Harden** — pre-publish checks: completeness, dead links, secrets, build artifacts, doc↔code consistency, security by design
- **Remediate** — fix findings from a `clawhub.ai/<owner>/<slug>/security-audit` page (hard → code/config, soft → docs/policy)
- **Publish & verify** — proper changelog, then poll through the moderation queue until `Latest:` flips

## Provenance

The remediation patterns in this skill are distilled from real audits:

| Case | Audit findings | Key fixes |
|------|---------------|-----------|
| `epic-novel-writer@1.2.1` | command injection (Medium) ×1 + LLM soft findings ×9 | allowlist sanitization, quoted paths, tightened triggers, intent-contradiction removal, language note |
| `image-with-comfyui@1.7.1` | data egress (High) ×1 + supply chain (Medium) ×1 + soft findings ×22 | loopback-only default, runtime disclosure, pinned commits (incl. repo renames/migrations), doc/code mismatch fixes, consent scope limits |
| `image-with-comfyui@4.7.5` | A.I.G: Bearer cross-origin redirect (T09) + residual server files; LLM `verdict: suspicious` → `benign` | `SafeRedirectHandler` strips Bearer on cross-origin 3xx; run-scoped `_RUN_ARTIFACTS` registry + deduped `purge_remote` |
| `music-with-comfyui@0.4.14` | A.I.G: Bearer cross-origin redirect (T09) | same `SafeRedirectHandler` + patch `urllib.request.urlopen` once (7 call sites); residual-files finding N/A (single-product workflow) |

## File layout

| File | Contents |
|------|----------|
| `SKILL.md` | Main flow: review-model cognition → 4 capabilities (author / harden / remediate / publish) → security self-check |
| `references/authoring-guide.md` | ClawHub authoring conventions: frontmatter field reference, slug/naming rules, versioning, tags, file layout, license model, description writing, security by design |
| `references/publish-checklist.md` | Completeness / publish / verification checklist with exact CLI commands (registry diff, moderation polling, repo liveness checks) |
| `references/audit-patterns.md` | 12 audit patterns → fix mapping (incl. 5 real cases + false-positive table) |
| `LICENSE` | BSD 3-Clause |
| `VERSION` | 1.2.0 |

## Core cognitions

1. **ClawHub review has two layers**: the static pattern scan produces **hard findings** (file:line — must be fixed in code/config); the LLM review produces **soft findings** (confidence-scored — usually docs/policy clarification).
2. **False positives exist**: path-traversal *defense* code gets flagged as credential access; reading your own workflow gets flagged as memory poisoning. Never delete a guard to "fix" a finding.
3. **Registry `MIT-0` vs in-package `LICENSE`**: the listing page always shows the platform's fixed registration term (MIT-0); the in-package `LICENSE` is the license installers get. A mismatch is not an error.
4. **Publishing enters a `pending.publication` moderation queue** — poll `clawhub inspect <slug>` until `Latest: X.Y.Z` appears before claiming the release is live. The `Reason` field is the real decider: `scanner.llm.clean`/`scanner.vt.clean` = clean; `scanner.llm.review` = LLM had to work around a finding. Read the live `clawhub inspect` (not a dry-run or hanging process).

## Install

```bash
clawhub install skill-author
```

## License

BSD 3-Clause (see `LICENSE`)
