# Authentication Guide

This guide covers how to authenticate with an Odoo instance for both interactive (web UI) and programmatic (XML‑RPC / API key) access.

---

## 1. Logging In via the Web UI

### URL

Odoo exposes its login page at:

```
https://<your-odoo-domain>/web/login
```

Examples:

| Scenario | URL |
|---|---|
| Local development | `http://localhost:8069/web/login` |
| Production domain | `https://erp.example.com/web/login` |

### Default Credentials (Fresh Install)

A freshly provisioned Odoo instance ships with a superuser account:

| Field | Value |
|---|---|
| Database | (the database you created during init) |
| Email / Username | `admin` |
| Password | `admin` |

> **⚠️ Change this immediately after first login.** Default credentials are a well‑known attack vector.

### Changing Your Password

1. Log in with `admin` / `admin`.
2. Click your user avatar in the top‑right corner → **My Profile** (or **Preferences**).
3. In the **Change Password** section:
   - Enter your current password.
   - Enter a new, strong password (min 12 characters, mixed case + digits + symbols).
   - Confirm the new password.
4. Click **Change Password**.

You will be forced to log in again with the new credentials.

### Database Manager

If you need to create, duplicate, or drop databases, use the database manager:

```
https://<your-odoo-domain>/web/database/manager
```

Master password (set during install) may be required — never share it.

---

## 2. Creating an API Key

API keys let external systems authenticate on behalf of a user without exposing their login password.

### Step‑by‑Step

1. **Navigate to the user form**
   - Menu path: **Settings → Users & Companies → Users**
   - Select the user who needs API access (e.g. an integration service account).

2. **Open the API Keys section**
   - Scroll down to the **API Keys** tab/section (usually near the bottom of the user form).

3. **Generate a new key**
   - Click **New API Key**.
   - Optionally give the key a descriptive name (e.g. `prod-xmlrpc-2026`).

4. **Copy the key immediately**
   - Odoo displays the key **only once**. After you dismiss the dialog, it cannot be retrieved again.
   - Paste it into a secure location (1Password, Bitwarden, Vault, etc.).

5. **Save the user record**
   - Click **Save** to persist the new API key.

> **🔐 Security reminder:** Treat API keys like passwords. Never share them in plain text, commit them to version control, or log them.

---

## 3. Using the API Key with XML‑RPC

Odoo's XML‑RPC interface has two main endpoints:

| Endpoint | Purpose |
|---|---|
| `/xmlrpc/2/common` | Version info, authentication check |
| `/xmlrpc/2/object` | CRUD operations on models |

### 3.1 Verifying Credentials

```python
import xmlrpc.client

url = "https://erp.example.com"
db = "my_database"
username = "admin@example.com"
api_key = "your-api-key-here"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")

# Verify credentials — returns uid if valid
uid = common.authenticate(db, username, api_key, {})
print(f"Authenticated as uid: {uid}")
```

> If authentication fails, `authenticate()` returns `False` or raises a fault. Check your credentials and ensure the API key belongs to the specified user.

### 3.2 Performing CRUD Operations

```python
# Connect to the object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# --- Create ---
partner_id = models.execute_kw(
    db, uid, api_key,
    "res.partner", "create",
    [{"name": "Acme Corp", "email": "contact@acme.example.com"}],
)
print(f"Created partner id: {partner_id}")

# --- Read ---
partner = models.execute_kw(
    db, uid, api_key,
    "res.partner", "read",
    [[partner_id], ["name", "email"]],
)
print(f"Partner: {partner}")

# --- Update ---
models.execute_kw(
    db, uid, api_key,
    "res.partner", "write",
    [[partner_id], {"phone": "+1-555-0100"}],
)

# --- Search ---
matches = models.execute_kw(
    db, uid, api_key,
    "res.partner", "search_read",
    [[("email", "ilike", "acme")], ["name", "email"]],
    {"limit": 5},
)
print(f"Found: {matches}")
```

### 3.3 Full Working Script

```python
#!/usr/bin/env python3
"""Minimal Odoo XML-RPC example using API key authentication."""

import os
import xmlrpc.client

# Load from environment variables — never hardcode!
url = os.environ["ODOO_URL"]          # e.g. https://erp.example.com
db = os.environ["ODOO_DB"]           # e.g. my_database
username = os.environ["ODOO_USERNAME"]
api_key = os.environ["ODOO_API_KEY"]

# 1. Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, api_key, {})
if not uid:
    raise RuntimeError("Authentication failed. Check credentials.")

# 2. Connect to object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# 3. List all customers (limit 10)
customers = models.execute_kw(
    db, uid, api_key,
    "res.partner", "search_read",
    [[("customer_rank", ">", 0)], ["name", "email"]],
    {"limit": 10},
)

for c in customers:
    print(f"  {c['name']}  <{c.get('email', 'no email')}>")
```

---

## 4. Troubleshooting

| Error | Likely Cause | Fix |
|---|---|---|
| `Access Denied` | API key lacks required permissions or the user has no access rights to the model | Verify the user's access group (Settings → Users) covers the target model. Regenerate the API key if it was created under a different permission set. |
| `404 Not Found` | Wrong endpoint URL | Confirm URL ends with `/xmlrpc/2/common` or `/xmlrpc/2/object`. Watch for trailing slashes, typos, and missing `/xmlrpc/` prefix. |
| `Invalid credentials` / `authenticate()` returns `False` | Username, password, or API key mismatch | Ensure you're using the key that belongs to the specified user. Keys are per-user. Verify the correct database name. |
| `Connection refused` | Odoo service is down or a firewall blocks the port | Check that the Odoo service is running and the port (usually 443 or 8069) is reachable: `curl -I https://erp.example.com`. |
| XML-RPC returns `AccessError: Record rules` | The authenticated user cannot access specific records due to record‑level security | Ask an admin to adjust record rules or assign the user to an appropriate access group. |

---

## 5. Best Practices

- **Never hard‑code credentials.** Load them from environment variables (`os.environ["ODOO_API_KEY"]`) or a secrets manager. Never commit keys to git — add any key‑containing file to `.gitignore`.
- **Rotate API keys regularly.** Generate a new key every 90 days (or per your org's policy) and revoke the old one immediately.
- **Use dedicated service accounts.** Create a user specifically for each integration (e.g. `api-sync@example.com`) rather than sharing a personal user's key. This makes auditing and revocation clean.
- **Follow the principle of least privilege.** Grant only the access groups the integration actually needs. A key for reading contacts does not need admin rights.
- **Log and monitor.** Track which API keys are active. Revoke any that show unexpected usage patterns.
- **Use HTTPS in production.** Plain HTTP exposes credentials in transit. Always use TLS.
- **Scope API keys to the minimum model set.** If an integration only needs `res.partner`, don't grant full admin.
- **Store keys securely.** Use a password manager (1Password, Bitwarden, HashiCorp Vault) or your CI/CD secrets store. Never paste them in chat, emails, or issue trackers.

---

## Further Reading

- [Odoo External API documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html)
- [Odoo XML-RPC reference](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html#record-operations)
- [XML‑RPC library (Python stdlib)](https://docs.python.org/3/library/xmlrpc.client.html)
