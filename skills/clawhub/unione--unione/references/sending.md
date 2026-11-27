# Sending with email/send

One `email/send` call sends one message to up to **500 recipients**; each recipient gets a separate copy with
its own substitutions, metadata, tracking links and unsubscribe link. There is no batch endpoint: for different
messages make one call per message, for the same message to many people use one call with many `recipients`.

## Request

```json
{
  "message": {
    "recipients": [
      {"email": "alex@example.com", "substitutions": {"name": "Alex"}, "metadata": {"user_id": "42"}},
      {"email": "kim@example.com", "substitutions": {"name": "Kim"}, "metadata": {"user_id": "43"}}
    ],
    "from_email": "noreply@example.com",
    "from_name": "Example",
    "subject": "Your order, {{name}}",
    "body": {
      "html": "<p>Hello, {{name}}!</p>",
      "plaintext": "Hello, {{name}}!"
    },
    "global_substitutions": {"shop": "Example"},
    "tags": ["orders"],
    "idempotence_key": "order-confirmation-1001"
  }
}
```

| Field | Notes |
|---|---|
| `recipients[]` | 1–500. `email` required; `substitutions` per recipient; `metadata` comes back in webhooks (max 10 keys, key ≤ 64, value ≤ 1024 chars). Special substitution `to_name` sets the name in the `To` header (≤ 78 chars). |
| `from_email` | Must be on a verified domain (or the sandbox domain). Required unless `template_id` gives it. |
| `body.html` / `body.plaintext` / `body.amp` | `html` or `plaintext` is required. Send both: plaintext helps deliverability. |
| `template_id` | Id from `template/set`; the template supplies the fields not passed in the call. |
| `template_engine` | `simple` (default), `velocity`, `liquid` or `none`. See [templates.md](templates.md). |
| `global_substitutions` / `global_metadata` | For all recipients; per-recipient values win. |
| `tags` | Up to 4 unique strings, ≤ 100 chars each; filter statistics and event dumps by them. |
| `headers` | Up to 50; only `X-` headers, plus `To` / `CC` (see below). |
| `attachments[]` / `inline_attachments[]` | `{type, name, content}`, `content` in base64 (about a third larger than the file), the whole request ≤ 10 MB. Inline: `name` is the content id, `<img src="cid:NAME">`. |
| `reply_to`, `reply_to_name` | Reply-To header. |
| `options.send_at` | `"YYYY-MM-DD hh:mm:ss"` in **UTC**, up to 24 hours ahead. |
| `options.unsubscribe_url` | Your own unsubscribe link (substitutions work in it). |
| `track_links`, `track_read`, `skip_unsubscribe` | Defaults are 1, 1, 0. Turning them off needs UniOne support to enable it for the account. |
| `idempotence_key` | ≤ 64 chars; a repeated key **within one minute** is declined. |

Substitutions work in `body.html`, `body.plaintext`, `body.amp`, `subject`, `from_name`, `headers` and
`options.unsubscribe_url`. Names: Latin letters, digits and `_`, starting with a letter.

## Response

```json
{"status": "success", "job_id": "1ZymBc-00041N-9X", "emails": ["alex@example.com"],
 "failed_emails": {"kim@example.com": "unsubscribed"}}
```

**Partial acceptance:** invalid, duplicate, unsubscribed or suppressed addresses are returned in
`failed_emails` and the message still goes to the others. Always read `failed_emails` — a `success` status does
not mean every recipient was accepted. When every recipient fails, the call returns an error (API code 204).
Delivery itself is reported later by webhooks ([webhooks.md](webhooks.md)).

## CC and BCC

Put every address that must receive the message into `recipients` (each one is a billed copy); set the visible
`To` and `CC` headers in `headers`. A recipient missing from both headers is a blind copy.

```json
"recipients": [{"email": "john@example.com"}, {"email": "mary@example.org"}, {"email": "audit@example.com"}],
"headers": {"To": "John <john@example.com>", "CC": "Mary <mary@example.org>"}
```

`CC` requires `To`; up to 10 addresses in each header and up to 10 blind copies. A blind copy must be on a
domain verified in your account.

## Retries

- Set `idempotence_key` on every send you may retry, derived from your entity: `order-confirmation-<order_id>`.
  The window is **one minute**: it guards against a quick double submit or a retry after a timeout, not against a
  job that runs again hours later — keep your own "already sent" flag for that.
- Retry only retryable errors (network errors, timeouts, HTTP 429 and 5xx: `retryable` of the SDK error) with
  backoff and the same `idempotence_key`, inside the minute (e.g. 1 s, 4 s, 16 s, ~45 s); later, check your "already
  sent" flag first. Do not retry other 4xx unchanged: fix the request.
- A timeout does not mean the message was not sent: retry with the same `idempotence_key`.

## Scheduling and large volumes

`options.send_at` schedules up to 24 hours ahead; for later sends, schedule in your own queue. For newsletters to
large lists send in chunks of up to 500 recipients, respect unsubscribes, and warm up a new domain gradually
(see the email-best-practices skill).
