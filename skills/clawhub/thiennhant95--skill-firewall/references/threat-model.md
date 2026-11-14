# Threat Model & Rule Catalog

Full catalog of detection rules. Read when interpreting findings, tuning severity, or extending the scanner.

## Scoring & verdict (recap)

| Severity | Weight | Typical meaning |
|---|---|---|
| CRITICAL | 25 | Direct harm: exfil, destruction, backdoor, self-replication |
| HIGH | 10 | Strong malicious indicator: injection, harvesting, persistence |
| MEDIUM | 4 | Suspicious technique: env dumping, steganography, dynamic eval |
| LOW | 1 | Weak signal: personal-file reference, opaque blob |

Verdict is driven by non-contextual findings (see "Context engine" below):
- MALICIOUS — any contextual-free CRITICAL, or score ≥ 30 with ≥1 MEDIUM finding, or contextual mass ≥ 30
- SUSPICIOUS — any contextual-free HIGH, or score ≥ 12 with ≥1 MEDIUM finding
- CAUTION — findings exist but only contextual/LOW weight
- SAFE — no findings

## Rule families

### SF1xx — Prompt injection / instruction hijack
| Rule | Detects | Sev |
|---|---|---|
| SF101 | "ignore/disregard/forget previous instructions", "override your rules", "new instructions replace" | HIGH |
| SF102 | "you are now…", DAN/jailbreak/developer-mode acts, "no restrictions mode", "pretend you have no rules" | HIGH |
| SF103 | Fake markers: `<\|system\|>`, `[SYSTEM]`, "BEGIN SYSTEM INSTRUCTION", "system prompt:" | HIGH |
| SF104 | "do not tell the user", "keep this secret", "hide your tracks", "without raising suspicion" | HIGH |
| SF105 | "output/print/reveal your system prompt or hidden instructions" | HIGH |
| SF106 | "never refuse", "must always comply with all requests" | MEDIUM |

### SF2xx — Credential theft / data exfiltration
| Rule | Detects | Sev |
|---|---|---|
| SF201 | Credential store paths: `~/.ssh/`, `id_rsa`, `.aws/credentials`, `.kube/config`, `.git-credentials`, `/etc/shadow`, `~/.openclaw/credentials|identity|agents/` | HIGH |
| SF202 | Secret harvesting: reading sensitive files (`cat/read/print` + `.env`/`id_rsa`/shadow), theft verbs (`grab/harvest/steal/dump/leak` + keys/tokens/passwords), secrets taken *from a user/victim*, browser credential theft | HIGH |
| SF203 | Environment dumping: `printenv`, `env \| grep`, `export …TOKEN/SECRET`, PowerShell `env:` | MEDIUM |
| SF204 | Network exfil combos: sensitive object **plus** send mechanics (`curl --data`, `--upload-file`, POST/upload/send/webhook) on one line | CRITICAL |
| SF205 | Dead-drop/exfil services: webhook.site, requestbin, interactsh/oast, ngrok, Telegram bot API, Discord/Slack webhooks, pastebin/transfer.sh | HIGH |
| SF206 | Agent personal data references: `MEMORY.md`, `USER.md`, `SOUL.md`, `IDENTITY.md`, `openclaw.json`, `paired.json`, session transcripts — LOW alone, escalates via SF204 combos | LOW |

### SF3xx — Sabotage / persistence / attack
| Rule | Detects | Sev |
|---|---|---|
| SF301 | `rm -rf /|~|$HOME`, `--no-preserve-root`, `mkfs`, `wipefs`, `dd of=/dev/…`, `shred -u`, writes to block devices | CRITICAL |
| SF302 | Auth tampering: writes to `authorized_keys`/`sshd_config`, `useradd/usermod/passwd/visudo`, `chmod 777`, chmod/chown on auth files | CRITICAL |
| SF303 | Persistence: crontab edits, `systemctl enable`, `.bashrc/.zshrc` appends, schtasks/reg add/launchctl, init.d installs | HIGH |
| SF304 | Privilege escalation: `sudo su/-i/bash/tee/passwd`, setuid, disabling firewall/SELinux/defender/audit tooling | HIGH |
| SF305 | Reverse/bind shells (`bash -i >& /dev/tcp/`, `nc -e`, socat exec), fork bombs, attack tooling (nmap/sqlmap/metasploit/msfvenom/hashcat…), "reverse shell"/"brute force" intent | CRITICAL |

### SF4xx — Obfuscation / stealth
| Rule | Detects | Sev |
|---|---|---|
| SF401 | Decode-and-exec chains: `exec(base64.b64decode(…))`, `atob`, `String.fromCharCode`, `base64 -d \| bash` | HIGH |
| SF402 | Hex/charcode string building: `\xNN` runs ≥8, `\uNNNN` runs ≥8, `String.fromCharCode(`, chained `chr()` | HIGH |
| SF403 | Dynamic execution: `eval/exec` on constructed or external input, `compile(…, exec)`, `Invoke-Expression` | MEDIUM |
| SF404 | ≥3 zero-width/invisible Unicode chars (steganography hiding content from review) | MEDIUM |
| SF405 | Instruction-like text inside HTML comments / non-rendered markup | HIGH |
| SF406 | Opaque blob: length ≥64 and Shannon entropy >4.5 bits/char that fails text decode | LOW |

Decoded payloads (base64/hex) are re-scanned against the **full catalog** and reported at the blob's line with `decoded-payload` evidence. They never receive context downgrades — encoding is deliberate evasion.

