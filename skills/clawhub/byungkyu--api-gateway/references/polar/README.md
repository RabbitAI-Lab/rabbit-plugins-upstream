# Polar

## API Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../../SKILL.md#security--permissions) for full security policy.

> **Money and customers — Polar writes act on real payments.** Polar is the merchant of record for the user's software sales: products and prices are what customers are charged, subscriptions renew real cards, and refunds return real money. A mistaken write cannot always be undone.
> - **Refunds, subscription cancellations and revocations, price changes, discounts, dispute acceptance, and webhook endpoints are high-impact.** Before any of them, show the user the exact object (product, order, subscription or customer by name and ID), the amount and currency, and the effect (for example "revokes access immediately" vs "cancels at period end"), and get explicit approval for that one change.
> - Amounts are integers in the smallest currency unit (cents). Read a price back to the user as currency (`1900` is $19.00) before writing it.
> - **Customer records are personal data.** Customers, members, orders, checkouts and payments carry names, email addresses, billing addresses and tax IDs of the user's buyers. Filter server-side (`customer_id`, `email`, `product_id`, `organization_id`) rather than paging through everything, return the narrowest answer, and never forward customer data to a third-party host without explicit approval for that specific transfer.
> - **License keys and checkout `client_secret` values are credentials.** Show `display_key`, not `key`, unless the user asks for a specific customer's key.
> - The sample values below (`Jane Doe`, `jane@example.com`, `Pro Plan`) are **placeholders**. Never send them to a live account, and never invent prices, emails, or product details — ask the user.

**App name:** `polar`
**Upstream base URL:** `api.polar.sh`

Replace the upstream base URL with the app name. Everything after the base URL including query strings is kept as-is. Any account-specific part of the base URL and the API credentials are stored in the Maton connection, and the gateway injects both so requests never carry them. For example:

- Upstream: `api.polar.sh/v1/products/`
- Gateway: `api.maton.ai/polar/v1/products/`

The connection is an OAuth2 user token for **Polar production** (the sandbox is not supported). It covers every organization the user belongs to, unless they limited it to one on Polar's consent screen; most list endpoints accept `organization_id` to narrow results to one organization, and creates need `organization_id` when the user has more than one.

**Keep the trailing slash on collection paths** (`/v1/products/`, `/v1/orders/`). Without it Polar answers `307` with a `Location` on `api.polar.sh`, outside the gateway; do not follow that redirect.

Polar recommends pinning the API version with a `Polar-Version` header (for example `-H 'Polar-Version: 2026-10'`). It is optional: the gateway passes it through and sets none itself, Polar uses its current version when it is absent, and every response reports the version used in its `polar-version` header.

### Identity

#### Get the Connected User

```bash
maton api '/polar/v1/oauth2/userinfo'
```

**Response:**

```json
{
  "sub": "{user_id}",
  "email": "jane@example.com",
  "email_verified": true
}
```

`name` may be absent. `GET /v1/users/me` returns `403 NotPermitted` for OAuth tokens even with every scope; use `/v1/oauth2/userinfo`.

### Organizations

#### List Organizations

```bash
maton api '/polar/v1/organizations/'
```

Returns the organizations the token can reach, each with `id`, `name`, `slug`, `status`, `default_presentment_currency`, and `capabilities`. Use the `id` as `organization_id` elsewhere. Also accepts `slug`.

#### Get Organization

```bash
maton api '/polar/v1/organizations/{organization_id}'
```

**Note:** `{organization_id}` stands for a real value; fill it in before sending the request.

### Products

#### List Products

```bash
maton api '/polar/v1/products/?limit=10'
```

**Query parameters:**
- `organization_id` - Filter by organization (repeat for several)
- `query` - Search by name
- `is_archived` - `true` or `false`
- `is_recurring` - `true` for subscription products, `false` for one-time
- `benefit_id` - Products granting this benefit
- `visibility` - `draft`, `private`, or `public`
- `page`, `limit` - Pagination (default `limit` 10, max 100)
- `sorting` - e.g. `-created_at` (default), `name`, `price_amount`

