# MGC Blackbox Meta Skill

A documentation skill for building **zero‑exposure AI skills** using MGC Blackbox.

## What This Skill Is

MGC Blackbox Meta Skill teaches AI skill developers how to build skills that:
- Store sensitive data (tokens, passwords, configs, scripts) securely
- Execute stored scripts without plaintext leakage
- Use MCP tools for AI‑agent integration

## Prerequisites

- Python 3.10+
- Install: `pip install mgc-blackbox` (requires MGC 1.4.10+)
- Start MGC: `mgc` (API runs at http://127.0.0.1:57219, WebUI at http://127.0.0.1:57218)

## Quick Start

### 1. Store Sensitive Data

```python
# Use MCP tool to store
mgc_save(
    info_type="token",
    info_owner="my_skill_api_key",
    content="sk-abc123..."
)
```

### 2. Retrieve at Runtime

```python
# AI retrieves via MCP - gets result only
result = mgc_get(
    info_type="token",
    info_owner="my_skill_api_key"
)
```

### 3. Execute Scripts

```python
# Store executable script
mgc_save(
    info_type="script",
    info_owner="query_db",
    ext01="python",
    content="import argparse\nparser = argparse.ArgumentParser()\nparser.add_argument('--query', default='SELECT * FROM users')\nargs = parser.parse_args()\nprint(args.query)"
)
# MGC auto-parses argparse and fills ext02

# Execute later - AI never sees script source
mgc_run(
    info_type="script",
    info_owner="query_db",
    diff_1="..."
)
```

## Supported Platforms

- Windows
- macOS
- Linux

## MCP Tools

| Tool | Description |
|------|-------------|
| mgc_save | Store sensitive data or scripts (auto-parses argparse for scripts) |
| mgc_get | Retrieve decrypted content of an entry |
| mgc_run | Execute a stored script (recommended over mgc_get action="run") |
| mgc_seal | Seal script for delegated execution across nodes |
| mgc_list | List stored entries (metadata only) |
| mgc_open_webui | Open WebUI in browser |

> **Note:** `mgc_run` is the recommended tool for script execution. `mgc_get` with `action="run"` is kept for backward compatibility.

## Links

- **Main Repo**: https://github.com/zkeviny/MGC-Blackbox
- **Issues**: https://github.com/zkeviny/MGC-Blackbox/issues
- **Contact**: mirgincipher@outlook.com

## Related Skills (Zero‑Exposure Ecosystem)
These skills are built on top of MGC Blackbox and follow the same zero‑exposure pattern:

SMTP Token Security — Secure storage for SMTP credentials used in email workflows.

Database Credential Security — Zero‑exposure storage for database passwords and connection strings.

Webhook Token Security — Safe storage for Slack / Telegram / DingTalk / Feishu webhook tokens.

Key‑Safe Generator — Generates strong random keys for scripts and configurations.

All of these skills use MGC Blackbox as their encrypted execution layer.
