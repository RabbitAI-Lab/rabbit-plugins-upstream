---
name: unione
description: "Use when working with the UniOne transactional email Web API — sending email (one call, up to 500 personalized recipients), templates and substitutions (simple, Velocity, Liquid), delivery webhooks, sending domains (DNS, DKIM), the sandbox domain and confirmed emails, suppressions and unsubscribes, event dumps, tags, projects and API keys, email validation, installing the UniOne SDK or a framework package, or sending through the UniOne SMTP relay (Nodemailer, Django, Laravel, PHPMailer, WordPress; options in the X-UNIONE header). Always use this skill when the user mentions UniOne, even for a simple \"send an email\" — it holds the gotchas (one-minute idempotence window, partial acceptance in failed_emails, MD5 webhook signature, sandbox limits) that break production integrations."
license: MIT
metadata:
  author: "UniOne"
  version: "1.1.8"
  homepage: https://docs.unione.io/en/web-api-ref
  source: https://github.com/unione-repo/unione-skills
compatibility: "Requires UNIONE_API_KEY: the UniOne API key (the account key, or a project key for project data) from https://cp.unione.io/en/, server-side only."
---

# UniOne

UniOne is a transactional email service. Web API: `https://api.unione.io/en/transactional/api/v1` (an account registered on another datacenter uses its host: `eu1.unione.io`, `us1.unione.io`); every method is `POST https://api.unione.io/en/transactional/api/v1/<method>.json?platform=skill` with a JSON body and the `X-API-KEY` header (`?platform=skill` marks a direct HTTP call; an SDK sets its own). Keep the key in `UNIONE_API_KEY`, server-side only.

For actions in the user's account right now (send a test, check a domain, create a template) the UniOne MCP server `https://mcp.unione.io/mcp` gives the tools; this skill is for writing the integration code.

## Quick send

### Which package

Find the stack in the project and take the first matching row: on a framework install its package, not the bare SDK (it brings the SDK, configuration, the mailer and the webhook endpoint). Old runtimes (PHP 7.2, Node.js 14, Java 8, .NET Standard 2.0) need the older major (1.x) of the same package: Composer picks it by the PHP version itself, npm, NuGet and Maven need it set as in installation.md. Code and setup of every package: [installation.md](references/installation.md).

