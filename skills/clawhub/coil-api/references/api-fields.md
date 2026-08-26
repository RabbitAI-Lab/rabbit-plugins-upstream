# Coil API Fields

Responses use snake_case. Request bodies generally accept the field names shown by the CLI and API route schemas.

## Auth Context

`GET /api/auth/status` returns:

| Field | Type | Notes |
| --- | --- | --- |
| `authenticated` | boolean | Whether the bearer token is valid. |
| `userId` | string/null | Human Clerk user ID when present. |
| `orgId` | string/null | Clerk organization ID. |
| `orgRole` | `org:admin`/`org:member`/null | Role for human sessions; API keys map to member behavior. |
| `tokenType` | string/null | Usually `session_token` or `api_key`. |
| `actor` | object | `{ type, id, name }` where type is `human` or `machine`. |

## CLI Output Envelope

Use `--json --output-version 2` on list commands when possible:

```json
{
  "resource": "scrapes",
  "items": [],
  "total": 0,
  "limit": 25,
  "offset": 0,
  "nextOffset": null,
  "truncated": false,
  "hint": null
}
```

## Scrape

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | UUID. |
| `org_id` | string | Tenant isolation key. |
| `name` | string | Human-visible scrape name. |
| `status` | string | `pending`, `running`, `completed`, `failed`, or legacy/null values. |
| `job_titles` | string[] | Prospect scrape filter. |
| `locations` | string[] | Prospect scrape filter. |
| `company_sizes` | string[] | Prospect scrape filter. |
| `industries_include` | string[]/null | Prospect filter. |
| `industries_exclude` | string[]/null | Prospect filter. |
| `search_url` | string/null | Sales Navigator source URL in create payloads. |
| `fetch_count` | number | Requested prospect count. |
| `prospect_count` | number | Current stored lead count. |
| `smartlead_campaign_id` | string/null | Optional auto-send campaign. |
| `created_by_user_id` | string/null | Human creator when known. |
| `created_at` | ISO string | Creation timestamp. |

Create payloads:

```json
{
  "type": "prospect",
  "name": "Q2 prospects",
  "job_titles": ["VP Sales"],
  "locations": ["United States"],
  "company_sizes": ["11-50"],
  "fetch_count": 100,
  "confirm_provider_spend": true
}
```

```json
{
  "type": "sales-nav",
  "name": "Sales Nav export",
  "search_url": "https://www.linkedin.com/sales/search/people?...",
  "user_agent": "Mozilla/5.0 ...",
  "linkedin_cookie": "li_at=...",
  "confirm_provider_spend": true
}
```

`confirm_provider_spend` is required for provider-backed acquisition. Sales Navigator credentials are resolved server-side for execution and must not be stored in recipe inputs or copied into logs.

## Lead

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | UUID. |
| `org_id` | string | Tenant isolation key. |
| `scrape_id` | string | Parent scrape. |
| `full_name` | string/null | Lead name. |
| `first_name` | string/null | First name. |
| `last_name` | string/null | Last name. |
| `email` | string/null | Email when known. |
| `linkedin` | string/null | LinkedIn profile URL. |
| `job_title` | string/null | Role/title. |
| `company_name` | string/null | Company. |
| `company_domain` | string/null | Company domain. |
| `location` | string/null | Lead location. |
| `is_bad_fit` | boolean/null | Qualification marker. |
| `added_to_smartlead` | boolean/null | SmartLead send marker. |
| `smartlead_campaign` | string/null | Campaign name. |
| `date_scraped` | string/null | Scrape date. |

Filter conditions use:

```json
{
  "column": "email",
  "operator": "is_not_empty",
  "value": ""
}
```

Supported operators include equality, contains, empty/not-empty, booleans, and date comparisons. Use `coil agent-context --json` for the current command manifest.

## Automation

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | UUID. |
| `org_id` | string | Tenant isolation key. |
| `name` | string | Automation name. |
| `webhook_url` | string | HTTPS webhook URL. |
| `input_fields` | string[] | Lead fields sent to the webhook. |
| `scope` | `global`/`scrape` | Whether automation applies globally or to one scrape. |
| `scrape_id` | string/null | Required for scrape-scoped automation. |
| `status` | `draft`/`published`/`disabled` | API-key agents create drafts. |
| `created_by_actor_type` | `human`/`machine` | Actor attribution. |
| `created_by_actor_id` | string | User ID or API key ID. |
| `created_by_actor_name` | string/null | API key display name when available. |
| `published_by_user_id` | string/null | Human admin publisher. |
| `published_at` | ISO string/null | Publication timestamp. |

Create payload:

```json
{
  "name": "Enrich leads",
  "webhook_url": "https://hooks.example.com/enrich",
  "input_fields": ["email", "company_name"],
  "scope": "global",
  "scrape_id": null
}
```

## Automation Result

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | UUID. |
| `automation_id` | string | Parent automation. |
| `lead_id` | string | Processed lead. |
| `status` | `pending`/`running`/`success`/`error` | Delivery state. |
| `result` | string/null | Webhook response or summary. |
| `error_message` | string/null | Failure detail. |
| `created_at` | ISO string | Creation timestamp. |
| `updated_at` | ISO string | Last status update. |

## Automation Result Link

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | UUID. |
| `automation_result_id` | string | Parent automation result. |
| `kind` | `webhook_evidence`/`smartlead_campaign`/`delivery_evidence` | Accepted evidence class. |
| `label` | string/null | Short label or delivery ID, max 120 characters. |
| `url` | string | HTTPS URL, max 2048 characters. `smartlead_campaign` URLs must use a `smartlead.ai` host. |
| `created_at` | ISO string | Creation timestamp. |

Create payload:

```json
{
  "kind": "webhook_evidence",
  "label": "n8n execution",
  "url": "https://logs.example.com/run/1"
}
```

## Automation Policy

| Field | Type | Notes |
| --- | --- | --- |
| `domains` | string[] | Exact or wildcard allowed webhook hosts. |
| `fields` | string[] | Allowed lead fields for automation payloads. |

Only human org admins can update policy.

## Settings

Settings are stored in org-scoped JSON. Common keys:

| Key | Type | Notes |
| --- | --- | --- |
| `has_smartlead_key` | boolean | Read-only redacted presence marker. |
| `smartlead_api_key` | string | Legacy setting. New writes are rejected; configure SmartLead with `printf '%s' "$SMARTLEAD_API_KEY" \| coil integrations set smartlead` or `PUT /api/integrations/smartlead`. |
| `default_columns` | string[] | Optional lead table defaults. |

## Agent Caveats

- API-key agents currently behave as org members, not org admins.
- Admin-gated actions include destructive scrape/automation operations, automation policy management, and automation publishing.
- Prefer `coil feedback` for platform friction discovered while operating Coil.
