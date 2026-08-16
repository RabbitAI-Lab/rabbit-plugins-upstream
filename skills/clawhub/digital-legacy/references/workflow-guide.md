# Workflow Guide — Full Setup Process

This guide walks you through creating a complete digital legacy plan from
scratch. Allow 2-4 hours for the first setup.

## Phase 1: Preparation (15 minutes)

### Gather what you'll need

- [ ] List of your devices (phone, laptop, tablet) and their passcodes
- [ ] Access to your email accounts
- [ ] Your password manager open
- [ ] A notebook for brainstorming (you'll remember accounts as you go)
- [ ] 2-4 hours of uninterrupted time

### Choose your trusted person

- Primary: _______________
- Backup: _______________

They should be:
- Trustworthy and organized
- Technically capable (or know someone who is)
- Not likely to predecease you
- Emotionally able to handle the task

## Phase 2: Inventory (60-90 minutes)

### Step 1: Initialize the plan

```bash
python3 scripts/digital_legacy.py init
```

### Step 2: Email accounts (highest priority)

Email is the master key to resetting all other passwords.

```bash
python3 scripts/digital_legacy.py add-account
# Service: Gmail
# Type: email
# Access: password manager
```

Document ALL email addresses you have, including old ones.

### Step 3: Financial accounts

Go through:
- Bank accounts
- Credit cards
- Investment/brokerage
- PayPal, Venmo, Cash App
- Insurance portals
- Tax software

```bash
python3 scripts/digital_legacy.py add-account
# Service: Chase Bank
# Type: banking
# Access: password manager + 2FA app
```

### Step 4: Subscriptions

List everything that bills you monthly or annually:

```bash
python3 scripts/digital_legacy.py add-subscription
# Service: Netflix
# Cost: 15.99
# Cycle: monthly
# Action: cancel
```

Check your credit card statements for the last 3 months to find subscriptions
you forgot about.

### Step 5: Crypto wallets

For each wallet, document the TYPE and ACCESS METHOD (not the seed phrase
itself in plaintext):

```bash
python3 scripts/digital_legacy.py add-wallet
# Type: hardware (Ledger)
# Access: seed phrase in safe deposit box, PIN written on card in safe
# Value: approximately $___
```

### Step 6: Social media

For each platform, check if legacy features exist and set them up:

```bash
python3 scripts/digital_legacy.py add-account
# Service: Facebook
# Type: social
# Access: password manager
# Legacy: Legacy Contact set (Mom)
# Action: memorialize
```

**Do this now**: Set up Google Inactive Account Manager and Apple Legacy
Contact while you're thinking about it.

### Step 7: Cloud storage & important files

Document where important files live:

```bash
python3 scripts/digital_legacy.py add-account
# Service: Google Drive
# Type: cloud-storage
# Access: password manager
# Contents: tax returns, insurance docs, scanned deeds
```

Also note local files:
```bash
python3 scripts/digital_legacy.py add-account
# Service: Local Files
# Type: local
# Access: laptop login password + FileVault recovery key
# Contents: ~/Documents/Important/ — will, insurance, taxes
```

### Step 8: Review the checklist

Open `references/account-checklist.md` and go through every category. Add any
accounts you missed.

### Step 9: Verify inventory

```bash
python3 scripts/digital_legacy.py list
```

Review the full list. Are there accounts you forgot? Add them now.

## Phase 3: Specify Wishes (30 minutes)

For each account, decide what should happen:

| Wish          | When to Choose                            |
| ------------- | ----------------------------------------- |
| Archive       | Save data before closing (photos, docs)   |
| Memorialize   | Social media (Facebook, Instagram)        |
| Delete        | Close and delete all data                 |
| Transfer      | Give to a specific person (domains, etc.) |
| Maintain      | Keep active (domain, email forwarding)    |

Update each account's action:
```bash
python3 scripts/digital_legacy.py add-account  # re-add with updated info
```

## Phase 4: Generate Documents (15 minutes)

### Step 1: Choose a passphrase

Choose a strong passphrase (see `references/security-best-practices.md`).
Write it down on paper now — you'll need it.

### Step 2: Generate the encrypted will

```bash
python3 scripts/digital_legacy.py generate-will
```

The script will:
1. Compile all inventory and wishes into a will document
2. Prompt for your passphrase
3. Encrypt with AES-256-GCM
4. Write `digital_will.enc`

### Step 3: TEST decryption

```bash
python3 scripts/digital_legacy.py read-will digital_will.enc
```

Enter your passphrase. If it decrypts correctly, you're good. If not, re-
generate with the correct passphrase.

> **Do not skip this step.** A passphrase typo means the will is unrecoverable.

### Step 4: Generate the emergency guide

```bash
python3 scripts/digital_legacy.py emergency-guide
```

This creates `emergency_guide.html`. Edit the generated file to add:
- Your trusted person's name
- A passphrase hint
- Specific instructions (where to find the file)
- Key contacts

### Step 5: Print the guide

Print `emergency_guide.html`, sign it, and give it to your trusted person in
person.

## Phase 5: Secure Storage (15 minutes)

### Store the encrypted will in 2 locations

1. **Primary**: `~/Documents/DigitalLegacy/digital_will.enc` (your computer)
2. **Backup**: USB drive in safe deposit box, or encrypted cloud backup

### Store the passphrase in 2 locations

1. **Primary**: In your password manager
2. **Backup**: Written on paper, sealed in an envelope, in your safe deposit
   box or home safe

> **NEVER store the passphrase in the same location as the encrypted file.**

### Store the inventory

`accounts.json` contains metadata only (no secrets). Store alongside the
encrypted will.

### Give the emergency guide to your trusted person

Hand it to them physically. Explain what it is and what to do.

## Phase 6: Maintenance (ongoing)

### Annual review

Set a calendar reminder for January 1st (or your birthday). Review:

1. Any new accounts? Add them.
2. Any closed accounts? Remove them.
3. Any changed wishes? Update them.
4. Re-generate the encrypted will.
5. Re-test decryption.
6. Update the emergency guide if details changed.

### Life event updates

Update the plan after:
- Marriage or divorce
- Birth or death in family
- New major accounts (mortgage, business)
- Moving (update physical storage locations)
- Changing trusted person

### Platform changes

If a platform changes its legacy policy (they do), update your wishes
accordingly. Check `references/platform-policies.md` periodically.

## Quick Reference: Commands

```bash
# First-time setup
python3 scripts/digital_legacy.py setup

# Add items
python3 scripts/digital_legacy.py add-account
python3 scripts/digital_legacy.py add-subscription
python3 scripts/digital_legacy.py add-wallet

# Review
python3 scripts/digital_legacy.py list

# Generate
python3 scripts/digital_legacy.py generate-will
python3 scripts/digital_legacy.py emergency-guide

# Read
python3 scripts/digital_legacy.py read-will digital_will.enc
```

## Legal Disclaimer

This digital legacy plan is an **informational tool**, not a legal document.
It helps your family find and access your accounts, but it does not:

- Constitute a legally binding will
- Replace estate planning with a qualified attorney
- Override platform terms of service
- Address probate, estate taxes, or inheritance law

For a legally enforceable estate plan, consult a qualified estate planning
attorney in your jurisdiction. This tool complements legal estate planning —
it does not replace it.
