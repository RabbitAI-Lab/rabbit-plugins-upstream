---
name: bump-doctor
description: >-
  Before upgrading an npm or pypi dependency, assess what will actually break
  for you. Fetches the upstream release notes and follows the linked migration
  guide, cross-references the symbols your code actually uses, and returns a
  focused risk report with a score and the changes that affect you first, not a
  generic changelog dump. Use whenever the user is bumping a dependency version.
version: 1.0.2
license: MIT-0
metadata:
  openclaw:
    requires:
      bins:
        - python3
---

# Bump Doctor

Assess the real risk of a dependency upgrade **before** running it. Use whenever
the user is about to bump an npm or pypi package and wants to know what breaks
*for them specifically*.

## When to use

- "Is it safe to upgrade `<package>` from X to Y?"
- "What breaks if I bump `<package>`?"
- Any dependency version change where the migration cost is unknown.

## How to use

The skill bundles a self-contained analyzer (`analyzer.py`, Python 3, standard
library only, no install, no API key). Run it from the skill directory:

```bash
python3 analyzer.py <ecosystem> <package> <from_version> <to_version> --used "<symbols>"
```

- `<ecosystem>`: `npm` or `pypi`
- `--used`: comma-separated symbols/imports the user's code actually uses from
  the package. **Grep the codebase first to fill this in**, it's what turns a
  generic changelog into a report about *their* risk.

Example:

```bash
python3 analyzer.py npm express 4.18.2 5.0.0 --used "res.send,Router,app.del"
```

It prints JSON: a `risk_score` (0–100), a `headline`, and `items` where anything
with `affects_you: true` is sorted first.

## How to present the result

**Verify before you report, do not parrot the tool's `headline` or `risk_score`.**
They are a pre-verification heuristic that OVER-counts (it keyword-matches, so it
flags notes that merely mention a symbol you use). Your job is to turn that raw
list into a verified answer:

1. For each `items` entry with `affects_you: true`, read the relevant lines of the
   user's source and decide whether it *genuinely* applies. It will over-flag -
   common false alarms: a note that cites your symbol only as the safe
   *replacement*, or that breaks a call signature (e.g. arg count) the user
   doesn't use. Discard those.
2. Give the user your **verified** conclusion first: how many things genuinely
   break, and the exact change to make. Do not lead with the raw count.
3. If `headline` is `INCONCLUSIVE`, tell the user the changelog couldn't be
   retrieved and they must verify manually, do **not** imply the upgrade is safe.

Do **not** paste the raw changelog, and do **not** present every `affects_you`
match as a definite break. The deliverable is a short, verified list of what
actually affects this codebase.

## Notes

Free and self-contained. Reads public release data from the npm/pypi registries
and GitHub; needs network access but no credentials. Optionally set a
`GITHUB_TOKEN` env var to raise GitHub's rate limit on heavy use.
