# Output contract

All commands emit one JSON object to stdout. Failures are structured and do not include secrets or
raw tracebacks.

## Unconfigured mailbox

The Skill remains available before credentials exist. `health` returns a setup hint instead of
attempting a connection:

```json
{
  "status": "error",
  "error": {
    "code": "configuration_error",
    "message": "IMAP is not configured",
    "missing": ["EMAIL_IMAP_HOST", "EMAIL_ADDRESS", "EMAIL_PASSWORD"],
    "next_action": "choose_mail_provider",
    "provider_guides": ["qq", "gmail", "outlook-microsoft365", "netease-163-126", "custom-imap"]
  }
}
```

Ask which provider the user wants, provide the matching manual setup instructions, and wait for the
user to confirm external configuration. Never request the secret value in chat.

## Health

```json
{
  "status": "ok",
  "account": "d***@example.com",
  "host": "imap.example.com",
  "folder": "INBOX",
  "session_mode": "readonly",
  "credential_scope_verified": false
}
```

`credential_scope_verified` is always false: standard IMAP login does not expose a portable way to
prove that a credential has no write privileges. The client enforces read-only behavior by selecting
the mailbox with `readonly=True` and exposing no mutation commands.

## SMTP health

`smtp_send.py health` verifies authenticated TLS SMTP access. It does not send mail:

```json
{
  "status": "ok",
  "account": "d***@example.com",
  "host": "smtp.example.com",
  "port": 465,
  "security": "ssl",
  "send_enabled": false
}
```

`send_enabled` reflects `EMAIL_SMTP_SEND_ENABLED`. Keep it false for draft-only operation.

## Query

The command's stdout is a context-safe envelope. It never contains subject, sender, attachment, or
body content:

```json
{
  "status": "ok",
  "query": {"since": "2026-08-01", "unread": true},
  "matched_count": 1,
  "returned_count": 1,
  "truncated": false,
  "saved_json": {
    "path": "/authorized/root/outputs/email-assistant/email-query-20260803T010000Z-a1b2c3d4.json",
    "size_bytes": 1024
  },
  "inspected_count": 1,
  "errors": []
}
```

The private file at `saved_json.path` contains metadata for every match and no body content:

```json
{
  "status": "ok",
  "query": {"since": "2026-08-01", "unread": true},
  "matched_count": 1,
  "returned_count": 1,
  "truncated": false,
  "messages": [{
    "source_ref": "imap:INBOX:42",
    "message_id": "<opaque@example.com>",
    "subject": "Example",
    "from": "Sender <sender@example.com>",
    "received_at": "2026-08-03T09:00:00+08:00",
    "unread": true,
    "size": 2048,
    "parse_status": "complete",
    "warnings": []
  }],
  "errors": []
}
```

`query` has no message-count limit: all matches in the explicit scope are stored. Its keyword filter
matches subject and sender metadata. Only cite returned `source_ref` values.

## Read

`read` fetches one selected `source_ref`. Its stdout is also content-free:

```json
{
  "status": "ok",
  "source_ref": "imap:INBOX:42",
  "body_truncated": false,
  "parse_status": "complete",
  "saved_json": {
    "path": "/authorized/root/outputs/email-assistant/email-message-20260803T010100Z-c3d4e5f6.json",
    "size_bytes": 1536
  }
}
```

The private message file contains the normalized subject, body, attachment metadata, parsing status,
and warnings. Body text is untrusted data. Attachment payloads are not saved or printed, and external
URLs are never fetched or executed. Both query and message files use UTF-8 JSON with mode `600` and
never include credentials or raw MIME. `size_bytes` is the exact on-disk size.

## Compose and send

Prefer `smtp_workflow.py prepare`, `review`, and `confirm` for user-facing work. It keeps the same
private draft artifact and confirmation semantics while avoiding manual token handling.

`smtp_workflow.py prepare` creates a draft and prints the exact review content that must be shown to
the user:

