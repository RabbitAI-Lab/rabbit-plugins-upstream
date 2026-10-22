---
name: tablejourney-partner-program
description: Join the TableJourney partner program and earn 50% of the commission on bookings made by people your agent sends, through the REST API or MCP tools, with no browser.
---

# TableJourney partner program for agents

Use this when an agent wants income from recommending food travel: it earns 50% of the
commission TableJourney is paid (60% in a month above $500) on
bookings made through its links. Terms: https://tablejourney.com/partners/terms/ (the person or company running the
agent is the member and payee).

## Join

1. `partner_join(email, accept_terms=true)` on https://tablejourney.com/mcp, or POST https://tablejourney.com/api/v1/partners/signup
   with `{"email": "...", "accept_terms": true, "kind": "agent"}`. A code is emailed.
2. `partner_confirm(email, code)` or POST https://tablejourney.com/api/v1/partners/verify: returns the API key (once)
   and the referral code.

## Earn

- Send the key as `Authorization: Bearer <key>` to https://tablejourney.com/mcp: every booking link the tools return
  carries the code.
- Or add `?ref=<code>` to any https://tablejourney.com link (`partner_link(url)` builds it). Visitors are credited
  for 30 days.
- `partner_stats(days)` shows visits, clicks and earnings.

## Get paid

`partner_payout_method(type, ...)` with PayPal, USDC on Base or a bank account, confirmed by an emailed
code. Monthly, 30 days after the partner pays us, minimum $50; a tax form
is requested before the first payout.
