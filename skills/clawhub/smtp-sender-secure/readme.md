# Zero-Exposure SMTP Mail Sender

Send emails securely without exposing SMTP passwords using MGC Blackbox.

> **This skill only executes scripts with explicit user authorization.**

---

## What This Skill Does

This is a documentation skill that teaches how to send emails securely:

1. **User stores credentials** via MGC WebUI (AI never sees)
2. **User stores email script** via WebUI or mgc_save (AI can assist)
3. **(Optional) User stores email content** via WebUI for privacy
4. **AI executes script** via mgc_get (AI only sees result)

---

## Quick Start

### Step 1: Store Credentials (via WebUI)

Open http://127.0.0.1:57218 and save:

```
info_type: "config"
info_owner: "smtp_gmail"
content: {"address": "you@gmail.com", "password": "...", "smtp_server": "smtp.gmail.com", "smtp_port": 587}
```

### Step 2: Store Email Script (via mgc_save)

```python
mgc_save(
    info_type="script",
    info_owner="send_email",
    ext01="python",
    content="your script"
)
```

### Step 3: AI Sends Email

```python
result = mgc_get(
    info_type="script",
    info_owner="send_email",
    action="run",
    ext02={"to": "to@example.com", "subject": "Test", "body": "Hello"}
)
```

---

## Security

- AI never sees credentials
- AI can assist with script writing (user stores it)
- (Optional) Email content can be stored separately for privacy
- User must approve each send

---

## MCP Tools

- mgc_save: Store scripts
- mgc_get: Execute scripts
- mgc_list: List stored items