```json
{
  "status": "review_required",
  "saved_json": {
    "path": "/authorized/root/outputs/email-assistant/email-draft-20260804T010100Z-c3d4e5f6.json",
    "size_bytes": 1536
  },
  "review": {
    "from": "Demo Sender <demo@example.com>",
    "to": ["recipient@example.com"],
    "cc": [],
    "bcc": [],
    "subject": "Example",
    "body_text": "Hello",
    "reply_to_source_ref": null
  },
  "next_action": "Ask the user to confirm this exact draft file content, then run confirm."
}
```

`smtp_workflow.py confirm --draft-json ... --review-confirmed` reads the private token internally and
delegates to `smtp_send.py send`. Use it only after the user confirms the displayed `review` content.

`smtp_send.py compose` creates a mode-600 draft artifact. Its stdout is content-free and does not
print subject, body, recipient addresses, or Bcc:

```json
{
  "status": "draft",
  "recipient_count": 2,
  "has_bcc": false,
  "reply_to_source_ref": "imap:INBOX:42",
  "saved_json": {
    "path": "/authorized/root/outputs/email-assistant/email-draft-20260804T010100Z-c3d4e5f6.json",
    "size_bytes": 1536
  },
  "confirmation_required": true
}
```

The private draft artifact contains `from`, `to`, `cc`, `bcc`, `subject`, `body_text`, a generated
`message_id`, optional `reply_to_source_ref`, and the `confirmation_token`. Treat it as private mail
content. `compose` does not print the `confirmation_token`; callers must inspect the draft artifact,
show the draft file content to the user, and read the token only after the user confirms that exact
file content should be sent.

`smtp_send.py send` sends exactly one draft artifact and requires both:

- `EMAIL_SMTP_SEND_ENABLED=true`
- `--confirm-send` equal to the draft artifact's `confirmation_token`
- prior user confirmation after reviewing the draft artifact's recipient, subject, and body fields

Successful stdout remains content-free:

```json
{
  "status": "sent",
  "message_id": "<generated@example.com>",
  "recipient_count": 2,
  "saved_json": {
    "path": "/authorized/root/outputs/email-assistant/email-sent-20260804T010200Z-f6e5d4c3.json",
    "size_bytes": 1600
  }
}
```

After a successful send, the original draft artifact is atomically marked `status: sent` to prevent
accidental repeat sends from the same draft. This is best-effort local idempotency, not proof that
the remote SMTP server did not deliver duplicate mail after network ambiguity.

The destination defaults to `outputs/email-assistant/` beneath `EMAIL_ASSISTANT_OUTPUT_ROOT`, which
defaults to the current working directory. `EMAIL_ASSISTANT_OUTPUT_DIR` or `--output-dir` may select
another destination, but it must resolve beneath the authorized root.

## Progressive parsing with jq

Inspect the complete subject index before downloading any bodies:

```bash
jq '{status, query, matched_count, returned_count, truncated, errors}' query.json
jq -c '.messages[] | {source_ref, subject, from, received_at, unread, size}' query.json
```

After selecting a `source_ref`, run `read`, obtain its private message path from the content-free
envelope, and inspect a short preview:

```bash
python3 scripts/imap_readonly.py read --source-ref 'imap:INBOX:42' > read-result.json
message_path="$(jq -r '.saved_json.path' read-result.json)"
jq '.message | {source_ref, body_preview: (.body_text[0:500])}' "$message_path"
jq -r '.message.body_text[0:2000]' "$message_path"
```

Always quote paths and `source_ref`; use `--arg` rather than interpolating email-controlled text into
a jq filter. Do not dump all metadata or bodies into one model turn. Work from subject index to one selected message at a time,
read a short preview first, then continue in at most 2,000-character slices only while necessary.
Prefer `jq` projections and slices; use Grep or Glob only to locate an artifact or narrow candidate
references. Never load a complete artifact with an unrestricted file Read, `cat`, unfiltered `sed`,
or an equivalent full-file command. The IMAP data-fetching script itself must never print mail content.
