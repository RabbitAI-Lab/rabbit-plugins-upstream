---
name: gdpr-checker
description: GDPR compliance audit for ZK-Bankir — data minimization verification, encryption audit, right-to-delete workflows, privacy policy validation, and data export procedures.
homepage: https://gitlab.com/1Beekeeper/zk-bankir
metadata:
  openclaw:
    requires:
      bins: ["curl", "jq", "ruby"]
    os: ["linux", "darwin"]
---

# GDPR Checker

Audit ZK-Bankir for GDPR compliance. Verifies data minimization, encryption at rest, right-to-delete procedures, privacy policy alignment, and data export capabilities. Designed for sovereign banking where privacy is paramount (Gebud 7).

## Prerequisites

- Running ZK-Bankir Rails server (default: `http://localhost:3000`)
- Local ZK-Bankir project checkout
- `curl`, `jq`, `ruby` on PATH

## Core Commands

### Data Minimization Audit

Check what personal data is stored in the database:

```bash
cd ZK_BANKIR_PATH

echo "=== Data Minimization Audit ==="

# Check Decision model columns (should NOT store PII)
echo "--- Decision columns ---"
bin/rails runner "
  Decision.columns.each do |col|
    puts \"  #{col.name}: #{col.type}\"
  end
" 2>&1

# Check for PII in schema
echo ""
echo "--- PII Check ---"
grep -iE "email|phone|name|address|ssn|passport|dob|birth" db/schema.rb 2>/dev/null && \
  echo "⚠️  POTENTIAL PII FIELDS DETECTED" || \
  echo "✅ No obvious PII fields in schema"

# Verify no plaintext secrets
echo ""
echo "--- Secrets Check ---"
grep -riE "secret_key|private_key|api_key|password" app/models/ 2>/dev/null && \
  echo "⚠️  CHECK FOR HARDCODED SECRETS" || \
  echo "✅ No hardcoded secrets in models"
```

### Encryption Verification

Verify encryption is in place for sensitive fields:

```bash
cd ZK_BANKIR_PATH

echo "=== Encryption Audit ==="

# Check for encrypted attributes
echo "--- Encrypted fields ---"
grep -r "encrypts\|has_encrypted\|attr_encrypted" app/models/ 2>/dev/null || \
  echo "⚠️  No ActiveRecord encryption found"

# Check credentials setup
echo "--- Credentials ---"
test -f config/credentials.yml.enc && echo "✅ Encrypted credentials exist" || echo "❌ MISSING"
test -f config/master.key 2>/dev/null && echo "⚠️  Master key present (should be gitignored)" || echo "✅ No master.key in repo"

# Check database encryption
echo "--- Database encryption ---"
grep -q "encrypted" config/database.yml 2>/dev/null && echo "✅ DB encryption configured" || echo "⚠️  Check DB encryption"
```

### Right-to-Delete Verification

Verify that the append-only Decision Ledger properly handles deletion requests (GDPR Art. 17):

```bash
cd ZK_BANKIR_PATH

echo "=== Right-to-Delete Audit ==="

# Verify destroy is blocked (Doctrine compliance)
echo "--- Decision#destroy ---"
bin/rails runner "
  begin
    Decision.new(action: 'TEST', amount: 0).destroy
    puts '❌ GDPR CONFLICT: destroy allowed on Decision'
  rescue => e
    puts '✅ Destroy blocked (append-only): ' + e.message[0..80]
  end
" 2>&1

# Check if update is blocked
echo "--- Decision#update ---"
bin/rails runner "
  begin
    d = Decision.last
    d.update(action: 'TAMPERED')
    puts '❌ GDPR CONFLICT: update allowed on Decision'
  rescue => e
    puts '✅ Update blocked (immutable): ' + e.message[0..80]
  end
" 2>&1

# Check if there's a tombstone/anonymization mechanism
echo "--- Anonymization path ---"
grep -r "anonymize\|tombstone\|gdpr\|delete.*request" app/ 2>/dev/null && \
  echo "✅ Some GDPR handling exists" || \
  echo "⚠️  No anonymization mechanism found"
```

Note: GDPR right-to-delete conflicts with ZK-Bankir's immutable audit trail (Gebud 6). Resolution: ZK-Bankir is a personal banking system where the data subject IS the controller. For a single-operator sovereign system, GDPR Art. 2(2)(c) (personal/household exemption) typically applies.

### Data Export (GDPR Art. 20 — Portability)

Generate a machine-readable export of all user data:

