# Coil API Endpoints

Base URL comes from the selected CLI profile or `COIL_BASE_URL`.

All authenticated requests use:

```http
Authorization: Bearer <session-token-or-ak-key>
Content-Type: application/json
```

Coil organization API keys (`ak_...`) are accepted by agent-compatible routes.

## Auth and Context

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/api/auth/status` | Returns authenticated actor, org, role, token type, and auth mode. |
| GET | `/api/auth/api-keys` | Lists Coil organization API keys for human org admins. |
| DELETE | `/api/auth/api-keys/{id}` | Revokes a Coil organization API key for human org admins. |
| POST | `/api/auth/verify-key` | Verifies a Coil organization API key without exposing it. |

CLI discovery wrapper:

```bash
coil agent-context --json
```

## Activation, Marketplace, and Recipes

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/activation` | `coil activation status --json` |
| GET | `/api/marketplace/templates` | `coil marketplace templates --json` |
| POST | `/api/marketplace/templates/{id}/install` | `coil marketplace install <template-id> --json` |
| GET | `/api/recipes` | `coil recipes list --json` |
| GET | `/api/recipes/{id}` | `coil recipes view <recipe-id> --json` |
| POST | `/api/recipes/{id}/validate` | `coil recipes validate <recipe-id> --json` |
| POST | `/api/recipes/{id}/publish` | `coil recipes publish <recipe-id> --json` |
| POST | `/api/recipes/{id}/run` | `coil recipes run <recipe-id> --confirm-provider-spend ... --json` |
| GET | `/api/recipe-runs/{id}` | `coil recipe-runs view <run-id> --json` |
| POST | `/api/recipe-runs/{id}/cancel` | `coil recipe-runs cancel <run-id> --json` |
| POST | `/api/recipe-runs/{id}/retry` | `coil recipe-runs retry <run-id> --json` |

Provider-backed admission requires explicit spend confirmation. A `202` queued response is durable admission, not terminal success. Recipe publication and ambiguous-effect reconciliation require a human organization admin.

## Scrapes

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/scrapes?limit=100` | `coil scrapes list --json` |
| POST | `/api/scrapes` | `coil scrapes create ... --json` |
| GET | `/api/scrapes/{id}` | `coil scrapes get <id> --json` |
| PATCH | `/api/scrapes/{id}` | `coil scrapes rename <id> --name ...` |
| DELETE | `/api/scrapes/{id}` | `coil scrapes delete <id> --force` |
| POST | `/api/scrapes/{id}/recount` | `coil scrapes recount <id> --json` |
| GET | `/api/scrapes/{id}/leads` | `coil leads list <scrape-id> --json` |
| GET | `/api/leads` | `coil leads list --json` |

Machine callers can create scrapes. Admin-gated destructive routes require a human org admin session.

## Leads

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/scrapes/{scrapeId}/leads?limit=50&offset=0` | `coil leads list <scrape-id> --json` |
| GET | `/api/leads?limit=50&offset=0` | `coil leads list --json` |
| GET | `/api/leads/{id}` | `coil leads get <id> --json` |
| PATCH | `/api/leads/{id}` | `coil leads update <id> --fields '{...}' --json` |
| DELETE | `/api/leads/{id}` | `coil leads delete <id> --force --json` |
| PATCH | `/api/leads/bulk` | `coil leads bulk-update --ids ... --fields '{...}' --json` |
| POST | `/api/export/csv` | `coil leads export <scrape-id> [--filter/--view/--ids] [--output]` |
| GET | `/api/leads/emails?scrapeId={id}` | `coil leads emails <scrape-id>` |

## Automations

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/automations?status=published` | `coil automations list --json` |
| POST | `/api/automations` | `coil automations create ... --json` |
| GET | `/api/automations/{id}` | `coil automations view <id> --json` |
| PATCH | `/api/automations/{id}` | `coil automations update <id> ... --json` |
| DELETE | `/api/automations/{id}` | `coil automations delete <id> --force --json` |
| POST | `/api/automations/{id}/validate` | `coil automations validate <id> --json` |
| POST | `/api/automations/{id}/publish` | `coil automations publish <id> --json` |
| POST | `/api/automations/{id}/run` | `coil automations run <id> --scrape <scrape-id> --json` |
| GET | `/api/automations/{id}/results` | `coil automations results list --automation <id> --json` |
| GET | `/api/automations/results` | `coil automations results list --json` |
| GET | `/api/automations/results/{resultId}` | `coil automations results view <result-id> --json` |
| GET | `/api/automations/results/{resultId}/links` | `coil automations results links list <result-id> --json` |
| POST | `/api/automations/results/{resultId}/links` | `coil automations results links add <result-id> --kind webhook_evidence --url https://... --json` |
| DELETE | `/api/automations/results/{resultId}/links/{linkId}` | `coil automations results links delete <result-id> <link-id> --json` |
| GET | `/api/automations/policy` | `coil automations policy get --json` |
| PUT | `/api/automations/policy` | `coil automations policy set --domains ... --fields ... --json` |

API-key callers create draft automations. Publishing, deletion, and policy changes require a human org admin session. Automation result links are deliberately narrow traceability records for delivery evidence; they are not a generic metadata surface.

## Settings, Preferences, Members

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/settings` | `coil settings get --json` |
| PATCH | `/api/settings` | `coil settings set <key> <value> --json` |
| GET | `/api/preferences/columns?scrapeId={id}` | `coil preferences get --scrape <id> --json` |
| PUT | `/api/preferences/columns` | `coil preferences set --scrape <id> ... --json` |
| GET | `/api/members` | `coil members list --json` |

## Integrations and SmartLead

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/integrations` | `coil integrations list --json` |
| GET | `/api/integrations/{provider}` | `coil integrations status <provider> --json` |
| PUT | `/api/integrations/{provider}` | `printf '%s' "$PROVIDER_API_KEY" \| coil integrations set <provider> --json` |
| DELETE | `/api/integrations/{provider}` | `coil integrations disconnect <provider> --json` |
| POST | `/api/integrations/{provider}/test` | `coil integrations test <provider> --json` |
| POST | `/api/integrations/rotate` | `coil integrations rotate [--apply] --json` |
| GET | `/api/integrations/smartlead/campaigns` | `coil smartlead campaigns --json` |
| GET | `/api/integrations/smartlead/campaigns/sequences?campaignId={id}` | `coil smartlead sequences --campaign <id> --json` |
| POST | `/api/integrations/smartlead/send` | `coil smartlead send <scrape-id> --campaign <id> --json` |

## Feedback

| Method | Path | CLI |
| --- | --- | --- |
| POST | `/api/feedback` | `coil feedback "..." --json` |

The CLI also supports local feedback drafts and resend commands for retryable failures.

## Activity and Usage

| Method | Path | CLI |
| --- | --- | --- |
| GET | `/api/activity` | `coil activity list --json` |
| GET | `/api/usage?view=summary` | `coil usage summary --json` |
| GET | `/api/usage?view=events` | `coil usage events --json` |
| GET | `/api/usage?view=limits` | `coil usage limits --json` |

Activity cursors are opaque. Usage endpoints require an organization admin, so machine API keys are intentionally rejected by the shared role gate.
