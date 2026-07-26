---
name: google-sheets
description: "Google Sheets: Work with Google Sheets using safe short actions: create and find spreadsheets, list tabs, read data, append rows at the true table end, append columns at the current data edge, update selected fields by key, export. Use when an agent needs google sheets, google sheets api, append spreadsheet rows safely, update crm style rows by key, export a sheet to csv or pdf, create reporting spreadsheets, add conditional formatting, spreadsheet id through AgentPMT-hosted remote tool calls."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-sheets-api
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-sheets-api"}}
---
# Google Sheets

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Create, read, update, format, share, and export Google Sheets with agent-safe spreadsheet workflows. Append rows at the true table end, append columns after the last non-empty data column, update selected fields in matched rows, manage tabs, apply validation and formatting, and store CSV/PDF/XLSX exports in File Manager.

## Product Instructions
### Google Sheets

Use short action names. Prefer `read`, `append_rows`, `append_column`, `update_row`, and `export_sheet` for common workflows.

Safety rules:
- Do not guess a tab is named `Sheet1`; omit `sheet_name` or call `list_sheets`.
- Do not calculate append row or column positions; use `append_rows` or `append_column`.
- `append_rows` appends at the true table end. `append_column` writes after the last non-empty data column, not at a blank default grid edge.
- Do not overwrite full rows when only selected fields changed; use `update_row` with `updates`.
- Use `export_sheet` for CSV/TSV/PDF/XLSX/ODS/HTML/ZIP exports. Specific-sheet rendered exports use an official temporary-spreadsheet flow.

Examples:
```json
{"action":"read","spreadsheet_id":"1abc...","sheet_name":"Leads","range":"A1:D20"}
```
```json
{"action":"append_rows","spreadsheet_id":"1abc...","sheet_name":"Leads","rows":[{"Name":"Ada","Status":"New"}]}
```
```json
{"action":"append_column","spreadsheet_id":"1abc...","sheet_name":"Leads","column_name":"Owner","column_values":["Sam","Riley"]}
```
```json
{"action":"update_row","spreadsheet_id":"1abc...","sheet_name":"Leads","key_column":"Email","key_value":"ada@example.com","updates":{"Status":"Qualified","Owner":"Sam"}}
```
```json
{"action":"export_sheet","spreadsheet_id":"1abc...","sheet_name":"Leads","format":"pdf","filename":"leads.pdf"}
```

## When To Use
- Use this skill for `Google Sheets` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google sheets, google sheets api, append spreadsheet rows safely, update crm style rows by key, export a sheet to csv or pdf, create reporting spreadsheets, add conditional formatting, spreadsheet id.
- Supported action names: `add_conditional_formatting`, `add_named_range`, `add_sheet`, `append_column`, `append_rows`, `copy_paste`, `create`, `cut_paste`, `delete_named_range`, `delete_sheet`, `export_sheet`, `find_replace`, `format_cells`, `get_data_range`, `get_headers`, `list_sheets`, `protect_range`, `read`, `rename_sheet`, `search`, `set_data_validation`, `share`, `sort`, `unprotect_range`, `update_row`.

## Use Cases
- append spreadsheet rows safely
- update CRM-style rows by key
- export a sheet to CSV or PDF
- create reporting spreadsheets
- add data validation to templates
- protect header ranges
- share sheets with collaborators
- copy or move spreadsheet ranges
- format dashboards
- manage sheet tabs

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `25`.
x402 availability: not enabled for this product.

