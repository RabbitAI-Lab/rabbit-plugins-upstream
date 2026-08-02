---
spec: usk/3.0
id: zero_exposure_smtp_sender
version: 2.1.0
name: Zero-Exposure SMTP Mail Sender (Script-Based)
description: Send emails securely without exposing SMTP credentials. Users store email scripts in MGC, AI executes scripts via mgc_run without ever seeing credentials. Requires MGC 1.4.7+. This is a documentation skill.
author: MirginCipher Team
license: MIT
tags: security, email, smtp, mgc, zero-exposure, sandbox
platform_compatibility: windows, macos, linux
changelog:
  - version: 2.1.0
    changes:
      - Requires MGC 1.4.7+ for mgc_run support
      - Use mgc_run instead of mgc_get action="run"
  - version: 2.0.0
    changes:
      - Redesigned: script-based approach, AI never sees credentials
      - Removed MCP server, now uses MGC native tools only
      - Users store credentials via WebUI, scripts via mgc_save
  - version: 1.0.0
    changes:
      - Initial release with MCP tool
---

# Overview

**Zero-Exposure SMTP Mail Sender** is a documentation skill that teaches how to send emails securely without exposing SMTP credentials.

This skill uses **MGC Blackbox** to achieve true zero-exposure:
- Users store SMTP credentials via MGC WebUI
- Users store email scripts in MGC (AI can assist writing)
- (Optional) Users can store email content separately for privacy
- AI executes scripts via `mgc_run`
- AI **never sees** credentials or email content

---

# What This Skill Enables

After reading this documentation, you will understand how to:

- Store SMTP credentials securely via MGC WebUI
- Store email scripts in MGC
- Execute scripts via MCP tools (AI sees only results)
- Build secure email workflows

This skill **does not provide executable code**, only documentation.

---

# Prerequisites

