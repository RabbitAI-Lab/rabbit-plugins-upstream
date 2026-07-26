---
name: zoho-books
description: "Zoho Books: manage chart of accounts, journal entries, contacts, invoices, bills, expenses, payments, projects, time entries. Permission-gated. Use when an agent needs zoho books, list organizations, list chart of accounts, create journal entries, import bank statements, bank get matching transactions, organization id, record id through AgentPMT-hosted remote tool calls. Discovery terms: zoho books, list organizations, list chart of accounts, create journal entries, import bank statements."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/zoho-books
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/zoho-books"}}
---
# Zoho Books

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Access Zoho Books with OAuth to list organizations and manage core accounting resources such as chart of accounts, journal entries, contacts, items, invoices, estimates, credit notes, bills, expenses, payments, projects, tasks, and time entries. Includes explicit invoice status and bank reconciliation actions with permission gating and supports organization-scoped queries.

## Product Instructions
### Zoho Books

#### Actions

Use `describe_action` with `action_to_describe` to get the full schema for any action.

#### Supported Resources

contacts, items, invoices, estimates, creditnotes, chartofaccounts, journals, bankaccounts, banktransactions, bankstatements, bills, expenses, vendorcredits, customerpayments, vendorpayments, projects, tasks, time_entries

**Note:** `tasks` requires `project_id`. `bankstatements` only supports `create_record`.

#### Pagination

List responses default to **25 records per page**. Use `per_page` (max 200) and `page` in `query_params` to control pagination. Check the `page_context` object in the response for `has_more_page`.

#### Tool Call Format

##### List Organizations
```json
{
  "action": "list_organizations"
}
```

##### List Records
```json
{
  "action": "list_records",
  "resource": "invoices",
  "organization_id": "YOUR_ORG_ID",
  "query_params": {
    "page": 1,
    "per_page": 25
  }
}
```

