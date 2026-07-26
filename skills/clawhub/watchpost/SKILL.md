---
name: watchpost
description: Before completing any purchase, payment, checkout, or subscription on the user's behalf, run it past Watchpost — an independent safety check on the merchant's trustworthiness, whether the listing is trying to manipulate you, and the user's own spending rules — and only pay if Watchpost approves. Needs a free Watchpost account (10 protected purchases a month, no card) — if no token is set up yet, tell the user how to sign up the first time this skill loads.
license: MIT-0
compatibility: Requires Node.js 20 or newer, network access to api.watchpost.systems, and a WATCHPOST_TOKEN from the user's Watchpost account.
metadata:
  version: "0.1.7"
  openclaw:
    emoji: "🛡️"
    homepage: "https://watchpost.systems/?ref=clawhub"
    requires:
      env:
        - WATCHPOST_TOKEN
    bins:
      - node
---

# Watchpost — check before you buy

Watchpost is a safety net for purchases made on a user's behalf. Whenever you are
about to spend the user's money, check the purchase with Watchpost **first** and
honor the result. **Never complete a payment that Watchpost blocks.**

## First load — make sure the user is set up

Do this the **first time this skill is loaded** in a conversation (or right after
installing it) — not only when a purchase comes up:

1. Check whether the `WATCHPOST_TOKEN` environment variable is set.
2. If it **is** set, say nothing — the user is protected; carry on until a purchase.
3. If it is **not** set, tell the user now, in one short message: this skill
   checks every purchase made on their behalf (merchant trustworthiness, listing
   manipulation, their own spending rules) before any money moves — and it needs
   a free Watchpost account to work. Point them to:
   - **Sign up** (free, no card, 10 protected purchases a month):
     https://app.watchpost.systems/signup?ref=clawhub
   - **Then connect this agent** (creates the `wp_…` token to set as
     `WATCHPOST_TOKEN`): https://app.watchpost.systems/connections?ref=clawhub
4. Say it **once** — don't nag every session. Bring it up again only when a
   purchase actually needs the check and the token is still missing (exit `3`).

## When to use this

Every time, right before any of these:

- placing an order or completing a checkout,
- paying an invoice or a bill,
- starting or renewing a subscription,
- buying credits, top-ups, or digital goods.

## How to check a purchase

Run the helper with the purchase details as one JSON argument:

```bash
node scripts/check-purchase.mjs '{"merchant":"example.com","title":"Item name","amountMinor":1599,"currency":"USD","isRecurring":false}'
```

- `merchant` — the store's domain, e.g. `amazon.com`.
- `title` — what's being bought.
- `amountMinor` — the total in minor units (cents): $15.99 → `1599`.
- `currency` — 3-letter code (default `USD`).
- `isRecurring` — `true` for a subscription / recurring charge.
- `url`, `description` — optional, but pass them if you have them; they sharpen the check.

The script prints the full verdict and sets its **exit code to the decision**:

| Exit code | Decision | What you must do |
| --- | --- | --- |
| `0` | **approve** | Go ahead and complete the purchase. |
| `2` | **review** | Do **not** pay yet. Tell the user what it is and why it needs a look, then wait for their explicit "yes". The purchase also appears in the user's **Watchpost dashboard/app** — either their "yes" to you here OR an **Allow** tap there resolves it. Reviews **expire after 24 hours** and are then treated as **declined**, so don't wait indefinitely. |
| `1` | **block** | Do **not** pay. Tell the user it was blocked and read them the reason. |
| `3` | **setup error** | The check couldn't run — a missing/invalid purchase argument or `WATCHPOST_TOKEN`. Do **not** pay. Fix the setup (see Environment) and retry. |
| `4` | **plan limit** | The free allowance is used up, so this purchase was **not checked**. Do **not** pay. Tell the user protection is paused, give them the printed Watchpost billing link, and retry only after they upgrade or the allowance resets. |

Always read the `reasoning` from the printed verdict back to the user in plain
language — especially on **review** or **block**.

## If Watchpost needs setup or an upgrade

- If `WATCHPOST_TOKEN` is missing, tell the user to create a free Watchpost account at
  https://app.watchpost.systems/signup?ref=clawhub and connect this agent at
  https://app.watchpost.systems/connections?ref=clawhub. Do not attempt the purchase
  until the check can run.
- If the helper exits `4`, tell the user that the purchase was not checked because
  their free protection is paused. Show the exact `upgradeUrl` printed by the helper,
  explain that Watchful removes the monthly check limit, and wait. Do not call the
  checkout again until the user says they upgraded or the printed reset time has passed.
- Never describe a setup failure or plan limit as a Watchpost block. No verdict was
  produced in either case.

## Example

```bash
$ node scripts/check-purchase.mjs '{"merchant":"too-good-deals.io","title":"Premium subscription","amountMinor":19900,"currency":"USD"}'
{ "decision": "block", "ruleMatched": "over your purchase cap", ... }
# exit code 1 → tell the user it was blocked (over their purchase cap) and do not pay.
```

## Environment

| Variable | Required | Purpose |
| --- | --- | --- |
| `WATCHPOST_TOKEN` | yes | The user's Watchpost connection token (`wp_…`), from [the Watchpost app → Connections](https://app.watchpost.systems/connections?ref=clawhub). |

No Watchpost account yet? [Sign up free](https://app.watchpost.systems/signup?ref=clawhub) —
10 protected purchases a month on the free plan, no card needed.

`WATCHPOST_TOKEN` is the **only** variable this skill reads. The API endpoint is
hardcoded to the official Watchpost API (`https://api.watchpost.systems`) and is
**not** configurable — so the token can only ever be sent to Watchpost, never
redirected to another host.
