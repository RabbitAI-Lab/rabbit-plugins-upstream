---
name: security-hardener
description: Harden a ZK-Bankir sovereign banking deployment — threat model audit, hash-chain integrity, dependency scanning, access control review, and runbook validation against De 10 Gebuden.
homepage: https://gitlab.com/1Beekeeper/zk-bankir
metadata:
  openclaw:
    requires:
      bins: ["curl", "jq", "ruby", "bundle"]
    os: ["linux", "darwin"]
---

# Security Hardener

Harden a ZK-Bankir sovereign banking deployment. Audits the threat model, verifies hash-chain integrity, scans for vulnerable dependencies, reviews access controls, and cross-references runbooks against De 10 Gebuden.

## Prerequisites

- Running ZK-Bankir Rails server (default: `http://localhost:3000`)
- Local ZK-Bankir project checkout
- `curl`, `jq`, `ruby`, `bundle` on PATH
- Read access to `docs/03-threat-model.md` and `docs/04-runbooks.md`

## Core Commands

### Hash-Chain Integrity Verification

Verify the Decision Ledger's SHA-256 hash chain (Gebud 6 — mandatory):

```bash
cd ZK_BANKIR_PATH
bin/rails runner "puts Decision.verify_chain ? '✅ Chain intact' : '❌ CHAIN BROKEN — RESTORE FROM BACKUP'"
```

If chain is broken, do NOT proceed with any other operations. Restore from backup immediately.

### Dependency Vulnerability Scan

Check Ruby gems for known CVEs:

```bash
cd ZK_BANKIR_PATH
bundle audit check --update 2>&1
```

Also check for outdated gems:

```bash
bundle outdated --filter-patch 2>&1 | head -30
```

### Threat Model Cross-Reference

Validate that all 15 threats from `docs/03-threat-model.md` have mitigations in place:

```bash
cd ZK_BANKIR_PATH

echo "=== Threat Model Status ==="

# T1: Server compromise
echo -n "T1 (Server compromise): "
grep -q "watch-only" app/models/treasury_service.rb && echo "✅ No keys on server" || echo "❌ CHECK"

# T2: Database breach
echo -n "T2 (Database breach): "
grep -q "encrypted" app/models/decision.rb && echo "✅ Encrypted fields" || echo "⚠️  PARTIAL"

# T3: API abuse
echo -n "T3 (API abuse): "
grep -q "rack-attack" Gemfile && echo "✅ Rate limiting active" || echo "❌ MISSING"

# T4: Hash chain tampering
echo -n "T4 (Hash chain): "
grep -q "verify_chain" app/models/decision.rb && echo "✅ Verification method exists" || echo "❌ MISSING"

# T5: Unauthorized trades
echo -n "T5 (Unauthorized trades): "
grep -q "PolicyEngine" app/controllers/api/v1/decisions_controller.rb && echo "✅ Policy-gated" || echo "⚠️  CHECK"

# T6: Private key leak
echo -n "T6 (Private key leak): "
grep -q "NEVER STORE" app/models/kraken_service.rb 2>/dev/null && echo "✅ Guard documented" || echo "⚠️  CHECK — verify no key storage"

# T7: Backup failure
echo -n "T7 (Backup failure): "
test -f backups/backup-*.tar.gz 2>/dev/null && echo "✅ Recent backup found" || echo "⚠️  No recent backup"

# T8: Dependency hijack
echo -n "T8 (Dependency hijack): "
test -f Gemfile.lock && echo "✅ Lockfile present" || echo "❌ MISSING"

# T9: Configuration leak
echo -n "T9 (Config leak): "
grep -q "credentials" config/environments/production.rb 2>/dev/null && echo "✅ Encrypted creds" || echo "⚠️  CHECK"

# T10: RPC endpoint exposure
echo -n "T10 (RPC exposure): "
grep -q "127.0.0.1\|localhost" config/deploy.yml 2>/dev/null && echo "✅ Local binding" || echo "⚠️  CHECK binding"
```

### Access Control Review

Verify the Policy Engine's 3-tier evaluation is intact:

