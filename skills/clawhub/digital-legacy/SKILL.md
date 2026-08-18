---
name: digital-legacy
description: >
  Plan what happens to your digital life if you die or become incapacitated.
  Inventory accounts, subscriptions, crypto wallets, important files, social
  media legacy contacts, and generate a sealed instruction document for
  trusted family. Includes encrypted digital will template and printable
  emergency access guide.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - estate-planning
  - digital-inheritance
  - security
  - encryption
  - emergency
  - legacy
---

# Digital Legacy

> Your digital life outlives you. Plan for it.

`Digital Legacy` is a skill that helps you create a complete digital
inheritance plan. It inventories your accounts, subscriptions, crypto wallets,
and important files; configures social media legacy contacts; and generates a
sealed, encrypted instruction document that trusted family members can access
in an emergency.

## When to Use

Activate this skill when:

- You want to create a digital will or inheritance plan
- You need to inventory online accounts and subscriptions
- You want to document crypto wallet access for heirs
- You're setting up emergency access for a trusted person
- You need a printable emergency access guide
- You're helping someone else organize their digital legacy

## What It Produces

The skill generates three deliverables:

### 1. Account Inventory (`accounts.json`)
A structured inventory of all digital accounts:
- Email, social media, banking, subscriptions
- Crypto wallets and exchange accounts
- Cloud storage and backup locations
- Domain registrations and hosting
- Status: active, dormant, to-close

### 2. Encrypted Digital Will (`digital_will.enc`)
A sealed instruction document containing:
- Access instructions (where to find passwords, recovery keys)
- Wishes for each account (archive, memorialize, delete, transfer)
- Crypto wallet seed phrases and access paths
- Location of important local files
- Contact information for services with legacy/deceased policies

Encrypted with AES-256 using a passphrase you choose. Only someone with the
passphrase can open it.

### 3. Emergency Access Guide (`emergency_guide.html`)
A printable one-page guide for your trusted person:
- The passphrase hint (NOT the passphrase itself)
- Where to find the encrypted will file
- Immediate steps to take
- Key contacts (lawyer, financial advisor, tech-savvy friend)
- Services that require death certificates

## Quick Reference

| Need                              | Command                                                              |
| --------------------------------- | -------------------------------------------------------------------- |
| Initialize a new legacy plan      | `python3 scripts/digital_legacy.py init`                             |
| Add an account                    | `python3 scripts/digital_legacy.py add-account`                      |
| Add a subscription                | `python3 scripts/digital_legacy.py add-subscription`                 |
| Add a crypto wallet               | `python3 scripts/digital_legacy.py add-wallet`                       |
| List all inventory                | `python3 scripts/digital_legacy.py list`                             |
| Generate encrypted will           | `python3 scripts/digital_legacy.py generate-will`                    |
| Generate emergency guide          | `python3 scripts/digital_legacy.py emergency-guide`                  |
| Full plan (interactive)           | `python3 scripts/digital_legacy.py setup`                            |
| Decrypt and read the will         | `python3 scripts/digital_legacy.py read-will digital_will.enc`       |

## Security Model

This skill uses a **passphrase-based encryption** model:

1. You choose a strong passphrase and give a **hint** (not the passphrase) to
   your trusted person.
2. The will document is encrypted with AES-256-GCM using a key derived from
   your passphrase via PBKDF2 (100,000 iterations).
3. The encrypted file can only be opened with the passphrase.
4. The passphrase is **never stored** anywhere in plaintext.

> **Important:** If you lose the passphrase, the encrypted will cannot be
> recovered. Store the passphrase securely (password manager + physical copy in
> a safe deposit box). See `references/security-best-practices.md`.

## Workflow

### Phase 1: Inventory (`setup` or individual `add-*` commands)

1. List all your online accounts (email, social, banking, shopping)
2. List recurring subscriptions (streaming, software, memberships)
3. Document crypto wallets (type, access method, approximate value)
4. Note important local files (taxes, deeds, insurance, will)
5. Record legacy contact settings (Google, Facebook, Apple)

### Phase 2: Specify Wishes

For each account, specify what should happen:
- **Archive**: Save data, then close
- **Memorialize**: Convert to memorial page (Facebook, Google)
- **Delete**: Close and delete all data
- **Transfer**: Transfer ownership to a specific person
- **Maintain**: Keep active (e.g., domain, email forwarding)

### Phase 3: Generate Documents

1. Run `generate-will` to create the encrypted instruction document
2. Run `emergency-guide` to create the printable HTML guide
3. Share the guide with your trusted person
4. Store the encrypted will in a location your trusted person can access

See `references/workflow-guide.md` for a detailed step-by-step process.

## Files

- `references/security-best-practices.md` — encryption, passphrase, storage
- `references/account-checklist.md` — comprehensive list of account types
- `references/platform-policies.md` — Google, Apple, Facebook, etc. legacy policies
- `references/workflow-guide.md` — full step-by-step setup process
- `scripts/digital_legacy.py` — the main inventory and encryption tool
- `scripts/templates/template_will.md` — plaintext will template
- `scripts/templates/template_guide.html` — emergency guide HTML template

## Common Pitfalls

1. **Storing the passphrase with the encrypted file.** The passphrase must be
   stored separately. If someone finds both, the encryption is useless.

2. **Forgetting to update.** Your digital life changes constantly. Re-run the
   inventory at least annually, or after major life events (new accounts,
   marriages, deaths).

3. **Not testing decryption.** After generating the will, test that you can
   decrypt it with your passphrase. A typo in the passphrase is a common,
   catastrophic error.

4. **Crypto wallet seed phrases.** Never store seed phrases in a plain text
   file. The encrypted will is acceptable, but also store a physical copy in a
   secure location (safe deposit box).

5. **Assuming family knows your accounts.** Most people have accounts their
   family doesn't know about (old email addresses, dormant exchanges, digital
   purchases). Be thorough in the inventory.

6. **Legal validity.** This tool creates an informational document, not a
   legally binding will. For legal estate planning, consult a lawyer.
   See `references/workflow-guide.md`.

## Verification Checklist

- [ ] All significant accounts inventoried (not just the ones you use daily)
- [ ] Subscriptions documented with billing cycle and cost
- [ ] Crypto wallets documented with access method (NOT seed phrase in plaintext)
- [ ] Wishes specified for each account (archive/delete/transfer/maintain)
- [ ] Will encrypted with a strong passphrase you've tested
- [ ] Passphrase stored securely (password manager + physical copy)
- [ ] Emergency guide printed and shared with trusted person
- [ ] Trusted person knows where to find the encrypted will file
- [ ] Plan reviewed and updated within the last 12 months

## License

MIT © Denis Voronin
