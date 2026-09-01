# 🧬 Snapshot-Wipe Resilience

Detect and auto-repair partially-wiped agent workspaces. Verifies **integrity**
(sha256, byte counts, exec bits, tree sentinels, Merkle roots) instead of mere
existence, then runs tiered, dependency-ordered restore recipes for exactly the
damaged pieces — with signed manifests (HMAC + ML-DSA-87), encrypted off-box
sync, and agent presets.

## Functionality

- Five verifiers (`file`/`blob`/`tree`): corruption, truncation, stripped `+x`,
  gutted directories, partial installs — plus `--ldd`/`--smoke` for binaries.
- Tiers 0–4 restore order with a `--needs` dependency DAG; failed dependencies
  skip their dependents instead of failing twice.
- `swr init --agent arena|openclaw|claude-code|generic` presets: known
  credential/config trees protected in one command (secrets hash-tracked, never
  written into recipes).
- `swr models [--apply]`: finds `.gguf/.safetensors/.onnx/...` weights and tracks
  them as byte-count-verified blobs.
- `swr export-recipes --format sh|md|json`: a portable recovery runbook for any
  agent, topologically ordered, `bash -n`-valid.
- Signed manifests — restore recipes are code, so a hijacked paste URL cannot
  execute (`swr attacktest` regression-covers 7 attack classes including
  signature forgery and decompression bombs).
- Off-box sync (`swr_paste.py`): redaction + hybrid post-quantum encryption
  (X25519+ML-KEM-1024, ML-DSA-87) to dpaste/paste.rs/pastebin.com; `swr escrow`
  embeds small files so a total wipe recovers from one short URL.
- `canary`, `stats` (survival probabilities), `why`, `audit`, `retighten`.

## Permissions

Reads the whole workspace; writes only `~/.swr/` (manifest, signing key, cache,
history) and — during `restore`/`doctor` — executes the manifest's recorded
restore recipes, which run only after signature verification (or an explicit
`--i-trust-this-manifest <digest>`). Quarantine moves damaged files aside
rather than deleting.

## Security & Privacy

- Manifests are HMAC-signed with a local key (mode 600, never uploaded) and
  carry an ML-DSA-87 public-key signature for cross-machine trust.
- Secrets in recipes are redacted to `${ENV_VAR}` placeholders before any
  upload; preset recipes restore only directories/permissions/placeholders —
  secret VALUES never travel through the manifest.
- Encrypted pastes use standard primitives (X25519, ML-KEM-1024, ML-DSA-87,
  HKDF-SHA-512, ChaCha20, HMAC); the composition is unaudited — for life-safety
  threat models use Signal or `age`.
- Metadata (recipient fingerprint, size, timing) is visible on public pastes.

## Verification

- sha256: db6ac43ed7bd4de90dc83c98d5188c1606f018da7018a117a0f3795bf60f2c30
  (of this release's `SKILL.md` — verify with `sha256sum SKILL.md`)
- `python3 scripts/swr.py selftest` → 12/12 recipes idempotent;
  `attacktest` → ALL PASS; `scripts/swr_crypto.py selftest` → ALL PASS.
- Preset end-to-end on an isolated `$HOME`: doctor restored a deleted npx shim
  **byte-identical**, flagged (never fabricated) a truncated secret, and a
  symlinked preset path pointing outside the workspace was refused.