```bash
cd ZK_BANKIR_PATH

echo "=== Data Export ==="

EXPORT_FILE="gdpr-export-$(date +%Y%m%d-%H%M%S).json"

bin/rails runner "
  require 'json'
  
  export = {
    exported_at: Time.now.iso8601,
    system: 'ZK-Bankir',
    decisions: Decision.all.map { |d|
      {
        id: d.id,
        action: d.action,
        amount: d.amount.to_s,
        status: d.status,
        created_at: d.created_at.iso8601,
        hash: d.hash_chain
      }
    },
    treasury: Treasury.all.map { |t|
      {
        asset: t.asset,
        balance: t.balance.to_s,
        updated_at: t.updated_at.iso8601
      }
    }
  }
  
  File.write('#{EXPORT_FILE}', JSON.pretty_generate(export))
  puts \"✅ Export written to #{EXPORT_FILE} (#{export[:decisions].count} decisions)\"
" 2>&1

echo "Export file: $(pwd)/$EXPORT_FILE"
```

### Privacy Policy Validation

Cross-reference the privacy posture against Gebud 7 (Privacy Per Design):

```bash
cd ZK_BANKIR_PATH

echo "=== Privacy Policy Validation (Gebud 7) ==="

# ZK transactions as default
echo -n "ZK default: "
grep -q "zk\|zero.knowledge\|Payy" app/models/payy_service.rb 2>/dev/null && \
  echo "✅ Payy ZK integration present" || \
  echo "⚠️  No ZK integration found"

# Encrypted memos
echo -n "Encrypted memos: "
grep -qi "encrypt\|cipher" app/models/decision.rb 2>/dev/null && \
  echo "✅ Encryption referenced" || \
  echo "⚠️  Check memo encryption"

# Stealth addresses
echo -n "Stealth addresses: "
grep -qi "stealth\|hd.*wallet\|bip32" app/models/treasury.rb 2>/dev/null && \
  echo "✅ HD/stealth concepts present" || \
  echo "⚠️  No stealth address support detected"

# No tracking
echo -n "No tracking: "
grep -qi "analytics\|tracking\|google\|facebook\|pixel" app/views/ 2>/dev/null && \
  echo "❌ TRACKING DETECTED" || \
  echo "✅ No third-party tracking"

# Privacy headers
echo -n "Privacy headers: "
curl -sI http://localhost:3000/health 2>/dev/null | grep -qi "referrer-policy\|x-content-type\|x-frame" && \
  echo "✅ Security headers present" || \
  echo "⚠️  Check security headers"
```

## Usage Patterns

### Full GDPR Audit

When the user requests a GDPR compliance audit:

1. **Data minimization** — check for unnecessary PII in schema
2. **Encryption** — verify credentials, database, and field-level encryption
3. **Right-to-delete** — verify append-only ledger + household exemption
4. **Data portability** — generate full data export
5. **Privacy policy** — cross-reference Gebud 7 compliance
6. **Third-party data flows** — audit external API calls

### Privacy Impact Assessment (PIA)

For changes that affect data handling:

1. Identify what new data is collected/stored
2. Verify encryption at rest and in transit
3. Check data minimization (collect only what's needed)
4. Document retention periods
5. Update threat model if new attack surface

### Data Retention Review

```bash
cd ZK_BANKIR_PATH

echo "=== Data Retention ==="

# Check for old decisions (retention policy)
bin/rails runner "
  oldest = Decision.minimum(:created_at)
  newest = Decision.maximum(:created_at)
  count = Decision.count
  puts \"Decisions: #{count} (from #{oldest} to #{newest})\"
  puts \"Retention period: #{(Time.now - oldest).to_i / 86400} days\"
" 2>&1
```

## GDPR Applicability Notes

ZK-Bankir is a **personal banking system** for a single operator:

- **Art. 2(2)(c)** — The "household exemption" likely applies: GDPR does not cover processing by a natural person in the course of a purely personal or household activity.
- **Data controller = data subject** — The operator is both the controller and the data subject, making most GDPR rights self-referential.
- **No third-party data** — ZK-Bankir stores only the operator's own financial decisions.

However, if ZK-Bankir is opened to other users or processes third-party data, full GDPR compliance becomes mandatory.

## Gebuden Compliance

- **§7 Privacy Per Design** — ZK transactions default, encrypted memos, stealth addresses
- **§6 Audit Trail** — Append-only ledger (conflicts with right-to-delete; resolved by household exemption)
- **§5 Watch-Only** — No private keys on server (reduces breach impact)
- **§1 Sovereignty First** — Data stays on operator's hardware

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `ZK_BANKIR_PATH` | `/home/cwn/App/domains/finance/zk-bankir` | Project path |
| `GDPR_EXPORT_DIR` | `./exports` | Directory for data exports |
| `DATA_RETENTION_DAYS` | `3650` | Expected data retention period (10 years) |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| PII fields detected | Schema includes personal data | Review if fields are truly needed; encrypt if so |
| No encryption found | ActiveRecord encryption not configured | `bin/rails db:encryption:init` |
| Export fails | Disk space or permissions | Check disk space and write permissions |
| Destroy test succeeds | Kill switch disabled | This is a critical security issue — investigate immediately |
