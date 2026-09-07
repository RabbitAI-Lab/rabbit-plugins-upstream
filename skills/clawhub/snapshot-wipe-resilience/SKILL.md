---
name: snapshot-wipe-resilience
description: "Detect and repair partially wiped agent workspaces with integrity checks, signed manifests, guarded restore recipes, bounded local recovery state, and explicit off-box sync. Use when files, scripts, trees, models, or build outputs disappear or lose integrity between turns."
metadata: { "openclaw": { "emoji": "🧬", "category": "reliability", "requires": { "bins": ["python3"] }, "install": [] } }
categories: [operations, security, agents]
topics: [workspace-recovery, integrity, disaster-recovery, sentinels, runbook]
---

# 🧬 Snapshot-Wipe Resilience

Version **1.5.6**. This skill is a small, provider-neutral recovery utility;
it does not depend on an AI provider or a particular agent runtime. It helps an
operator detect state loss between turns and run a reviewed recovery plan.

It is not a backup service, immutable storage system, sandbox boundary, or
secret manager. A restore recipe is executable code. Review it, sign the
manifest, and rehearse recovery before relying on it.

## When to use it

Use it when a workspace can be partially persisted or recreated:

- a directory survives but its contents are empty or incomplete;
- a download has a valid header but is truncated;
- a script keeps its contents but loses its executable bit;
- build, dependency, model, or skill trees disappear between turns;
- the manifest itself needs an explicit off-box recovery copy.

The tool does not infer that a file is safe to restore merely because its path
exists. It compares the current state to a healthy capture in the manifest.

## Quick start

```bash
python3 scripts/swr.py init --workspace "$HOME"
python3 scripts/swr.py autopilot --workspace "$HOME"
python3 scripts/swr.py sign
python3 scripts/swr.py --json check
```

`check` does not alter the workspace and skips recorded smoke commands unless
the operator adds `--run-smoke`; it may refresh the local cache. That option
requires a trusted manifest because a smoke string is also shell code.
`restore` and `doctor` verify a manifest before executing recipes; use
`--dry-run` to inspect a plan without executing it.

```bash
python3 scripts/swr.py doctor --dry-run
python3 scripts/swr.py doctor --quarantine --resume
python3 scripts/swr.py why --only entry-id
```

Run a turn-start hook only after reviewing every recipe and its required
network, credentials, and destructive operations. The reference hook is an
example, not an automatic installation step.

## Integrity model

| Kind | Default check | What it catches |
|---|---|---|
| `file` | SHA-256 and executable mode | edits, truncation, and lost `+x` |
| `blob` | exact byte count plus 1 MiB head/tail digest | truncation and sampled same-size corruption with bounded I/O |
| `tree` | sentinels and a tight file-count lower bound | empty or partially installed trees |
| `tree` with `--content-hash` | full-content tree digest | same-size edits in every regular file, at the cost of reading the tree |

`--content-hash` is the supported name; `--merkle` remains a CLI alias for
compatibility. New entries store `tree_sha256`, a deterministic full-content
tree digest. Older entries containing `merkle` are still read as legacy
metadata-only fingerprints over relative path, size, and mode. That legacy
field is not a content hash and is not called a Merkle tree here.

`--no-cache` forces re-verification. The normal cache is a performance
optimization based on size, mtime, and inode plus an expiry; it is not a tamper
boundary. A hostile actor who can change a file and preserve those attributes
can defeat a cached check, so use `--no-cache` for a high-assurance check.

Add entries while healthy:

```bash
swr add run.sh --kind file --tier 1 --restore 'chmod +x "$HOME/run.sh"'
swr add src --kind tree --tier 2 --sentinel main.c --content-hash \
  --restore 'rebuild-command'
swr models                    # report large model/weight files
swr models --apply            # track them as byte-counted blobs; no recipe is invented
```

The `--restore` and `--smoke` values are stored shell strings. They are not
parsed into a safe command list. This is intentional for portability, but it
means the author must quote paths and review side effects.

## Ordering, repair, and output

