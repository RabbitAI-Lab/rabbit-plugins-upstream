# Zero-Exposure SMTP Email Script Template
# This is the script content to be stored in MGC via mgc_save
# Users should customize this script and store it themselves

import smtplib
import os
import json
import requests

# ========== Configuration ==========
# Replace these with your credential names (info_owner)
SMTP_CREDENTIAL_NAME = "smtp_gmail"      # SMTP credentials
EMAIL_CONTENT_NAME = "email_template_001"  # (Optional) Email content stored in MGC

def get_credential(cred_name):
    """Read credential from MGC local API"""
    token_path = os.path.expanduser("~/.mgc/database/mgc_black_box/.mgc_token")
    if not os.path.exists(token_path):
        return None

    with open(token_path) as f:
        token = f.read().strip()

    resp = requests.post(
        "http://127.0.0.1:57219/api/mgc/sensitive/get",
        headers={
            "X-MGC-Token": token,
            "Content-Type": "application/json"
        },
        json={
            "info_type": "config",
            "info_owner": cred_name
        }
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

def get_email_content(content_name):
    """Read email content from MGC (optional privacy feature)"""
    token_path = os.path.expanduser("~/.mgc/database/mgc_black_box/.mgc_token")
    if not os.path.exists(token_path):
        return None

    with open(token_path) as f:
        token = f.read().strip()

    resp = requests.post(
        "http://127.0.0.1:57219/api/mgc/sensitive/get",
        headers={
            "X-MGC-Token": token,
            "Content-Type": "application/json"
        },
        json={
            "info_type": "content",  # or "prompt", etc.
            "info_owner": content_name
        }
    )

    if resp.status_code == 200:
        data = resp.json()
        if data.get("code") == 200:
            data_field = data.get("data")
            if isinstance(data_field, str):
                return data_field
            elif isinstance(data_field, dict):
                return data_field.get("content", "")
    return None

def send_email(to_address, subject, body, use_stored_content=False):
    """Send email via SMTP"""
    cred = get_credential(SMTP_CREDENTIAL_NAME)
    if not cred:
        return {"success": False, "error": "Failed to get SMTP credentials"}

    # If privacy mode: read email content from MGC
    if use_stored_content:
        stored_content = get_email_content(EMAIL_CONTENT_NAME)
        if stored_content:
            # Parse stored content (e.g., JSON or plain text)
            try:
                content_data = json.loads(stored_content)
                subject = content_data.get("subject", subject)
                body = content_data.get("body", body)
            except:
                # If not JSON, treat as body
                body = stored_content

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
        return {"success": True, "message": "Email sent successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}

# ========== Main ==========
# Get parameters from MGC (passed via ext02)
params = json.loads(os.environ.get("MGC_PARAMS", "{}"))

# Determine if using stored content for privacy
use_stored = params.get("use_stored_content", False)

result = send_email(
    to_address=params.get("to", ""),
    subject=params.get("subject", ""),
    body=params.get("body", ""),
    use_stored_content=use_stored
)

print(json.dumps(result))
