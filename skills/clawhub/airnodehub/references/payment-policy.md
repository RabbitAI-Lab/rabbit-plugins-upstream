# Payment policy

This skill is deliberately non-spending.

Before calling, inspect the live document. If `x-airnode.payment.prices` contains the operation, return:

```json
{
  "state": "needs-payment-authorisation",
  "operation": "<operation>",
  "priceUsd": "<published price>",
  "network": "<network>",
  "asset": "<asset>"
}
```

Do not:

- accept or read raw private keys;
- infer payment authority from wallet availability;
- sign an x402 authorization;
- silently choose a free or cheaper provider;
- retry a paid operation as if it were free.

A separate execution skill may accept a host-provided x402 payer plus explicit maximum spend, timeout, and fallback policy. Preserve the `X-PAYMENT-RESPONSE` settlement receipt when that exists.