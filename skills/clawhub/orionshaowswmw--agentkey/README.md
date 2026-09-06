# 🔑 AgentKey — v2.0.0

Local, offline, **actually-encrypted** API-key vault for agents. Real
add/get/rotate/list, a hash-chained evidence-grade audit log, staleness and
expiry reporting, redacted inventories, and key fingerprints — with zero
network traffic of any kind. Full guide: `SKILL.md` · `docs/operations.md`.

## Requirements

- `python3` (3.8+, stdlib only) and system `openssl` (for AES-256-CBC +
  PBKDF2). Both verified at call time; missing openssl = honest rc 3, never
  silent plaintext.

## Privacy & security

- **Complete privacy:** keys stay on this machine. No network, no telemetry,
  no update beacon, no third-party API. (v1.0.7 shipped a beacon; v2.0.0
  removed it — see CHANGELOG.md.)
- **Encryption at rest:** AES-256-CBC, PBKDF2-SHA256 600k iterations, fresh
  salt per write, HMAC-SHA256 Encrypt-then-MAC verified before decrypt
  (docs/evidence.md for the design rationale and standards references).
- **Writes:** only under `${AGENTKEY_HOME:-~/.agentkey}` (dirs 0700, files 0600).
- **Inputs:** keys via stdin or a 0600 file; passphrase via `AGENTKEY_PASS`,
  0600 `--pass-file`, or tty. Empty pass refused. Nothing in argv.

## Known limits (honest)

- Vault-files are only as safe as the filesystem user protecting them: this
  vault guards at-rest confidentiality (laptop stolen, disk imaged), not a
  live root attacker over your shoulder.
- The tool stores and hands back keys; it cannot tell whether a provider
  still considers a key valid.

## Verify it

`bash scripts/selftest.sh` — offline regression suite: crypto roundtrip,
wrong-pass/tamper rc-4 paths, audit-chain edit detection, redaction checks,
perm checks, staleness/expires exit mapping, version sync.
