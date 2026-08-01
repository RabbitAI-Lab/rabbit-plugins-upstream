---
name: waitlister
description: Create and run product-launch waitlists on waitlister.me — create a waitlist and publish a hosted landing page (dark/light, optional AI-generated design) in one prompt, collect signups with a referral program, read stats. Use when the user wants a waitlist, coming-soon/launch page, or pre-launch email capture.
homepage: https://waitlister.me
metadata:
  openclaw:
    requires:
      env:
        - WAITLISTER_API_KEY
---

# Waitlister — waitlists + hosted landing pages via API

Waitlister is waitlist software for product launches: hosted signup pages, a referral
program with fraud detection, email automation. Signups get a queue position and a
referral link; referrals move them up.

**Prereq (one human step, free, ~1 minute):** an **account API key** (`wl_acct_…`) from
https://waitlister.me → Settings → API keys, in the `WAITLISTER_API_KEY` env var. Account
keys work on **every plan including free** and can create waitlists — no dashboard steps
needed after that. (A per-waitlist `wl_…` key also works for an existing waitlist, but
needs the Growth plan for most endpoints — prefer the account key.)

API base `https://waitlister.me/api/v1` · auth header `X-Api-Key` (NOT `Authorization:
Bearer`) · full spec: https://waitlister.me/openapi.json · full agent guide:
https://waitlister.me/skill.md

## Golden path — live waitlist + landing page in two calls

1. Create the waitlist WITH a landing page (draft):

```bash
curl -X POST "https://waitlister.me/api/v1/waitlists" \
  -H "Content-Type: application/json" -H "X-Api-Key: $WAITLISTER_API_KEY" \
  -d '{"name":"My Product","landing_page":{"headline":"Join the beta","description":"Early access for founders.","button_text":"Join the waitlist","theme":"dark"}}'
# → 201: data.waitlist.key (use everywhere below), data.waitlist.form_action_url
```

2. Publish it:

```bash
curl -X POST "https://waitlister.me/api/v1/waitlist/WAITLIST_KEY/landing-page/publish" \
  -H "X-Api-Key: $WAITLISTER_API_KEY"
# → hosted_page_url, live at https://waitlister.me/p/{slug}
```

Pages are **drafts until you publish**. `{"unpublish": true}` in the publish body takes
the page offline again. One page per waitlist (creating a second → 409).

## Everything else

```bash
# Add a signup (works on free plan with an account key; idempotent per email)
curl -X POST ".../api/v1/waitlist/WAITLIST_KEY/sign-up" -H "X-Api-Key: $WAITLISTER_API_KEY" \
  -H "Content-Type: application/json" -d '{"email":"user@example.com"}'

# Stats for "X people waiting" widgets
curl ".../api/v1/waitlist/WAITLIST_KEY/stats" -H "X-Api-Key: $WAITLISTER_API_KEY"

# Read the page (status, copy, hosted_page_url, analytics)
curl ".../api/v1/waitlist/WAITLIST_KEY/landing-page" -H "X-Api-Key: $WAITLISTER_API_KEY"

# Update copy/theme/SEO (any subset; unknown keys → 400 that lists the allowed keys)
curl -X PATCH ".../api/v1/waitlist/WAITLIST_KEY/landing-page" -H "X-Api-Key: $WAITLISTER_API_KEY" \
  -H "Content-Type: application/json" -d '{"headline":"New headline","seo":{"title":"…"}}'

# AI-designed page (costs 1 AI credit, takes under a minute; edit later with "is_edit": true)
curl -X POST ".../api/v1/waitlist/WAITLIST_KEY/landing-page/generate" -H "X-Api-Key: $WAITLISTER_API_KEY" \
  -H "Content-Type: application/json" -d '{"prompt":"dark, bold, dev-tool aesthetic"}'
```

Node SDK (optional): `npm install waitlister` — reads `WAITLISTER_API_KEY` automatically;
`waitlister-js`/`waitlister-sdk`/`waitlister-node`/`@waitlister/sdk` are deprecated
aliases of the same package. No Python SDK — use the REST API from Python.

## Facts that prevent wrong guesses

- **AI-built pages return 409 on copy-field PATCHes** — their copy lives inside the
  generated HTML. Edit them via `…/landing-page/generate` with `"is_edit": true`
  (`theme` and `seo` PATCH fine on both page types).
- AI generation costs **1 credit per call** (shared with the dashboard AI builder; free
  plans include a few one-time credits). Out of credits → 402 with the balance. Never
  auto-retry a generate call.
- Plan gating: account keys allow create/sign-up/stats/landing-page on **every plan**
  (low rate limits: 5/min writes, 10/min sign-up/stats on free). Listing/getting/
  updating/deleting subscribers requires **Growth+** — don't retry gated endpoints
  expecting different results.
- Plan-gated page levers (custom domain, branding removal, tracking IDs) are **not in
  the API at any plan** — unknown keys 400. Don't try.
- Publish validates: headline ≥3 chars, email field + submit button present. API
  publishes skip the social-share OG image (a dashboard publish backfills it).
- No image/asset uploads via the API.
- Rate-limit headers: `X-RateLimit-Limit` / `-Remaining` / `-Reset` on every response.
- Signup email validation rejects fake/test addresses — verify with a real, deliverable
  email.

## Verify before telling the user it's done

1. GET the landing page — `status: "published"` and a `hosted_page_url`.
2. Fetch the `hosted_page_url` — the headline renders.
3. Sign up a real email → `success: true` + a queue position; then it appears via
   `stats` (`subscribers_total`).

Docs: https://waitlister.me/docs/overview (append `.md` to any /docs/ URL for raw
markdown) · Pricing: https://waitlister.me/pricing