- `add_conditional_formatting` (action slug: `add-conditional-formatting`): Add a conditional formatting rule to a range. Price: `5` credits. Parameters: `range`, `rule`, `sheet_name`, `spreadsheet_id`.
- `add_named_range` (action slug: `add-named-range`): Create a named range. Price: `5` credits. Parameters: `name`, `range`, `sheet_name`, `spreadsheet_id`.
- `add_sheet` (action slug: `add-sheet`): Add a new tab to a spreadsheet. Price: `5` credits. Parameters: `new_sheet_name`, `spreadsheet_id`.
- `append_column` (action slug: `append-column`): Append one new column immediately after the last non-empty data column and write its header and values. Price: `5` credits. Parameters: `column_name`, `column_values`, `sheet_name`, `spreadsheet_id`.
- `append_rows` (action slug: `append-rows`): Append rows at the true table end. Object rows are mapped by sheet headers. Price: `5` credits. Parameters: `header_row`, `rows`, `sheet_name`, `spreadsheet_id`, `value_input_option`.
- `copy_paste` (action slug: `copy-paste`): Copy a source range to a destination range. Price: `5` credits. Parameters: `destination_range`, `paste_orientation`, `paste_type`, `sheet_name`, `source_range`, `spreadsheet_id`.
- `create` (action slug: `create`): Create a new spreadsheet, optionally with an initial tab, headers, and rows. Price: `5` credits. Parameters: `initial_headers`, `initial_sheet_name`, `rows`, `title`.
- `cut_paste` (action slug: `cut-paste`): Move a source range to a destination start cell. Price: `5` credits. Parameters: `destination_range`, `paste_type`, `sheet_name`, `source_range`, `spreadsheet_id`.
- `delete_named_range` (action slug: `delete-named-range`): Delete a named range by id. Price: `5` credits. Parameters: `named_range_id`, `spreadsheet_id`.
- `delete_sheet` (action slug: `delete-sheet`): Delete a tab by name, id, or index. Price: `5` credits. Parameters: `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `export_sheet` (action slug: `export-sheet`): Export a specific sheet or whole spreadsheet to File Manager as CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP. Price: `5` credits. Parameters: `expiration_days`, `filename`, `format`, `range`, `sheet_id`, `sheet_name`, `spreadsheet_id`.
- `find_replace` (action slug: `find-replace`): Find and replace text across the spreadsheet or one sheet. Price: `5` credits. Parameters: `find`, `match_case`, `match_entire_cell`, `replacement`, `search_by_regex`, `sheet_name`, `spreadsheet_id`.
- `format_cells` (action slug: `format-cells`): Apply cell formatting or number format to a range. Price: `5` credits. Parameters: `cell_format`, `number_format`, `range`, `sheet_name`, `spreadsheet_id`.
- `get_data_range` (action slug: `get-data-range`): Find the last non-empty row/column and recommended append start for a tab. Price: `5` credits. Parameters: `range`, `sheet_name`, `spreadsheet_id`.
- `get_headers` (action slug: `get-headers`): Read the header row and return header-to-column mappings plus duplicate diagnostics. Price: `5` credits. Parameters: `header_row`, `sheet_name`, `spreadsheet_id`.
- `list_sheets` (action slug: `list-sheets`): List the tabs in a spreadsheet with sheet ids and dimensions. Price: `5` credits. Parameters: `spreadsheet_id`.
- `protect_range` (action slug: `protect-range`): Protect a range, optionally warning-only or with explicit editor emails. Price: `5` credits. Parameters: `description`, `editor_emails`, `range`, `sheet_name`, `spreadsheet_id`, `warning_only`.
- `read` (action slug: `read`): Read values from a tab or A1 range. If sheet_name is omitted, resolves the real first tab. Price: `5` credits. Parameters: `range`, `sheet_id`, `sheet_name`, `spreadsheet_id`, `value_render_option`.
- `rename_sheet` (action slug: `rename-sheet`): Rename a tab by name, id, or index. Price: `5` credits. Parameters: `new_sheet_name`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `search` (action slug: `search`): Search or list recent Google Sheets spreadsheets. Price: `5` credits. Parameters: `max_results`, `query`.
- `set_data_validation` (action slug: `set-data-validation`): Set a Sheets data validation rule on a range. Price: `5` credits. Parameters: `range`, `sheet_name`, `spreadsheet_id`, `validation_rule`.
- `share` (action slug: `share`): Share a spreadsheet with a user, group, domain, or anyone. Price: `5` credits. Parameters: `domain`, `email`, `permission_type`, `role`, `spreadsheet_id`.
- `sort` (action slug: `sort`): Sort a range, preferably by header name. Price: `5` credits. Parameters: `range`, `sheet_name`, `sort_specs`, `spreadsheet_id`.
- `unprotect_range` (action slug: `unprotect-range`): Remove protection by protected range id. Price: `5` credits. Parameters: `protected_range_id`, `spreadsheet_id`.
- `update_row` (action slug: `update-row`): Update selected columns in a matched row using header names. Touches only requested cells. Price: `5` credits. Parameters: `key_column`, `key_value`, `multi`, `row_number`, `sheet_name`, `spreadsheet_id`, `updates`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-sheets-api"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-sheets-api"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-sheets-api"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-sheets-api"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-sheets-api"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-sheets-api"
  }
}
```

## Call This Tool
Product slug: `google-sheets-api`

Marketplace page: https://www.agentpmt.com/marketplace/google-sheets-api

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
    "name": "Google-Sheets",
    "arguments": {
      "action": "add_conditional_formatting",
      "range": "example range",
      "rule": {},
      "sheet_name": "example sheet name",
      "spreadsheet_id": "example spreadsheet id"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-sheets-api",
  "parameters": {
    "action": "add_conditional_formatting",
    "range": "example range",
    "rule": {},
    "sheet_name": "example sheet name",
    "spreadsheet_id": "example spreadsheet id"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `add_conditional_formatting` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-sheets-api
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
