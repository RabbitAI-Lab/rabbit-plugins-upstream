---
name: google-contacts
description: "Google Contacts connector to list, search, create, update, and delete a user's contacts Use when an agent needs google contacts, search contacts by name or email or phone, list recent contacts for conversation context, create new contacts from agent interactions, update contact phone numbers and emails, create contact, contact, delete contact through AgentPMT-hosted remote tool calls. Discovery terms: google contacts, search contacts by name or email or phone."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-contacts
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-contacts"}}
---
# Google Contacts

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Connect your AI agent to Google Contacts for complete contact management capabilities. Search contacts by name, email, or phone number to quickly find the people you need, list recent contacts for context during conversations, and create new contacts directly from agent interactions. Update existing contact information including phone numbers, emails, addresses, company details, and notes. This tool is perfect for agents that support customer outreach, sales engagement, scheduling coordination, and customer service workflows. Keep your contact database synchronized with your CRM, auto-fill customer details during support interactions, build outreach lists from existing contacts, and maintain a clean, organized address book. All operations use the Google People API with your connected Google account credentials.

## Product Instructions
### Google Contacts

#### Overview
Manage your Google Contacts: list, search, create, update, and delete contacts. Supports both simple flat-field input and canonical Google People API format for maximum flexibility.

#### Actions

##### list_contacts
List all contacts sorted by first name ascending.

**Required fields:** none (just the action)

**Optional fields:**
- `page_size` (integer, 1-200, default 25) - number of contacts per page
- `page_token` (string) - pagination token from a previous response

**Example:**
```json
{
  "action": "list_contacts",
  "page_size": 50
}
```

**Response includes:** array of contacts (each with resource_name, etag, name, first_name, last_name, emails, phones, company, job_title, notes, addresses) and `next_page_token` if more results exist.

---

##### search_contacts
Search contacts by name, email, phone, or other text.

**Required fields:**
- `query` (string) - search text to match against contact fields

**Optional fields:**
- `page_size` (integer, 1-200, default 25)
- `page_token` (string)

**Example:**
```json
{
  "action": "search_contacts",
  "query": "Jane Smith",
  "page_size": 10
}
```

---

##### get_contact
Retrieve a single contact by resource name.

**Required fields:**
- `resource_name` (string) - contact identifier, e.g. `"people/c1234567890"`

**Example:**
```json
{
  "action": "get_contact",
  "resource_name": "people/c1234567890"
}
```

**Note:** You can pass the ID with or without the `people/` prefix; it will be normalized automatically.

---

##### create_contact
Create a new contact. At least one field must be provided in the `contact` object.

**Required fields:**
- `contact` (object) - contact data with at least one field

**Contact object fields (all optional, but at least one required):**
- `first_name` (string) - given name
- `last_name` (string) - family name
- `full_name` (string) - display name (used to derive first/last if those are not provided; splits on spaces)
- `email` (string) - primary email address
- `phone` (string) - primary phone number
- `company` (string) - organization name
- `job_title` (string) - job title
- `notes` (string) - free-text notes
- `address` (object) - with fields: `street_address`, `city`, `region`, `postal_code`, `country`

**Example:**
```json
{
  "action": "create_contact",
  "contact": {
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone": "+1-555-867-5309",
    "company": "Acme Corp",
    "job_title": "VP of Engineering",
    "notes": "Met at the 2026 tech conference",
    "address": {
      "street_address": "123 Main St",
      "city": "San Francisco",
      "region": "CA",
      "postal_code": "94105",
      "country": "US"
    }
  }
}
```

**Alternative input formats:** The contact object also accepts canonical Google People API format (e.g. `names`, `emailAddresses`, `phoneNumbers` arrays) and plural aliases (`emails`, `phones` arrays). The first element of each array is used.

---

##### update_contact
Update an existing contact. Only the fields you include in the `contact` object will be modified; other fields remain unchanged.

**Required fields:**
- `resource_name` (string) - the contact to update, e.g. `"people/c1234567890"`
- `contact` (object) - fields to update (same structure as create_contact)

**Optional fields:**
- `etag` (string) - ETag for optimistic concurrency. If omitted, the tool fetches the current ETag automatically.

**Example:**
```json
{
  "action": "update_contact",
  "resource_name": "people/c1234567890",
  "contact": {
    "job_title": "CTO",
    "company": "New Ventures Inc"
  }
}
```

**Note:** The update mask is automatically derived from the fields you provide. For example, providing `email` updates only the emailAddresses field on the contact.

---

##### delete_contact
Permanently delete a contact.

**Required fields:**
- `resource_name` (string) - the contact to delete, e.g. `"people/c1234567890"`

**Example:**
```json
{
  "action": "delete_contact",
  "resource_name": "people/c1234567890"
}
```

**Warning:** This action is irreversible. The contact is permanently removed.

