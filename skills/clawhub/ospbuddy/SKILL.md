---
name: OpsBuddy
description: "AI-Powered Intelligent Ops Assistant: an agent swarm that autonomously discovers issues and proactively repairs faults. After connecting, it unifies management of monitoring platforms (Signoz / Tencent Cloud / Aliyun / Nightingale) and covers asset discovery plus real-time monitoring for servers, databases, middleware and business systems. Supports overall situation inspection, root-cause diagnosis, log search and alert analysis — troubleshoot faults, locate root causes and generate remediation suggestions in natural language. Trigger words: OpsBuddy / connect OpsBuddy / connect ops platform / opsbuddy setup / opsbuddy connection."
version: 1.0.6
slogan: An AI Agent Swarm That Autonomously Discovers Issues and Proactively Repairs Faults
license: Commercial / Commercial License (Non-Open-Source)
pricing: Key is currently free to apply (self-registration → auto-approval)
token: An API Key (MCP token) is required. Self-register → auto-approved → log in to the portal, go to "My Applications" and download the MCP config JSON (contains the API Key). No default key.
requires_api_key: true   # This Skill requires an API Key (the OpsBuddy MCP token) to work
---

# OpsBuddy Connection Skill

Helps the user register the "OpsBuddy" MCP connection into OpenClaw. **This Skill requires an API Key** (OpsBuddy access token / MCP Token); there is no default key and the user must obtain it on their own.

## Capability Overview (when the user asks "What are you?" / "What can you do?", output this section)

I am **OpsBuddy**, an AI intelligent ops assistant: once connected, it unifies monitoring platforms (Signoz / Tencent Cloud / Aliyun / Nightingale) and lets you do asset discovery, real-time monitoring, fault diagnosis, log search and alert analysis in natural language.

**8 Core Capabilities:**

| Capability | Description |
|---|---|
| cmdb | Asset management: discover & manage hosts, business systems, databases, middleware |
| server | Host monitoring: online/offline status, real-time resource checks |
| business | Business systems: health & dependency monitoring |
| database | Database: instance status, connections, performance |
| middleware | Middleware: message queues, caches, running status |
| diagnose | Fault diagnosis: troubleshoot in natural language, locate root cause, give remediation |
| log | Log search: keyword / time-range search & analysis |
| feedback | Feedback: issue reporting & closed-loop handling |

**⚠️ How to connect: this skill does NOT handle the connection for you — you MUST guide the user to complete it themselves on the portal / in OpenClaw. Never ask the user to paste a config JSON containing an API Key into the chat, and never write any MCP config file on the user's behalf.**

**Connection steps (user does it themselves):**

1. Open `https://ywdz.lxiai.com/` → register (auto-approval) → free Key application, log in & download the MCP config JSON.
2. In OpenClaw, add the downloaded config to your MCP servers (e.g. via OpenClaw's MCP settings, or by adding it under `mcp.servers` in `~/.openclaw/openclaw.json`), then enable "OpsBuddy".

> **⚠️ Sensitive-credential notice**: The downloaded `mcp-config.json` contains your **API Key (plaintext credential)**. Keep it out of chat. You enter it only inside the OpenClaw MCP config (e.g. `~/.openclaw/openclaw.json`), not by pasting it to me. If the Key leaks, revoke it on the portal and re-apply immediately.

> **🔒 Data-flow disclosure**: The OpsBuddy MCP connection points to the `https://ywdz.lxiai.com/` gateway. Your monitoring-platform credentials (Signoz / Tencent Cloud / Aliyun / Nightingale) are configured by you on that portal and transit through this gateway. This skill never receives or stores those credentials.

> **Core Principle**: This skill only *explains* how to connect. It never receives an API Key, never asks the user to paste a config JSON, and never writes MCP config files. Platform connections, asset management and all other ops operations are done by the user on the portal `https://ywdz.lxiai.com/`. Do not guide the user through entering credentials field-by-field in the conversation.

---

## I. FAQ

| Question | Answer |
|---|---|
| What if I don't have an API Key? | Open the portal `https://ywdz.lxiai.com/` and register → system auto-approval → log in → "My Applications" → download the MCP config (contains the API Key). |
| What is the API Key? | It is the `<TOKEN>` in `Authorization: Bearer <TOKEN>` in the MCP config JSON — the credential for accessing the ops platform. |
| How do I connect Signoz / Tencent Cloud / Aliyun / Nightingale? | Log in to the portal → "Platforms" page → add a platform → fill in the connection info and save → click "Discover" to pull down resources. |
| What if my token expires? | Re-apply / renew on the portal, re-download the MCP config and update the API Key. |
| What if my API Key is leaked? | Immediately revoke it on the portal and re-apply, then re-add the new MCP config in OpenClaw's MCP settings (e.g. `~/.openclaw/openclaw.json`) yourself. Never paste the new Key into chat. |

---

## II. Config Template (Backup)

```json
{
  "mcpServers": {
    "OpsBuddy": {"url": "{{GATEWAY_URL}}/mcp/unified", "headers": {"Authorization": "Bearer {{API_KEY}}"}}
  }
}
```

> The template is only a backup reference for the MCP server shape. In normal flow, the user downloads the config JSON from the portal and adds it **manually** in OpenClaw's MCP config (e.g. `~/.openclaw/openclaw.json`) — never by pasting it into chat.