**Response (trimmed):**

```json
{
  "items": [
    {
      "id": "{product_id}",
      "name": "Pro Plan",
      "description": "Everything in Pro",
      "visibility": "public",
      "is_recurring": true,
      "recurring_interval": "month",
      "recurring_interval_count": 1,
      "is_archived": false,
      "organization_id": "{organization_id}",
      "prices": [
        {"id": "{price_id}", "amount_type": "fixed", "price_currency": "usd", "price_amount": 1900, "is_archived": false}
      ],
      "benefits": []
    }
  ],
  "pagination": {"total_count": 1, "max_page": 1}
}
```

#### Get Product

```bash
maton api '/polar/v1/products/{product_id}'
```

**Note:** `{product_id}` stands for a real value; fill it in before sending the request.

#### Create Product

```bash
maton api -X POST '/polar/v1/products/' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "name": "Pro Plan",
  "description": "Everything in Pro",
  "organization_id": "{organization_id}",
  "recurring_interval": "month",
  "prices": [
    {"amount_type": "fixed", "price_currency": "usd", "price_amount": 1900}
  ]
}
JSON
```

**Note:** `{organization_id}` stands for a real value; fill it in before sending the request. `name` and `prices` are required. `recurring_interval` (`day`, `week`, `month`, `year`) makes it a subscription product; omit it (or send `null`) for a one-time purchase. Other price types (`amount_type`): `custom` (pay what you want), `seat_based`, `unit_based`, `metered_unit`, `metered_tiers`; a `fixed` price with `price_amount` `0` is free. New products default to `public` visibility, so they can be bought as soon as a checkout links to them; set `"visibility": "draft"` to review first.

#### Update Product

```bash
maton api -X PATCH '/polar/v1/products/{product_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "description": "Everything in Pro, plus priority support"
}
JSON
```

**Note:** `{product_id}` stands for a real value; fill it in before sending the request. Sending `prices` **replaces** the price list: include existing prices as `{"id": "{price_id}"}` to keep them; any left out are removed from the product. A price change applies to new purchases; confirm the new amount with the user. `"is_archived": true` stops new sales of the product; existing subscribers keep access.

### Checkout Links

A checkout link is a reusable, shareable URL that starts a checkout for one or more products.

#### List Checkout Links

```bash
maton api '/polar/v1/checkout-links/?limit=10'
```

**Query parameters:** `organization_id`, `product_id`, `page`, `limit`, `sorting`.

#### Create Checkout Link

```bash
maton api -X POST '/polar/v1/checkout-links/' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "payment_processor": "stripe",
  "products": ["{product_id}"],
  "label": "Pricing page",
  "allow_discount_codes": true,
  "success_url": "https://example.com/thanks?checkout_id={CHECKOUT_ID}"
}
JSON
```

**Note:** `{product_id}` stands for a real value; fill it in before sending the request. `{CHECKOUT_ID}` is left literally; Polar substitutes it on redirect. `payment_processor` (`stripe`) and `products` are required. The response `url` is the shareable link.

#### Delete Checkout Link

```bash
maton api -X DELETE '/polar/v1/checkout-links/{checkout_link_id}'
```

**Note:** `{checkout_link_id}` stands for a real value; fill it in before sending the request. Anyone with the old URL can no longer buy through it.

### Checkout Sessions

#### List Checkout Sessions

```bash
maton api '/polar/v1/checkouts/?limit=10'
```

**Query parameters:** `organization_id`, `product_id`, `customer_id`, `external_customer_id`, `status` (`open`, `expired`, `confirmed`, `succeeded`, `failed`), `query`, `page`, `limit`, `sorting`.

#### Get Checkout Session

```bash
maton api '/polar/v1/checkouts/{checkout_id}'
```

**Note:** `{checkout_id}` stands for a real value; fill it in before sending the request.

#### Create Checkout Session

