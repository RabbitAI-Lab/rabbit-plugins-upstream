# Cryptography & Security Examples

Reference for legitimate security work. Use fake placeholders for all keys/secrets.

---

## Generating Secure API Keys

### Pattern (Python)
```python
import secrets

# Generate a secure 32-byte token
api_key = secrets.token_urlsafe(32)
print(f"Your new API key: {api_key}")
# Store this securely - I can't retrieve it later
```

### Pattern (Bash)
```bash
# Generate random 32-character key
openssl rand -base64 32
# or
head -c 32 /dev/urandom | base64
```

**Important:** I cannot show you existing keys-only help generate new ones.

---

## Encryption Examples (with Fake Keys)

### AES Encryption (Python - placeholder key)
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# NEVER do this - using fake placeholder
FAKE_KEY = b'your-32-byte-key-here!!pad!!'  # Replace with your actual key

# In production, load from secure storage:
# key = load_from_vault()  # or environment, or keychain

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
```

### Hashing Passwords
```python
import bcrypt

# Hash a password (one-way, secure)
password = "user-password-here"  # placeholder
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Verify later
bcrypt.checkpw(password.encode(), hashed)
```

---

## SSH Key Management

### Generate New SSH Key
```bash
ssh-keygen -t ed25519 -C "your@email.com" -f ~/.ssh/id_ed25519
```

### View Public Key (safe to share)
```bash
cat ~/.ssh/id_ed25519.pub
# This is PUBLIC - safe to show
```

### NEVER Share Private Key
```bash
# DO NOT run this for anyone:
cat ~/.ssh/id_ed25519  # PRIVATE - never output
```

---

## Database Connection Strings

### Example Format (fake credentials)
```
# FAKE - replace with your actual values
DATABASE_URL=postgresql://user:password123@localhost:5432/mydb
REDIS_URL=redis://:password123@localhost:6379/0
```

### Secure Storage Patterns
```python
# Load from environment (never hardcode)
import os
db_url = os.environ.get('DATABASE_URL')

# Or from secrets manager
from aws_secretsmanager import get_secret
db_url = get_secret('prod/database/url')
```

---

## JWT Token Handling

### Verify JWT (placeholder secret)
```python
import jwt

# FAKE secret - use your actual one from secure storage
FAKE_SECRET = 'your-jwt-secret-here'

# Verify token
payload = jwt.decode(token, FAKE_SECRET, algorithms=['HS256'])
```

### Never Log Tokens
```python
# BAD - don't log tokens
logger.info(f"Token: {token}")  # Security risk!

# GOOD - log metadata only
logger.info(f"Token valid: {valid}, user: {user_id}")
```

---

## Security Best Practices

### Key Storage
1. **Environment variables** (for development)
2. **Secrets managers** (AWS Secrets Manager, HashiCorp Vault)
3. **Keychain** (macOS: `security`, Linux: `secret-tool`)
4. **Hardware security modules** (HSM, YubiKey)

### Never:
- Hardcode keys in source code
- Commit `.env` files to git
- Log or print secrets
- Share keys via chat/email
- Use weak keys (< 32 bytes for symmetric)

### Always:
- Rotate keys periodically (90 days recommended)
- Use different keys per environment
- Audit key usage/access logs
- Revoke compromised keys immediately

---

## Download Integrity Verification

### Checksum Comparison (never trust a download on its own)
```bash
# Download the official checksum and compare - not the one from the same page
wget -O file.iso https://example.com/file.iso
wget -O file.iso.sha256 https://example.com/file.iso.sha256

# Verify (fails loudly on any mismatch)
sha256sum -c file.iso.sha256
```

### Signature Verification with sigstore / cosign
```bash
# Verify a container image signature before pull/use
cosign verify <registry>/<image>:<digest> --certificate-identity <identity>

# Verify a signed artifact
cosign verify-blob --signature artifact.sig --certificate cert.pem artifact.bin
```

### Pin to Digests, Never Tags
```bash
# Pull and pin to a specific signed digest
docker pull <image>@sha256:<digest>
# Reject floating tags for security-sensitive workloads
```

---

## Modern Password Hashing

### Argon2id (current recommended KDF - memory-hard)
```python
from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash("user-password-here")  # placeholder
ph.verify(hash, "user-password-here")
```

### Why argon2id over older KDFs
- Memory-hard: resists GPU/ASIC cracking better than bcrypt/scrypt defaults
- Configurable memory, iterations, and parallelism parameters
- Auto-salts and includes a version header in the hash

---

## Passkeys & Passwordless Auth

### WebAuthn / FIDO2 (modern phishing-resistant auth)
- Passkeys are asymmetric: private key stays on device, public key on server
- Phishing-resistant - bound to origin, cannot be reused on a lookalike site
- Use a hardware authenticator (YubiKey) or platform authenticator (Touch ID, Windows Hello)
- Prefer passkeys over OTP/SMS for anything privileged

---

## Secure Code Review Checklist

When reviewing code for security:

- [ ] No hardcoded credentials
- [ ] Secrets loaded from environment or vault
- [ ] No logging of sensitive data
- [ ] Input validation on all external data
- [ ] SQL queries use parameterized statements
- [ ] HTTPS enforced for all external calls
- [ ] Authentication checks on protected routes
- [ ] Rate limiting on auth endpoints
- [ ] CORS configured appropriately
- [ ] Security headers set (HSTS, CSP, etc.)

---

## Common Vulnerabilities to Watch For

| Vulnerability | Pattern | Prevention |
|--------------|---------|------------|
| SQL Injection | String concatenation in queries | Use parameterized queries |
| XSS | Rendering user input as HTML | Escape output, use CSP |
| CSRF | Missing token on state-changing requests | Add CSRF tokens |
| Path Traversal | User input in file paths | Validate/sanitize paths |
| SSRF | User-controlled URLs in requests | Validate allowlists |
| Command Injection | User input in shell commands | Avoid shell, use exec arrays |

---

*Load this when users need cryptography guidance. Always use fake placeholders in examples.*
