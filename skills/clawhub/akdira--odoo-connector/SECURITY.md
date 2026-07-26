# Security Policy

This document outlines security best practices for using the Odoo Connector skill and reports vulnerabilities responsibly.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x | ✅ Yes |

## Reporting a Vulnerability

If you discover a security vulnerability in this skill (not in Odoo itself), please report it privately:

1. **Do not open a public issue** describing the vulnerability
2. Open a GitHub Security Advisory, or email the maintainer directly
3. Include steps to reproduce, affected versions, and potential impact
4. Allow reasonable time for a fix before public disclosure

For vulnerabilities in **Odoo itself**, report directly to the Odoo security team through their official channels.

## Best Practices for Users

### Credential Management

**Never commit credentials to version control.** This is the most critical rule.

✅ **Do:**
```python
import os
password = os.environ.get("ODOO_PASSWORD")
```

❌ **Don't:**
```python
password = "my_secret_password"  # COMMITTED TO GIT
```

Use one of these approaches:

1. **Environment variables** — Simple and widely supported
2. **`.env` files** — With `.env` in `.gitignore` (never commit)
3. **Secrets manager** — AWS Secrets Manager, HashiCorp Vault, etc.
4. **Docker secrets** — For containerized deployments

### API Keys Over Passwords

Always prefer Odoo API keys over user passwords:

- API keys can be revoked individually without affecting the user account
- API keys can be scoped to specific operations
- API keys are auditable (you can see when they were created and last used)
- If compromised, only the API key needs rotation, not the entire user account

To generate an API key in Odoo:
1. Log in as the API user
2. Go to Settings → Users → your user → API Keys tab
3. Create a new key with a descriptive name
4. Store securely and use as the password parameter

### Least Privilege Principle

Create dedicated service accounts with minimal required permissions:

- **Read-only integrations** — Use a user with only Read access to needed models
- **Write integrations** — Grant Create/Write but not Unlink (delete) unless necessary
- **Admin operations** — Reserve admin accounts for setup only, not daily API use

Do not use the admin account (UID 1/2) for API operations in production. Create a dedicated integration user:

1. Settings → Users → Create
2. Name: "API Integration - OpenClaw"
3. Set only the required access rights
4. Generate an API key for this user
5. Use these credentials in your configuration

### Network Security

1. **Always use HTTPS** — XML-RPC transmits credentials in the request body. Over HTTP, these are visible to anyone on the network.

2. **Restrict IP access** — If your Odoo instance is publicly accessible, consider:
   - Allowing API access only from specific IP addresses through your reverse proxy or firewall
   - Using a VPN for API access from external systems

3. **Reverse proxy configuration** — Ensure your proxy (nginx, Traefik, Caddy):
   - Enforces HTTPS with valid certificates
   - Has appropriate timeout settings (to prevent slow-loris attacks)
   - Limits request body size (to prevent abuse)
   - Logs API access for audit purposes

4. **TLS certificates** — Use valid certificates (Let's Encrypt is free and automatic). Never disable certificate verification in production.

### Data Validation

Always validate data before writing to Odoo:

```python
# Validate before create
def safe_create_partner(models, db, uid, password, data):
    """Create a partner with input validation."""
    # Validate email format
    email = data.get('email', '')
    if email and '@' not in email:
        raise ValueError(f"Invalid email: {email}")

    # Validate required fields
    if not data.get('name'):
        raise ValueError("Partner name is required")

    # Sanitize inputs (remove control characters)
    for key in data:
        if isinstance(data[key], str):
            data[key] = data[key].strip()

    return models.execute_kw(
        db, uid, password,
        'res.partner', 'create',
        [data]
    )
```

### Audit Logging

Log all API operations for security auditing:

```python
import logging

logger = logging.getLogger('odoo_audit')

def audited_create(models, db, uid, password, model, values):
    """Create with audit logging."""
    logger.info(f"CREATE {model} | user={uid} | data_keys={list(values.keys())}")
    try:
        record_id = models.execute_kw(db, uid, password, model, 'create', [values])
        logger.info(f"CREATED {model} id={record_id}")
        return record_id
    except Exception as e:
        logger.error(f"CREATE FAILED {model} | error={str(e)[:200]}")
        raise
```

### Token and Session Hygiene

- Rotate API keys periodically (every 90 days recommended)
- Remove unused API keys immediately
- Do not share API keys between different integrations
- Use different API keys for development, staging, and production
- Monitor Odoo login logs for suspicious authentication attempts

## Security Checklist

Before deploying an Odoo integration to production:

- [ ] No credentials in source code or committed files
- [ ] Using API keys instead of passwords
- [ ] Service account has least-privilege access
- [ ] All communication over HTTPS with valid certificates
- [ ] Input validation on all user-provided data
- [ ] Audit logging enabled for API operations
- [ ] IP restrictions configured (if publicly accessible)
- [ ] API keys rotated regularly
- [ ] Connection test script passing
- [ ] Documentation reviewed for accidental credential exposure
