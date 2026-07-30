<div align="center">

# Credential Exposure Map

**Map every credential your OpenClaw agent can access. Risk-scored exposure report across env, config, memory, skills, MCP, and git history.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![Python 3](https://img.shields.io/badge/Python-3-green)](https://www.python.org/)
[![ClawHub](https://img.shields.io/badge/ClawHub-credential--exposure--map-orange)](https://clawhub.ai)

</div>

`[English](#english) | [中文](./README_CN.md)`

---

## English

### Introduction

Credential Exposure Map scans your entire OpenClaw environment and builds a comprehensive map of all credentials the agent can access at runtime. It covers environment variables, config files, memory files, installed skill permissions, MCP server connections, and git history.

Unlike static skill scanners that check code before installation, this tool maps the **live exposure surface** after everything is installed and configured.

### The Problem

- 92% of organizations lack visibility into their AI agent's credential access (Forrester, 2026)
- Credentials stored in MEMORY.md persist across sessions and are readable by any skill
- No existing tool inventories what real credentials the agent can actually reach
- Static scanners can be bypassed, but runtime exposure is always present

### How It Works

```
SCAN START
├── Environment variables → pattern match for keys/tokens/secrets
├── openclaw.json → parse JSON, find credential fields
├── .env files → grep for KEY/TOKEN/SECRET/PASS patterns
├── MEMORY.md + memory/*.md → regex scan for committed credentials
├── memory/*.json → parse JSON for credential-like values
├── skills/*/SKILL.md → capability analysis (exec/read/network/write)
├── MCP servers → list connected services with auth scope
└── git history → scan last 50 commit diffs for secrets
SCAN END

→ Risk score each finding
→ Generate credential inventory + skill capability matrix
→ Save report to ~/.openclaw/credential-exposure-report.json
```

### Features

- **8 scan sources**: env vars, config, .env files, memory (MD + JSON), skills, MCP servers, git history
- **16 secret patterns**: AWS, GitHub, OpenAI, Anthropic, Stripe, Slack, Google, JWT, PostgreSQL, Redis, generic keys
- **Risk scoring**: 0-100 per credential based on accessibility, persistence, and exposure paths
- **Skill capability matrix**: Shows which skills have exec, read, network, write access
- **Credential preview masking**: Never shows full values (first 8 chars + ***)
- **Zero dependencies**: Python 3 stdlib only

### Real-World Case Study

We ran Credential Exposure Map on a production OpenClaw workspace with 23 installed skills and 6 months of memory logs. Here's what it found:

```
=== Scan Complete: 40 finding(s) ===

Risk: 14 Critical | 5 High | 19 Medium | 2 Low

── Credential Inventory (top findings) ──
Credential         Risk      Source   Location              Note
ghp_****REDACTED   CRITICAL  memory   MEMORY.md:103         GitHub PAT, 2 copies
vcp_****REDACTED   CRITICAL  memory   MEMORY.md:102         Vercel token, 5 copies
ghp_****REDACTED   CRITICAL  memory   2026-04-22.md:45      Leaked into daily log
vcp_****REDACTED   CRITICAL  memory   2026-04-24.md:25      Leaked into daily log
sk-****REDACTED    CRITICAL  memory   2026-06-16.md:148     DeepSeek API key
****REDACTED       HIGH      env_var  OPENAI_API_KEY        In agent context
****REDACTED       HIGH      env_var  BRAVE_API_KEY         In agent context
****REDACTED       HIGH      env_var  ZAI_API_KEY           In agent context

── Key Finding ──
14 Critical credentials scattered across memory files.
5 duplicate copies of the same Vercel token.
Every installed skill (23) could read all of them.

── Skill Capability Matrix (23 skills) ──
Skill              Exec  Read  Net   Write  Risk
agent-canary        Y     Y    N     Y     45
multi-search-engine Y     Y    Y     N     45
danger-guard        Y     Y    Y     N     45
github              N     Y    N     N     15
feishu-recall       N     Y    N     N     15
...(23 skills total)

── Recommendations ──
1. CRITICAL: Redact all tokens from MEMORY.md and memory/*.md
2. Rotate GitHub PAT (exposed in 4 locations)
3. Rotate Vercel token (exposed in 5 locations)
4. Move env vars to secrets vault, remove from agent context
```

**Takeaway**: A workspace that looked clean on the surface had 14 Critical credential exposures in memory files. Any malicious skill installed during those 6 months could have silently exfiltrated all of them.

This is exactly the gap that Credential Exposure Map fills. Static scanners check skills. This checks your actual exposure.

### Installation

```bash
openclaw skills install @Thomaszhou22/credential-exposure-map
```

### Usage

```
You: credential audit
Agent: Running full exposure scan...
       Found 40 findings: 14 Critical, 5 High, 19 Medium, 2 Low.
       
       CRITICAL: GitHub Token in MEMORY.md:103
       → Persists across sessions, readable by all skills
       → Recommendation: Redact from MEMORY.md, rotate token

You: exposure map
Agent: [generates full report with skill capability matrix]
```

### Risk Scoring

| Factor | Points |
|--------|--------|
| Valid API key format detected | +30 |
| In agent config/env (loaded at startup) | +25 |
| Readable by any skill (file access) | +20 |
| Persisted in MEMORY.md (cross-session) | +20 |
| Write access to external service | +15 |
| Used in recent sessions | +10 |
| Stored in plaintext | +10 |

### Tech Stack

- Python 3 (stdlib only, zero dependencies)
- OpenClaw cron system for scheduled audits

### File Structure

```
credential-exposure-map/
├── SKILL.md                 # Skill instructions
└── scripts/
    └── scan_exposure.py     # Main scanner engine
```

### Comparison

| Tool | Approach | This Skill |
|------|----------|-----------|
| mcp-scan | Static skill code analysis | Runtime credential surface mapping |
| SkillGuard | Pre-install skill scanner | Post-install exposure inventory |
| Agent Canary | Plants decoy credentials | Maps real credential exposure |
| Pipelock | Network proxy (egress) | File/memory/config scanning |

### Limitations

- Cannot detect secrets in encrypted files
- Git history scan limited to last 50 commits for performance
- MCP server auth scope inferred from config, not runtime testing
- Skill capability inference is conservative (assumes exec = full access)

### License

MIT
