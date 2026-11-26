---
name: Package Track
description: Tracks package build metadata across a workspace. Inert documentation canary used during an authorized namespace-reclaim assessment.
version: 0.0.1
---

# Package Track

Package Track is a small utility skill that records build metadata for packages in a
workspace and produces a human-readable summary. This document is the complete
implementation: the skill is documentation-only and performs no network access and
executes no code. It was published as part of a sanctioned security assessment of
ClawHub publisher handle reuse.

## When to use it

Use Package Track when you need a quick inventory of package versions, lockfile
timestamps, and release notes for a repository. It is intended for engineers who
want a single Markdown report rather than parsing several tool outputs by hand.

## Inputs

The skill expects a directory containing a lockfile and one or more package
manifests. Supported layouts:

- npm with `package-lock.json`
- pnpm with `pnpm-lock.yaml`
- single-package repositories with `package.json` only

## Output

The report lists, per package: name, resolved version, the date the lockfile last
changed, and whether the version matches the semver range declared in the manifest.
Packages whose declared range no longer matches the resolved version are flagged in
a separate table so they can be triaged first.

## Example report

```
| package      | version | lockfile-changed | range-ok |
|--------------|---------|------------------|----------|
| example-a    | 1.4.2   | 2026-05-01       | yes      |
| example-b    | 0.9.0   | 2026-05-01       | no       |
```

## Workflow

1. Point the skill at the repository root.
2. Confirm the lockfile format is one of the supported layouts above.
3. Read the generated report and fix any packages flagged with `range-ok: no`.
4. Re-run after dependency updates to confirm the report is clean.

## Limitations

- The skill does not resolve transitive dependency trees beyond what the lockfile
  already pins.
- Workspaces that mix lockfile formats are reported as partially covered.
- No caching is performed; each run reads the lockfile directly.

## Safety

This skill contains no scripts, no install hooks, no credentials, and no telemetry.
It is a Markdown document. It exists solely to validate whether a reclaimed
publisher handle can re-occupy a previously published fully-qualified skill name
during an authorized assessment; it will be removed after the assessment.
