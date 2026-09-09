# 🧬 Snapshot-Wipe Resilience 1.5.6

A small, provider-neutral Python/ shell utility for detecting and repairing
partially wiped agent workspaces. It checks integrity rather than mere path
existence, orders repairs by tiers and explicit dependencies, and can export a
human- or machine-readable recovery plan.

It is deliberately not an autonomous host manager: it only operates on the
workspace named by the manifest, keeps all observations local, never reads
credentials implicitly, and treats restore and smoke-test strings as code.
Review recipes before signing or executing them.

## What is implemented

- `file`: SHA-256 and executable-mode checks.
- `blob`: exact byte count plus a head/tail digest, avoiding a full read of very
  large model or dataset files on every check.
- `tree`: sentinels and a bounded file-count rule. `--content-hash` adds an
  opt-in full-content tree digest; it reads every file. Older manifests using
  the historical `merkle` field remain readable as metadata-only tree
  fingerprints, not as content hashes.
- Tiers and `--needs` dependencies. A failed dependency prevents a dependent
  restore; dependency cycles fail closed instead of being treated as success.
- HMAC-SHA256 local manifest signatures and optional ML-DSA-87 signatures for
  cross-machine trust. Restore-oriented commands require a valid local HMAC or
  a trusted public-key signature, unless the operator approves the exact
  manifest digest with `--i-trust-this-manifest DIGEST`.
- Atomic, private persistence for manifests, cache, history, progress, and
  inline escrow restores. Local history is **off by default**; use `--record`
  explicitly with `check` or `doctor` if survival statistics are wanted.
- `swr_paste.py` off-box sync with redaction, a 64 MiB transport/decompression
  ceiling, bounded retries, transport hash verification, and optional
  encryption. Cleartext pushes require `--plaintext-ok`; an identity enables
  hybrid-PQ encryption to that identity by default.
- `swr_crypto.py` hybrid X25519 + ML-KEM-1024 encryption with ML-DSA-87 sender
  signatures when OpenSSL 3.5 or newer supplies the algorithms.

## Quick start

Run commands from the skill directory or use absolute paths:

```bash
python3 scripts/swr.py init --workspace "$HOME"
python3 scripts/swr.py autopilot --workspace "$HOME"
python3 scripts/swr.py add path/to/important-tree --kind tree --tier 2 \
  --sentinel src/main.c --content-hash \
  --restore 'git clone --depth 1 https://example.invalid/project.git "$HOME/important-tree"'
python3 scripts/swr.py sign
python3 scripts/swr.py --json check
```

`check` does not alter the workspace or execute recorded smoke commands by
default; it may refresh the local cache unless `--no-cache` is supplied. To run
smoke commands, use `--run-smoke` on a trusted, signed manifest. To repair, use
`restore` or `doctor`; those commands verify the manifest before executing
recipes. Start with `--dry-run` when reviewing a new manifest.

```bash
python3 scripts/swr.py doctor --dry-run
python3 scripts/swr.py doctor --quarantine --resume
python3 scripts/swr.py why --only entry-id
python3 scripts/swr.py export-recipes --format sh --allow-shell-export > recovery.sh
bash -n recovery.sh
```

A command can return: `0` healthy/success, `1` damaged, `2` unrepairable,
`3` re-check failure, or `4` bad manifest. An empty `selftest` is not a
coverage result and fails unless `--allow-empty` is supplied.

## Safety boundaries

- A manifest is data until its signature passes. Pulled or edited manifests
  cannot execute recipes through `restore`, `doctor`, or `selftest` without
  trust. Mutation commands do not silently re-sign an untrusted loaded
  manifest; after reviewing its exact digest, use `swr sign --approve-digest
  DIGEST` when that is genuinely intended. `check` still validates paths and
  hashes without running shell code.
- Restore recipes, smoke commands, exported shell runbooks, and environment
  expansion are executable content. They may use the network or modify files
  outside the tracked path if the author wrote them that way. Sign only
  reviewed recipes.
- Entry paths are realpath-checked against `workspace`; absolute paths are
  allowed only when they resolve inside it. Workspace `/` is rejected.
- Quarantine moves an existing tracked path into private `~/.swr/quarantine`
  preserves a copy of the damaged path rather than deleting it. Inline escrow validates size and decompression
  bounds before an atomic replacement.
- No network request is made by `swr.py` checks or restores unless a signed
  recipe itself asks for one. `swr_paste.py` is the separate, explicit sync
  tool. It accepts only HTTPS URLs for the implemented paste hosts, refuses
  embedded credentials, non-default ports, and redirects, and limits response
  size.
- No secret value is read automatically. Presets track credential-file
  integrity but restore only placeholders/directories; provide secrets through
  your own password manager or other manual secret channel. This utility does
  not read those values. Redaction is not encryption.
