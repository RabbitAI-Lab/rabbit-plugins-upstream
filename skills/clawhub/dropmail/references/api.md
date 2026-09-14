# GuerrillaMail API Reference

Base URL: `https://api.guerrillamail.com/ajax.php`

## Requirements

- All requests need params: `f` (function), `ip`, `agent` (user-agent string)
- `ip`: the API expects a client IP field. This client sends a fixed loopback value (`127.0.0.1`) — it does **not** send the end user's real IP address.
- `agent`: GuerrillaMail rejects non-browser User-Agents with 403, so the client sends a static browser UA. This is a compatibility requirement of the public API, not fingerprint evasion; no credentials or PII are attached.
- Maintain `PHPSESSID` cookie across calls — session expires after ~18 min of inactivity
- Sessions are per-email address — each address needs its own session cookie

## Functions

### `get_email_address`
Initialize session; get or create a disposable email address.

**Params:** `lang` (e.g., `en`)  
**Returns:** `email_addr`, `email_timestamp` (Unix), `s_active` (subscription Y/N)

### `set_email_user`
Switch session to a specific email username (part before @).

**Params:** `email_user` (e.g., `test` for test@guerrillamailblock.com), `lang`  
**Returns:** Same as `get_email_address`

### `check_email`
Get latest inbox messages (max 20 per call).

**Params:** `seq` (sequence/ID of oldest known email, use `0` for all)  
**Returns:**
```json
{
  "list": [
    {
      "mail_id": "12345",
      "mail_from": "sender@example.com",
      "mail_subject": "Hello",
      "mail_excerpt": "Short preview...",
      "mail_timestamp": 1776153180,
      "mail_read": 0,
      "mail_date": "14 Apr 2026 08:53"
    }
  ],
  "count": 1,
  "email": "user@guerrillamailblock.com",
  "ts": 1776153180
}
```

### `fetch_email`
Get full message body by ID.

**Params:** `email_id` (mail_id from check_email)  
**Returns:** `mail_body` (HTML), `mail_from`, `mail_subject`, `mail_date`

### `del_email`
Delete specific messages.

**Params:** `email_ids[]` (array of mail IDs)  
**Returns:** `{ "deleted_ids": [...] }`

### `forget_me`
Tell server to forget current session email (does NOT delete the address or its messages).

**Params:** (none extra)  
**Returns:** `{ "forgotten": 1 }`

### `extend`
Extend email expiry time by 60 minutes.

**Params:** (none extra)  
**Returns:** `{ "extended": 1 }`

## Email Expiry

- Each address expires 60 minutes after creation (`email_timestamp + 3600`)
- Sessions expire after ~18 minutes of inactivity (new session → new address auto-created)
- After expiry, messages are still accessible if you `set_email_user` back to the same username

## Domain

GuerrillaMail uses multiple domains. The API returns the full address including domain.
Common domain: `guerrillamailblock.com`
