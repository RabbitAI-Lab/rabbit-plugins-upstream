#!/bin/bash
# role-audit — Compare DB roles against expected manifest
# Usage: bash role-audit.sh [--fix-proposals]
# Reads references/role-manifest.json, compares with DB, reports mismatches
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$SCRIPT_DIR/../references/role-manifest.json"
ADC_HOST="${ADC_HOST:-8.163.44.127}"

if [ ! -f "$MANIFEST" ]; then
  echo "❌ Role manifest not found at $MANIFEST"
  exit 1
fi

# Get DB state
DB_DATA=$(ssh -o ConnectTimeout=15 "root@$ADC_HOST" \
  "docker run --rm -e PGPASSWORD=dd42107b8d47eb54dc3d7c45a509af49 --network agent-dev-center_backend postgres:16-alpine psql -h 172.21.0.2 -U postgres -d agent_dev_center -t -A -F '|' -c \"SELECT email, role, internal_role FROM users ORDER BY email;\"" 2>/dev/null)

python3 << PYEOF
import json, sys

with open("$MANIFEST") as f:
    expected = json.load(f)

db_lines = """$DB_DATA""".strip().split('\n')

db = {}
for line in db_lines:
    if '|' not in line:
        continue
    parts = line.split('|')
    if len(parts) >= 3:
        email = parts[0]
        db[email] = {'role': parts[1], 'internal': parts[2] if parts[2] else None}

issues = []
orphaned = []

for email, info in sorted(db.items()):
    exp = expected.get(email)
    if not exp:
        orphaned.append(f"  ⚠️ {email}: role={info['role']}, internal={info['internal']} (not in manifest)")
        continue
    
    exp_role = exp['role']
    exp_internal = exp.get('internal')
    db_role = info['role']
    db_internal = info['internal']
    
    role_ok = (db_role == exp_role)
    internal_ok = (db_internal == exp_internal)
    
    if not role_ok or not internal_ok:
        issue = f"  ❌ {exp['name']} ({email}):"
        if not role_ok:
            issue += f" role={db_role}→{exp_role}"
        if not internal_ok:
            issue += f" internal={db_internal}→{exp_internal}"
        issues.append(issue)

print("=" * 70)
print("🔍 ADC 角色审计")
print("=" * 70)

if issues:
    print(f"\n不一致 ({len(issues)}):")
    for i in issues:
        print(i)
else:
    print("\n✅ 所有角色与 manifest 一致")

if orphaned:
    print(f"\n未在 manifest 中 ({len(orphaned)}):")
    for o in orphaned:
        print(o)

print(f"\nTotal in DB: {len(db)} | In manifest: {len(expected)} | Mismatches: {len(issues)} | Orphaned: {len(orphaned)}")
PYEOF