```bash
maton api -X POST '/polar/v1/checkouts/' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "products": ["{product_id}"],
  "customer_email": "jane@example.com",
  "success_url": "https://example.com/thanks?checkout_id={CHECKOUT_ID}"
}
JSON
```

**Note:** `{product_id}` stands for a real value; fill it in before sending the request. `products` is required; the first is selected by default. Optional: `customer_id` or `external_customer_id` to link an existing customer, `discount_id`, `allow_discount_codes`, `metadata`. The response `url` is a one-off payment page for the customer; it charges nothing until they pay. Never fill `customer_email` with a guessed address.

### Orders

#### List Orders

```bash
maton api '/polar/v1/orders/?limit=10'
```

**Query parameters:**
- `organization_id`, `product_id`, `customer_id`, `external_customer_id`, `subscription_id`, `checkout_id`, `discount_id`
- `status` - `draft`, `pending`, `paid`, `refunded`, `partially_refunded`, `void`
- `product_billing_type` - `one_time` or `recurring`
- `created_after`, `created_before` - ISO 8601 timestamps
- `page`, `limit`, `sorting` (e.g. `-created_at`, `-amount`)

**Example:**

```bash
maton api '/polar/v1/orders/?status=paid&created_after=2026-11-01T00:00:00Z&limit=25'
```

**Response (trimmed):**

```json
{
  "items": [
    {
      "id": "{order_id}",
      "created_at": "2026-11-03T14:12:09Z",
      "status": "paid",
      "billing_reason": "subscription_cycle",
      "subtotal_amount": 1900,
      "discount_amount": 0,
      "tax_amount": 0,
      "total_amount": 1900,
      "refunded_amount": 0,
      "refundable_amount": 1900,
      "currency": "usd",
      "customer_id": "{customer_id}",
      "product_id": "{product_id}",
      "subscription_id": "{subscription_id}",
      "invoice_number": "INV-0001"
    }
  ],
  "pagination": {"total_count": 1, "max_page": 1}
}
```

Each order also embeds `customer`, `product`, `subscription`, and line `items`.

#### Get Order

```bash
maton api '/polar/v1/orders/{order_id}'
```

**Note:** `{order_id}` stands for a real value; fill it in before sending the request.

#### Get Order Invoice

```bash
maton api '/polar/v1/orders/{order_id}/invoice'
```

**Note:** `{order_id}` stands for a real value; fill it in before sending the request. Returns the invoice download `url` once it has been generated (`is_invoice_generated` on the order). `POST /v1/orders/{order_id}/invoice` triggers generation from the order's current billing details; ask first.

### Subscriptions

#### List Subscriptions

```bash
maton api '/polar/v1/subscriptions/?active=true&limit=10'
```

**Query parameters:**
- `organization_id`, `product_id`, `customer_id`, `external_customer_id`, `discount_id`
- `active` - `true` for active subscriptions only
- `status` - `incomplete`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, `paused`, ...
- `cancel_at_period_end` - `true` for subscriptions scheduled to end
- `started_after`, `started_before`, `canceled_at_after`, `canceled_at_before`
- `page`, `limit`, `sorting` (e.g. `-started_at`)

#### Get Subscription

```bash
maton api '/polar/v1/subscriptions/{subscription_id}'
```

**Note:** `{subscription_id}` stands for a real value; fill it in before sending the request. Key fields: `status`, `amount`, `currency`, `recurring_interval`, `current_period_end`, `cancel_at_period_end`, `customer`, `product`.

#### Cancel Subscription at Period End

> **High-impact.** Confirm the customer, product, and `current_period_end` with the user. The customer keeps access until the period ends and is not charged again.

```bash
maton api -X PATCH '/polar/v1/subscriptions/{subscription_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "cancel_at_period_end": true
}
JSON
```

**Note:** `{subscription_id}` stands for a real value; fill it in before sending the request. `"cancel_at_period_end": false` undoes a scheduled cancellation.

#### Change Plan

