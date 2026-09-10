---
name: mcp-config-security-checkup
description: "MCP security audit for AI-agent configs — run it before connecting any MCP server. 14 automated static rules catch hardcoded credentials, arbitrary command execution, writable mounts, SSRF attack surface, prompt-injection risks, plaintext HTTP endpoints and unpinned remote launchers, so unsafe agent tool calls get stopped before they run. Outputs CRIT/HIGH/MED/LOW findings with concrete fix advice. Runs 100% locally with zero network calls. Use when reviewing, auditing or scanning an MCP/agent server config (mcpServers JSON) for security issues, before wiring it into an agent."
version: 1.0.0
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_checkup
    emoji: "🛡️"
    envVars:
      - name: CCS_API_TOKEN
        required: false
        description: Optional API key for Correctover's hosted online checkup. Local mode needs no credentials at all.
---

# MCP Config Security Checkup — 14 static checks

> Before you wire an MCP (Model Context Protocol) server config into your
> agent, run it through a static security checkup first. This skill **runs
> fully on your machine by default** — the config never leaves the device and
> no network connection is ever made — and executes **14 automated static
> checks**, reporting findings as CRIT/HIGH/MED/LOW with concrete fix
> suggestions.
>
> 中文：在把 MCP 服务器配置挂到 Agent 前先做静态安全体检，默认全程本机运行、
> 零网络、配置不外传，输出 CRIT/HIGH/MED/LOW 分级发现与修复建议。

## What it checks

Pure static analysis of an MCP config document (usually a JSON containing
`mcpServers`; a single remote endpoint URL is also accepted). It never
connects to any address found in the config. The 14 checks cover:

- **CRIT**: cloud credential/secret signature strings hardcoded in the
  config; filesystem servers that are writable or mount root/home; exposure
  of arbitrary shell/command execution.
- **HIGH**: generic code/expression evaluation tools; fetch/network servers
  missing host allowlists (SSRF surface); generic secret/token strings in
  environment variables; database servers not declared read-only.
- **MED**: plaintext-HTTP remote endpoints; command strings with injection
  patterns (`$(...)`, backticks, pipe chaining); configs clustering
  exec/file/net dangerous capabilities; endpoints pointing at loopback,
  intranet, or cloud metadata addresses.
- **LOW**: `npx`/`uvx` remote package launchers with unpinned versions
  (supply-chain surface).

Outputs `risk_level` (CRIT/HIGH/MED/LOW/PASS), per-level counts, rule IDs,
server names, redacted evidence, and remediation advice.

## What it does NOT do

- **Zero network by default**: every check runs in a local process; the
  config document is never uploaded or sent anywhere, and no URL/endpoint in
  the config is ever contacted.
- **No dynamic probing**: even in `--endpoint-url` mode the URL is merely
  wrapped into a single-server config for static text checks — no connection
  is made. Live endpoint behavior, tool implementation code, permission
  boundaries, and data flows require a manual deep audit.
- It does not replace manual audit or penetration testing; the 14 automated
  checks are a first-pass screening layer, not a complete security
  assessment.
- It claims no endorsement by OWASP, IETF, or any standards body; standard
  names are referenced only to explain the check basis.

## Usage

```bash
# Check up an MCP config file (a document containing mcpServers)
python3 scripts/mcp_checkup.py -c examples/mcp_dangerous.json

# Static wrap check for a single remote endpoint URL (no connection made)
python3 scripts/mcp_checkup.py -u https://example.com/mcp

# Machine-readable JSON
python3 scripts/mcp_checkup.py -c mcp.json --json

# Read from stdin
cat mcp.json | python3 scripts/mcp_checkup.py
```

**Exit codes**: `0` = check ran to completion (any risk level counts as a
finding, including CRIT); `2` = input error; `3` = online mode returned
HTTP 402.

**Arguments**:

| Arg | Description |
|------|------|
| `-c/--config` | MCP config JSON file (contains `mcpServers`; a `{"config":{...}}` wrapper is also tolerated) |
| `-u/--endpoint-url` | A single remote MCP endpoint URL (static wrap check, no connection) |
| `--online` | Explicitly use Correctover's hosted online checkup (default is local, offline) |
| `--endpoint` | Online mode: override the CCS service endpoint |
| `--json` | Emit the full JSON report |

**Optional online mode**: by default every check runs locally with zero
network and zero data collection. Only with an explicit `--online` flag is
the config submitted to the Correctover CCS hosted service. That hosted
service is currently metered via Alipay A2M (Chinese payment rail); for
overseas users the **local mode is full-featured and free with no call
limits**, and an x402/USDC endpoint is on the roadmap. The local path needs
no credentials.

## Example

`examples/mcp_dangerous.json` is a deliberately dangerous config (root
filesystem mount, hardcoded cloud keys, shell executor, plaintext HTTP):

```text
  risk_level: CRIT
  Findings: CRIT=3  HIGH=3  MED=4  LOW=2
  Automated checks: 14
  [CRIT] Cloud credential/secret hardcoded in config          (MCP-001)
  [CRIT] Filesystem server writable or mounts root/home       (MCP-002)
  [CRIT] Arbitrary shell / command execution exposed          (MCP-003)
  [HIGH] Network/fetch server missing host allowlist (SSRF)   (MCP-005)
  ...
```

Secret values in evidence are redacted (e.g. `AKIAIO…(redacted)`); full
sensitive values are never echoed.

## Requirements

Python 3.7+, standard library only (`json`/`re`/`time`). No third-party
packages. Default mode makes no network requests.

## Privacy & security

- Pure static analysis, local by default: the config document never leaves
  the machine; no URL in the config is contacted.
- The script collects and uploads nothing; it is stateless and executes no
  commands against the target.
- Only explicit `--online` submits the config to the Correctover hosted
  service (self-managed API key). The server logs no request bodies — only
  an anonymous request ID, endpoint name, success/failure, and latency;
  request bodies are capped at 2 MiB.

## About

By **Correctover** (Guigui Wang) — *Correctover = AI Reliability*. We build
agent runtime verification: CCS (Correctover Conformance Shape) receipts,
Ed25519 tool-call verification, and AI-agent security tooling.
Homepage: <https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_checkup>

## Disclaimer

This report is auto-generated and applies only to the submitted input.
Automated checks are an aid only and constitute no security guarantee,
compliance conclusion, audit opinion, or legal opinion. No endorsement by
OWASP, IETF, or any standards body is claimed. The live behavior of remote
endpoints, tool implementation code, permission boundaries, and data flows
are outside the scope of automated checks and require manual review. Any
security decision must ultimately rely on qualified human review.

## License

MIT-0 for this ClawHub distribution. Anyone may use, modify, and
redistribute it, including commercially, with no attribution required.