Tiers are a sorting hint. `--needs ID` expresses a real dependency. A failed
dependency skips its dependent; a dependency cycle fails closed. `doctor` checks,
restores damaged entries, and checks again. `--quarantine` preserves a copy of the previous tracked path in private
`~/.swr/quarantine` before a recipe runs. Inline
`escrow` restores use a bounded decompressor and an atomic file replacement;
general shell recipes cannot be made atomic by this tool.

Machine-readable output is available with the global option before the command:

```bash
swr --json check
swr --json doctor --dry-run
swr --json why --only entry-id
swr --json stats
swr --json verify
```

Exit codes are stable: `0` healthy/success, `1` damaged, `2` unrepairable,
`3` re-check failure, and `4` malformed or unsupported manifest. `selftest`
executes selected signed recipes twice and verifies the entry after each run.
An empty selection fails rather than pretending to provide coverage; use
`--allow-empty` only when checking a newly initialized manifest.

`export-recipes --format sh|md|json` emits a recovery plan; Markdown is the
safe default. Shell output contains the recorded recipe strings and requires
`--allow-shell-export` plus a trusted manifest (or a second explicit override
for an untrusted manifest). `bash -n` is a useful syntax check but not a safety
review and does not execute the recipes.

## Signatures and trust

A manifest stores a local HMAC-SHA256 signature. When a local ML-DSA-87
identity is available, `swr sign` also stores a public-key signature. A restore
operation accepts the local HMAC or a public-key signature whose fingerprint is
in `~/.swr/trusted_signers.json`:

```bash
swr sign                         # a new local manifest
swr sign --approve-digest DIGEST # an edited/pulled manifest after review
swr verify
swr trust mine
swr trust add FINGERPRINT operator-name   # verify out of band first
```

A pulled, edited, unsigned, untrusted, or altered manifest cannot run recipes.
Mutation commands do not silently convert an untrusted loaded manifest into a
locally signed one. To sign a new or edited manifest, review its exact digest
and pass `swr sign --approve-digest DIGEST`; the digest is checked immediately
before signing. For a deliberate one-off execution review, `restore`, `doctor`,
and `selftest` accept `--i-trust-this-manifest DIGEST`; the digest must match the
exact content at execution time. These are explicit consent paths, not
authentication.

`check` validates manifest entries without executing restore or smoke strings.
`check --run-smoke` is the exception and requires the same signature guard.
`verify` reports both signature paths without modifying the manifest.

## Declared operational permissions

- **Local file read:** reads the manifest and tracked workspace paths to hash,
  verify, and plan recovery.
- **Local file write:** writes only the explicitly selected manifest, private
  state under `~/.swr`, quarantine copies, and requested restore targets inside
  the manifest workspace. Quarantine preserves existing data rather than
  deleting it.
- **Shell execution:** restore recipes, smoke commands, and exported runbooks
  are executable content and run only after the documented trust/consent
  checks; ordinary `check` does not execute them.
- **Environment access:** reads configuration such as the manifest path and
  optional redaction variables, but does not read credential values
  implicitly. Identity/private-key files are used only by the explicit crypto
  and sync commands.
- **Network:** the core checker makes no network calls. Only the explicit
  `swr_paste.py` sync component uses HTTPS, and only for the documented
  Pastebin, dpaste, and paste.rs hosts; it bounds payloads and refuses
  redirects. Network access is not required for local recovery.

## Privacy and local state

The core checker makes no network calls and does not read credential values.
Presets can hash-track credential files but their placeholder recipes only
recreate directories, permissions, or empty files. Supply secret values through
a password manager or other manual secret channel; this utility does not read
those values implicitly. Redaction is a precaution, not proof that a document
contains no secret.

By default, `check` and `doctor` do **not** write history. Add `--record` to
append local status codes to `~/.swr/history.jsonl` for `stats`; `--no-record`
remains as a compatibility flag. The file is local-only, private, rotated, and
contains entry IDs and statuses rather than file contents. No telemetry is sent.
Cache and resume state are also local and best-effort.

