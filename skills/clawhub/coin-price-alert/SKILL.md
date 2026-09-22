---
name: "coin-price-alert"
description: "Check a Nodary AirnodeHub crypto feed every five minutes, compare each price to the prior check, and announce an attested alert only after a 5% or greater change."
---

# Coin price alert

1. Collect the Nodary feed name in `BASE/QUOTE` form, such as `BTC/USD`. Confirm an ambiguous asset or quote currency before creating the alert. Completion: the exact feed name is explicit.

2. POST `{"operation":"latestFeeds","parameters":{"name":"BASE/QUOTE"}}` to `https://airnode-nodary.fly.dev/`. Read the numeric price from `data[feedName].value`, and use `data[feedName].timestamp` as the source timestamp. Completion: a live request returns that feed and both fields are numeric.

3. Create a recurring OpenClaw automation scheduled every five minutes. Its read-only condition trigger POSTs the selected operation, extracts the signed response's feed value, and stores the latest observed price in trigger state. Completion: the first check stores a baseline and sends no alert.

4. On each later check, calculate `abs(current - previous) / previous * 100`. Fire only when the absolute change is at least 5%; otherwise return `fire: false` and silently replace the stored baseline with the current price. Protect against a missing, zero, or non-numeric prior price by resetting the baseline without alerting. Completion: non-events have no user-visible output.

5. Configure the fired payload as a short agent turn that reports the feed name, current and previous prices, percentage change, direction, and Nodary source timestamp. Prefix an increase with 🟢 and a decrease with 🔴. Set delivery to `announce` for the requesting conversation. The scheduler sends the notification; do not call a channel messaging tool inside the job. Completion: a forced qualifying-change test produces exactly one message in the requesting conversation.

6. Give the job a descriptive name and report its job ID, source, five-minute interval, and 5% comparison rule. Verify a job before updating or removing it, and update the existing job rather than creating a duplicate. Completion: the alert can be managed unambiguously.

## Notes

- Nodary's Airnode response includes an Airnode address, request hash, timestamp, data, and signature; call it an attested snapshot. Verify a signature only if the user asks.
- Price alerts are informational, not trading advice.
- Never silently substitute an unrecognized feed.

## Sources

- https://airnode-v2-hub.api3.org/llms.txt
- https://airnode-nodary.fly.dev/
