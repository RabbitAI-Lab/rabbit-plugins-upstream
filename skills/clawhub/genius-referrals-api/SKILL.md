---
name: "genius-referrals-api"
description: "Inspect and manage Genius Referrals accounts, advocates, campaigns, bonuses, redemption requests, and reports through the public Genius Referrals API."
metadata:
  owner: genius-referrals
  publishable: true
  source_docs: https://api.geniusreferrals.com/doc
  tags: ["API", "Referral Marketing", "Growth Ops", "Developer Tools", "Rewards", "Partner Programs"]
  topics:
    - referral marketing
    - api
    - saas
    - growth tools
    - developer tools
    - marketing automation
    - affiliate programs
    - partner programs
  use_cases:
    - Account and campaign inspection
    - Advocate lookup, creation, and updates
    - Referral link generation and tracking
    - Bonus listing, checkup, and force-issuance (with approval)
    - Redemption request review and status updates
    - Report generation with date and account filters
    - API authentication testing
  example_prompts:
    - "List my Genius Referrals accounts"
    - "Show the last 10 advocates for account {slug}"
    - "List the last 10 referrals on my account"
    - "List the last 10 rewards on my account"
    - "List the last 10 payouts on my account"
    - "Test Genius Referrals API authentication and summarize the result"
allowed-tools:
  - exec
  - web_fetch
user-invocable: true
license: MIT
---

# Genius Referrals API

Use this skill to inspect, manage, test, or report on a Genius Referrals referral program through the Genius Referrals API.

## Boundaries

- Never store API tokens in the skill.
- Use `GR_API_TOKEN` from the environment or a user-approved credential source only.
- Send the token as `X-Auth-Token`; never put it in a URL.
- Default to read-only actions until the target environment, account slug, and intended change are clear.
- Treat production writes, payouts, redemption updates, bonus force actions, and deletes as high-impact. Ask for explicit confirmation before running them.
- Prefer QA or a non-production account for tests.

## Environment

Default base URL: `https://api.geniusreferrals.com`

Optional environment variables:

- `GR_API_TOKEN`: Genius Referrals API token.
- `GR_API_BASE_URL`: API base URL override.
- `GR_ACCOUNT_SLUG`: default account slug.

## Workflow

1. Confirm the requested task category: read/report, create/update, payout/redemption, delete, or docs lookup.
2. Identify the environment and account slug. Use `GR_API_BASE_URL` and `GR_ACCOUNT_SLUG` when available.
3. Verify authentication with `GET /test-authentication` before making account-scoped changes.
4. For read-only tasks, call the narrowest endpoint and summarize relevant fields only.
5. For write tasks, prepare a dry-run summary first: method, path, account slug, payload keys, expected impact, rollback or cleanup option.
6. For high-impact tasks, get explicit approval before execution.
7. After execution, report status code, endpoint, resource identifiers, and any next action.

## Common Tasks

- List accounts: `GET /accounts`
- Inspect account: `GET /accounts/{account_slug}`
- List advocates: `GET /accounts/{account_slug}/advocates`
- Create advocate or referral candidate: `POST /accounts/{account_slug}/advocates`
- Update advocate: `PATCH /accounts/{account_slug}/advocates/{advocate_token}`
- Link referral: `POST /accounts/{account_slug}/advocates/{advocate_token}/referrals`
- Get share links: `GET /accounts/{account_slug}/advocates/{advocate_token}/share-links`
- List bonuses: `GET /accounts/{account_slug}/bonuses`
- Bonus checkup: `GET /accounts/{account_slug}/bonuses/checkup`
- Force bonus: `POST /accounts/{account_slug}/bonuses/force` after explicit approval only.
- List redemption requests: `GET /accounts/{account_slug}/redemption-requests`
- Update redemption request: `PATCH /accounts/{account_slug}/redemption-requests/{redemption_request_id}` after explicit approval.
- Run reports: use `/reports/*` endpoints with the required date/account filters from the docs.

## Local Helper

Use `scripts/gr_api.py` when available. It uses only Python stdlib and should be run with `python3`.

Examples:

```bash
GR_API_TOKEN=... python3 scripts/gr_api.py GET /test-authentication
GR_API_TOKEN=... GR_ACCOUNT_SLUG=my-account python3 scripts/gr_api.py GET '/accounts/{account_slug}/advocates' --query limit=10
GR_API_TOKEN=... python3 scripts/gr_api.py PATCH '/accounts/{account_slug}/advocates/{advocate_token}' --account my-account --path-param advocate_token=abc123 --json '{"status":"active"}'
```

## Filter Notes

The docs use `filter` with `|` between clauses and `::` between field and value.

Example:

```text
filter=name::Jane|status::active
```

For advocates, documented filter fields include `fullname`, `name`, `lastname`, `email`, `advocate_token`, `advocate_code`, `bonus_exchange_method_slug`, `campaign_slug`, `can_refer`, `is_referral`, `from`, `to`, `created`, `status`, `status_date_from`, `status_date_to`, `is_email_confirmed`, `campaign_contract_slug`, `advocate_referrer_token`, and `fraudulent`.

## Verification

Before considering a task complete:

- Authentication was checked for API operations.
- Target base URL and account slug were stated.
- Mutating calls include method/path/payload summary.
- High-impact calls include explicit approval evidence.
- Returned status and resource identifiers were reported.
