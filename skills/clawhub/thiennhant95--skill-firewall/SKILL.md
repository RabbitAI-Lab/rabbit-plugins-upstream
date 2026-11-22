---
name: skill-firewall
description: Security scanner for AI agent skills (SKILL.md packs). Use before installing any skill from ClawHub, GitHub or external sources, when auditing a skill directory for malicious patterns (prompt injection, credential theft, exfiltration, destructive commands, obfuscated payloads, persistence), or when asked "is this skill safe?". Produces a SAFE/CAUTION/SUSPICIOUS/MALICIOUS verdict with evidence and CI-friendly exit codes. Strict by default; context-based severity reductions require an explicit opt-in.
allowed-tools: Read, Bash(python3:*)
permissions: [file_read, file_write]
---

# Skill Firewall v1.0.5

Static security scanner for third-party agent skills. Scan a skill before installing it.

## Install

```bash
clawhub install thiennhant95/skill-firewall
```

## Quick start

```bash
python3 scripts/skill_firewall.py <skill-dir-or-file>          # human report
python3 scripts/skill_firewall.py <target> --json              # machine-readable
python3 scripts/skill_firewall.py <target> --sarif             # SARIF 2.1.0 (GitHub code scanning)
python3 scripts/skill_firewall.py <target> --quiet             # one-line verdict
python3 scripts/skill_firewall.py <target> --context-downgrade # opt-in: audit defensive docs
python3 scripts/skill_firewall.py --version                    # scanner + ruleset version
```

**Enterprise triage** — suppress acknowledged findings via fingerprints (rule+file+evidence, line-independent):

```bash
python3 scripts/skill_firewall.py <target> --write-baseline accepted.json   # after human review
python3 scripts/skill_firewall.py <target> --baseline accepted.json         # subsequent scans
```

Exit codes: `0` SAFE · `1` CAUTION · `2` SUSPICIOUS · `3` MALICIOUS · `4` error (default `--fail-on caution` makes the exit code equal the verdict; use `--fail-on never` to always exit 0, `--fail-on malicious` to only block on MALICIOUS).

## Workflow

1. **Scan before install.** Point the scanner at the skill directory (it walks all text files: SKILL.md, scripts, references).
2. **Read the verdict:**
   - `SAFE` — install.
   - `CAUTION` — installable; review listed findings first. Typical for security docs or skills referencing agent config files.
   - `SUSPICIOUS` / `MALICIOUS` — **do not install.** Report rule IDs and excerpts to the user.
3. **Gate automation** via exit codes (default: exit = verdict). Relax with `--fail-on malicious` (only block MALICIOUS) or `--fail-on never` (report only). A pile of LOW findings alone never blocks (severity-weighted scoring).
4. **For CI / install hooks** use `--quiet` and the exit code.

## Verdict model

- Score weights: CRITICAL 25 · HIGH 10 · MEDIUM 4 · LOW 1.
- **Strict by default:** severity is not silently reduced by wording, so a file cannot earn a downgrade by adding reassuring words around an attack.
- **Opt-in context mode** (`--context-downgrade`) exists for auditing known defensive documents: a line with defensive phrasing is lowered by two rank steps and a line with example phrasing by one. Offensive phrasing (for example, directives to conceal behavior from the user) is not downgraded. Use it only on documents you already trust; accumulated mass can still escalate to MALICIOUS.

## What it detects

Five rule families (full catalog: [references/threat-model.md](references/threat-model.md)):

| Family | Examples |
|---|---|
| SF1xx prompt injection | instruction override, jailbreak/role hijack, fake system tags, secrecy directives, system-prompt theft |
| SF2xx data theft | credential store access, secret harvesting, env dumping, network exfil, dead-drop services |
| SF3xx sabotage | destructive commands, auth tampering, persistence (cron/systemd/bashrc), privilege escalation, reverse shells/attack tooling |
| SF4xx obfuscation | base64/hex payloads **decoded and re-scanned (multi-layer)**, charcode chains, dynamic eval, zero-width steganography, hidden markup instructions, **Unicode homoglyph evasion (SF407)**, remote content beacons (SF408) |
| SF5xx policy attacks | external instruction loading, self-modification/safety disable, self-replication |
| SF6xx supply chain | pipe-to-shell installs (SF601), package lifecycle-hook payloads (SF602), CI workflow injection / `pull_request_target` (SF603) |

Heuristics beyond regex: base64 blob decoding incl. multi-layer encoding (hidden payloads are matched against the full rule catalog), hex-escape decoding, Shannon entropy for opaque blobs, zero-width character counting, HTML-comment instruction hunting, **Unicode confusable folding** (Cyrillic/Greek homoglyphs and fullwidth forms normalized before matching), and **adjacent-line combo matching** against split-evasion (attack sentences broken over several short lines).

## Reading findings

Each finding: `severity rule_id file:line (category)` + matched evidence + source line. `[contextual]` marks downgraded findings and only appears when `--context-downgrade` is enabled.

Files scanned: common code/doc extensions plus SKILL.md/AGENTS.md/TOOLS.md; skips `.git`, `node_modules`, binaries, files >1MB.

## Verification

The test harness lives in the source repository (not shipped in this bundle, which keeps intentional attack fixtures out of published artifacts):

https://github.com/thiennhant95/agent-skills/tree/main/skill-firewall

It runs 18 malicious fixtures (inert test vectors, EICAR-style) and 15 benign fixtures (including false-positive stress cases: security education docs, `df.eval`, benign base64, `curl` without exfil), plus a strict-default check that a defensive-looking document is still flagged without `--context-downgrade`. Acceptance: 100% detection, 0 false positives. Results are written as JSON + Markdown evidence. Never modify fixtures to make tests pass — they are the contract.

## Limitations (state these when reporting)

- Static analysis: semantic attacks written as plain honest prose without known patterns can evade it. Pair with `skill-vetter`-style manual review for high-risk installs.
- Heavily obfuscated custom encodings (beyond base64/hex/charcode) may hide payloads.
- Strict mode flags security-education documents that quote attack text. If you are auditing a known defensive document, rerun with `--context-downgrade` and still read the flagged lines manually.

## Related skills

- `undo-first` — reversible-action guard: snapshots, risk gate, verified restore, audit journal. `clawhub install thiennhant95/undo-first`
- `vibecheck` — audit AI-generated code for security issues and AI slop. `clawhub install thiennhant95/vibecheck`
- `vibegit` — estimate AI-assisted work and slop signals from git history. `clawhub install thiennhant95/vibegit`
