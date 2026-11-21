# SMTP

Host `smtp.eu1.unione.io` or `smtp.us1.unione.io` (the datacenter of the account; the configs below use `smtp.eu1.unione.io`),
port 587 or 25 (STARTTLS) or 465 (implicit TLS); TLS 1.2+, no plain connections. Username: the account `user_id` or a
`project_id`; password: the account API key or the project's `api_key`. Keep them in `UNIONE_USER_ID` and `UNIONE_API_KEY`
(a DSN needs them URL-encoded).

## Configs

```javascript
// Nodemailer
const transporter = nodemailer.createTransport({
  host: "smtp.eu1.unione.io", port: 587, secure: false,
  auth: { user: process.env.UNIONE_USER_ID, pass: process.env.UNIONE_API_KEY },
});
```

```python
# Django settings.py
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.eu1.unione.io"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ["UNIONE_USER_ID"]
EMAIL_HOST_PASSWORD = os.environ["UNIONE_API_KEY"]
```

```dotenv
# Laravel .env
MAIL_MAILER=smtp
MAIL_HOST=smtp.eu1.unione.io
MAIL_PORT=587
MAIL_USERNAME="${UNIONE_USER_ID}"
MAIL_PASSWORD="${UNIONE_API_KEY}"
```

```yaml
# Symfony config/packages/mailer.yaml
framework:
  mailer:
    dsn: 'smtp://%env(UNIONE_USER_ID)%:%env(UNIONE_API_KEY)%@smtp.eu1.unione.io:587'
```

```properties
# Spring application.properties
spring.mail.host=smtp.eu1.unione.io
spring.mail.port=587
spring.mail.username=${UNIONE_USER_ID}
spring.mail.password=${UNIONE_API_KEY}
spring.mail.properties.mail.smtp.auth=true
spring.mail.properties.mail.smtp.starttls.enable=true
```

```ruby
# Rails config/environments/production.rb
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  address: "smtp.eu1.unione.io", port: 587, authentication: :plain, enable_starttls_auto: true,
  user_name: ENV["UNIONE_USER_ID"], password: ENV["UNIONE_API_KEY"],
}
```

## X-UNIONE header

UniOne options of `email/send` go in one header with JSON: `template_engine` (`simple`, `velocity`, `liquid` or
`none`), `template_id`, `global_substitutions`, `global_metadata` (comes back in webhooks), `tags`, `track_links`,
`track_read`, `global_language` (of the unsubscribe footer), `idempotence_key` (as in `email/send`: a repeat within a
minute is declined).

```
X-UNIONE: {"global_metadata": {"order_id": "1001"}, "global_substitutions": {"name": "Alex"}}
```

Encode headers with non-ASCII characters by MIME (e.g. `mb_encode_mimeheader` in PHP).

## Differences from the Web API

- No `failed_emails` in the answer: rejected recipients show up only in webhooks and event dumps.
- Every address in `To`, `CC` and `BCC` gets its own copy (billed separately), with only its address in `To`.
  To keep `To` and `CC` as written, pass `"strict": true` in `X-UNIONE`; up to 10 addresses in `CC` and in `BCC`,
  `BCC` only on your verified domains.
- The answer of the server carries the message id: it is the `job_id` in webhooks.
- Throughput: up to 5,000 emails an hour per connection, at most 10 connections. For more use the Web API.
- The unsubscribe link is added as with the API.