The optional canary command deliberately writes probe files to the workspace
and `/tmp`; run `swr canary clean` after reading the result. It is not part of a
normal check.

## Off-box manifest sync

`swr_paste.py` is separate from the local checker. It is an explicit network
operation for a recovery copy:

```bash
python3 scripts/swr_crypto.py keygen --name this-machine
python3 scripts/swr_paste.py push --mirror
python3 scripts/swr_paste.py pull 'https://dpaste.com/EXAMPLE' \
  --out "$HOME/.swr/manifest.json"
python3 scripts/swr.py verify
```

With an identity, `push` encrypts to that identity by default. Otherwise the
operator must choose `--pq-to`, `--encrypt-to` for an age recipient, or
explicitly acknowledge cleartext with `--plaintext-ok`. A manifest containing
inline `escrow` is **never** accepted for cleartext upload: compression and
Base64 are not confidentiality, so escrow requires encrypted transport.
Unencrypted pushes redact known token formats; `--paranoid` adds a heuristic
entropy pass and `--strict` refuses when unknown candidates remain. Encrypted
pushes also scan for known secret-shaped values and refuse by default;
`--allow-encrypted-secrets` is an explicit exception for a reviewed encrypted
manifest. Encryption and redaction are not combined by default because
redacting changes signed manifest bytes; `--force-redact` is a deliberate
signature-breaking option, not a normal recovery path.

Supported upload backends are Pastebin (when `PASTEBIN_API_KEY` is available),
dpaste, and paste.rs. `--verify` is enabled by default and compares the
transport payload after upload. Responses and decompressed payloads are capped
at 64 MiB, pull accepts only HTTPS URLs for those three approved hosts, refuses
embedded credentials and non-default ports, does not follow redirects, and
writes atomically. Pulled `${ENV_VAR}` placeholders are never expanded from
this process environment; set values manually through the operator's own
secret channel after review. Backend availability, expiry, access logs, URL
metadata, and service compromise remain outside this utility's control.

## Hybrid-PQ encryption limits

`swr_crypto.py` requires OpenSSL 3.5 or newer with ML-KEM-1024 and ML-DSA-87:

- X25519 ephemeral key agreement (RFC 7748);
- ML-KEM-1024 (NIST FIPS 203);
- HKDF-SHA-512 with a transcript (RFC 5869);
- ChaCha20 plus HMAC-SHA-512/256 encrypt-then-MAC;
- optional ML-DSA-87 sender authentication (NIST FIPS 204).

`SWR-HYBRID-v1` is an application-specific, unaudited composition. It is **not
RFC 8439 ChaCha20-Poly1305**, and this skill makes no formal claim that either
KEM can be broken only by breaking both, or that captured data is guaranteed
safe against every future adversary. Verify peer fingerprints out of band.
For high-consequence data, use a reviewed protocol such as age or Signal.
Private key files are mode 600 under a mode 700 identity directory; Python
memory cannot be reliably zeroized.

## Release and compatibility checks

Use a temporary HOME and a non-empty harmless fixture for restore tests. Do not
call an empty manifest a restore test. A local gate should include:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/swr_crypto.py selftest
python3 scripts/swr.py attacktest
bash -n reference/turn-start-hook.sh
# then test init/add/escrow/corruption/restore/re-check with a temp workspace
```

The scripts use Python standard-library modules. The PQ layer has an external
OpenSSL requirement; integrity checking, local HMAC signing, and guarded shell
restoration do not require ML-KEM. The skill emits text, Markdown, JSON, and
shell plans rather than depending on a specific model's output format.

## Files

- `scripts/swr.py` — integrity checker, signer, planner, and guarded restorer.
- `scripts/swr_paste.py` — explicit sync, redaction, and bounded transport.
- `scripts/swr_crypto.py` — OpenSSL-backed identity and hybrid-PQ envelopes.
- `reference/manifest.example.json` — annotated manifest schema.
- `reference/turn-start-hook.sh` — optional start-of-turn example.
- `skill-card.md` — risks and output summary.

MIT-0. Use normal backup, immutable-copy, access-control, and disaster-recovery
practices for important data.
