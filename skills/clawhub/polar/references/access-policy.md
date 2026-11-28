# Polar access policy

An access policy limits which endpoints Polar connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/polar#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Polar: its 57 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create polar --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/benefit-grants/"},
    {"method": "GET", "path": "v1/benefits/"},
    {"method": "GET", "path": "v1/benefits/{id}"},
    {"method": "GET", "path": "v1/benefits/{id}/files"},
    {"method": "GET", "path": "v1/benefits/{id}/grants"},
    {"method": "GET", "path": "v1/checkout-links/"},
    {"method": "GET", "path": "v1/checkout-links/{id}"},
    {"method": "GET", "path": "v1/checkouts/"},
    {"method": "GET", "path": "v1/checkouts/client/{id}"},
    {"method": "GET", "path": "v1/checkouts/{id}"},
    {"method": "GET", "path": "v1/custom-fields/"},
    {"method": "GET", "path": "v1/custom-fields/{id}"},
    {"method": "GET", "path": "v1/customer-meters/"},
    {"method": "GET", "path": "v1/customer-meters/{id}"},
    {"method": "GET", "path": "v1/customer-seats"},
    {"method": "GET", "path": "v1/customer-seats/claim/{id}"},
    {"method": "GET", "path": "v1/customers/"},
    {"method": "GET", "path": "v1/customers/external/{id}"},
    {"method": "GET", "path": "v1/customers/external/{id}/members"},
    {"method": "GET", "path": "v1/customers/external/{id}/members/{id}"},
    {"method": "GET", "path": "v1/customers/external/{id}/payment-methods"},
    {"method": "GET", "path": "v1/customers/external/{id}/state"},
    {"method": "GET", "path": "v1/customers/{id}"},
    {"method": "GET", "path": "v1/customers/{id}/members"},
    {"method": "GET", "path": "v1/customers/{id}/members/{id}"},
    {"method": "GET", "path": "v1/customers/{id}/payment-methods"},
    {"method": "GET", "path": "v1/customers/{id}/state"},
    {"method": "GET", "path": "v1/discounts/"},
    {"method": "GET", "path": "v1/discounts/{id}"},
    {"method": "GET", "path": "v1/disputes/"},
    {"method": "GET", "path": "v1/disputes/{id}"},
    {"method": "GET", "path": "v1/event-types/"},
    {"method": "GET", "path": "v1/events/"},
    {"method": "GET", "path": "v1/events/names"},
    {"method": "GET", "path": "v1/events/{id}"},
    {"method": "GET", "path": "v1/files/"},
    {"method": "GET", "path": "v1/meters/"},
    {"method": "GET", "path": "v1/meters/{id}"},
    {"method": "GET", "path": "v1/meters/{id}/quantities"},
    {"method": "GET", "path": "v1/metrics/"},
    {"method": "GET", "path": "v1/metrics/limits"},
    {"method": "GET", "path": "v1/oauth2/userinfo"},
    {"method": "GET", "path": "v1/orders/"},
    {"method": "GET", "path": "v1/orders/export"},
    {"method": "GET", "path": "v1/orders/{id}"},
    {"method": "GET", "path": "v1/orders/{id}/invoice"},
    {"method": "GET", "path": "v1/orders/{id}/receipt"},
    {"method": "GET", "path": "v1/organizations/"},
    {"method": "GET", "path": "v1/organizations/{id}"},
    {"method": "GET", "path": "v1/payments/"},
    {"method": "GET", "path": "v1/payments/{id}"},
    {"method": "GET", "path": "v1/products/"},
    {"method": "GET", "path": "v1/products/{id}"},
    {"method": "GET", "path": "v1/refunds/"},
    {"method": "GET", "path": "v1/subscriptions/"},
    {"method": "GET", "path": "v1/subscriptions/{id}"},
    {"method": "GET", "path": "v1/webhooks/deliveries"}
  ],
  "deny": []
}
```

## Endpoints

The Polar endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/benefit-grants/ | read | benefit grants | List Benefit Grants. |
| GET | v1/benefits/ | read | benefits | List Benefits. |
| POST | v1/benefits/ | write | benefits | Create Benefit. |
| DELETE | v1/benefits/{id} | write | benefits | Delete Benefit. |
| GET | v1/benefits/{id} | read | benefits | Get Benefit. |
| PATCH | v1/benefits/{id} | write | benefits | Update Benefit. |
| GET | v1/benefits/{id}/files | read | benefits | List Benefit Files. |
| GET | v1/benefits/{id}/grants | read | benefits | List Benefit Grants. |
| GET | v1/checkout-links/ | read | checkout links | List Checkout Links. The response can include each link’s client_secret. |
| POST | v1/checkout-links/ | write | checkout links | Create Checkout Link. |
| DELETE | v1/checkout-links/{id} | write | checkout links | Delete Checkout Link. |
| GET | v1/checkout-links/{id} | read | checkout links | Get Checkout Link. The response can include the client_secret. |
| PATCH | v1/checkout-links/{id} | write | checkout links | Update Checkout Link. |
| GET | v1/checkouts/ | read | checkouts | List Checkout Sessions. The response can include each checkout’s client_secret. |
| POST | v1/checkouts/ | write | checkouts | Create Checkout Session. |
| GET | v1/checkouts/client/{id} | read | checkouts | Get Checkout Session from Client. The response can include the client_secret. |
| PATCH | v1/checkouts/client/{id} | write | checkouts | Update Checkout Session from Client. |
| POST | v1/checkouts/client/{id}/confirm | write | checkouts | Confirm Checkout Session from Client. |
| GET | v1/checkouts/{id} | read | checkouts | Get Checkout Session. The response can include the client_secret. |
| PATCH | v1/checkouts/{id} | write | checkouts | Update Checkout Session. |
| GET | v1/custom-fields/ | read | custom fields | List Custom Fields. |
| POST | v1/custom-fields/ | write | custom fields | Create Custom Field. |
| DELETE | v1/custom-fields/{id} | write | custom fields | Delete Custom Field. |
| GET | v1/custom-fields/{id} | read | custom fields | Get Custom Field. |
| PATCH | v1/custom-fields/{id} | write | custom fields | Update Custom Field. |
| GET | v1/customer-meters/ | read | customer meters | List Customer Meters. |
| GET | v1/customer-meters/{id} | read | customer meters | Get Customer Meter. |
| GET | v1/customer-seats | read | customer seats | List Seats. |
| POST | v1/customer-seats | write | customer seats | Assign Seat. |
| POST | v1/customer-seats/claim | write | customer seats | Claim Seat. |
| GET | v1/customer-seats/claim/{id} | read | customer seats | Get Claim Info. |
| DELETE | v1/customer-seats/{id} | write | customer seats | Revoke Seat. |
| POST | v1/customer-seats/{id}/resend | write | customer seats | Resend Invitation. |
| POST | v1/customer-sessions/ | write | customer sessions | Create Customer Session. |
| GET | v1/customers/ | read | customers | List Customers. |
| POST | v1/customers/ | write | customers | Create Customer. |
| DELETE | v1/customers/external/{id} | write | customers | Delete Customer by External ID. |
| GET | v1/customers/external/{id} | read | customers | Get Customer by External ID. |
| PATCH | v1/customers/external/{id} | write | customers | Update Customer by External ID. |
| GET | v1/customers/external/{id}/members | read | customers | List Members by Customer External ID. |
| POST | v1/customers/external/{id}/members | write | customers | Create Member by Customer External ID. |
| DELETE | v1/customers/external/{id}/members/{id} | write | customers | Delete Member by External ID. |
| GET | v1/customers/external/{id}/members/{id} | read | customers | Get Member by External ID. |
| PATCH | v1/customers/external/{id}/members/{id} | write | customers | Update Member by External ID. |
| GET | v1/customers/external/{id}/payment-methods | read | customers | List Customer Payment Methods by External ID. |
| GET | v1/customers/external/{id}/state | read | customers | Get Customer State by External ID. |
| DELETE | v1/customers/{id} | write | customers | Delete Customer. |
| GET | v1/customers/{id} | read | customers | Get Customer. |
| PATCH | v1/customers/{id} | write | customers | Update Customer. |
| GET | v1/customers/{id}/members | read | customers | List Members. |
| POST | v1/customers/{id}/members | write | customers | Create Member. |
| DELETE | v1/customers/{id}/members/{id} | write | customers | Delete Member. |
| GET | v1/customers/{id}/members/{id} | read | customers | Get Member. |
| PATCH | v1/customers/{id}/members/{id} | write | customers | Update Member. |
| GET | v1/customers/{id}/payment-methods | read | customers | List Customer Payment Methods. |
| GET | v1/customers/{id}/state | read | customers | Get Customer State. |
| GET | v1/discounts/ | read | discounts | List Discounts. |
| POST | v1/discounts/ | write | discounts | Create Discount. |
| DELETE | v1/discounts/{id} | write | discounts | Delete Discount. |
| GET | v1/discounts/{id} | read | discounts | Get Discount. |
| PATCH | v1/discounts/{id} | write | discounts | Update Discount. |
| GET | v1/disputes/ | read | disputes | List Disputes. |
| GET | v1/disputes/{id} | read | disputes | Get Dispute. |
| POST | v1/disputes/{id}/accept | write | disputes | Accept Dispute. |
| GET | v1/event-types/ | read | event types | List Event Types. |
| PATCH | v1/event-types/{id} | write | event types | Update Event Type. |
| GET | v1/events/ | read | events | List Events. |
| POST | v1/events/ingest | write | events | Ingest Events. |
| GET | v1/events/names | read | events | List Event Names. |
| GET | v1/events/{id} | read | events | Get Event. |
| GET | v1/files/ | read | files | List Files. |
| POST | v1/files/ | write | files | Create File. |
| DELETE | v1/files/{id} | write | files | Delete File. |
| PATCH | v1/files/{id} | write | files | Update File. |
| POST | v1/files/{id}/uploaded | write | files | Complete File Upload. |
| GET | v1/license-keys/ | write | license keys | List License Keys. Kept out of read: returns customers’ license key values. |
| POST | v1/license-keys/activate | write | license keys | Activate License Key. |
| POST | v1/license-keys/deactivate | write | license keys | Deactivate License Key. |
| POST | v1/license-keys/validate | write | license keys | Validate License Key. |
| GET | v1/license-keys/{id} | write | license keys | Get License Key. Kept out of read: returns a customer’s license key value. |
| PATCH | v1/license-keys/{id} | write | license keys | Update License Key. |
| GET | v1/license-keys/{id}/activations/{id} | write | license keys | Get Activation. Kept out of read: returns a customer’s license key value. |
| POST | v1/license-keys/{id}/rotate | write | license keys | Rotate License Key. |
| GET | v1/meters/ | read | meters | List Meters. |
| POST | v1/meters/ | write | meters | Create Meter. |
| GET | v1/meters/{id} | read | meters | Get Meter. |
| PATCH | v1/meters/{id} | write | meters | Update Meter. |
| GET | v1/meters/{id}/quantities | read | meters | Get Meter Quantities. |
| GET | v1/metrics/ | read | metrics | Get Metrics. |
| GET | v1/metrics/limits | read | metrics | Get Metrics Limits. |
| GET | v1/oauth2/userinfo | read | oauth2 | Get User Info. |
| GET | v1/orders/ | read | orders | List Orders. |
| POST | v1/orders/ | write | orders | Create Order. |
| GET | v1/orders/export | read | orders | Export Orders. |
| GET | v1/orders/{id} | read | orders | Get Order. |
| PATCH | v1/orders/{id} | write | orders | Update Order. |
| POST | v1/orders/{id}/finalize | write | orders | Finalize Order. |
| GET | v1/orders/{id}/invoice | read | orders | Get Order Invoice. |
| POST | v1/orders/{id}/invoice | write | orders | Generate Order Invoice. |
| GET | v1/orders/{id}/receipt | read | orders | Get Order Receipt. |
| GET | v1/organizations/ | read | organizations | List Organizations. |
| POST | v1/organizations/ | write | organizations | Create Organization. |
| GET | v1/organizations/{id} | read | organizations | Get Organization. |
| PATCH | v1/organizations/{id} | write | organizations | Update Organization. |
| GET | v1/payments/ | read | payments | List Payments. |
| GET | v1/payments/{id} | read | payments | Get Payment. |
| GET | v1/products/ | read | products | List Products. |
| POST | v1/products/ | write | products | Create Product. |
| DELETE | v1/products/{id} | write | products | Delete Product. |
| GET | v1/products/{id} | read | products | Get Product. |
| PATCH | v1/products/{id} | write | products | Update Product. |
| POST | v1/products/{id}/benefits | write | products | Update Product Benefits. |
| GET | v1/refunds/ | read | refunds | List Refunds. |
| POST | v1/refunds/ | write | refunds | Create Refund. |
| GET | v1/subscriptions/ | read | subscriptions | List Subscriptions. |
| POST | v1/subscriptions/ | write | subscriptions | Create Subscription. |
| DELETE | v1/subscriptions/{id} | write | subscriptions | Revoke Subscription. |
| GET | v1/subscriptions/{id} | read | subscriptions | Get Subscription. |
| PATCH | v1/subscriptions/{id} | write | subscriptions | Update Subscription. |
| GET | v1/webhooks/deliveries | read | webhooks | List Webhook Deliveries. |
| GET | v1/webhooks/endpoints | write | webhooks | List Webhook Endpoints. Kept out of read: returns the endpoint signing secret. |
| POST | v1/webhooks/endpoints | write | webhooks | Create Webhook Endpoint. |
| DELETE | v1/webhooks/endpoints/{id} | write | webhooks | Delete Webhook Endpoint. |
| GET | v1/webhooks/endpoints/{id} | write | webhooks | Get Webhook Endpoint. Kept out of read: returns the endpoint signing secret. |
| PATCH | v1/webhooks/endpoints/{id} | write | webhooks | Update Webhook Endpoint. |
| PATCH | v1/webhooks/endpoints/{id}/secret | write | webhooks | Reset Webhook Endpoint Secret. |
| POST | v1/webhooks/events/{id}/redeliver | write | webhooks | Redeliver Webhook Event. |
