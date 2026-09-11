# Operations — agentkey v2.0.0

## Vault layout

```
${AGENTKEY_HOME:-~/.agentkey}/        0700
  vault/                              0700
    <name>.enc.json                   0600  current key (encrypted JSON blob)
    <name>.prev.enc.json              0600  previous key, kept one rotation
  audit.jsonl                         0600  hash-chained audit log
```

Entries carry: `schema, name, provider, created, rotated, rotations, expires,
key (+encoding=hex if binary)` — all inside the ciphertext. Only metadata
visible at rest is the FILENAME; keep key names non-sensitive
(`openai-prod`, not `alice-openai-pw-hunter2`).

## Common flows

```bash
# one-time
export AGENTKEY_HOME=~/.agentkey
export AGENTKEY_PASS='your-vault-passphrase'   # or: --pass-file ~/.agentkey/.pass (600)
python3 scripts/agentkey.py init

# add (stdin — never argv!)
printf '%s' "$KEY_FROM_SOMEWHERE" | python3 scripts/agentkey.py add anthropic --provider anthropic --expires 2027-09-01

# fetch for a client that wants it as an env var (pipe, don't paste)
export OPENAI_API_KEY="$(python3 scripts/agentkey.py get openai)"

# scheduled maintenance (cron / agent timer)
python3 scripts/agentkey.py report        # rc 1 stale>90d · rc 2 expired
python3 scripts/agentkey.py audit --verify # tamper check
```

## Rotation discipline

`rotate` keeps the retired key as `NAME.prev` (still decryptable this vault
session) so a mid-flight outage isn't fatal. After confirming the new key
works, remove the prev copy: `rm $AGENTKEY_HOME/vault/NAME.prev.enc.json`.
Rationale in evidence.md (staleness/expiry policy).

## Failure modes

| Exit | Meaning | Agent response |
|---|---|---|
| 2 | usage error (bad name/flags) | fix the call, don't retry blindly |
| 3 | no openssl or no passphrase | tell the user; never fake-encrypt |
| 4 | integrity fail (wrong pass or tamper) | do NOT retry; surface it (evidence!) |
| 5 | entry/vault missing | check `list`; add the key |
| 6 | refused (unsafe: existing name, empty key, bad passfile perms) | fix the cause |

## Portability

The vault is plain OS files (OpenSSL-compatible ciphertext) — tar/backup at
rest, restore anywhere with the same passphrase. No daemon, no formats beyond
`openssl` CLI semantics.
