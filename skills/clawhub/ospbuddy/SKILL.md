---
name: OpsBuddy
description: "AI-Powered Intelligent Ops Assistant: an agent swarm that autonomously discovers issues and proactively repairs faults. After connecting, it unifies management of monitoring platforms (Signoz / Tencent Cloud / Aliyun / Nightingale) and covers asset discovery plus real-time monitoring for servers, databases, middleware and business systems. Supports overall situation inspection, root-cause diagnosis, log search and alert analysis — troubleshoot faults, locate root causes and generate remediation suggestions in natural language. Trigger words: ops / OpsBuddy / intelligent ops / server monitoring / host monitoring / database monitoring / middleware monitoring / business monitoring / fault diagnosis / alert analysis / log troubleshooting / connect ops platform / connect OpsBuddy."
version: 1.0.3
slogan: An AI Agent Swarm That Autonomously Discovers Issues and Proactively Repairs Faults
license: Commercial / Commercial License (Non-Open-Source)
pricing: Key is currently free to apply (self-registration → auto-approval)
token: An API Key (MCP token) is required. Self-register → auto-approved → log in to the portal, go to "My Applications" and download the MCP config JSON (contains the API Key). No default key.
requires_api_key: true   # This Skill requires an API Key (the OpsBuddy MCP token) to work
---

# OpsBuddy Connection Skill

Helps the user register the "OpsBuddy" MCP connection into WorkBuddy. **This Skill requires an API Key** (OpsBuddy access token / MCP Token); there is no default key and the user must obtain it on their own.

> **Core Principle**: This skill is only responsible for **configuring the API Key** and writing the MCP config JSON into the WorkBuddy configuration file. Platform connections (Signoz / Tencent Cloud / Aliyun / Nightingale), asset management and all other ops operations should be guided to the portal `http://119.45.243.120:45321`. Do not guide the user through entering credentials field-by-field in the conversation.

---

## I. What You Need to Prepare (Important)

> Connecting to "OpsBuddy" **requires** an **API Key (MCP token)** first. This key is the credential for accessing the ops platform; without it, connection fails.

**Where does the API Key come from?**
1. Open the portal `http://119.45.243.120:45321` → register an account → **system auto-approval** (no need to wait for an admin)
2. Log in to the portal → "My Applications" → click **"Download MCP Config"** on the approved record
3. You get `mcp-config.json`; the **`<TOKEN>` in `Authorization: Bearer <TOKEN>` is your API Key**
4. Keep it safe; do not share it in public

> ⚠️ If the user does not have an API Key yet, **do not** attempt to connect directly; first guide them through the registration and download above.

---

## II. Connection Flow (2 Steps)

Regardless of what the user asks, first present the following overview:

> Connecting "OpsBuddy" takes 2 steps:
> 1. **Obtain the API Key**: Open the portal `http://119.45.243.120:45321` → register (system auto-approval) → log in → "My Applications" → download the MCP config JSON (contains the API Key).
> 2. **Write the config**: Paste the downloaded JSON to me, and I write it into `~/.workbuddy/mcp.json`; then in WorkBuddy "Plugins → MCP Servers", click "Trust / Enable" for "OpsBuddy".
>
> After connecting, all ops capabilities are covered: cmdb (assets), server (hosts), business (business systems), database (databases), middleware (middleware), diagnose (fault diagnosis), log (logs), feedback (feedback).
> For platform connections (Signoz / Tencent Cloud / Aliyun / Nightingale), log in to the portal and operate in the "Platforms" page.

---

## III. Connection Guide (Step by Step)

### Step 1: Obtain the API Key (MCP Config JSON)

- Guide the user to open the portal **`http://119.45.243.120:45321`** (state the URL clearly) → registration page → fill in username / password / company / email / email verification code → submit the application.
- After submission, the **system auto-approves**, and the account is immediately usable (no need to wait for an admin).
- The user logs in to the portal → "My Applications" → click **"Download MCP Config"** on the approved record → get `mcp-config.json`.
- Ask the user to paste the **full** JSON to you (it contains the API Key).

### Step 2: Write the Config and Enable

- After receiving the JSON, write it directly to `~/.workbuddy/mcp.json` (create if not exists; merge-append if exists, overwrite same name). This step is not counted or announced separately; just mention it in one line ("Config written").
- WorkBuddy **will not automatically reload** the file after writing; the user needs to open "Plugins → MCP Servers → Configure MCP" or restart WorkBuddy, and click "Trust / Enable" for "OpsBuddy".
- After the user clicks "Trust / Enable", tell the user:
  > ✅ MCP connection is ready and the API Key is configured successfully. Next, log in to the portal `http://119.45.243.120:45321` → "Platforms" page, configure the monitoring platform yourself (currently supported: Signoz, Aliyun, Tencent Cloud, Nightingale), and click "Discover" after configuration to pull down its resources.

---

## IV. FAQ

| Question | Answer |
|---|---|
| What if I don't have an API Key? | Open the portal `http://119.45.243.120:45321` and register → system auto-approval → log in → "My Applications" → download the MCP config (contains the API Key). |
| What is the API Key? | It is the `<TOKEN>` in `Authorization: Bearer <TOKEN>` in the MCP config JSON — the credential for accessing the ops platform. |
| How do I connect Signoz / Tencent Cloud / Aliyun / Nightingale? | Log in to the portal → "Platforms" page → add a platform → fill in the connection info and save → click "Discover" to pull down resources. |
| What if my token expires? | Re-apply / renew on the portal, re-download the MCP config and update the API Key. |
| What if my API Key is leaked? | Immediately revoke it on the portal and re-apply, then update the WorkBuddy config. |

---

## V. Config Template (Backup)

```json
{
  "mcpServers": {
    "OpsBuddy": {"url": "{{GATEWAY_URL}}/mcp/unified", "headers": {"Authorization": "Bearer {{API_KEY}}"}}
  }
}
```

> The template is only a backup. In normal flow, the user pastes the JSON downloaded from the portal (which contains the API Key) to you.
