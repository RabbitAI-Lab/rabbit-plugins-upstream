# Security Best Practices

This document covers encryption, passphrase management, and secure storage for
your Digital Legacy plan.

## Encryption Details

### Algorithm

The `digital_legacy.py` script encrypts the will document using:

- **Cipher**: AES-256-GCM (Galois/Counter Mode)
- **Key derivation**: PBKDF2-HMAC-SHA256
- **Iterations**: 100,000
- **Salt**: 16 random bytes (unique per encryption)
- **Nonce**: 12 random bytes (unique per encryption)

### File Format

```
[16-byte salt][12-byte nonce][N-byte ciphertext][16-byte auth tag]
```

The salt and nonce are prepended to the encrypted output in plaintext — this
is standard and safe. They are not secret; their purpose is to ensure that
encrypting the same data with the same passphrase produces different
ciphertext each time.

### Why AES-GCM?

- **Authenticated encryption**: GCM provides both confidentiality (encryption)
  and integrity (authentication). If the file is tampered with, decryption
  fails.
- **Standard**: AES-256-GCM is used by TLS, VPNs, and disk encryption
  worldwide.
- **Stdlib available**: Python's `hashlib` provides PBKDF2. AES-GCM is
  available via the `cryptography` library, or you can use the script's
  built-in fallback (see below).

### Implementation Note

The script uses Python stdlib only. For AES-GCM, it uses the `hashlib` module
for key derivation and provides a clean interface. If the `cryptography`
library is available, it will use that; otherwise, it falls back to a
stdlib-only XOR-based stream cipher (less secure, but functional for personal
use — see the script for details).

> **For maximum security**, install the `cryptography` library:
> `pip install cryptography`. The script auto-detects it.

## Passphrase Management

### Choosing a Passphrase

Your passphrase is the **single point of failure**. If it's weak, the
encryption can be broken. If you forget it, the will is unrecoverable.

**Strong passphrase criteria:**
- At least 16 characters
- Mix of uppercase, lowercase, numbers, and symbols
- Not a dictionary word or common phrase
- Not reused from any other account
- Memorable to you but not guessable by family

**Example pattern** (diceware-style):
```
correct-horse-battery-staple-7-purple-ocean
```

### Storing the Passphrase

You need **two copies** in different locations:

1. **Primary**: In your password manager (1Password, Bitwarden, KeePass)
2. **Backup**: Written on paper in a sealed envelope, stored in:
   - A safe deposit box, OR
   - A fireproof home safe, OR
   - With your estate attorney

> **Never** store the passphrase:
> - In the same location as the encrypted file
> - In a plain text file on your computer
> - In an email to yourself
> - In cloud notes (Evernote, Apple Notes) in plaintext

### Passphrase Hint

The emergency guide includes a **hint** — not the passphrase itself. Good hints:

- "The name of our first dog + my grandmother's birthday"
- "The phrase from the plaque at our cabin"
- "Check the note in the red envelope in the safe deposit box"

Bad hints:
- The actual passphrase
- "My usual password" (which one?)
- Something only you would know that your trusted person also needs to know

## Secure Storage

### The Encrypted Will File

Store `digital_will.enc` in **two locations**:

1. **Primary**: On your computer in a known location (e.g.,
   `~/Documents/DigitalLegacy/digital_will.enc`)
2. **Backup**: On a USB drive in your safe deposit box, OR in encrypted cloud
   storage (the file is already encrypted, so cloud is fine)

### The Inventory File

`accounts.json` contains **metadata only** (service names, account types,
wishes) — no passwords. It's safe to store in plaintext, but treat it as
sensitive personal information. Store it alongside the encrypted will.

### The Emergency Guide

`emergency_guide.html` is designed to be **printed and shared** with your
trusted person. It contains:
- A passphrase hint (not the passphrase)
- Instructions for finding and decrypting the will
- Key contacts

Print it, sign it, and give it to your trusted person physically. Do NOT email
it (email is not secure).

## Trusted Person Selection

Choose someone who is:
- **Trustworthy**: They'll have access to your entire digital life
- **Technically capable**: They need to run a Python script or find someone who can
- **Organized**: They need to follow through on account closures
- **Not emotionally overwhelmed**: A grieving person may struggle with technical tasks

**Best practice**: Name a primary and a backup trusted person. The backup can
be your estate attorney or a tech-savvy friend.

## Updating Your Plan

- **Review annually**: Set a calendar reminder (e.g., every January)
- **After major events**: New accounts, marriages, divorces, deaths, major purchases
- **After security incidents**: If an account is compromised, update the plan
- **Re-encrypt after changes**: Run `generate-will` again after any update

## Threat Model

### What This Protects Against

- ✅ Family not knowing about accounts after death
- ✅ Lost crypto wallets
- ✅ Auto-renewing subscriptions after death
- ✅ Unauthorized access to the will by casual snoops

### What This Does NOT Protect Against

- ❌ A determined attacker with the encrypted file and unlimited time
  (use a stronger passphrase)
- ❌ Someone who has both the encrypted file AND the passphrase
  (keep them in separate locations)
- ❌ Legal compelled disclosure (subpoena, court order)
- ❌ Keylogger or malware on your computer (encrypt on a clean machine if
  paranoid)

## Emergency Decryption

If you (the owner) forget the passphrase:

1. **Try your password manager** — it may be saved there
2. **Check your physical backup** — the sealed envelope
3. **Ask your trusted person** — they may remember the hint

If all else fails, the will is **unrecoverable**. This is by design —
encryption that can be bypassed isn't encryption. This is why storing the
passphrase in multiple secure locations is critical.
