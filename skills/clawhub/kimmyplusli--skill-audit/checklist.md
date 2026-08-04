# The full checklist (source: post-ClawHavoc ClawHub publishing bar)

Each row: what to check, how to verify, and why it exists. Layers map to the
four threat categories: code = malicious executable code; SKILL.md = prompt
injection / social engineering; metadata = supply-chain takeover & trust.

## Code layer — Threat 1: malicious executable code

| Check | How to verify | Why (the incident behind it) |
|---|---|---|
| No eval / exec / dynamic execution | `grep -rnE "eval\(|exec\(|os\.system|subprocess|child_process"` | Dynamic execution is a supply-chain attacker's favorite entry point; ClawHavoc reverse shells used direct `os.system()` calls |
| No suspicious network calls | List every target domain in requests/urllib/fetch/curl; each must be explainable in one sentence | Silent-exfiltration skills uploaded credentials to attacker C2 servers with no visible output |
| No sensitive file reads | Search for `.env`, `.ssh`, Keychain, Credentials, `.aws` | A "weather assistant" in ClawHavoc read `~/.clawdbot/.env` and exfiltrated every API key and wallet credential |
| No base64/zlib-encoded payloads | Flag base64-ish strings > 100 chars; decode and inspect any found | Standard payload-hiding technique; obfuscation in a skill has no legitimate purpose |
| Dependency list is clean | `pip-audit` / `npm audit` if the skill has deps | Your code being safe ≠ the libraries you pulled in being safe |

## SKILL.md layer — Threat 2: prompt injection & social engineering

| Check | How to verify | Why |
|---|---|---|
| No "Prerequisites" ClickFix trick | No instruction telling the USER to copy-paste `curl \| bash` / `wget \| sh` into a terminal | ClawHavoc's main human-target tactic: disguise payload delivery as dependency installation |
| No scripts pulled from external links | Every external URL in SKILL.md is explained; none is fetched-and-executed | "Pull a helper script from outside" is a hard line — that's how payloads update after review |
| Trigger scenarios explicit | SKILL.md states when to use AND when not to | Prevents the agent from firing the skill in contexts the author never audited |
| No agent-directed injection | Read the prose as instructions to an AI: anything directing data to external services, reading unrelated files, or hiding output from the user → quote it verbatim | Half of ClawHavoc's tricks targeted the AGENT, not the human — code scanners cannot catch instructions written in natural language |
| Declarations complete | Every env var / CLI tool the code or instructions actually use appears in `metadata.openclaw.requires` | Declaration-vs-behavior mismatch is exactly what ClawHub's automated security analysis flags |

## Release metadata layer — Threat 4: trust & takeover

| Check | How to verify | Why |
|---|---|---|
| Public repo with complete README | Homepage URL resolves (HTTP 200) to a public repo whose contents match the published files | Unreadable source = unauditable; users must be able to diff what's published against what's on GitHub |
| Homepage is real | `curl -s -o /dev/null -w "%{http_code}"` on the homepage URL | So users and the registry know who to contact when something goes wrong |
| SemVer version | Matches `^\d+\.\d+\.\d+$`; first release `0.1.0` | Version numbers are promises; malformed ones fail publish validation outright |
| CHANGELOG.md exists | File present with an entry for the current version at the top | What downstream users rely on to judge whether an upgrade is safe — silent-takeover attacks hide in unexplained version bumps |
| No custom license field | `grep -n "^license" SKILL.md` returns nothing | ClawHub forces MIT-0 on every skill; a conflicting license field is at best noise, at worst misleading |
| Slug valid | Folder/name matches `^[a-z0-9][a-z0-9-]*$` | Non-compliant slugs fail publishing outright |
| Text-only files under 50MB | Every file is text-type (md/json/yaml/toml/js/ts/svg); total < 50MB | Binary files can't be reviewed by humans and get the release rejected |

## Scan-state reference (what the registry itself will do after publish)

`pending` → scanning not finished · `clean` → installable · `suspicious` →
manual review · `malicious` → unsafe · `held`/`quarantined`/`hidden` → not
installable right now. This audit's goal is that the skill lands on `clean`
on the first try.
