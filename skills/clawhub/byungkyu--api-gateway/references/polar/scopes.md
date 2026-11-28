# Polar scopes

The OAuth scopes Polar connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/polar#permissions.

```bash
maton connection create polar --scopes user:read
```

| Scope | Requested |
| --- | --- |
| `openid` | Always |
| `profile` | Always |
| `email` | Always |
| `user:read` | By default |
| `user:write` | By default |
| `organizations:read` | By default |
| `organizations:write` | By default |
| `custom_fields:read` | By default |
| `custom_fields:write` | By default |
| `discounts:read` | By default |
| `discounts:write` | By default |
| `checkout_links:read` | By default |
| `checkout_links:write` | By default |
| `checkouts:read` | By default |
| `checkouts:write` | By default |
| `transactions:read` | By default |
| `transactions:write` | By default |
| `payouts:read` | By default |
| `payouts:write` | By default |
| `products:read` | By default |
| `products:write` | By default |
| `benefits:read` | By default |
| `benefits:write` | By default |
| `events:read` | By default |
| `events:write` | By default |
| `meters:read` | By default |
| `meters:write` | By default |
| `files:read` | By default |
| `files:write` | By default |
| `subscriptions:read` | By default |
| `subscriptions:write` | By default |
| `customers:read` | By default |
| `customers:write` | By default |
| `members:read` | By default |
| `members:write` | By default |
| `wallets:read` | By default |
| `wallets:write` | By default |
| `disputes:read` | By default |
| `disputes:write` | By default |
| `customer_meters:read` | By default |
| `customer_sessions:write` | By default |
| `member_sessions:write` | By default |
| `customer_seats:read` | By default |
| `customer_seats:write` | By default |
| `orders:read` | By default |
| `orders:write` | By default |
| `refunds:read` | By default |
| `refunds:write` | By default |
| `payments:read` | By default |
| `metrics:read` | By default |
| `metrics:write` | By default |
| `webhooks:read` | By default |
| `webhooks:write` | By default |
| `license_keys:read` | By default |
| `license_keys:write` | By default |
| `customer_portal:read` | By default |
| `customer_portal:write` | By default |
| `notifications:read` | By default |
| `notifications:write` | By default |
| `notification_recipients:read` | By default |
| `notification_recipients:write` | By default |
