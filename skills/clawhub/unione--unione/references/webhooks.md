# Webhooks

Delivery is asynchronous: `email/send` only accepts the message. Statuses come to your HTTPS endpoint registered
with `webhook/set` (one webhook per URL; `webhook/get`, `webhook/list`, `webhook/delete`).

```json
{
  "url": "https://example.com/unione/webhook",
  "event_format": "json_post",
  "delivery_info": 1,
  "single_event": 0,
  "max_parallel": 10,
  "events": {
    "email_status": ["delivered", "opened", "clicked", "unsubscribed", "subscribed", "soft_bounced", "hard_bounced", "spam"],
    "spam_block": ["*"]
  }
}
```

## Notification

```json
{
  "auth": "<md5 signature>",
  "events_by_user": [{
    "user_id": 456, "project_id": "6432890213745872",
    "events": [{
      "event_name": "transactional_email_status",
      "event_data": {"job_id": "1a3Q2V-0000OZ-S0", "email": "alex@example.com", "status": "delivered",
                     "event_time": "2015-11-30 15:09:42", "metadata": {"user_id": "42"},
                     "delivery_info": {"delivery_status": "...", "destination_response": "..."}}
    }]
  }]
}
```

`event_name`: `transactional_email_status` (statuses `sent`, `delivered`, `opened`, `clicked`, `unsubscribed`,
`subscribed`, `soft_bounced`, `hard_bounced`, `spam`) or `transactional_spam_block`. One request can carry several
events (`single_event: 0`); `json_post_gzip` gzips the body.

## Verify the signature

`auth` is the MD5 (hex) of the **raw request body** in which the value of `auth` is replaced by the API key of the
account or project that owns the webhook. Compute it over the exact bytes received, before parsing JSON.

```javascript
import express from "express";
import { createHash, timingSafeEqual } from "node:crypto";

const app = express();
const AUTH = /"auth"\s*:\s*"([0-9a-fA-F]{32})"/;

app.post("/unione/webhook", express.text({ type: "*/*" }), (req, res) => {
  const raw = req.body;
  const match = AUTH.exec(raw);
  if (!match) return res.sendStatus(401);
  const expected = createHash("md5").update(raw.split(match[1]).join(process.env.UNIONE_API_KEY), "utf8").digest("hex");
  if (!timingSafeEqual(Buffer.from(expected), Buffer.from(match[1].toLowerCase()))) return res.sendStatus(401);
  for (const user of JSON.parse(raw).events_by_user) {
    for (const event of user.events) {
      // enqueue the event; handle it idempotently (job_id + email + status + event_time)
    }
  }
  res.sendStatus(200);
});
```

```python
import hashlib
import hmac
import os
import re

from flask import Flask, request

app = Flask(__name__)
AUTH = re.compile(rb'"auth"\s*:\s*"([0-9a-fA-F]{32})"')


@app.post("/unione/webhook")
def webhook():
    body = request.get_data()
    match = AUTH.search(body)
    if not match:
        return "", 401
    expected = hashlib.md5(body.replace(match.group(1), os.environ["UNIONE_API_KEY"].encode())).hexdigest()
    if not hmac.compare_digest(expected, match.group(1).decode().lower()):
        return "", 401
    for user in request.get_json(force=True)["events_by_user"]:
        for event in user["events"]:
            pass  # enqueue the event; handle it idempotently
    return "", 200
```

The framework packages of UniOne (Laravel, Symfony, Django, Flask, FastAPI, Express, NestJS, Rails, Spring,
ASP.NET Core, net/http, axum) ship this endpoint with the check built in: see [installation.md](installation.md).

## Delivery rules

- Answer **HTTP 200 within 3 seconds**: put events on a queue and process them later.
- A failed delivery is repeated every 10 minutes for 24 hours (with `retry_count`); when every notification of at
  least 10 events in 24 hours fails, the webhook is switched off (`status: stopped`) and the account's technical
  contact gets an email. Turn it on again with `webhook/set` and `status: active`.
- Events can repeat and arrive out of order: deduplicate, and never let `delivered` overwrite `hard_bounced`.
- `hard_bounced` and `spam` mean: stop sending to the address (it is also suppressed automatically).
