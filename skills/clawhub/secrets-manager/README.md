# Secrets Manager

**Encrypted local secret storage for OpenClaw agents.** AES-256-GCM authenticated encryption, rotation tracking, audit, and safe command injection.

> **TL;DR**: Secrets are encrypted at rest with AES-256-GCM. The master key is stored separately in `.master-key` (chmod 0600). If you lose `.master-key`, your secrets are unrecoverable — back it up.

## Features

- **AES-256-GCM Encryption** — secrets encrypted at rest with a 256-bit master key and per-secret random 96-bit IVs. Authenticated encryption (GCM auth tag) detects tampering.
- **Secure Storage** — `store`, `get`, `list`, `delete` lifecycle
- **Auto-Expiry & Rotation** — 90-day default rotation cycle with audit reporting
- **Safe Command Injection** — substitutes `{{placeholder}}` and writes to a private temp file (chmod 0600) by default. NEVER prints secrets to stdout unless you opt in.
- **Masked Output** — default output shows masked values (`sup****ue`)
- **Status & Audit** — health checks, expired/stale secret reporting
- **Zero External Dependencies** — pure Node.js `crypto` module

## ⚠️ Security Warnings

### Raw Mode (`--get --raw`) Prints Secrets to stdout
The secret value goes to stdout, which may be captured in:
- Shell history / terminal scrollback
- Process logs / journald / syslog
- CI/CD pipeline output
- Agent transcripts / OpenClaw session history
- Downstream tool output

Use only when piping directly to a private process or writing to a chmod-0600 file:
```bash
node secrets-manager.js --get --raw api-key > /tmp/api-key.txt && chmod 600 /tmp/api-key.txt
```

### Command Injection (`--inject`) Default: Safe
By default, `--inject` substitutes `{{secrets}}` and writes the resolved command to a temp file (chmod 0600), then prints **only the file path** to stdout. Run the command with `sh /path/to/file`.

To print the resolved command to stdout (DANGEROUS — leaks secrets to logs), use **both** flags:
```bash
node secrets-manager.js --inject-stdout --confirm-expose "curl -H 'Authorization: Bearer {{api-key}}' https://api.example.com"
```
The skill will refuse to print the resolved command unless you pass `--confirm-expose`.

### Master Key Backup
The master key lives in `memory/secrets/.master-key` (chmod 0600). If you lose this file, all stored secrets are unrecoverable. Back it up to a secure location (encrypted disk, password manager, OS keychain).

You can also use `SECRETS_MASTER_KEY=<hex>` env var instead of the file (useful for ephemeral environments).

### Not for Production Credentials (But Better Than Plain JSON)
This is a local agent tool with file-based key storage. For production-grade secret management with HSM-backed keys, audit trails, and access policies, use HashiCorp Vault, AWS Secrets Manager, etc. That said, **this skill provides real AES-256-GCM encryption** — secrets are not stored in plaintext or base64.

## Installation

```bash
# Auto-loaded by OpenClaw via the skill registry.
# For standalone use:
const SM = require('./secrets-manager.js');
SM.storeSecret('api-key', 'sk-abc123');
```

## Commands

```
store <name> <value>        Store a secret (encrypted)
get <name>                  Get secret (masked)
get <name> --raw            Get secret (⚠️ raw value to stdout)
list                        List all secret names + metadata
delete <name>               Delete a secret
rotate <name>               Generate new random value
rotate --all                Rotate all secrets
inject <command>            Substitute {{secrets}} → write to temp file (safe)
inject-stdout --confirm-expose <command>
                            Substitute and print (DANGEROUS)
audit                       Check for expired/stale secrets
status                      Show storage health
```

## API (require as module)

```javascript
const SM = require('./secrets-manager.js');

SM.storeSecret('api-key', 'sk-abc123');
const value = SM.getSecret('api-key');              // returns plaintext value
const masked = SM.getSecret('api-key');             // prints masked, returns value
SM.listSecrets();                                    // prints table
SM.deleteSecret('api-key');
SM.rotateSecret('api-key');
SM.auditSecrets('expired');
SM.showStatus();
```

## Security Architecture

- **AES-256-GCM** authenticated encryption (256-bit key, 96-bit IV per secret, 128-bit auth tag)
- **Master key** auto-generated on first `store`, stored in `memory/secrets/.master-key` (chmod 0600)
- **Per-secret IVs** — same plaintext encrypted twice produces different ciphertext
- **Auth tag verification** — tampered ciphertext returns `null` from decrypt (no partial decryption)
- **Atomic file writes** — temp file + rename to prevent corruption on crash
- **chmod 0600** on all sensitive files (POSIX)
- **No external dependencies** — pure Node.js `crypto`

## Data Layout

```
memory/secrets/
  .master-key       # 32 random bytes as hex, chmod 0600
  secrets.json      # { name: { iv, ct, tag, created, updated, ... } }, chmod 0600
  permissions.json  # Per-secret access rules (optional), chmod 0600
```

## Testing

```bash
# Self-test suite (isolated temp directory)
node tests/run-self-tests.js

# Quick smoke test
node test/run-tests.js
```

### Test Coverage

| Suite | Tests | Status |
|---|---|---|
| Self-tests (isolated) | 29 | ✅ Passing |
| Quick tests | 9 | ✅ Passing |

## Examples

**Store an API key:**
```javascript
SM.storeSecret('github-token', 'ghp_abc123...');
```

**Get for use in a script:**
```javascript
const key = SM.getSecret('github-token');  // returns plaintext (handle carefully)
```

**Audit for expired secrets:**
```javascript
SM.auditSecrets('expired');
```

**Rotate all secrets:**
```javascript
SM.rotateAllSecrets();
```

**Inject into a command (safe):**
```bash
$ node secrets-manager.js --inject "curl -H 'Authorization: Bearer {{api-key}}' https://api.example.com"
[secrets-manager] ✅ Injected 1 secret(s) into: /tmp/secrets-inject-12345-1234567890.sh
[secrets-manager]    Run with: sh /tmp/secrets-inject-12345-1234567890.sh
$ sh /tmp/secrets-inject-12345-1234567890.sh
# ... command output ...
```