| Project (detected by) | Install |
|---|---|
| Laravel (`laravel/framework` in composer.json) | `composer require unione-repo/unione-laravel` |
| Symfony (`symfony/framework-bundle` in composer.json) | `composer require unione-repo/unione-symfony-bundle` |
| PHP, other (`composer.json`) | `composer require unione-repo/unione-php-sdk` |
| Django (`django` dependency, `manage.py`) | `pip install unione-django` |
| Flask (`flask` dependency) | `pip install unione-flask` |
| FastAPI (`fastapi` dependency) | `pip install unione-fastapi` |
| Python, other (`pyproject.toml`, `requirements.txt`) | `pip install unione-sdk` |
| Express (`express` in package.json) | `npm install unione-express` |
| NestJS (`@nestjs/core` in package.json) | `npm install unione-nestjs` |
| Node.js, other (`package.json`) | `npm install unione` |
| Ruby on Rails (`rails` in Gemfile) | `bundle add unione-rails` |
| Ruby, other (`Gemfile`) | `bundle add unione` |
| Go net/http (HTTP service on `net/http`, chi or gorilla/mux) | `go get github.com/unione-repo/unione-nethttp` |
| Go, other (`go.mod`) | `go get github.com/unione-repo/unione-go-sdk` |
| Spring Boot (`spring-boot-starter-*` dependency) | Maven / Gradle `io.unione:unione-spring-boot-starter` |
| Java, other (`pom.xml`, `build.gradle`) | Maven / Gradle `io.unione:unione-java-sdk` |
| ASP.NET Core (`Microsoft.NET.Sdk.Web` in *.csproj) | `dotnet add package UniOne.AspNetCore` |
| .NET (C#), other (`*.csproj`) | `dotnet add package UniOne` |
| axum (`axum` in Cargo.toml) | `cargo add unione-axum` |
| Rust, other (`Cargo.toml`) | `cargo add unione-rust-sdk` |

### Node.js

```bash
npm install unione
```

```javascript
import { UniOneClient } from "unione";
import { MessageObjectRecipientsItem as Recipient } from "unione/api/email";

const client = new UniOneClient(process.env.UNIONE_API_KEY ?? "");

const { jobId } = await client.email.send({
  message: {
    recipients: [Recipient.fromAddress("Alex <alex@example.com>")],
    from_email: "shop@example.com",
    from_name: "Shop",
    subject: "Your order",
    body: { html: "<p>Hello, {{to_name}}! Your order has shipped.</p>" },
  },
});
console.log(jobId);
```

### Python

```bash
pip install unione-sdk
```

```python
import os

import unione
from unione.api.email import EmailSendRequest, MessageObject, MessageObjectRecipientsItem as Recipient
from unione.common import BodyObject

client = unione.client(os.environ["UNIONE_API_KEY"])

response = client.email.send(EmailSendRequest(
    message=MessageObject(
        recipients=[Recipient.from_address("Alex <alex@example.com>")],
        from_email="shop@example.com",
        from_name="Shop",
        subject="Your order",
        body=BodyObject.from_html("<p>Hello, {{to_name}}! Your order has shipped.</p>"),
    ),
))
print(response.job_id)
```

### PHP

```bash
composer require unione-repo/unione-php-sdk
```

```php
<?php

use UniOne\Api\Email\Model\EmailSendRequest;
use UniOne\Api\Email\Model\MessageObject;
use UniOne\Api\Email\Model\MessageObjectRecipientsItem as Recipient;
use UniOne\Client\ApiException;
use UniOne\Common\Model\BodyObject as Body;
use UniOne\UniOne;

$client = UniOne::client(getenv('UNIONE_API_KEY'));

try {
    $response = $client->email()->send(new EmailSendRequest(new MessageObject(
        recipients: [Recipient::fromAddress('Alex <alex@example.com>')],
        body: Body::html('<p>Hello, {{to_name}}! Your order has shipped.</p>'),
        subject: 'Your order',
        fromEmail: 'shop@example.com',
        fromName: 'Shop',
    )));

    echo $response->jobId, PHP_EOL;
} catch (ApiException $e) {
    // the message: method, API error code, HTTP status and how to fix it; kind: what failed; retryable: a repeat may succeed
    echo $e->getMessage(), PHP_EOL;
    echo $e->getKind(), ' ', $e->isRetryable() ? 'retryable' : 'not retryable', PHP_EOL;
}
```

### cURL

```bash
curl -X POST "https://api.unione.io/en/transactional/api/v1/email/send.json?platform=skill" \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $UNIONE_API_KEY" \
  -d '{"message": {"recipients": [{"email": "user@example.com", "substitutions": {"name": "Alex"}}], "body": {"html": "<p>Hello, {{name}}!</p>", "plaintext": "Hello, {{name}}!"}, "subject": "Hello", "from_email": "noreply@example.com", "from_name": "Example"}}'
```

All SDKs (PHP, Python, Node.js, Ruby, Go, Java, .NET, Rust) and the framework packages: [references/installation.md](references/installation.md). Errors of the SDKs: [Errors](#errors).

## SMTP

Prefer the Web API or a package above: they return `failed_emails` at once and send faster. Use SMTP when the
user asks for it, or the stack has no UniOne package (PHPMailer, WordPress or another CMS, a legacy app, a relay
that only speaks SMTP). Then the switch is a config change: new host and credentials, the code stays.

| Setting | Value |
|---|---|
| Host | `smtp.eu1.unione.io` or `smtp.us1.unione.io`, by the datacenter of the account (ask the user if the config does not tell) |
| Port | 587 or 25 (STARTTLS), 465 (implicit TLS); TLS 1.2+, no plain connections |
| Username | the account `user_id` (control panel, under the email in the top-left corner), or a `project_id` |
| Password | the account API key, or the project's `api_key` |

UniOne options go in one `X-UNIONE` header with JSON. Configs for Nodemailer, Django, Laravel, Symfony, Spring, Rails: [smtp.md](references/smtp.md).

## Response: check failed_emails

`email/send` answers `job_id`, `emails` (accepted) and `failed_emails` (`{address: reason}`): invalid, duplicate, unsubscribed and suppressed recipients are dropped and **the rest still get the message**. When all recipients fail, the call fails (API code 204). Delivery is reported later by [webhooks](references/webhooks.md).

## Many recipients, no batch endpoint

One call takes up to 500 `recipients`, each with its own `substitutions` and `metadata`, and each gets a separate copy. Different messages = one call each. CC / BCC: every address in `recipients`, the visible ones in `headers.To` / `headers.CC` ([sending.md](references/sending.md#cc-and-bcc)).

## Idempotence

| | |
|---|---|
| Field | `message.idempotence_key`, up to 64 chars |
| Format | `<event>-<entity-id>`, e.g. `order-confirmation-1001` |
| Window | **1 minute**: a repeat with the same key is declined |
| Longer protection | your own "sent" record per event |

Retry only retryable errors (network errors, timeouts, 429 and 5xx: the SDK error tells it) with backoff and the same key, within the minute; fix other 4xx.

## Webhooks in one paragraph

`webhook/set` registers an HTTPS endpoint for statuses (`sent`, `delivered`, `opened`, `clicked`, `unsubscribed`, `subscribed`, `soft_bounced`, `hard_bounced`, `spam`). Verify every notification: `auth` = MD5 of the raw body with the `auth` value replaced by the API key; answer 200 within 3 seconds and queue the work. Code for Node.js and Python: [references/webhooks.md](references/webhooks.md).

## What do you need?

| Task | Reference |
|---|---|
| Send email: fields, attachments, CC/BCC, scheduling, retries | [sending.md](references/sending.md) |
| Templates, substitutions, template engines, the visual editor | [templates.md](references/templates.md) |
| Delivery events, signature, retries of notifications | [webhooks.md](references/webhooks.md) |
| Sending domain (DNS, DKIM) and the sandbox domain | [domains.md](references/domains.md) |
| Suppressions and unsubscribes | [suppressions.md](references/suppressions.md) |
| Account and project API keys, projects | [projects.md](references/projects.md) |
| Install an SDK or a framework package | [installation.md](references/installation.md) |
| Send through SMTP: settings, X-UNIONE header, framework configs | [smtp.md](references/smtp.md) |
| API error codes (grep it by the code, it is long) | [errors.md](references/errors.md) |
| Every method of Email | [api/email.md](references/api/email.md) |
| Every method of Template | [api/template.md](references/api/template.md) |
| Every method of Webhook | [api/webhook.md](references/api/webhook.md) |
| Every method of Suppression | [api/suppression.md](references/api/suppression.md) |
| Every method of Domain | [api/domain.md](references/api/domain.md) |
| Every method of Confirmed email | [api/confirmed-email.md](references/api/confirmed-email.md) |
| Every method of Event-dump | [api/event-dump.md](references/api/event-dump.md) |
| Every method of Tag | [api/tag.md](references/api/tag.md) |
| Every method of Project | [api/project.md](references/api/project.md) |
| Every method of Email-validation | [api/email-validation.md](references/api/email-validation.md) |
| Every method of System | [api/system.md](references/api/system.md) |

Related skills: `unione-email-templates` (HTML and template syntax), `unione-email-best-practices` (deliverability, compliance), `unione-migrate` (from SendGrid, Mailgun, Resend, Postmark).

## Setup

- API key: control panel https://cp.unione.io/en/ → API key of the account, or of a project ([projects.md](references/projects.md)). Store it in `UNIONE_API_KEY`, never in code.
- Package: by the stack of the project ([Which package](#which-package)).
- First email without DNS: the sandbox domain ([domains.md](references/domains.md#sandbox-the-first-email-without-dns)); production: a verified domain.

## Common mistakes

| # | Mistake | Fix |
|---|---|---|
| 1 | **Retrying without `idempotence_key`** | Set it on every retryable send (`<event>-<entity-id>`); it only covers one minute — keep your own sent flag. |
| 2 | **Treating `status: success` as delivered to everyone** | Read `failed_emails`: rejected recipients are listed there while the others get the message. |
| 3 | **One API call per recipient of the same message** | Up to 500 `recipients` with per-recipient `substitutions` in one call. |
| 4 | **Template syntax does not match `template_engine`** | `simple` is the default: set `liquid` / `velocity` for `{{ x.y }}` / `$x.y` bodies, `none` for literal `{{`. |
| 5 | **Parsing the webhook JSON before checking `auth`** | Compute the MD5 over the raw body with `auth` replaced by the API key, then parse. |
| 6 | **Slow webhook handler** | Answer 200 within 3 seconds and queue the work; a failing endpoint is switched off after 24 hours. |
| 7 | **Sending from an unverified domain or the wrong subdomain** | `from_email` must be on a domain with confirmed verification and active DKIM (`domain/list`). |
| 8 | **Testing with fake addresses at real providers** | Use the sandbox domain with confirmed addresses, or your own mailboxes. |
| 9 | **Using a project key for account methods** | Projects, the sandbox domain and confirmed emails need the account key. |
| 10 | **Calling the API from the browser or a mobile app** | Server-side only; the key must never reach a client. |
| 11 | **Expecting standard headers in `headers`** | Only `X-` headers (plus `To` / `CC`) are accepted; others are ignored. |
| 12 | **`send_at` in local time or days ahead** | UTC `YYYY-MM-DD hh:mm:ss`, at most 24 hours ahead. |
| 13 | **Inventing methods or fields** | Check `references/api/*.md` or the API reference; there is no batch, CC field or inbound API. |
| 14 | **API key as the SMTP username** | The username is the `user_id` (or `project_id`), the key is the password; the host is regional: `smtp.eu1` / `smtp.us1`. |

## Errors

| HTTP | Action |
|---|---|
| 400 | Fix the request (the API code and message tell which field, e.g. a project key on an account-only method); do not retry unchanged. |
| 401 | Missing or invalid API key. |
| 403 | The account or sending is not allowed: API turned off, inactive user, daily limit, sandbox limits (1598, 1599). |
| 413 | The request is too large: ≤ 10 MB with the attachments in base64 (a third larger than the files). |
| 429 | Too many requests: retry with exponential backoff. |
| 5xx | Server error: retry with exponential backoff and the same `idempotence_key`. |

The JSON body carries `code` (API code) and `message`. To look up a code, grep [errors.md](references/errors.md) for it (e.g. `grep -n '206' references/errors.md`) instead of reading the whole table.

Every SDK throws one error class (PHP, Java, .NET: `ApiException`; Python, Node.js, Ruby: `ApiError`; Go: `*APIError`; Rust: `ApiError`) with:

- the message: the method, the API code, the HTTP status and a fix hint, ready for a log;
- kind: `api`, `network`, `timeout`, `invalid_response` (a reply that is not the API's JSON) or `invalid_request` (caught before sending: no API key, no recipients; nothing was sent);
- retryable: true for `network`, `timeout`, HTTP 429 and 5xx — retry only then, with backoff and the same `idempotence_key`;
- the HTTP status (0 when there was no HTTP response: `network`, `timeout`, `invalid_request`), the API code, the method, the hint;
- the API's own message, without decoration (PHP `getApiMessage()`, Python / Ruby `api_message`, Node.js `apiMessage`, Go `APIMessage`, Java `getApiMessage()`, .NET `ApiMessage`, Rust `api_message`), empty when there was no API response.

## Testing

Never send tests to made-up addresses at real providers (`test@gmail.com`): they bounce and hurt the reputation. Use the sandbox domain with the user's confirmed addresses, or the user's own mailboxes; ask the user for a real address before the first send.

## Resources

- [API reference](https://docs.unione.io/en/web-api-ref)
- [llms.txt](https://docs.unione.io/llms.txt), [llms-full.txt](https://docs.unione.io/llms-full.txt)
- [Control panel](https://cp.unione.io/en/)