```bash
maton api -X PATCH '/polar/v1/subscriptions/{subscription_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "product_id": "{new_product_id}",
  "proration_behavior": "prorate"
}
JSON
```

**Note:** `{subscription_id}` and `{new_product_id}` stand for real values; fill them in before sending the request. Changes what the customer is billed. `proration_behavior` is `invoice` (charge the difference now), `prorate` (on the next invoice), `next_period`, or `reset`; omitted, the organization default applies. Other single-purpose bodies for this endpoint: `{"discount_id": ...}` (`null` removes it), `{"trial_end": ...}`, `{"seats": ...}`. Send one kind of change per request.

#### Revoke Subscription Immediately

> **High-impact and immediate.** Ends the subscription now and revokes the customer's benefits (license keys, repository access, downloads). Prefer cancel at period end unless the user explicitly asks for immediate revocation.

```bash
maton api -X DELETE '/polar/v1/subscriptions/{subscription_id}'
```

**Note:** `{subscription_id}` stands for a real value; fill it in before sending the request. `PATCH` with `{"revoke": true}` does the same.

### Customers

#### List Customers

```bash
maton api '/polar/v1/customers/?limit=10'
```

**Query parameters:** `organization_id`, `email` (exact match), `query` (name or email search), `active`, `page`, `limit`, `sorting`.

**Example:**

```bash
maton api '/polar/v1/customers/?email=jane%40example.com'
```

#### Get Customer

```bash
maton api '/polar/v1/customers/{customer_id}'
maton api '/polar/v1/customers/external/{external_id}'
```

**Note:** `{customer_id}` and `{external_id}` stand for real values; fill them in before sending the request. `external_id` is the user's own ID for the customer, if they set one.

#### Get Customer State

```bash
maton api '/polar/v1/customers/{customer_id}/state'
```

**Note:** `{customer_id}` stands for a real value; fill it in before sending the request. Returns the customer with their active subscriptions, granted benefits, and meter balances in one call — the usual way to answer "what does this customer have access to?".

#### Update Customer

```bash
maton api -X PATCH '/polar/v1/customers/{customer_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "name": "Jane Doe"
}
JSON
```

**Note:** `{customer_id}` stands for a real value; fill it in before sending the request. Updatable: `email`, `name`, `billing_address`, `tax_id`, `locale`, `external_id` (set once), `metadata`. `DELETE /v1/customers/{customer_id}` cannot be undone: it immediately cancels the customer's active subscriptions and revokes all their benefits. Never run it without explicit approval naming the customer.

#### List Members

```bash
maton api '/polar/v1/members/?limit=10'
maton api '/polar/v1/customers/{customer_id}/members'
```

**Note:** `{customer_id}` stands for a real value; fill it in before sending the request. Members are the people within a team customer.

### Refunds

#### List Refunds

```bash
maton api '/polar/v1/refunds/?limit=10'
```

**Query parameters:** `organization_id`, `order_id`, `subscription_id`, `customer_id`, `succeeded`, `page`, `limit`, `sorting`.

#### Create Refund

> **High-impact: returns real money and cannot be reversed.** Read the order first, confirm the order, customer, amount (within `refundable_amount`) and currency, and whether benefits should be revoked, then get explicit approval.

```bash
maton api -X POST '/polar/v1/refunds/' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "order_id": "{order_id}",
  "amount": 1900,
  "reason": "customer_request",
  "comment": "Requested within 14 days"
}
JSON
```