- No telemetry is sent. `--record` writes only local status codes to
  `~/.swr/history.jsonl`, bounded to a small rotated history; omit it for no
  history writes.

## Off-box sync

The manifest itself can disappear, so sync it only when you explicitly choose
to. With an identity from `swr_crypto.py keygen`, a plain `push` encrypts to
that identity. Without an encryption recipient, `push` refuses until you pass
`--plaintext-ok`; however, a manifest containing inline `escrow` always
requires encryption because compressed/Base64 escrow is not confidential and
must not bypass redaction.

```bash
python3 scripts/swr_crypto.py keygen --name this-machine
python3 scripts/swr_paste.py push --mirror
python3 scripts/swr_paste.py pull 'https://dpaste.com/EXAMPLE' \
  --out "$HOME/.swr/manifest.json"
```

Backends are `dpaste`, `pasters` (paste.rs), and optional Pastebin. Pull accepts
only HTTPS URLs for those approved hosts, rejects embedded credentials and
non-default ports, and refuses redirects. Public paste hosts still see URL,
timing, expiry, and payload-size metadata; encrypted payloads protect content,
not metadata or endpoint availability. `--verify` is enabled by default and
compares the stored transport payload. Use `--sha256` on pull when an
out-of-band hash is available.

Known secret-shaped values are replaced with `${ENV_VAR}` on unencrypted
pushes. `--paranoid` adds a heuristic high-entropy pass and `--strict` refuses
unrecognised candidates; neither method can prove a document contains no
secrets. Encrypted pushes still scan for known secret-shaped values and refuse
by default; use `--allow-encrypted-secrets` only after reviewing why those
values must be in the encrypted manifest. `--force-redact` changes signed bytes
and is therefore not a normal recovery path. Pull never expands placeholders
from the process environment; supply values manually through your own secret
channel after reviewing the pulled manifest. `--no-redact` is safe only when
encryption is enabled or the operator has explicitly accepted cleartext.

## Hybrid-PQ layer and its limits

`SWR-HYBRID-v1` uses:

- X25519 ephemeral key agreement (RFC 7748);
- ML-KEM-1024 (NIST FIPS 203) for the post-quantum KEM;
- HKDF-SHA-512 with transcript binding (RFC 5869);
- ChaCha20 plus HMAC-SHA-512/256 encrypt-then-MAC;
- optional ML-DSA-87 sender signatures (NIST FIPS 204).

The last construction is **not** RFC 8439 ChaCha20-Poly1305. It is an
unaudited composition of standard primitives implemented through OpenSSL and
Python; this project makes no formal security or “unbreakable” claim. For
high-consequence data, prefer a reviewed protocol such as age or Signal. Verify
peer fingerprints out of band before sending sensitive data. OpenSSL versions
without the required PQ algorithms cannot use this layer; choose `age` with an
explicit recipient or consciously use `--plaintext-ok`.

## Useful commands

```text
init / autopilot       create or enrich a manifest
preset                 add a known agent layout opportunistically
models [--apply]       find large model/weight files; never invents recipes
add                    capture a healthy file, blob, or tree
check                  integrity report; --json is machine-readable
restore / doctor       guarded repair, optional quarantine and resume
selftest               execute selected signed recipes twice to check idempotence
attacktest             local regression checks for manifest/escrow attacks
trust                  manage explicitly verified public-key fingerprints
escrow                 embed bounded small files for wipe recovery
why / stats / audit    explain risk, local survival observations, and gaps
canary                 explicitly probe persistence; `canary clean` removes it
export-recipes         emit shell, Markdown, or JSON recovery plans
```

## Release checks

From this directory, a release review should include:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/swr_crypto.py selftest
python3 scripts/swr.py attacktest
# Use a temporary HOME/workspace and a non-empty signed fixture:
python3 scripts/swr.py --manifest /tmp/manifest.json selftest --max-tier 4
bash -n reference/turn-start-hook.sh
```

The selftest fixture must contain at least one harmless, idempotent recipe; a
pass against an empty manifest is intentionally not treated as restore
coverage. Network backends are not required for the local gate; any publication
check must separately inspect the uploaded version, scan result, cold install,
and post-publication behavior.

## Files

- `scripts/swr.py` — integrity checker, signer, planner, and guarded restorer.
- `scripts/swr_paste.py` — explicit off-box sync and bounded transport wrapper.
- `scripts/swr_crypto.py` — OpenSSL-backed hybrid-PQ identity and envelope tool.
- `reference/manifest.example.json` — annotated schema example.
- `reference/turn-start-hook.sh` — optional operator-controlled hook.
- `skill-card.md` — risk and output summary.

MIT-0. This utility is not a substitute for backups, immutable storage, or a
rehearsed disaster-recovery plan.
