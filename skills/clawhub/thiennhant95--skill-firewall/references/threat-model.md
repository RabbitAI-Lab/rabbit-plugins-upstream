# Threat Model & Rule Catalog

Summary of what the scanner looks for and how the verdict is computed. The
matching patterns live in `scripts/skill_firewall.py`; this document describes
them in prose so it can be read safely without reproducing attack payloads.

## Scoring & verdict (recap)

| Severity | Weight | Typical meaning |
|---|---|---|
| CRITICAL | 25 | Direct harm: exfiltration, destruction, backdoor, self-replication |
| HIGH | 10 | Strong malicious indicator: injection, harvesting, persistence |
| MEDIUM | 4 | Suspicious technique: environment dumping, obfuscation, dynamic evaluation |
| LOW | 1 | Weak signal: personal-file reference, opaque blob |

Verdicts use severity-weighted mass:
- MALICIOUS — any CRITICAL finding, or score ≥ 30 with at least one MEDIUM+ finding
- SUSPICIOUS — any HIGH finding, or score ≥ 12 with at least one MEDIUM+ finding
- CAUTION — findings exist but only at LOW weight
- SAFE — no findings

## Rule families

### SF1xx — Prompt injection / instruction hijack
| Rule | Detects | Sev |
|---|---|---|
| SF101 | Attempts to change the agent's task or safety rules mid-context | HIGH |
| SF102 | Role hijack / jailbreak personas and "no restrictions" framing | HIGH |
| SF103 | Fake system/instruction markers that impersonate the runtime | HIGH |
| SF104 | Secrecy or anti-reporting directives aimed at the agent | HIGH |
| SF105 | Requests to expose the agent's configuration or private directives | HIGH |
| SF106 | Unconditional-compliance framing that removes the ability to decline | MEDIUM |

### SF2xx — Credential theft / data exfiltration
| Rule | Detects | Sev |
|---|---|---|
| SF201 | References to well-known credential-store locations | HIGH |
| SF202 | Secret-harvesting phrasing (reading and removing credentials) | HIGH |
| SF203 | Environment dumping of secrets/tokens | MEDIUM |
| SF204 | Sensitive-object + network-send combination on one line | CRITICAL |
| SF205 | Known dead-drop / exfiltration service endpoints | HIGH |
| SF206 | Agent memory, identity, or config file references | LOW |

### SF3xx — Sabotage / persistence / attack
| Rule | Detects | Sev |
|---|---|---|
| SF301 | Recursive filesystem destruction or raw-device writes | CRITICAL |
| SF302 | Authentication tampering and unsafe permission widening | CRITICAL |
| SF303 | Persistence via scheduled tasks, services, or shell profiles | HIGH |
| SF304 | Privilege escalation or disabling security controls | HIGH |
| SF305 | Reverse/bind shell constructs, fork bombs, offensive tooling names | CRITICAL |

### SF4xx — Obfuscation / stealth
| Rule | Detects | Sev |
|---|---|---|
| SF401 | Decode-then-execute chains | HIGH |
| SF402 | Hex/charcode string construction of payloads | HIGH |
| SF403 | Dynamic evaluation of constructed or external input | MEDIUM |
| SF404 | Runs of zero-width/invisible Unicode (hidden content) | MEDIUM |
| SF405 | Directives embedded in non-rendered markup | HIGH |
| SF406 | Opaque high-entropy blobs that do not decode as text | LOW |
| SF407 | Homoglyph/confusable substitution used to evade matching | HIGH |
| SF408 | Remote content beacons carrying session or tracking data | MEDIUM |

Decoded payloads are re-scanned against the full catalog and do not receive a
context downgrade — encoding is treated as deliberate evasion.

### SF5xx — Policy attacks
| Rule | Detects | Sev |
|---|---|---|
| SF501 | Loading task directives from external locations | HIGH |
| SF502 | Rewriting the agent's own rules, memory, or safety constraints | CRITICAL |
| SF503 | Self-replication / mass distribution directives | CRITICAL |

### SF6xx — Supply chain
| Rule | Detects | Sev |
|---|---|---|
| SF601 | Install commands piped directly into an interpreter | MEDIUM |
| SF602 | Package lifecycle hooks that fetch or execute at install time | HIGH |
| SF603 | CI workflow injection via untrusted event fields | HIGH |

## Context policy (strict by default)

Severity is **not silently reduced** by wording. A malicious file could otherwise
wrap an attack in reassuring words to earn a downgrade, so
the default is strict: what the rules match is what you get.

An explicit opt-in exists for auditing known defensive documents (security
education material that quotes threats in order to teach detection):

```bash
python3 scripts/skill_firewall.py <target> --context-downgrade
```

When enabled:
- A line with defensive phrasing is lowered by two rank steps.
- A line with example phrasing is lowered by one rank step.
- Offensive phrasing wins: directives to hide information from the user are
  not downgraded.

This mode is for documents you already trust. Do not use it as a general
false-positive filter on untrusted input; accumulated mass can still escalate to
MALICIOUS.

## Known limitations

- Static analysis: semantic manipulation with novel wording can pass. Use manual
  review plus behavioral tests for high-risk installs.
- Character encodings outside base64/hex/charcode are not decoded.
- Line-oriented matching can miss attacks split across many short lines; the
  decoder, entropy, and zero-width heuristics only partially compensate.
- Scores can exceed 100 by design: they are a risk-mass indicator, not a
  percentage.

## Extending

Add rules to `RULES` in `scripts/skill_firewall.py` (id, name, category,
severity, regex patterns, case-insensitive). Add one malicious fixture that the
rule must catch and one benign fixture that must stay clean, and require the
repository test harness to pass before shipping.