```bash
cd ZK_BANKIR_PATH

# Check policy rules exist (stored as JSON in `rules` column)
echo "=== Policy Engine Status ==="
bin/rails runner "
  Policy.where(active: true).each do |p|
    puts \"Policy ##{p.id}: #{p.name}\"
    puts \"  Rules: #{p.rules}\"
    puts \"  Auto-approve: <\$#{p.rules['approval_threshold']}\"
    puts \"  Hard-deny: >\$#{p.rules['max_trade_size']}\"
  end
" 2>&1
```

Verify the risk tiers:
- **Auto-approve:** amount < $1,000 (Gebud 8)
- **Human approval:** $1,000 ≤ amount ≤ $10,000 (Gebud 4)
- **Hard deny:** amount > $10,000 (Gebud 8)

### Runbook Validation

Check that daily operations match runbook procedures:

```bash
cd ZK_BANKIR_PATH

echo "=== Runbook Compliance ==="

# Check daily health endpoint
echo -n "Health endpoint: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health
echo ""

# Check treasury endpoint
echo -n "Treasury endpoint: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v1/treasury/balances
echo ""

# Check decision ledger
echo -n "Decision ledger: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v1/decisions
echo ""

# Verify hash chain
echo -n "Hash chain: "
bin/rails runner "puts Decision.verify_chain ? 'INTACT' : 'BROKEN'" 2>&1
```

### Kill Switch Test

Verify that the kill switch mechanism works (Gebud 10 — Test What You Fear):

```bash
# Check that Decision#destroy raises
cd ZK_BANKIR_PATH
bin/rails runner "
  begin
    Decision.last.destroy
    puts '❌ KILL SWITCH FAILED: destroy allowed'
  rescue => e
    puts '✅ Kill switch active: destroy blocked'
  end
" 2>&1
```

## Usage Patterns

### Full Security Audit

When the user requests a full security audit:

1. **Hash-chain integrity** — verify SHA-256 chain (CRITICAL)
2. **Dependency scan** — check for CVEs in gems
3. **Threat model cross-ref** — all 15 threats verified
4. **Access control review** — Policy Engine tiers intact
5. **Runbook validation** — endpoints respond correctly
6. **Kill switch test** — destructive operations blocked

### Pre-Deployment Checklist

Before deploying to production:

1. Hash chain intact
2. No critical CVEs in dependencies
3. Rate limiting enabled (rack-attack)
4. Encrypted credentials in place
5. Backup routine verified (recent backup exists)
6. All threat model mitigations confirmed
7. Policy Engine tiers tested

### Incident Response

If a security incident is suspected:

1. **Lock down** — verify kill switches active
2. **Verify chain** — check hash-chain for tampering
3. **Audit decisions** — list all recent decisions, flag anomalies
4. **Check threats** — cross-reference against threat model
5. **Restore if needed** — locate latest verified backup

## Gebuden Compliance

This skill enforces ZK-Bankir's non-negotiable doctrine:

- **§6 Audit Trail** — hash-chain verification is the first check
- **§8 Risk-Weighted** — validates Policy Engine tiers
- **§10 Test What You Fear** — kill switch tests mandatory
- **§3 Trust, but Verify** — cross-references threats against actual code

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `ZK_BANKIR_HOST` | `http://localhost:3000` | ZK-Bankir server URL |
| `ZK_BANKIR_PATH` | `/home/cwn/App/domains/finance/zk-bankir` | Project path for local checks |
| `AUDIT_ALERT_WEBHOOK` | (optional) | Slack/Discord webhook for audit alerts |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| bundle-audit not found | gem not installed | `gem install bundler-audit` |
| Hash chain verification fails | DB corruption | Restore from backup, verify chain post-restore |
| Policy count is 0 | No policies seeded | `bin/rails db:seed` |
| rack-attack not in Gemfile | Missing dependency | Add `gem "rack-attack"` to Gemfile |

## Security

- **Read-only by default** — audits and verifies, never modifies
- **No secrets transmitted** — all checks are local or over localhost
- **Kill switch respected** — never attempts to bypass destroy protections
- **Backup-aware** — flags missing backups, recommends restore when needed