### SF5xx — Policy attacks
| Rule | Detects | Sev |
|---|---|---|
| SF501 | "follow/read/download the instructions at <url>" — external instruction loading | HIGH |
| SF502 | Rewriting own system prompt/SOUL.md/AGENTS.md/safety rules, disabling guardrails, appending self-granted permissions | CRITICAL |
| SF503 | Self-replication: "copy this skill to all agents", "replicate yourself", "send this file to every…" | CRITICAL |

## Context engine (anti-false-positive + anti-disguise)

Two signals decide downgrades:

1. **Line context** — defensive phrases ("never", "reject", "red flag", "malicious", "禁止"…) → −2 ranks; example phrases ("example", "e.g.") → −1 rank.
2. **File gate** — downgrades apply only if the file is defensive/educational: file name matches security vocabulary (security, threat, firewall, scanner, defender, vetting, hardening, injection, pentest…) OR ≥50% of flagged lines carry defensive context.

A malicious file sprinkling "Example:"/"never" onto a few lines fails the file gate → full severity. This was verified by fixture `m13_example_disguise.md` (detected MALICIOUS) while `b03_security_education.md` (a doc quoting attack strings to teach detection) stays CAUTION.

Trade-off: an attacker can name a file like `security-notes.md` to seek downgrades — but findings still accumulate score, and contextual mass ≥30 escalates to MALICIOUS. For paranoia use `--fail-on caution` plus manual review.

## v1.1 additions (enterprise round)

| Rule | Detects | Sev |
|---|---|---|
| SF407 | Unicode confusable/homoglyph evasion — attack strings rebuilt from Cyrillic/Greek lookalikes (`іgnore аll prevіous`); fires when confusable folding enables a rule match | HIGH |
| SF408 | Remote content beacon — markdown/HTML images loading from URLs with session/key/track parameters, or raw-IP image hosts | MEDIUM |
| SF601 | Pipe-to-shell install — `curl … \| sh/python/node` (legitimate installers land CAUTION by design: review before run) | MEDIUM |
| SF602 | Package lifecycle-hook payload — `preinstall/postinstall/prepare` executing curl/chmod/bash/base64/.env access at install time | HIGH |
| SF603 | CI workflow injection — `pull_request_target`, interpolation of `github.event.pull_request.title/body/head` into run context | HIGH |

Matching engine upgrades: **confusable folding** (NFKC + Cyrillic/Greek map) applied before every rule match; **multi-layer base64** (up to 3 layers decoded and re-scanned); **adjacent-line combo pass** for SF101/SF204/SF5xx/SF602 against split-evasion; **SARIF 2.1.0** output; **baseline fingerprints** (sha1 of rule+file+evidence, line-independent) for governed suppression; parallel file scanning.

## Tuning notes (from dogfood on real repositories)

Data-driven adjustments made after scanning real-world skill packs (mattpocock/skills, Snyk toxicskills-goof, 43 installed skills). Documented so future tuning doesn't regress:

1. **Whole-word verbs** — verb tokens use `\b` boundaries. Without them, `cat` matches "category", `read` matches "already", `type` matches "prototype" (real FPs observed).
2. **Determiner requirement** — theft-verb + secret-word combos require `all|every|the|their|your|user's|victim's`. Otherwise honest questions like "Will the repro leak secrets?" match `leak secrets` (real FP observed).
3. **Generic words are not objects** — "token/secret/password" alone never trigger SF204 combos; only path-like objects (`.ssh`, `id_rsa`, `.env`, `MEMORY.md`…) combine with send mechanics. Docs routinely mention "tokens" next to URLs (real FP observed on changelogs).
4. **Weak env/config reads are LOW (SF206)** — "reads your .env" is common in honest tool documentation; only strong acquisition verbs (`cat/dump/grab/…`) keep SF202 HIGH.
5. **Entropy heuristic skips noise carriers** — lockfiles/manifests (`package-lock.json`, `yarn.lock`, `go.sum`, `*.min.js`…) and pure-hex tokens (git/SHA hashes; 111 real FPs observed in one lockfile) are excluded from SF406 only — decode-and-rescan still runs everywhere.
6. **Offensive phrasing beats defensive words** — "Do not tell the user…", "keep it secret" contain prohibition markers ("do not") that a naive defensive-context heuristic rewards. `OFFENSIVE_CTX` is checked first and forbids downgrades (real fixture miss m16 before fix).
7. **Security-sounding filenames are not blanket cover** — a malicious workflow named `ci_injection.yml` exploited the security-doc name heuristic (real fixture miss m18 before fix). Name-based cover: −1 rank only, prose files only (.md/.txt); code/config never covered by name.
8. **Exit-code contract** — default `--fail-on caution` makes exit code equal the verdict (0/1/2/3); `--fail-on never` always exits 0; `--fail-on malicious` only blocks MALICIOUS. Verified by 15-case edge battery (CRLF, UTF-8 truncation, binary skip, symlink loops, 1MB perf, empty files, unicode).

## Known limitations

- Static analysis: purely semantic manipulation (novel wording, no known patterns) can pass. Use manual review for high-risk installs.
- Custom encodings beyond base64/hex/charcode are not decoded.
- Line-oriented matching: multi-line split evasion (pattern spread across many lines with no single matching line) is a residual gap; the decoder/entropy/ZWC heuristics partially compensate.
- Scores can exceed 100 by design — it is a risk mass indicator, not a percentage.

## Extending

Add rules to `RULES` in `scripts/skill_firewall.py` (id, name, category, severity, regex patterns — case-insensitive). Then add a malicious fixture that the rule must catch and a benign fixture that must stay clean, and require `tests/test_firewall.py` PASS before shipping.
