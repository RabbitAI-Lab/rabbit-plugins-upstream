---
name: fuze-crm
description: Manage contacts, companies, sales opportunities, tasks, notes, dashboards and follow-up workflows in Fuze CRM. Use when the user asks to connect to Fuze, set up a CRM workspace, maintain their Fuze records, review their sales pipeline, or try a fictional CRM demo.
---

# Fuze CRM

Use the user's existing Fuze CRM connection for their requested CRM work. The hosted MCP server is `https://crm.withfuze.com/mcp` (Streamable HTTP, OAuth). A connection is scoped to one private workspace.

## Connect when requested

- If an authorized Fuze MCP connection is present, call `workspace` first. It returns the actual table and field keys, plan, limits, usage and dashboards. Do not create a second workspace to do the same work.
- Otherwise, use the client's normal remote MCP connection flow and ask the user to approve access. Approval creates a private workspace if this is a new connection. Do not approve OAuth or sign up on the user's behalf without authorization. See [setup by client](https://crm.withfuze.com/for-agents).
- A browser-capable assistant can instead help the user try the [live demo](https://crm.withfuze.com/demo) if requested. Clicking Start free live demo creates a temporary workspace. A chat that can only read pages must offer the demo or connection link, not claim to have created a workspace.
- For a client with HTTP tools but no MCP support, the [official API guide](https://crm.withfuze.com/llms.txt) describes the separate, temporary REST signup. Follow it only when the user authorizes setup. Store any returned credentials in the client's protected credential storage, never in messages, public files, CRM data or logs.

## Work with the user's records

1. Read `workspace` to discover the schema. The built-in tables are `crm_company`, `crm_person`, `crm_deal`, `crm_task` and `crm_note`. Use the live schema rather than guessing field names, relation targets or select choices.
2. Search existing records with `list_records` before creating or updating them; page if necessary. Identify the exact record before changing it. Use its returned ID for relationships and updates.
3. Perform only the writes the user authorized. For an example workspace, use clearly fictional records. Explain impact before deleting records, replacing a handover link, or enabling a workflow that makes future changes. Never delete an actual customer record as part of a demo or test.
4. Read back saved records or workflow runs and report the actual outcome. If a tool reports an error, say which action failed; do not invent an ID, result or completed write.

### Small examples

- Find a company: `list_records` with `{"table":"crm_company","search":"Acme Ltd"}`.
- Add a fictional company when requested: `create_record` with `{"table":"crm_company","data":{"name":"Acme Ltd"}}`.
- Review the sales pipeline: `chart` with `{"table":"crm_deal","field":"stage"}`. Confirm the field exists and distinguish counts from monetary totals.
- Save a pipeline dashboard: `create_dashboard` with `{"name":"Pipeline","charts":[{"title":"Deals by stage","table":"crm_deal","field":"stage"}]}`.
- With the user's approval, create a task when a deal is created using `create_workflow` with `{"name":"Follow up new deals","trigger":{"table":"crm_deal","event":"record_created"},"steps":[{"action":"create_record","table":"crm_task","data":{"title":"Follow up: {{record.name}}","status":"To do","deal":"{{record.id}}"}}]}`. Check recent `list_workflow_runs` after a matching change. Pause using `set_workflow_enabled` if requested.

## Limits and ownership

The Free workspace currently allows 1,000 records, 10 MB of logical record data, six tables (including five built-ins), two dashboards, 20 workflows and 5,000 record writes per UTC day. Read `workspace` for current limits. Connected Free workspaces are removed after 90 days of inactivity; anonymous browser/REST trials expire within 70 hours unless ownership is approved. Workflows run immediately on record events, one to three steps; no scheduled execution, cascading workflows, email, file uploads, payments or other external actions.

When a user explicitly wishes to take ownership, use `get_claim_link` only for an unowned MCP workspace; it invalidates any earlier handover code. Provide the code privately to the intended owner; they enter their name and email on the handover page and await approval before signing in. No agent plan purchase or automatic human-account approval.

Reference: [MCP tools and HTTP API](https://crm.withfuze.com/docs/mcp) · [Privacy](https://crm.withfuze.com/privacy) · [Terms](https://crm.withfuze.com/terms).
