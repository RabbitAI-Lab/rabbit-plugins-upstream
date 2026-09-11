# Integration — agentkey v2.0.0 (model-agnostic)

Any agent that can run `python3` and read stdout can use the vault. Nothing
here is Claude/GPT/Gemini-specific — plain JSON in, JSON or raw key out.

## Pattern 1 — fetch a key for a per-run tool call

```python
import os, subprocess
os.environ["AGENTKEY_PASS"] = vault_pass
key = subprocess.run(
    ["python3", "scripts/agentkey.py", "get", "openai"],
    capture_output=True, text=True, check=True).stdout.rstrip("\n")
headers = {"Authorization": f"Bearer {key}"}   # piped into the API call, never logged
```

## Pattern 2 — identify-before-reveal (fingerprint check)

```bash
FP_LOCAL=$(python3 scripts/agentkey.py get openai --fingerprint | python3 -c 'import sys,json;print(json.load(sys.stdin)["fp"])')
# compare FP_LOCAL against the fingerprint the task manifest expects — no key reveal
```

## Pattern 3 — health gate at session start

```bash
python3 scripts/agentkey.py report;  case $? in
  0) echo "keys fresh" ;;
  1) echo "STALE keys — schedule rotation" ;;
  2) echo "EXPIRED keys — renew now" ;;
esac
python3 scripts/agentkey.py status | python3 -c 'import sys,json; d=json.load(sys.stdin); assert d["audit_integrity"]=="ok"'
```

## Redaction contract for model context

- Only `get` outputs raw key material; pipe it into the exact consumer
  (`export`, curl header), never echo transcript-visible.
- `list`, `status`, `audit`, `report`, `--fingerprint` disclose at most: key
  NAMES, providers, timestamps, rotation counts, 16-hex fingerprints. Safe to
  paste anywhere — keep them that way (choose non-secret names).

## Contracts for machine consumers

`agentkey.status.v1` (init/status), `agentkey.list.v1`, `agentkey.audit.v1`,
`agentkey.report.v1` — additive changes only; ignore unknown keys.

## Not this skill's job (avoid scope hallucinations)

- Network calls of any kind (the vault is offline by design).
- Storage of non-API secret classes (SSH private keys, disks, TLS**: use dedicated
  ISO/OS tooling).
- Detecting whether the *value* of a key is valid at its provider — we store
  and hand over; provider-side validity is the provider's answer.
