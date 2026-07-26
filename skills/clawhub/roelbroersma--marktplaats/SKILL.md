---
name: "marktplaats-publisher"
description: "Marktplaats publisher 0.6.1: strictere gates en mini-model flow."
metadata: {"clawdbot":{"emoji":"🇳🇱","requires":{"bins":["node"]}}}
---

# marktplaats-publisher 0.6.1 update

Applied update to the live skill files before publishing.

## Changes

- Removed unsupported `homepage` frontmatter so public skill validation passes.
- Bumped package and skill metadata to `0.6.1`.
- Included `references/` in `package.json` so referenced docs are packaged.
- Tightened `SKILL.md`, README, and references for smaller models: one phase, one verification, then next phase.
- Clarified that scripts are gates and UI/publication remains browser work with readback verification.
- Added explicit guidance for one or two subtle product-relevant typo/search variants.
- Added `marktplaats-copy-qa --min-variants` support.
- Added `marktplaats-place-probe --open-background URL --wait-ms N` to open Safari in the background before probing.
- Changed curl probe default body retention to `--body-limit 0` for privacy.
- Added security/payment signal detection to place probes without logging page body text.
- Made live verification accept `<br>`/single-newline paragraph preservation while still rejecting flat one-line descriptions.
- Added live description-window domain/email/URL detection.
- Stored live verification `passed` and live website reference evidence in `ad.json`.
- Made `marktplaats-register-update` block by default unless live verification succeeded; `--allow-unverified` is explicit and intended only for drafts.

## Validation

- `npm test` passed.
- `python3 .../quick_validate.py /Users/roelbroersma/.openclaw/workspace/skills/marktplaats` passed.
- `npm pack --dry-run` shows `references/` included in the package.