##### Get Record
```json
{
  "action": "get_record",
  "resource": "contacts",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Create Record
```json
{
  "action": "create_record",
  "resource": "contacts",
  "organization_id": "YOUR_ORG_ID",
  "payload": {
    "contact_name": "Bowman & Co"
  }
}
```

##### Update Record
```json
{
  "action": "update_record",
  "resource": "contacts",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049",
  "payload": {
    "contact_name": "Bowman & Co (Updated)"
  }
}
```

##### Delete Record
```json
{
  "action": "delete_record",
  "resource": "invoices",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Invoice - Mark as Sent
```json
{
  "action": "invoice_mark_sent",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Invoice - Mark as Void
```json
{
  "action": "invoice_mark_void",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Invoice - Mark as Draft
```json
{
  "action": "invoice_mark_draft",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Invoice - Send Email
```json
{
  "action": "invoice_email",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049",
  "payload": {
    "to_mail_ids": ["customer@example.com"],
    "subject": "Invoice from Your Company",
    "body": "Please find the invoice attached."
  }
}
```

##### Bank - Get Matching Transactions
```json
{
  "action": "bank_get_matching_transactions",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Bank - Match Transaction
```json
{
  "action": "bank_match_transaction",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049",
  "payload": {
    "transactions_to_be_matched": [
      {"transaction_id": "460000000026050", "transaction_type": "invoice"}
    ]
  }
}
```

##### Bank - Unmatch Transaction
```json
{
  "action": "bank_unmatch_transaction",
  "organization_id": "YOUR_ORG_ID",
  "record_id": "460000000026049"
}
```

##### Describe Action
```json
{
  "action": "describe_action",
  "action_to_describe": "list_records"
}
```

##### Tasks (requires project_id)
```json
{
  "action": "list_records",
  "resource": "tasks",
  "organization_id": "YOUR_ORG_ID",
  "project_id": "460000000030001"
}
```

#### Permissions

Write actions require the corresponding permission in the `permissions` array:
- `create_record` requires `add`
- `update_record`, `invoice_mark_sent`, `invoice_mark_void`, `invoice_mark_draft`, `invoice_email`, `bank_match_transaction`, `bank_unmatch_transaction` require `edit`
- `delete_record` requires `delete`
- Combine exact scopes as needed, such as `[`read`, `edit`]` for read plus update access.
- If `permissions` is omitted, Zoho Books defaults to read-only access.

## When To Use
- Use this skill for `Zoho Books` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: zoho books, list organizations, list chart of accounts, create journal entries, import bank statements, bank get matching transactions, organization id, record id.
- Supported action names: `bank_get_matching_transactions`, `bank_match_transaction`, `bank_unmatch_transaction`, `create_record`, `delete_record`, `describe_action`, `get_record`, `invoice_email`, `invoice_mark_draft`, `invoice_mark_sent`, `invoice_mark_void`, `list_organizations`, `list_records`, `update_record`.

## Use Cases
- List organizations
- List chart of accounts
- Create journal entries
- Import bank statements
- Match bank transactions
- Sync contacts
- Create invoices
- Update invoice status
- Email invoices
- Track expenses

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `14`.
x402 availability: not enabled for this product.

- `bank_get_matching_transactions` (action slug: `bank-get-matching-transactions`): Find existing transactions that could match an uncategorized bank transaction. Price: `5` credits. Parameters: `organization_id`, `query_params`, `record_id`.
- `bank_match_transaction` (action slug: `bank-match-transaction`): Match an uncategorized bank transaction to one or more existing transactions. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `payload`, `query_params`, `record_id`.
- `bank_unmatch_transaction` (action slug: `bank-unmatch-transaction`): Remove the match from a previously matched bank transaction. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `query_params`, `record_id`.
- `create_record` (action slug: `create-record`): Create a new record for a given resource type. Requires 'add' permission. The bankstatements resource only supports this action (used to import statements). Price: `5` credits. Parameters: `organization_id`, `payload`, `project_id`, `query_params`, `resource`.
- `delete_record` (action slug: `delete-record`): Delete a record. Requires 'delete' permission. Price: `5` credits. Parameters: `organization_id`, `project_id`, `query_params`, `record_id`, `resource`.
- `describe_action` (action slug: `describe-action`): Get the detailed parameter schema for any action. Useful for discovering required and optional fields. Price: `5` credits. Parameters: `action_to_describe`.
- `get_record` (action slug: `get-record`): Retrieve a single record by its ID. Price: `5` credits. Parameters: `organization_id`, `project_id`, `query_params`, `record_id`, `resource`.
- `invoice_email` (action slug: `invoice-email`): Send an invoice by email. Requires 'edit' permission. Payload must include recipient email addresses, subject, and body. Price: `5` credits. Parameters: `organization_id`, `payload`, `query_params`, `record_id`.
- `invoice_mark_draft` (action slug: `invoice-mark-draft`): Revert an invoice to draft status. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `query_params`, `record_id`.
- `invoice_mark_sent` (action slug: `invoice-mark-sent`): Mark an invoice as sent. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `query_params`, `record_id`.
- `invoice_mark_void` (action slug: `invoice-mark-void`): Mark an invoice as void. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `query_params`, `record_id`.
- `list_organizations` (action slug: `list-organizations`): Retrieve all Zoho Books organizations associated with your account. Use this first to obtain your organization_id. Price: `5` credits. Parameters: `query_params`.
- `list_records` (action slug: `list-records`): List records for a given resource type with pagination support. Defaults to 25 records per page. Price: `5` credits. Parameters: `organization_id`, `project_id`, `query_params`, `resource`.
- `update_record` (action slug: `update-record`): Update an existing record. Requires 'edit' permission. Price: `5` credits. Parameters: `organization_id`, `payload`, `project_id`, `query_params`, `record_id`, `resource`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "zoho-books"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "zoho-books"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "zoho-books"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "zoho-books"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "zoho-books"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "zoho-books"
  }
}
```

## Call This Tool
Product slug: `zoho-books`

Marketplace page: https://www.agentpmt.com/marketplace/zoho-books

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
    "name": "Zoho-Books",
    "arguments": {
      "action": "bank_get_matching_transactions",
      "organization_id": "example organization id",
      "query_params": {},
      "record_id": "example record id"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "zoho-books",
  "parameters": {
    "action": "bank_get_matching_transactions",
    "organization_id": "example organization id",
    "query_params": {},
    "record_id": "example record id"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `bank_get_matching_transactions` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/zoho-books
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
