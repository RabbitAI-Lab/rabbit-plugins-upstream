---
name: maddy-mail
description: Use Maddy's native CLI over SSH plus SMTP submission to list, read, send, add, and delete mail on trusted self-hosted Maddy servers. Prefer this over generic IMAP clients when Maddy is under your control and CLI access is authorized.
metadata:
  openclaw:
    requires:
      bins: ["ssh", "python3"]
---

# Maddy Mail

Use this skill for trusted self-hosted Maddy mailboxes where the operator has SSH access to the Maddy host and authorization to run `maddy imap-msgs` as the `maddy` user.

Do **not** use this pattern for third-party mailboxes or servers where admin-level mailbox access is not explicitly authorized.

## Helper script

This skill includes `scripts/maddy-mail`, a Python helper that:

- lists mailbox messages with `maddy imap-msgs list`
- reads raw messages with `maddy imap-msgs dump --uid`
- extracts a plain-text body for agent-friendly reading
- adds a raw message to a mailbox with `maddy imap-msgs add`
- deletes by UID with `maddy imap-msgs remove --uid --yes`
- sends mail via SMTP STARTTLS using Python `smtplib`
- runs a safe `selftest` that sends a disposable self-addressed message, waits for delivery, reads it, deletes it, and verifies removal

Install locally if needed:

```bash
install -m 755 scripts/maddy-mail ~/.local/bin/maddy-mail
```

## Config

Default config path:

```bash
~/.config/maddy-mail/config.json
```

Override with `MADDY_MAIL_CONFIG=/path/to/config.json`.

Example:

```json
{
  "ssh_host": "mail-host",
  "maddy_path": "/usr/local/bin/maddy",
  "default_account": "mail",
  "accounts": {
    "mail": {
      "email": "mail@example.com",
      "smtp_host": "mail.example.com",
      "smtp_port": 587,
      "password_cmd": ["cat", "~/.config/maddy-mail/mail.pass"]
    }
  }
}
```

`password_cmd` runs without a shell, as an argv list or as a string split like shell words. A leading `~` is expanded. To use a pipeline or a password manager CLI, put it in a small script and point `password_cmd` at that script.

Keep password files out of git and mode `0600`. SMTP submission uses STARTTLS and verifies the server certificate; trust a private CA through the system store rather than turning verification off.

## Common commands

List:

```bash
maddy-mail list
maddy-mail list --json
```

Read UID 3 without relying on IMAP client parsing:

```bash
maddy-mail read 3
maddy-mail read 3 --raw
```

Send from the configured account:

```bash
printf 'Hello from Maddy.\n' | maddy-mail send --to user@example.com --subject 'Test'
```

Add a raw RFC 5322 message to a mailbox:

```bash
cat message.eml | maddy-mail add --folder INBOX
```

Delete a specific UID:

```bash
maddy-mail delete 4 --yes
```

Full safe smoke test:

```bash
maddy-mail selftest
```

## Operational guidance

- Prefer UIDs, not sequence numbers. The helper uses `--uid` for read/delete.
- For destructive operations, delete only messages created for the test or explicitly identified by the user.
- If `list` and `read` disagree, trust Maddy's native CLI over generic IMAP client output.
- If SMTP send fails, check Maddy logs and DNS/PTR/SPF/DKIM/DMARC before blaming the helper.
- For remote production hosts, avoid bulk loops; batch reads/lists and serialize writes/deletes.
