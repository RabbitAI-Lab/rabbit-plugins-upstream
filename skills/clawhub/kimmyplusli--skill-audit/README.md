# skill-audit 🔍

An [OpenClaw](https://openclaw.ai) meta-skill that runs a pre-publish
security self-audit on any skill folder — the post-ClawHavoc ClawHub
publishing checklist, automated.

## Install

```bash
clawhub install skill-audit
```

## Use

Point it at a skill directory:

> "Audit my skill at `skills/my-skill` before I publish"
> "Pre-publish check on this folder"
> "Is this third-party skill safe to install?"

The agent walks three audit layers and emits a scored report:

| Layer | Checks | Threat it addresses |
|---|---|---|
| Code | eval/exec, network calls, sensitive file reads, base64 payloads, dependency audit | Malicious executable code |
| SKILL.md | ClickFix (`curl\|bash`) tricks, external scripts, trigger clarity, agent-directed prompt injection, declaration-vs-behavior match | Prompt injection & social engineering |
| Release metadata | SemVer, changelog, no custom license, slug rules, file types/size, homepage reachability | Supply-chain takeover & trust |

Scoring: 100 baseline; code-layer failures −40 (publish blockers),
SKILL.md-layer −25, metadata-layer −10, warnings −5.
**90+ READY · 70–89 FIX FIRST · 40–69 NOT READY · <40 DO NOT PUBLISH.**

Beyond the mechanical checks, the skill reads the audited skill's prose *as
instructions to an AI* and quotes anything that directs the agent to contact
external services, read unrelated files, or hide output — the class of attack
regex can't catch.

## Files

- `SKILL.md` — procedure, verification commands, scoring, report format
- `checklist.md` — the full checklist with the incident behind every item

## Why

In February 2026 the ClawHavoc campaign put 300+ malicious skills on ClawHub;
the registry ultimately delisted 42% of its catalog. Every row in this
checklist traces to something that incident (or npm's `event-stream` /
`ua-parser-js` era) taught the ecosystem. Run the audit before `clawhub skill
publish`; aim to land on `clean` on the first try.

## License

MIT-0 (as with all ClawHub skills).
