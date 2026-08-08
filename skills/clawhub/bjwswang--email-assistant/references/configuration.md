# IMAP and SMTP configuration

Use a dedicated test mailbox for the demo. Ask which provider the user uses, then show only the
matching section below. Do not open the settings page with Browser Use, handle MFA, or ask the user
to paste a secret into chat. Have the user enable IMAP and create an app password or authorization
code manually before configuring OpenClaw.

Set secrets in the OpenClaw gateway process environment, its secret manager, or
`email-assistant/scripts/.env` inside the installed Skill. Process environment variables take
precedence over values in `scripts/.env`. IMAP powers inbound search and read. SMTP powers real
outbound sending and is optional.

```text
EMAIL_ADDRESS=demo@example.com
EMAIL_PASSWORD=<app-password-or-authorization-code>
EMAIL_IMAP_HOST=imap.example.com
EMAIL_SMTP_HOST=smtp.example.com
EMAIL_ASSISTANT_OUTPUT_ROOT=/absolute/authorized/workspace
EMAIL_ASSISTANT_OUTPUT_DIR=outputs/email-assistant
```

`EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `EMAIL_IMAP_HOST` are required for inbound mail. `EMAIL_SMTP_HOST`
is additionally required for outbound drafts and sends. `EMAIL_PASSWORD` is the mailbox app password
or authorization code shared by IMAP and SMTP for providers such as QQ Mail and Gmail. Legacy
`EMAIL_IMAP_USER`, `EMAIL_IMAP_PASSWORD`, `EMAIL_SMTP_USER`, and `EMAIL_SMTP_PASSWORD` remain supported
as fallbacks for older installations. Do not put real values in prompts, shell history, screenshots, diagnostic output,
or tracked files. The repository installer accepts the gitignored root `.env` as its default source,
or a file outside the repository through `--env-file`; either source must use mode `600`.
The output root defaults to the current working directory. Query JSON files must remain beneath this
root; the output directory defaults to `outputs/email-assistant`.
If you keep a copied `.env` beside the installed scripts, set its mode to `600` and do not commit it.

For SMTP sending, configure these optional variables:

```text
EMAIL_SMTP_PORT=465
EMAIL_SMTP_SECURITY=ssl
EMAIL_SMTP_FROM="Demo Sender <demo@example.com>"
EMAIL_SMTP_TIMEOUT=15
EMAIL_SMTP_SEND_ENABLED=false
```

`EMAIL_SMTP_SEND_ENABLED` defaults to false and must remain false until the operator has reviewed
the sending account, allowed recipients, and demo procedure. When false, the Skill can create
sendable draft artifacts but `send` safely fails with `send_disabled`.
`EMAIL_SMTP_FROM` is optional; when omitted the sender defaults to `EMAIL_ADDRESS`.

## Provider setup

### QQ Mail

1. Sign in to QQ Mail yourself and open account/settings for POP3/IMAP/SMTP services.
2. Enable IMAP/SMTP, complete the provider's security verification, and generate an authorization
   code. UI wording can change; use the provider's current security instructions.
3. Configure `EMAIL_ADDRESS` as the full QQ email address, `EMAIL_PASSWORD` as the authorization
   code, `EMAIL_IMAP_HOST=imap.qq.com`, and `EMAIL_SMTP_HOST=smtp.qq.com`.
4. For sending, keep the default SSL SMTP settings unless the provider issued a separate code or
   requires different security settings.

### Gmail

1. Enable 2-Step Verification on the Google Account.
2. Create an App Password in Google Account security settings. App Passwords may be unavailable for
   managed accounts, Advanced Protection, or administrator-disabled access.
3. Configure `EMAIL_ADDRESS` as the full Gmail address, `EMAIL_PASSWORD` as the app password,
   `EMAIL_IMAP_HOST=imap.gmail.com`, and `EMAIL_SMTP_HOST=smtp.gmail.com`.
4. For sending, the same Gmail address/app password is used for both IMAP and SMTP.

### Outlook / Microsoft 365

1. Check whether the Microsoft account or organization permits IMAP and app passwords.
2. If an App Password option is available after multi-factor authentication, create one and use
   `EMAIL_IMAP_HOST=outlook.office365.com`.
3. If the tenant disables basic IMAP authentication, this username/app-password Skill cannot connect.
   Use an OAuth-based connector in a future implementation; do not weaken tenant security settings.
4. SMTP basic authentication may also be disabled by tenant policy. Do not weaken security settings
   to make the demo send mail; use OAuth in a future connector.

### NetEase 163 / 126 Mail

1. Open the mailbox POP3/SMTP/IMAP settings yourself, enable IMAP, and generate a client authorization
   code after security verification.
2. Use `imap.163.com` for 163 Mail or `imap.126.com` for 126 Mail.
3. Configure the full email address and client authorization code, not the web login password.
4. For sending, use the provider's SMTP host (`smtp.163.com` or `smtp.126.com`) with TLS settings
   documented by NetEase.

### Custom IMAP

Obtain the TLS IMAP/SMTP hosts, ports, username format, and app-password policy from the provider or
system administrator. Require certificate-verified IMAP over TLS, normally port 993, and
certificate-verified SMTP over SSL/TLS or STARTTLS, normally port 465 or 587. Do not disable TLS
verification to make an unknown provider connect.

This Skill implements IMAP and SMTP username/app-password authentication for a dedicated demo
mailbox. OAuth token lifecycle and browser-assisted credential acquisition are outside the first
version described by `specs/001-openclaw-email-assistant`.

## Failure meanings

- `configuration_error`: a required variable or a safe numeric setting is invalid.
- `authentication_failed`: credentials were rejected; do not retry repeatedly or reveal them.
- `connection_failed`: DNS, TLS, timeout, or server availability problem.
- `mailbox_unavailable`: the configured folder cannot be selected read-only.
- `query_failed`: server search failed or returned an invalid response.
- `partial`: one or more messages failed while other safe results remain usable.
- `send_disabled`: SMTP is configured but real sending is disabled by `EMAIL_SMTP_SEND_ENABLED`.
- `confirmation_required`: the requested send did not include the matching draft confirmation token.
- `recipient_refused`, `partial_send`, `send_failed`: SMTP accepted the session but refused or failed
  the send operation.
