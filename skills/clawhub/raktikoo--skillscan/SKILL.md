---
name: skillscan
description: Scan an AI-agent skill or MCP server folder for malicious or risky behaviour before installing it — credential and SSH key reads, data exfiltration, network sends, hidden instructions, obfuscation, and install-time tricks in code, scripts and manifests. Use when asked to scan, vet, audit or check a skill, plugin or MCP server before installing it, when a skill looks suspicious, or when reviewing a SKILL.md someone shared. Not for general security review of ordinary code projects, for checking CI workflow files (use ci-command-truth), or for checking package dependencies in a pull request (use phantomdep-pr-gate).
license: MIT
compatibility: Requires Python 3.10+ and pip. Installing needs network access to GitHub; scanning itself is fully offline by default and uses only the Python standard library.
---

# SkillScan

## What this tool does

SkillScan statically reads an AI-agent skill or MCP server folder and
gives one plain-English verdict — BLOCK, CAUTION, or PASS — from
deterministic rules; every finding points at the rule, file and line.
Scanned code is never executed: files are only read and parsed.
It is a linter, not a guarantee of safety: PASS means no known-bad
patterns were found in what was scanned, not that a skill is safe.

## Install

```bash
pip install git+https://github.com/RakTikoo/skillscan
```

This provides the `skillscan` command. Prefer a virtual environment
for the install. (The `skillscan` name on PyPI is a different tool
by another author — use the GitHub route.)

## Run

Scan a skill folder before installing it, or get a machine-readable
report for tooling:

```bash
skillscan path/to/skill-folder
skillscan path/to/skill-folder --format json
```

The repo bundles sample skills under `samples/` — `good/`, `caution/`
and `bad/` (e.g. `samples/bad/ssh-stealer`); scan one to see a verdict.

Other formats: `--format md` and `--format sarif`. A GitHub repo URL
can be scanned directly. An optional `--llm` review can add findings
on top of the offline verdict — never remove or change them — and
needs an API key; leave it off unless asked.

## Reading the results

The exit code is the verdict:

- `0` — PASS: no known-bad patterns found in what was scanned.
- `1` — CAUTION: worth a human read before installing. Noisy by design
  for capability flags in honest tools (subprocess, deletion, network).
- `2` — BLOCK: at least one block-severity pattern found. Read the
  finding before judging; context matters.
- `3` — usage or IO error: the scanner could not run (bad path, bad
  flags). Distinct from BLOCK — no verdict was produced.

Every report states how many files were scanned and which were skipped
(unreadable, over the 2 MB per-file cap, symlinks, binary-looking
content). If anything suspicious was skipped, or nothing was scanned at
all, the verdict cannot be a clean PASS (`SCAN_INCOMPLETE`). Findings
print as severity, rule name, file and line, with the offending line
quoted. The JSON report carries `verdict`, `exit_code`, `findings`,
`scanned_files`, `skipped_files` and `target`.

## Limits

- Static analysis only: behaviour decided at runtime (from a server
  response, the date, or an encrypted config) is invisible to it.
- Strong encryption or packing beyond base64/hex is flagged at most as
  obfuscation, not decoded.
- JavaScript is checked by pattern matching and string squeezing, not a
  full AST — deeply dynamic JavaScript can slip through.
- Secret detection is heuristic: short, weak, split or encoded secrets
  can evade it, and random-looking test values can trip a CAUTION.
- Scan budgets are finite: 2,000 files or 32 MB per scan. Hitting a
  budget is reported and forces SCAN_INCOMPLETE — never a silent PASS.
- Phrase and concealment checks match fixed patterns, not meaning: a
  novel phrasing or a purely semantic deception can pass.