1. **Install MGC Blackbox**: `pip install mgc-blackbox`
2. **Start MGC**: `mgc` (WebUI: http://127.0.0.1:57218, API: http://127.0.0.1:57219)
3. **MCP tools available**: mgc_save, mgc_get, mgc_list

---

# Security Model

## Traditional Approach (Unsafe)

```
AI → receives credentials → sends email
     ↓
  Credentials exposed to AI
```

## This Skill Approach (Zero-Exposure)

```
User → stores credentials (WebUI) → stores email script (mgc_save)
                                                  ↓
AI → executes script (mgc_run) → script reads credentials locally
                                                  ↓
                                    AI only sees execution result
```

AI **never** sees credentials or script content.

---

# Step 1: Store Credentials (User via WebUI)

> **Important**: Credentials must be stored by the user manually via MGC WebUI.

1. Start MGC: `mgc`
2. Open WebUI: http://127.0.0.1:57218
3. Navigate to **Save** page
4. Fill in:

```
info_type: "config"
info_owner: "smtp_gmail"  # You choose this name
content:
{
  "address": "your@gmail.com",
  "password": "app_specific_password",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587
}
```

> **Remember**: Tell AI the credential name (`info_type=config, info_owner=smtp_gmail`) but NEVER share the actual content.

---

# Step 2: Store Email Script (User via mgc_save)

Create an email script and store it in MGC:

```python
# Script: send_email.py
import smtplib
import os
import json
import requests

def get_credential():
    """Read credential from MGC local API"""
    token_path = os.path.expanduser("~/.mgc/database/mgc_black_box/.mgc_token")
    with open(token_path) as f:
        token = f.read().strip()

    # Replace with your credential name
    cred_name = os.environ.get("MGC_CRED_NAME", "smtp_gmail")

    resp = requests.post(
        "http://127.0.0.1:57219/api/mgc/sensitive/get",
        headers={"X-MGC-Token": token, "Content-Type": "application/json"},
        json={"info_type": "config", "info_owner": cred_name}
    )

    if resp.status_code == 200:
        data = resp.json()
        if data.get("code") == 200:
            data_field = data.get("data")
            if isinstance(data_field, str):
                return json.loads(data_field)
            elif isinstance(data_field, dict):
                content = data_field.get("content", "")
                if content:
                    return json.loads(content)
    return None

def send_email(to_address, subject, body):
    """Send email via SMTP"""
    cred = get_credential()
    if not cred:
        return {"success": False, "error": "Failed to get credentials"}

    try:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        msg = MIMEMultipart()
        msg['From'] = cred['address']
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        with smtplib.SMTP(cred["smtp_server"], cred["smtp_port"]) as server:
            server.starttls()
            server.login(cred["address"], cred["password"])
            server.sendmail(cred["address"], [to_address], msg.as_string())
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Get parameters from environment (passed by mgc_get ext02)
import json
params = json.loads(os.environ.get("MGC_PARAMS", "{}"))
result = send_email(
    to_address=params.get("to", ""),
    subject=params.get("subject", ""),
    body=params.get("body", "")
)
print(json.dumps(result))
```

Store the script:

```python
mgc_save(
    info_type="script",
    info_owner="send_email_script",
    ext01="python",
    ext02='{"to": "", "subject": "", "body": ""}',
    content="<paste your script here>"
)
```

---

# Step 3: AI Executes Script (Zero-Exposure)

When user wants to send an email, AI only needs to know:

- Script name: `send_email_script`
- Credential name: `smtp_gmail` (provided by user)

AI executes:

**Option A: Pass simple string ext02 (Recommended for cross-platform compatibility)**
```python
import json
ext02_str = json.dumps({"to": "recipient@example.com", "subject": "Hello", "body": "Message"})

result = mgc_get(
    info_type="script",
    info_owner="send_email_script",
    action="run",
    ext02=ext02_str  # pass as JSON string
)
```

**Option B: Pass JSON object directly (may fail on some MCP clients)**
```python
result = mgc_get(
    info_type="script",
    info_owner="send_email_script",
    action="run",
    ext02={"to": "recipient@example.com", "subject": "Hello", "body": "Message"}
)
# ⚠️ Some MCP clients may not auto-convert dict to JSON string, causing 422 error
```

**If ext02 fails, use external execution instead** (see Fallback section below).

**AI never sees:**
- SMTP credentials
- Script content
- Email implementation details

---

# Security Boundaries

## This Skill Provides

- Secure credential storage via MGC WebUI
- Script-based execution (zero-exposure)
- MCP tool integration

## This Skill Does NOT Provide

- Automated email sending
- Credential generation
- Script modification by AI (only assists writing)

## Additional Privacy Feature

Users can also store email content in MGC separately:
- Store email content as "content" info_type
- Script reads content when sending
- Even email body stays encrypted until execution

## ⚠️ Important Warnings

1. **Credentials must be stored via WebUI**: AI should not handle credentials
2. **Tell AI only credential name**: info_type and info_owner, never the content
3. **User must approve each send**: AI cannot auto-send without authorization
4. **Script content stays local**: AI only executes, never reads

---

# MCP Tools Reference

## mgc_save

**Store email script:**
```json
{
  "info_type": "script",
  "info_owner": "send_email_script",
  "ext01": "python",
  "ext02": "{\"to\": \"\", \"subject\": \"\", \"body\": \"\"}",
  "content": "your script content"
}
```

## mgc_get

**Execute email script (use JSON string for ext02 to avoid MCP client compatibility issues):**
```json
{
  "info_type": "script",
  "info_owner": "send_email_script",
  "action": "run",
  "ext02": "{\"to\": \"to@example.com\", \"subject\": \"Test\", \"body\": \"Hello\"}"
}
```

**Fallback: External execution** (if MGC internal execution fails)
If your MCP client cannot pass ext02 correctly (common with object types), you can:
1. Download the script from MGC via WebUI
2. Run it locally with: `python send_email_script.py --to user@example.com --subject "Test" --body "Hello"`
3. Script will still read credentials from MGC internally

---

# Troubleshooting

| Issue | Solution |
|-------|----------|
| Script execution fails | Check if credentials stored correctly in WebUI |
| Credential not found | Verify info_owner matches exactly |
| SMTP error | Check SMTP server/port settings |
| ext02 422 error | Use `json.dumps()` to convert to string before passing |

---

# Related Links

- **Main Repository**: https://github.com/zkeviny/MGC-Blackbox
- **Issues**: https://github.com/zkeviny/MGC-Blackbox/issues
- **Contact**: mirgincipher@outlook.com
