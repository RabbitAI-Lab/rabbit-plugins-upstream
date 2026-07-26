---
name: plaud
description: "Plaud: Work with the user's connected Plaud account to act on their voice recordings. Use when an agent needs plaud, turn meeting recordings into crm notes and follow up tasks, draft follow up emails from a call transcript, summarize interviews and save notes to a shared doc, extract action items from voice memos into a task manager, get current user, get file, file id through AgentPMT-hosted remote tool calls. Discovery terms: plaud, turn meeting recordings into crm notes and follow up tasks."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/plaud
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/plaud"}}
---
# Plaud

## Freshness
Last updated: `2026-07-21`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Bring your Plaud recordings into every tool you already use. Plaud captures your meetings, calls, and voice memos as recordings, AI summaries, and full transcripts — and this makes all of it available to your AI assistant so nothing stays trapped in the app. Search recordings by name or date, pull speaker-attributed transcripts and AI notes, and build automations and workflows around what was said: follow-up emails, CRM notes, tasks, project updates, and shared documents. Connect Plaud once and every conversation you capture can flow automatically into the tools your team already runs on.

## Product Instructions
Plaud captures the user's voice recordings along with AI-generated notes and full transcripts. The user must link their Plaud account once through the Plaud connection before any call succeeds — always use the stored account connection and never ask the user for a Plaud username or password.

Typical flow:
1. Use list_files to find a recording. Filter with `query` (name substring) and/or `date_from`/`date_to` when the user references a specific meeting or day.
2. Use get_note for a quick AI summary, action items, and key topics.
3. Use get_transcript for the full speaker-attributed, timestamped transcript when you need exact wording or quotes.
4. Use get_file for a recording's details, and get_current_user to confirm the connected account.

Only surface recordings the connected Plaud account can access, and respect the user's Plaud account permissions.

## When To Use
- Use this skill for `Plaud` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: plaud, turn meeting recordings into crm notes and follow up tasks, draft follow up emails from a call transcript, summarize interviews and save notes to a shared doc, extract action items from voice memos into a task manager, get current user, get file, file id.
- Supported action names: `get_current_user`, `get_file`, `get_note`, `get_transcript`, `list_files`.

## Use Cases
- Turn meeting recordings into CRM notes and follow-up tasks
- Draft follow-up emails from a call transcript
- Summarize interviews and save notes to a shared doc
- Extract action items from voice memos into a task manager
- Search past recordings by topic
- name
- or date
- Pull speaker-attributed transcripts for analysis or quotes
- Review a recording's AI summary before a follow-up
- Sync Plaud meeting notes into project and CRM tools

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `5`.
x402 availability: not enabled for this product.

- `get_current_user` (action slug: `get-current-user`): Get current authenticated user info Price: `5` credits. Parameters: none.
- `get_file` (action slug: `get-file`): Get details of a specific Plaud recording by ID Price: `5` credits. Parameters: `file_id`.
- `get_note` (action slug: `get-note`): Fetch AI-generated notes for a Plaud recording — compact summary, action items, and key topics Price: `5` credits. Parameters: `file_id`.
- `get_transcript` (action slug: `get-transcript`): Fetch the full timestamped transcript with speaker attribution for a Plaud recording Price: `5` credits. Parameters: `file_id`.
- `list_files` (action slug: `list-files`): List Plaud recordings. Supports optional client-side filtering: `query` (case-insensitive name substring), `date_from`/`date_to` (YYYY-MM-DD, inclusive). When any filter is set, paginates up to 5 pages × 100 recordings and returns all matches. Price: `5` credits. Parameters: `date_from`, `date_to`, `page`, `page_size`, `query`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "plaud"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "plaud"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "plaud"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "plaud"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "plaud"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "plaud"
  }
}
```

## Call This Tool
Product slug: `plaud`

Marketplace page: https://www.agentpmt.com/marketplace/plaud

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Plaud",
    "arguments": {
      "action": "get_current_user"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "plaud",
  "parameters": {
    "action": "get_current_user"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `get_current_user` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/plaud
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