**Note:** `{order_id}` stands for a real value; fill it in before sending the request. `order_id`, `amount` (cents, at least 1) and `reason` are required. `reason` is `duplicate`, `fraudulent`, `customer_request`, `service_disruption`, `satisfaction_guarantee`, or `other`. `"revoke_benefits": true` also revokes what the order granted; Polar allows it only for one-time purchases (a subscription's benefits end when the subscription is revoked).

### Payments and Disputes

```bash
maton api '/polar/v1/payments/?limit=10'
maton api '/polar/v1/payments/{payment_id}'
maton api '/polar/v1/disputes/?limit=10'
maton api '/polar/v1/disputes/{dispute_id}'
```

**Note:** `{payment_id}` and `{dispute_id}` stand for real values; fill them in before sending the request. Payments filter by `organization_id`, `checkout_id`, `order_id`, `customer_id`, `status` (`pending`, `succeeded`, `failed`), `method`. Disputes filter by `organization_id`, `order_id`, `status` (`needs_response`, `under_review`, `won`, `lost`, ...). `POST /v1/disputes/{dispute_id}/accept` concedes the chargeback and the funds; only on explicit request.

### Discounts

#### List Discounts

```bash
maton api '/polar/v1/discounts/?limit=10'
```

**Query parameters:** `organization_id`, `query`, `page`, `limit`, `sorting`.

#### Create Discount

```bash
maton api -X POST '/polar/v1/discounts/' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "name": "Launch week",
  "type": "percentage",
  "basis_points": 2000,
  "duration": "once",
  "code": "LAUNCH20",
  "max_redemptions": 100,
  "ends_at": "2026-12-31T23:59:59Z",
  "organization_id": "{organization_id}"
}
JSON
```

**Note:** `{organization_id}` stands for a real value; fill it in before sending the request. `basis_points` is hundredths of a percent (`2000` = 20%). For a fixed amount use `"type": "fixed"` with `amount` (cents) and `currency`. `duration` is `once`, `forever`, or `repeating` (with `duration_in_months`). `products` limits which products it applies to. Confirm the amount, code, and limits; a public code can be redeemed by anyone who has it.

### Benefits and License Keys

```bash
maton api '/polar/v1/benefits/?limit=10'
maton api '/polar/v1/benefits/{benefit_id}/grants?limit=10'
maton api '/polar/v1/license-keys/?limit=10'
maton api '/polar/v1/license-keys/{license_key_id}'
```

**Note:** `{benefit_id}` and `{license_key_id}` stand for real values; fill them in before sending the request. Benefits filter by `organization_id`, `type` (`license_keys`, `downloadables`, `github_repository`, `discord`, `custom`, `meter_credit`, `feature_flag`, ...). License keys filter by `organization_id`, `benefit_id`, `status` (`granted`, `revoked`, `disabled`); each carries the full `key` and a masked `display_key`.

#### Disable a License Key

```bash
maton api -X PATCH '/polar/v1/license-keys/{license_key_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "status": "disabled"
}
JSON
```

**Note:** `{license_key_id}` stands for a real value; fill it in before sending the request. The customer's software stops validating; confirm the customer first. Also settable: `limit_activations`, `limit_usage`, `expires_at`.

### Metrics

#### Get Metrics

```bash
maton api '/polar/v1/metrics/?start_date=2026-10-01&end_date=2026-10-31&interval=day'
```

**Query parameters:**
- `start_date`, `end_date`, `interval` - Required. `interval` is `hour`, `day`, `week`, `month`, or `year`
- `timezone` - IANA name, default `UTC`
- `organization_id`, `product_id`, `billing_type` (`one_time`, `recurring`), `customer_id`
- `metrics` - Limit to specific metric slugs (repeat for several)

**Response (trimmed):**

```json
{
  "periods": [
    {"timestamp": "2026-10-01T00:00:00Z", "orders": 3, "revenue": 5700, "net_revenue": 5300, "active_subscriptions": 12, "monthly_recurring_revenue": 22800, "churned_subscriptions": 0}
  ],
  "totals": {"orders": 41, "revenue": 77900},
  "metrics": {"revenue": {"slug": "revenue", "display_name": "Revenue", "type": "currency"}}
}
```

Money metrics are in cents.

#### Get Metric Limits

```bash
maton api '/polar/v1/metrics/limits'
```

Returns `min_date` and, per interval, the allowed range in days (for example `day` up to 366 days, `hour` up to 7).

### Usage Billing

```bash
maton api '/polar/v1/meters/?limit=10'
maton api '/polar/v1/meters/{meter_id}/quantities?start_timestamp=2026-11-01T00:00:00Z&end_timestamp=2026-11-26T00:00:00Z&interval=day'
maton api '/polar/v1/customer-meters/?customer_id={customer_id}'
maton api '/polar/v1/events/?limit=10'
maton api '/polar/v1/events/names'
```

**Note:** `{meter_id}` and `{customer_id}` stand for real values; fill them in before sending the request. `POST /v1/events/ingest` records usage that customers are billed for; ingest only events the user supplies.

### Other Read Endpoints

```bash
maton api '/polar/v1/custom-fields/?limit=10'
maton api '/polar/v1/files/?limit=10'
maton api '/polar/v1/benefit-grants/?limit=10'
maton api '/polar/v1/customer-seats?subscription_id={subscription_id}'
```

**Note:** `{subscription_id}` stands for a real value; fill it in before sending the request. `customer-seats` requires `subscription_id` or `order_id` (otherwise `400`).

### Webhook Endpoints

```bash
maton api '/polar/v1/webhooks/endpoints'
maton api '/polar/v1/webhooks/deliveries?endpoint_id={endpoint_id}&limit=10'
```

**Note:** `{endpoint_id}` stands for a real value; fill it in before sending the request.

#### Create Webhook Endpoint

> **Standing egress of customer and order data.** A Polar webhook sends every matching event — with customer names, emails, and order amounts — to the URL until it is deleted. Create one only for a URL the user names, list the events and say what the payloads contain, and get explicit approval. For automation inside Maton, a Maton trigger and function are the usual path.

```bash
maton api -X POST '/polar/v1/webhooks/endpoints' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "url": "https://hooks.example.com/polar",
  "format": "raw",
  "events": ["order.paid", "subscription.canceled"],
  "organization_id": "{organization_id}"
}
JSON
```

**Note:** `{organization_id}` stands for a real value; fill it in before sending the request. `url`, `format` (`raw`, `discord`, `slack`) and `events` are required. The response includes the signing `secret`; treat it as a credential and do not print it. `DELETE /v1/webhooks/endpoints/{endpoint_id}` stops delivery.

### Pagination

List endpoints take `page` (from 1) and `limit` (default 10, max 100) and return `items` with a `pagination` object:

```json
{"items": [], "pagination": {"total_count": 42, "max_page": 5}}
```

```bash
maton api '/polar/v1/orders/?limit=100&page=1'
maton api '/polar/v1/orders/?limit=100&page=2'
```

Stop when `page` reaches `max_page`.

### Notes

- IDs are UUIDs; a malformed ID returns `422 RequestValidationError`, an unknown one `404 ResourceNotFound`.
- Amounts are integers in the smallest currency unit; currencies are lowercase ISO codes (`usd`).
- Timestamps are ISO 8601 (UTC).
- Array filters repeat the parameter: `?product_id={a}&product_id={b}`. `sorting` takes a field name, `-` prefix for descending.
- Errors are JSON `{"error": "...", "detail": ...}`; validation errors list each field in `detail`.
- Payouts, transactions and wallets have OAuth scopes but no endpoints in Polar's public API; they are not part of this reference.
- Rate limit: Polar documents 500 requests per minute in production. On `429`, wait for `Retry-After`.

### Resources

- [Polar API Reference](https://polar.sh/docs/api-reference/introduction)
- [API Versioning](https://polar.sh/docs/api-reference/versioning)
- [Products](https://polar.sh/docs/features/products)
- [Checkout Links](https://polar.sh/docs/features/checkout/links)
- [Refunds](https://polar.sh/docs/features/refunds)
- [Subscriptions](https://polar.sh/docs/features/subscriptions)
- [Metrics](https://polar.sh/docs/features/analytics)
- [OpenAPI Spec](https://api.polar.sh/openapi.json)
- [Maton CLI Manual](https://cli.maton.ai/manual)
