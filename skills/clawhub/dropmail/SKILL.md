---
name: dropmail
description: Manage disposable email addresses using GuerrillaMail. Use when a user wants to create a temporary/throwaway email address, check a disposable inbox for messages, or avoid sharing their real email with untrusted services. Triggers on the phrases "temp email", "disposable email", "temporary email", "throwaway email", or "create a burner email".
---

# DropMail Skill

Create and manage disposable email addresses via GuerrillaMail API. Emails expire after 60 minutes. All data is stored locally in SQLite at `~/.dropmail/dropmail.db`.

## What this skill accesses

Declared so its authority is reviewable before you run it — it does exactly this and no more:

- **Network:** HTTPS requests to `https://api.guerrillamail.com/ajax.php` only. No other host is contacted.
- **Filesystem:** reads and writes only under `~/.dropmail/` (the SQLite DB and `sessions.json`). Nothing else on disk is read or written.
- **No shell execution, no environment-variable reads, no credentials.** The skill runs no subprocesses and needs no API keys or secrets.

## Privacy — read before use

This skill sends inbox traffic through a **third-party service, GuerrillaMail**, and keeps mailbox state on your local disk. Before using it, understand:

- **GuerrillaMail sees everything sent to the disposable address** — full message bodies, senders, and subjects pass through their servers. Do **not** route sensitive account recovery, financial, medical, or long-lived login flows through it.
- **Received mail is cached locally.** `dropmail refresh`/`read` store full message bodies in `~/.dropmail/dropmail.db`. Disposable inboxes often carry verification codes and login links; treat that DB as sensitive and run `dropmail <email> remove` when done.
- **Session cookies are stored on disk.** Per-email `PHPSESSID` cookies live in `~/.dropmail/sessions.json`. Anyone who can read that file could reuse your mailbox session, so the files are locked down (see Security below).
- **No real identifying metadata is sent.** The client sends a fixed loopback `ip` (`127.0.0.1`) and a static browser User-Agent to satisfy the API — your real IP is not put in the request payload (your network-level source IP is still visible to GuerrillaMail, as with any HTTPS call).

## Installation

Create a symlink to `dropmail.py` on your PATH:

```bash
# System-wide
ln -s <skill-dir>/scripts/dropmail.py /usr/local/bin/dropmail

# User-local
ln -s <skill-dir>/scripts/dropmail.py ~/.local/bin/dropmail
```

Data is stored at `~/.dropmail/` (auto-created on first run). Requires Python 3.7+, no extra dependencies.

## Commands

```
dropmail new                            # Get a new disposable email
dropmail list                           # List all tracked emails with expiry status
dropmail <email> inbox                  # Show all messages in inbox
dropmail <email> inbox -c 3             # Show last 3 messages only
dropmail <email> refresh                # Fetch new messages from GuerrillaMail API
dropmail <email> read <id>              # Read full body of a message
dropmail <email> remove                 # Remove email + all messages from local DB
dropmail <email> expire                 # Show time remaining before expiry
```

## Typical Workflow

1. `dropmail new` — get a fresh email
2. Share the email address with the untrusted service
3. `dropmail <email> refresh` - pull new messages from the server
4. `dropmail <email> inbox` - browse received messages
5. `dropmail <email> read <id>` - read a specific message
6. `dropmail <email> remove` - clean up when done

## Notes

- **Data location:** All data stored in `~/.dropmail/` (DB + sessions). Auto-created on first run.
- **Sessions:** Per-email PHPSESSID cookies stored in `~/.dropmail/sessions.json`. Expire after ~18 min of API inactivity.
- **Offline inbox:** Messages are cached locally. `inbox` reads from cache; `refresh` syncs from server.
- **403 errors:** GuerrillaMail blocks non-browser User-Agents. The script uses `Mozilla/5.0` by default. If blocked, check `references/api.md`.
- **Expiry:** Emails last 60 minutes. After expiry, old messages are still accessible by calling `set_email_user` via `refresh`.

## Security

- **TLS is always verified.** API traffic uses the system CA store (falling back to `certifi` only if no system CAs exist). Verification is never disabled.
- **Local data is private.** `~/.dropmail/` is created `0700`; the SQLite DB and `sessions.json` (which holds `PHPSESSID` cookies) are `0600`, so other users on the machine can't read your sessions or cached mail.
- **Untrusted mail is sanitized.** Inbox content is attacker-controlled; terminal control/escape characters are stripped before anything is printed, preventing ANSI-escape injection into your terminal.
- **CLI input is validated** (email shape, numeric message IDs) before it reaches the DB or API.

## API Reference

For full GuerrillaMail API details, see `references/api.md`. Load it when:
- Debugging API call failures
- Adding new API features (extend, delete messages, forget)
- Understanding session/cookie handling
