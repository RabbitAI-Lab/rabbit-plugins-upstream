<div align="center">

# Agent Canary

**Decoy credentials for OpenClaw workspaces. Canary tokens trigger alerts when read, copied, or exfiltrated by malicious skills.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![Python 3](https://img.shields.io/badge/Python-3-green)](https://www.python.org/)
[![ClawHub](https://img.shields.io/badge/ClawHub-agent--canary-orange)](https://clawhub.ai)

</div>

`[English](#english) | [中文](./README_CN.md)`

---

## English

### Introduction

Agent Canary is an active defense skill for OpenClaw. It generates realistic-looking fake credentials (AWS keys, GitHub tokens, API keys, Stripe keys, database passwords) and plants them in strategic locations across your workspace. When a malicious skill reads, copies, or exfiltrates these credentials, Agent Canary detects it and alerts you immediately.

Unlike static scanners that only check skills before installation, Agent Canary catches malicious behavior at runtime, when a skill actually tries to access your credentials.

### The Problem

- 7.6% of ClawHub skills contain malicious patterns (Snyk research, Feb 2026)
- 36% contain at least one security flaw
- Static scanners can be bypassed in under 1 hour (Trail of Bits, Jun 2026)
- Malicious skills can steal credentials from `.env` files, memory files, and config
- No existing tool actively monitors for credential theft at runtime

### How It Works

```
┌─────────────────────────────────────────────────┐
│  1. GENERATE fake credentials                    │
│     AWS keys, GitHub PATs, Stripe keys, etc.    │
│     Each has unique CANARY fingerprint           │
│                                                  │
│  2. PLANT in strategic locations                 │
│     .env.canary, secrets.backup.json,            │
│     memory/canary-tokens.json                   │
│                                                  │
│  3. MONITOR via cron (every 30 min)              │
│     ┌──────────┬──────────┬───────────────────┐ │
│     │ Hash     │ atime    │ Log + Git grep    │ │
│     │ modified │ accessed │ Token exfiltrated │ │
│     └──────────┴──────────┴───────────────────┘ │
│                                                  │
│  4. ALERT when triggered                         │
│     Severity + file + token ID + recommendation  │
└─────────────────────────────────────────────────┘
```

### Features

- **5 token types**: AWS Access Keys, GitHub PATs, Stripe keys, Generic API keys, Database passwords
- **3 placement locations**: `.env.canary`, `secrets.backup.json`, `memory/canary-tokens.json`
- **4 detection methods**: File hash comparison, access time monitoring, exec log grepping, git diff checking
- **Automatic alerting**: Immediate notification with severity, file, and recommendation
- **Clean setup and teardown**: Deploy and cleanup with a single command
- **Zero real credentials touched**: All tokens are fake, marked with `CANARY`, cannot authenticate

### Live Demo

**Before** (no protection):

```
Malicious skill installed
  → silently reads .env
  → finds AWS_ACCESS_KEY_ID
  → exfiltrates to attacker server
  → you never know
```

**After** (with Agent Canary):

```
Malicious skill installed
  → reads .env.canary (canary file)
  → finds fake AWS key "AKIACANARY7F3A2B9X0"
  → exfiltrates to attacker server
  → cron check finds token in logs
  → YOU GET ALERTED IMMEDIATELY
  → rotate real credentials, uninstall skill
```

### Installation

#### As OpenClaw Skill

```bash
openclaw skills install @Thomaszhou22/agent-canary
```

#### Manual

```bash
git clone https://github.com/Thomaszhou22/agent-canary.git
cd agent-canary
```

### Usage

```
You: deploy canary
Agent: Canary deployed! 5 tokens planted in 3 files.
       Monitoring cron active (every 30 min).

You: canary status
Agent: 3 canary files intact. Last check: 2026-07-30 12:00.
       0 incidents.

You: canary check
Agent: Running immediate check...
       CRITICAL: Token "AKIACANARY..." found in exec log!
       File: .env.canary
       Recommendation: Check which skill was running at 12:34.

You: canary cleanup
Agent: 3 files removed. Monitoring stopped.
```

### Tech Stack

- Python 3 (stdlib only, zero dependencies)
- OpenClaw cron system for scheduled monitoring
- OpenClaw message tool for alerting

### File Structure

```
agent-canary/
├── SKILL.md                      # Skill instructions
├── scripts/
│   ├── generate_tokens.py        # Token generation engine
│   ├── plant_canaries.py         # Canary file deployment
│   ├── check_canaries.py         # Monitoring and detection
│   └── cleanup_canaries.py       # Removal
└── templates/                    # Canary file templates
```

### Comparison

| Tool | Approach | Agent Canary |
|------|----------|-------------|
| sukiraman/canary | Passive secret scanning | Active decoy planting |
| mcp-scan | Static code analysis before install | Runtime detection after install |
| SkillGuard | Pre-installation scanner | Continuous post-install monitoring |
| Pipelock | Network proxy (requires setup) | No network config needed |

### Limitations

- Cannot detect exfiltration through encrypted channels without network-level inspection
- File access time (atime) may not work on all filesystems
- Checks on 30-minute cron interval (not real-time)
- `CANARY` markers make tokens obvious to human inspection (by design, for safe cleanup)

### License

MIT