---

#### Common Workflows

##### 1. Find and Update a Contact
Search for a contact, then update their information:
1. `search_contacts` with `query: "Jane Smith"` to find the contact
2. Note the `resource_name` from the result (e.g. `"people/c1234567890"`)
3. `update_contact` with that `resource_name` and the fields to change

##### 2. Export a Contact List
Retrieve all contacts with pagination:
1. `list_contacts` with `page_size: 200` (maximum per page)
2. If `next_page_token` is returned, call `list_contacts` again with that `page_token`
3. Repeat until no `next_page_token` is returned

##### 3. Add a New Contact and Verify
Create a contact and confirm it was saved:
1. `create_contact` with the contact details
2. Note the `resource_name` from the response
3. `get_contact` with that `resource_name` to verify all fields were saved correctly

#### Important Notes
- **Pagination:** Maximum `page_size` is 200. Default is 25. Use `next_page_token` to retrieve additional pages.
- **Resource names:** Contact identifiers look like `"people/c1234567890"`. You can pass just the ID portion (e.g. `"c1234567890"`) and it will be normalized.
- **Name derivation:** If you provide `full_name` without `first_name`/`last_name`, the tool splits on spaces: first word becomes given name, remaining words become family name.
- **Update behavior:** Only fields included in the `contact` object are updated. Omitted fields are not cleared.
- **ETag handling:** For updates, the ETag is fetched automatically if not provided. You can pass the `etag` from a previous get/list response for optimistic concurrency control.
- **Single values only:** The flat input format (`email`, `phone`) stores one value per field. If you need multiple emails or phones, use the People API array format (`emailAddresses`, `phoneNumbers`), though only the first entry in each array is used.
- **Sorting:** `list_contacts` always returns results sorted by first name ascending.
- **Delete is permanent:** There is no undo for `delete_contact`.

## When To Use
- Use this skill for `Google Contacts` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google contacts, search contacts by name or email or phone, list recent contacts for conversation context, create new contacts from agent interactions, update contact phone numbers and emails, create contact, contact, delete contact.
- Supported action names: `create_contact`, `delete_contact`, `get_contact`, `list_contacts`, `search_contacts`, `update_contact`.

## Use Cases
- Search contacts by name or email or phone
- List recent contacts for conversation context
- Create new contacts from agent interactions
- Update contact phone numbers and emails
- Add notes and organization details to contacts
- Look up contacts by resource name
- Sync contacts with external CRM systems
- Auto-fill customer details during support
- Build outreach lists from existing contacts
- Maintain an organized address book

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `6`.
x402 availability: not enabled for this product.

- `create_contact` (action slug: `create-contact`): Create a new contact. At least one field must be provided in the contact object. Price: `5` credits. Parameters: `contact`.
- `delete_contact` (action slug: `delete-contact`): Permanently delete a contact. This action is irreversible. Price: `5` credits. Parameters: `resource_name`.
- `get_contact` (action slug: `get-contact`): Retrieve a single contact by resource name. Price: `5` credits. Parameters: `resource_name`.
- `list_contacts` (action slug: `list-contacts`): List all contacts sorted by first name ascending. Price: `5` credits. Parameters: `page_size`, `page_token`.
- `search_contacts` (action slug: `search-contacts`): Search contacts by name, email, phone, or other text. Price: `5` credits. Parameters: `page_size`, `page_token`, `query`.
- `update_contact` (action slug: `update-contact`): Update an existing contact. Only the fields included in the contact object are modified; other fields remain unchanged. Price: `5` credits. Parameters: `contact`, `etag`, `resource_name`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-contacts"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-contacts"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-contacts"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-contacts"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-contacts"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-contacts"
  }
}
```

## Call This Tool
Product slug: `google-contacts`

Marketplace page: https://www.agentpmt.com/marketplace/google-contacts

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
    "name": "Google-Contacts",
    "arguments": {
      "action": "create_contact",
      "contact": {
        "address": {
          "city": "example city",
          "country": "example country",
          "postal_code": "example postal code",
          "region": "example region",
          "street_address": "example street address"
        },
        "company": "example company",
        "email": "user@example.com",
        "first_name": "example first name",
        "full_name": "example full name",
        "job_title": "example job title",
        "last_name": "example last name",
        "notes": "example notes"
      }
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-contacts",
  "parameters": {
    "action": "create_contact",
    "contact": {
      "address": {
        "city": "example city",
        "country": "example country",
        "postal_code": "example postal code",
        "region": "example region",
        "street_address": "example street address"
      },
      "company": "example company",
      "email": "user@example.com",
      "first_name": "example first name",
      "full_name": "example full name",
      "job_title": "example job title",
      "last_name": "example last name",
      "notes": "example notes"
    }
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `create_contact` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-contacts
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
