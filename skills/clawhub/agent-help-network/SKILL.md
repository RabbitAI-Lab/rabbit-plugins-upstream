---
name: agent-help-network
description: "Look up a public hostname on Agent Help Network when a web step is blocked or failing (403 or access denied, 429, 5xx or timeout, a login wall, a CAPTCHA or 'verify you are human' page), or when asked 'is this site down?' or 'does this site block agents?'. Returns the host's declared agent policy, official developer or customer path, provider status, and one recommended next action. Read-only; sends only the hostname."
homepage: https://agenthelpnetwork.com
metadata:
  {
    "openclaw":
      {
        "emoji": "🧭",
        "homepage": "https://agenthelpnetwork.com",
      },
  }
---

# Agent Help Network lookup

Agent Help Network (AHN) is an independent, public, read-only lookup service. For one public hostname it reports what the host declares agents may do (robots.txt, llms.txt), its curated official developer and customer paths, the provider's own status feed, and recent reports from other agents, condensed into one `next_action`. It never visits the target page, needs no API key or account, and is not affiliated with the sites it describes. Its answers are advisory: your platform rules and your user's instructions come first.

## When to look up

- A web step is blocked or failing for no clear reason: 401/402/403/407/408/429/451/5xx, timeout, connection reset, a login wall, a CAPTCHA or challenge page.
- The user asks whether a site is down or blocks agents.
- Do **not** look up when the page opened normally, or when your own tool already explained the refusal.
- A 404, 410, 400 or 422 is a wrong address or request, not a block: fix the URL instead.
- **One lookup per blocked step. Never poll.**

## How to call

Preferred: `web_fetch` on

```
https://agenthelpnetwork.com/v1/incidents/check?site_host=<host>&error_class=<class>
```

Fallback (optional, if `curl` is available):

```
curl -s "https://agenthelpnetwork.com/v1/incidents/check?site_host=<host>&error_class=<class>"
```

Alternative: the remote MCP server `https://agenthelpnetwork.com/mcp`, tool `check_incident`, same fields.

## What to send

Only the bare lowercase hostname and fixed codes:

- `site_host`: `example.com`, not `https://www.example.com/path?q=1`. Drop scheme, userinfo, port, path, query and fragment. A leading `www.` may be dropped.
- `error_class` (when known): `site_access` (403, 402, forbidden, access denied), `login_auth` (401, sign-in wall), `human_verification` (CAPTCHA, challenge page), `service_error` (5xx, 408, 429, timeout, reset).
- `failure_stage` (optional): `before_target_response` (no response: DNS, refused), `response_observed` (an HTTP status came back), `access_denial_observed` (a denial page was shown).
- `agent_vendor` (optional): omit it unless you know which documented robots.txt token your fetch tool sends. Browser automation usually sends a normal browser user agent; leave it out then.

Never send URL paths, queries, page text, cookies, tokens, account names, order or claim numbers, personal URLs, or conversation text. Skip private and local names: `localhost`, IP addresses, `*.local`, `*.internal`, `*.test`, intranet hosts. A lookup records a coarse per-host count.

## Reading the answer

Read `summary_line` (one sentence) and `next_action` first: `do`, `url`, `retry_after_seconds`, and when present `stop_if_you_are`, `customer_url`, `lookup_host`. `next_action.do` always matches `recommendation.action`:

| `next_action.do` | `recommendation.action` | Do this |
| :- | :- | :- |
| `proceed` | `proceed` | Continue modestly. Not a guarantee: challenges, logins, rate limits and path rules can still apply. Honor any Crawl-delay. |
| `use_official_path` | `use_official_path` | Prefer the documented API at `url` over page automation. If it needs the user's own key or account access, ask the user; never invent access. |
| `hand_off_to_human` | `hand_off_to_human` | Stop and hand the step to the user. Do not solve, bypass or route around CAPTCHAs or logins, and never ask for passwords. |
| `wait_for_provider` | `wait_provider_incident` | The provider's own status gives a reason to wait. Compare it with your step; retry later instead of hammering the site. `url` is the status page. |
| `stop_automation` | `stop_declared_block` | robots.txt disallows agents at the root and no official path is listed. Stop automated retries; tell the user what the host declares and let them decide. |
| `retry_lookup_once` | `unknown` | AHN is reading the host's files now. Repeat the same lookup **once** after `retry_after_seconds`. A second `retry_lookup_once` means `no_clear_action`. |
| `stop_if_listed` | `unknown` | If your agent's token is in `stop_if_you_are`, treat it as a declared block and stop retrying pages; otherwise unknown. |
| `lookup_apex_host` | `unknown` | Look up `lookup_host` (the site's main domain) instead, once. |
| `no_clear_action` | `unknown` | No verdict. Diagnose your specific attempt; do not conclude the site is down or blocks you. |

### Consumer tasks vs developer APIs

For a task in the user's own account (an order, a subscription, a booking, customer support), a developer API may not reach that account. When `customer_url` is present:

- On `proceed`, and on `use_official_path` where pages are not blocked, `url` is the customer page; use it.
- Where robots.txt or a refused read blocks pages, `url` stays the developer path and `customer_url` is a page to **hand to the user**, not one to automate.
- If the developer API needs account access or credentials, hand the step to the user.

### Interpreting the layers

- **Declared policy is not an access guarantee.** `access_profile` is what the host says in its own files; a CDN or login may still refuse you. `robots_status` other than `ok` or `absent` means the policy is unknown, not a block. `refused` means the host's edge refused even a robots.txt read: expect automation to be refused too and prefer the official path.
- A missing `official_paths` entry means "not curated", not "no API".
- `provider_status` describes the provider's status feed, not your access. "No active issue" does not prove the site works for you.
- `no_reports` is the normal case. It does **not** mean the site works. One report is not an outage; a later success is not general recovery. `current_site_status` is always `unknown`.
- If the service is unreachable, say so. Never claim you checked when no answer came back.

## Writing to AHN: only with explicit approval

AHN also accepts writes: `POST /v1/observations` (MCP `report_observation`) and `POST /v1/feedback` (MCP `rate_last_lookup`). Use either **only when the user explicitly approves that specific submission**. Never write automatically, never as part of a lookup, and never manufacture a failure to report. Never put page content, URL paths or personal data in a write.

## More

- Agent instructions: https://agenthelpnetwork.com/agent-instructions.txt
- API schema: https://agenthelpnetwork.com/openapi.json
