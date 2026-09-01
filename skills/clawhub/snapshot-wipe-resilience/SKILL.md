---
name: snapshot-wipe-resilience
description: "Detect and auto-repair partially-wiped agent workspaces, with hybrid post-quantum end-to-end encryption (X25519+ML-KEM-1024, ML-DSA-87) for any data sent off-box in sandboxes that only persist part of the filesystem between turns, and sync the recovery manifest off-box to a pastebin so it survives a total wipe. Verifies integrity (hash, byte-size, exec bits, tree sentinels) instead of mere existence, then runs tiered restore recipes for exactly the damaged pieces. Use when: (1) an agent sandbox 'forgets' files, binaries, models, or credentials between turns, (2) a build directory, node_modules, or venv keeps disappearing, (3) scripts lose their +x bit or a cloned repo comes back with empty subdirectories, (4) large model/dataset downloads exceed a snapshot size cap, (5) you want a one-command health check at the start of every turn, (6) you need to restore a workspace from nothing but a short pastebin URL. Secrets in restore recipes are redacted to ${ENV_VAR} placeholders before any upload. Supports pastebin.com, dpaste, and paste.rs."
metadata: { "openclaw": { "emoji": "🧬", "category": "reliability", "requires": { "bins": ["python3"] }, "install": [] } }
categories: [operations, security, agents]
topics: [workspace-recovery, integrity, disaster-recovery, sentinels, runbook]
---
 🧬 Snapshot-Wipe Resilience  <sub>v1.5.0</sub>

**The problem:** many agent sandboxes persist only *part* of the filesystem between turns.
Size caps drop your models, exclusion lists eat `build/` and `node_modules/`, and restores
silently strip execute bits. Your workspace looks fine, then everything fails at once.

**The trap:** `if [ -f file ]` is not a health check. Real observed damage:

| What you see | What actually happened |
|---|---|
| `llama.cpp/` exists, cmake fails | `ggml/src/` restored with **0 files** — `src` sat under an excluded parent |
| `model.gguf` exists, loads fail | download **truncated** — valid header, half the bytes |
| `run.sh` exists, "Permission denied" | **exec bit stripped** by restore |
| `skills/` exists, count is short | install died when `.shim/npx` vanished mid-loop |

`swr` verifies **integrity, not presence**, then repairs only what's broken.

## Quick start

```bash
python3 scripts/swr.py autopilot    # init + auto-track + first report, one command
python3 scripts/swr.py sign         # sign the manifest (recipes are code)
python3 scripts/swr.py doctor       # check -> restore -> re-check
```

Run `doctor` as the **first command of every turn**. Exit code `0` = healthy, `1` = still damaged.

## The five verifiers

| Kind | Verifies | Catches |
|---|---|---|
| `file` | sha256 + exec-bit | corruption, truncation, **stripped `+x`** |
| `blob` | exact byte count | truncated/partial downloads (skips hashing GB files) |
| `tree` | file count > 0, `min_files`, **sentinels** | **dir present but emptied**, partial installs |

**Sentinels are the key idea.** For a tree, name a few files that *must* exist and be non-empty.
`ggml/src/ggml.c` as a sentinel catches the gutted-repo case that `-d llama.cpp` misses entirely.

## Tiers = restore order

Recipes run low tier first, so dependencies heal before dependents:

```
0  credentials, PATH shims      <- everything else needs these
1  scripts (chmod +x)           <- cheap, instant
2  source trees, skill installs
3  large downloads (models)
4  build artifacts              <- needs tier 2 source to be healthy
```

Restoring a build *before* re-cloning gutted source just fails twice. Tiers prevent that.

## Commands

```bash
swr init --workspace ~                 # auto-detect scripts + big blobs
swr add PATH --kind tree --tier 2 \
    --sentinel src/main.c \
    --restore 'git clone … '           # capture size/hash/mode from disk NOW
swr check [--only ID …]                # verify; exit 1 if damaged
swr preset arena|openclaw|claude-code|generic   # add a known agent's state
swr models [--apply] [--min-mb N]     # find+track .gguf/.safetensors/... blobs
swr export-recipes --format sh|md|json # portable runbook for any agent
swr restore [--dry-run]                # repair damaged entries only
swr doctor [--dry-run]                 # check -> restore -> re-check
swr explain --only ID                  # why is this fragile? what's the fix?
```

Add entries **while the workspace is healthy** — `add` snapshots the good state as truth.

## Worked example (real 2 vCPU sandbox, llama.cpp + 4 GGUF models + 174 skills)

```bash
# tier 0 — auth/shim first
swr add .shim/npx --id shim --tier 0 \
  --restore 'mkdir -p ~/.shim && printf "#!/bin/bash\nexec /usr/bin/npx --yes \"\$@\"\n" > ~/.shim/npx && chmod +x ~/.shim/npx'

# tier 2 — source, sentineled on the dir that silently empties
swr add llama.cpp --id llama-src --kind tree --tier 2 \
  --sentinel ggml/src/ggml.c --sentinel ggml/cmake/ggml-config.cmake.in \
  --restore 'rm -rf ~/llama.cpp && git clone --depth 1 -q https://github.com/ggerganov/llama.cpp.git ~/llama.cpp'

# tier 3 — models verified by exact byte count, resumable fetch
swr add model.gguf --kind blob --tier 3 \
  --restore "cd ~ && rm -f model.gguf && curl -sSL --retry 3 --retry-all-errors -C - -o model.gguf '$URL'"

# tier 4 — binaries, only after source is proven healthy
swr add llama.cpp/build/bin --id llama-bins --kind tree --tier 4 \
  --sentinel llama-completion \
  --restore 'cd ~/llama.cpp && cmake -B build -DLLAMA_BUILD_SERVER=OFF … && cmake --build build …'
```

Damage injected, then one `doctor` run:

```
== check ==
  STRIPPED run.sh      mode 0644, exec bit lost (want 0755)
  CORRUPT  repo        sentinel missing: ggml/src/core.c
  CORRUPT  model.gguf  1,500,000 bytes (want 3,000,000, -1,500,000)
  MISSING  build       directory absent
  0/4 healthy, 4 damaged
== restore ==   (tier order: chmod -> reclone -> redownload -> rebuild)
== re-check ==
  4/4 healthy
```

## Field-learned rules 🌀

1. **Never trust `exists()`.** Directories survive while being emptied; that is the failure that
   wastes the most time, because configure/build errors point at cmake, not at missing files.
2. **Verify blobs by byte count, not hash.** Hashing 2.2 GB every turn is wasteful; a truncated
   download always has the wrong size. Get the true size from HTTP `x-linked-size` /
   `content-length` before trusting a local file.
3. **Always `curl -C - --retry 3 --retry-all-errors`.** Plain `curl -sSL` fails silently mid-stream
   and leaves a valid-looking header on a half file.
4. **Restore credentials/shims at tier 0.** A vanished `npx` shim caused 40 consecutive "failures"
   that had nothing to do with the packages — mass-install loops must re-check their tooling.
5. **Exec bits are lost far more often than content.** Cheapest possible fix, so keep it tier 1.
6. **Scoped package names change install paths** (`skills/@scope/name/`), so count files by
   `find -name SKILL.md`, never by `ls | wc -l`.
7. **Make every restore idempotent** — `doctor` may run many times per session.
8. Anything under `build/ dist/ out/ target/ node_modules/ .venv/ __pycache__/ .cache/` is
   *unconditionally* volatile regardless of size. Treat as rebuildable, never as storage.

## 🧳 v1.5.0 — any workspace, any agent

Designed with multi-model review (gpt-oss-120b + Nemotron-550B consensus) and
verified end-to-end against live damage.

### `swr init --agent PRESET` / `swr preset PRESET`

One command protects the state of a *known* agent layout — `arena`,
`openclaw`, `claude-code`, or `generic`:

```bash
swr init --workspace ~ --agent arena     # fresh manifest + preset in one shot
swr preset claude-code                   # merge into an existing manifest
```

Each preset adds tier-0 credential/config entries (`.shim/npx`,
`secrets/api_credentials.json`, `.clawhub/TOKEN`, `.claude/…`,
`.openclaw/…`) plus tier-2 state trees, opportunistically — paths absent on
this machine are skipped, and preset entries whose $HOME-shaped paths fall
outside the workspace root are skipped rather than tracked misleadingly.

**Secrets rule (unchanged, now enforced in presets too):** credential files
are hash-TRACKED (truncation and rotation are caught) but their recipes only
restore the directory, permissions, and an empty placeholder. The secret
value comes back through your own channel — env, password manager, or
`swr escrow` (encrypted). A doctor run therefore *flags* a damaged secret
file instead of silently fabricating one.

### `swr export-recipes --format sh|md|json`

A portable recovery runbook for **any agent** — the fresh box has neither the
manifest nor this tool, but it can run a shell script. Entries are
topologically sorted (dependencies before dependents, tier-broken ties), the
`sh` form is a valid `set -euo pipefail` script (verified with `bash -n`),
`md` is human-readable, `json` (`swr.export.v1`) is machine-readable. Escrow
recipes export as comments (they need the encrypted manifest itself). An
invalid manifest signature prints a loud warning line into the runbook.

### `swr models scan` → blob entries

`swr models [--apply] [--min-mb N]` finds `.gguf/.safetensors/.onnx/.bin/.pt/.ckpt`
files (skipping known-volatile dirs), lists them with sizes, and with
`--apply` tracks each as a **blob** (exact byte-count verification — one
stat() catches the invisible truncation that a valid GGUF header hides).
Scan never invents download recipes; add those with
`swr add <path> --kind blob --restore "curl -C - …"`.

### Verified this release

Preset end-to-end on an isolated $HOME: init→3 entries, damage (shim deleted,
secret truncated) → doctor restored the shim **byte-identical + executable**
and correctly left the secret flagged; `export-recipes --format sh` passed
`bash -n` with correct tier/DAG order; `models --apply` tracked an 11 MB
`.gguf` and `check` verified it; selftest / attacktest / crypto selftest all
ALL PASS unchanged; the preset's own shim recipe was live-tested to restore
`#!/bin/bash\nexec /usr/bin/npx --yes "$@"\n` exactly.

## 🔐 Signed manifests — recipes are code

Restore recipes execute as shell commands. v1.1 would run whatever a pulled manifest contained,
so a hijacked or mistyped paste URL was **remote code execution** (a paste.rs key is 5 chars).

v1.2 HMAC-signs the manifest with a local key (`~/.swr/signing.key`, mode 600, never uploaded).
`doctor`/`restore` **refuse to execute** unless the signature verifies:

```
REFUSING TO RUN RESTORE RECIPES: signature invalid — SIGNATURE MISMATCH — manifest was altered
```

`check` still works unsigned (read-only). Override deliberately with `--i-trust-this-manifest`.
A stolen paste is inert: the attacker cannot forge a signature without your local key.

## Verifiers

| Kind | Verifies | Catches |
|---|---|---|
| `file` | sha256 + exec-bit (+ optional `--ldd`, `--smoke`) | corruption, stripped `+x`, unresolved `.so`, binaries that exist but fail |
| `blob` | exact byte count **+ head/tail hash** | truncation *and* same-size corruption, in ~2 MB of I/O |
| `tree` | sentinels, `min_files`, **Merkle root** | emptied dirs, partial installs, any single-file drift across thousands |

Merkle over `(relpath,size,mode)` catches one changed byte in a 5,248-file tree. Sentinels alone
are only a sample — a tree can lose 80% of its files and still pass three sentinel checks.

## Dependency DAG

`--needs` expresses real edges, not just tier ordering. A dependent whose dependency failed is
**skipped**, not attempted:

```
[1/2] -> llama-src: exit 1
[2/2] skip llama-bins — dependency failed: llama-src
```

That is a 6-minute build correctly not run.

## Learning the platform

- `swr canary plant` / `canary read` — scatter probes, see empirically what your sandbox keeps.
- `swr stats` — per-entry survival probability from real history (`~/.swr/history.jsonl`).
- `swr check` names the **wipe signature**: `cold-start`, `size-cap-eviction`, `exclusion-sweep`,
  `permission-reset`, `credential-loss`, `local-corruption`.
- `swr why <id>` — plain-language cause, risk, dependents, and fix.
- `swr audit` — untracked artifacts worth protecting (skips known-volatile caches).

## Performance & safety

`--jobs` parallel verification · incremental `(mtime,size,inode)` cache skips re-hashing ·
`flock` prevents two doctors racing the same clone · per-entry `timeout_s` with process-group
kill · `--quarantine` moves corrupt files aside instead of deleting · `--resume` continues a
restore interrupted mid-turn · `--json` on `check`/`doctor`/`stats`/`why`/`verify` for agent
consumption · `swr retighten` migrates loose tree bounds from older manifests ·
exit codes `0/1/2/3/4` (healthy/damaged/unrepairable/recheck-failed/bad-manifest).

## 📋 Off-box manifest sync (pastebin)

**The bootstrap problem:** the manifest is workspace state too. If the wipe takes
`~/.swr/manifest.json`, the thing that knows how to rebuild everything is gone — you're back to
rebuilding from memory. `swr_paste.py` pushes it to a pastebin so recovery needs nothing but a
short URL you can paste into any fresh box.

```bash
python3 scripts/swr_paste.py push                  # -> https://dpaste.com/B6DNYEPFK.txt
# ... total wipe happens ...
python3 scripts/swr_paste.py pull <raw-url> --expand
python3 scripts/swr.py doctor                      # rebuilds the whole workspace
```

### 🔒 Secrets are redacted by default

Restore recipes routinely embed tokens (`clawhub login --token …`). Uploading raw would publish
them. Every push rewrites known secret shapes to `${ENV_VAR}` **before** the request is sent:

```
redacted before upload:
  clh_95Tm…m-vY  ->  ${CLAWHUB_TOKEN}
  claw_sk_…rg15  ->  ${CLAWARENA_API_KEY}
```

Detected: ClawHub, ClawArena, GitHub, GitLab, OpenAI, HuggingFace, Slack, AWS, Google,
DigitalOcean, npm, JWTs, **PEM private-key blocks**, and **URL-embedded passwords**
(`postgres://user:pass@…`). `--paranoid` additionally redacts unknown-shape high-entropy
strings (Shannon ≥ 4.0) — this catches `MY_CORP_TOKEN=…`, which pattern matching alone misses.
`--strict` refuses to push while any unrecognised secret-looking string remains.
`--show-diff` prints exactly what changes before anything leaves the box.
`pull --expand` substitutes them back from your environment and **warns loudly** about any var
that is unset rather than silently writing a broken recipe. `--no-redact` exists but prints a
warning — only for manifests you have personally confirmed clean.

### Backends

| Backend | Key | Notes |
|---|---|---|
| `pastebin` | `PASTEBIN_API_KEY` | unlisted by default; `PASTEBIN_USER_KEY` enables true private; expiry `10M…N` |
| `dpaste` | none | keyless default, expiry in days |
| `pasters` | none | keyless (paste.rs), no expiry control |

`push --mirror` replicates to every available backend at once — worth doing, since paste hosts
rate-limit (429), and two died during development (0x0.st disabled uploads; dpaste.org's API
405s). Transient 429/5xx retry with backoff honouring `Retry-After`.

**Integrity:** every push pins a `sha256` and re-fetches to confirm the stored copy matches.
`pull --sha256 <hash>` **fails closed** on mismatch. `--compress` (zlib+base64) typically cuts
the payload to ~40%. `--encrypt-to <age-recipient>` encrypts instead of redacting, so a fully
automatic restore needs no env vars. Each push prints a mnemonic recovery code
(`bishop-harbor-quartz-jasper`) and `--qr` renders a scannable code.

```bash
swr_paste.py backends   # availability, incl. age/qrencode
swr_paste.py status     # replica hash health + expiry countdown
```

**Verified round-trip:** live 16-entry manifest pushed → public copy contains zero secrets →
pulled to a clean path with `--expand` → **byte-identical to the original** → drove
`swr.py check` to 16/16 healthy.

## 🛡️ Hybrid post-quantum E2E encryption (`swr_crypto.py`)

**On "the #1 most secure encryption":** there isn't one, and treating any single algorithm that
way is a warning sign. A one-time pad is *information-theoretically* secure but needs a truly
random key as long as the message, pre-shared — which is exactly the problem E2E key agreement
solves, so it cannot do this job. What is actually defensible is: **NIST-standardized
post-quantum primitives at the highest security category, hybridized with a battle-tested
classical primitive, authenticated, with forward secrecy.** That is what this implements, and
it is the same design class as TLS 1.3 `X25519MLKEM768` and Signal's PQXDH.

### Ciphersuite `SWR-HYBRID-v1`

| Layer | Primitive | Standard |
|---|---|---|
| Classical KEM | X25519 ECDH, **ephemeral** | RFC 7748 |
| Post-quantum KEM | **ML-KEM-1024** (Kyber) | FIPS 203, NIST cat. 5 |
| KDF | HKDF-SHA-512 over both secrets **+ full transcript** | RFC 5869 |
| AEAD | ChaCha20 + HMAC-SHA-512/256, encrypt-then-MAC | RFC 8439 / 4231 |
| Sender auth | **ML-DSA-87** (Dilithium) | FIPS 204, NIST cat. 5 |

`key = HKDF(ss_X25519 ‖ ss_MLKEM ‖ transcript)`. An attacker must break **both** KEMs — classical
*and* quantum — to recover anything. This is the Giacon–Heuer–Poettering KEM combiner, which
preserves IND-CCA2 if either component holds. It defeats **harvest-now-decrypt-later**: a paste
captured today stays sealed against a future quantum adversary.

### Use

```bash
python3 scripts/swr_crypto.py keygen --name laptop      # X25519 + ML-KEM + ML-DSA
python3 scripts/swr_crypto.py export > my.pub           # share this (never ~/.swr/identity/)
python3 scripts/swr_crypto.py peer-add their.pub --name bob
python3 scripts/swr_crypto.py encrypt --to bob --in secret.txt --out sealed.json
python3 scripts/swr_crypto.py decrypt --in sealed.json --from bob
```

Wired straight into off-box sync — encryption **replaces** redaction, so a fully automatic
restore needs no env vars:

```bash
python3 scripts/swr_paste.py push --pq-to bob --compress --no-redact
python3 scripts/swr_paste.py pull <raw-url> --pq-from bob
```

Verify fingerprints (`3nwiu-2nxkq-b2263-6mqhc`) **out-of-band** — voice, in person, QR. Public-key
crypto without fingerprint verification is just encryption to whoever handed you a key.

### Measured against real attacks

A manifest containing live tokens was pushed to a **public** paste with `--no-redact`:

```
clh_95TmhmX     not present      llama       not present
claw_sk_b0336   not present      entries     not present
ciphertext entropy: 7.934 / 8.0 bits per byte (indistinguishable from random)
```

| Attack | Result |
|---|---|
| Eavesdropper decrypts | rejected — not addressed to this identity |
| Impersonate sender (swap ML-DSA key) | rejected — signature invalid |
| Flip one ciphertext bit | rejected — signature invalid |
| Flip one bit, **unsigned** message | rejected — AEAD authentication failed |
| Strip/replace ML-KEM ciphertext (PQ downgrade) | rejected — transcript binding |
| Wrong expected sender | rejected — sender mismatch |

Every public value is folded into the KDF transcript, so a downgrade attempt changes the derived
key and fails. Forward secrecy is verified: ephemeral X25519 and KEM ciphertext differ per
message, so compromising a long-term key does not retroactively open captured pastes.
`swr_crypto.py selftest` runs all of the above (9/9 pass).

### Audit round 1 (v1.3.1)

Six real bugs, found by attacking my own code rather than re-running passing tests:

| # | Bug | Severity |
|---|---|---|
| 1 | `selftest` executed restore recipes **without the signature guard** — a full bypass of the v1.2 protection | 🔴 security |
| 2 | Ephemeral X25519 **private key written to disk-backed `/tmp`**, weakening the forward-secrecy claim | 🟠 security |
| 3 | Every `encrypt()` leaked a temp directory (5 encryptions → 5 dirs, forever) | 🟡 resource |
| 4 | `push --pq-to <other peer> --verify` hard-failed: round-trip check tried to *decrypt*, needing the recipient's private key | 🔴 broke the main use case |
| 5 | `SWR_ID_DIR`/`SWR_PEERS_DIR` ignored when imported as a library — silently used the wrong identity | 🔴 wrong-key bug |
| 6 | Malformed envelopes raised raw Python tracebacks instead of clean errors | 🟡 robustness |

Also: temp files holding key material are now overwritten before unlink (`_shred`), `selftest`
survives recipe timeouts instead of crashing, and `pull --sha256` accepts either the plaintext
or transport digest.

### Audit round 2 (v1.3.2) — exercising never-run code paths

Round 1 attacked the crypto. Round 2 ran every subcommand that had never been executed
(`init`, `autopilot`, schema migration, `--resume`, `peer-list`, hostile peer files) and found
**eleven more**, including one regression I introduced while fixing the others:

| # | Bug | Severity |
|---|---|---|
| 7 | `min_files = nf//2` — a tree could lose **50% of its files and still pass**. Tightened to a 5% churn bound | 🔴 core detection |
| 8 | `autopilot` picked only root-level sentinels, so a gutted `src/` was invisible — the exact bug this skill exists for | 🔴 core detection |
| 10 | Schema migration mutated a signed v1 manifest, making a **legitimate, untampered manifest verify as TAMPERED** and blocking recovery | 🔴 false alarm |
| 11 | `progress.json` was global, so one workspace's resume state **skipped another workspace's identically-named entries** | 🔴 silent data loss |
| 12 | `peer-add` accepted garbage/RSA keys, failing later with a raw OpenSSL error | 🟠 |
| 13 | `--dry-run` exited before validating encryption, so it "succeeded" for an unknown peer or missing `age` | 🟠 false confidence |
| 15 | `check --only <typo>` reported `0/0 healthy` and **exit 0** — a silent pass in a turn-start hook | 🟠 |
| 17 | **Regression from fix #10**: excluding bookkeeping keys broke verification of already-signed manifests | 🔴 self-inflicted |
| 9, 14, 16 | No early warning for recipe-less entries; unhelpful 404-vs-429 hints; unclamped `--jobs` | 🟡 |

Verified after: signature matrix (live v2 valid / signed-v1 valid / tampered rejected / bypass
blocked), concurrent `doctor` runs contend on the lock without tracebacks, corrupt `cache.json`
and `history.jsonl` both recover silently, and a third party decrypts a public encrypted push
byte-identically that we ourselves cannot read.

### Audit round 3 (v1.3.3) — shipped artifacts and doc-vs-code drift

Rounds 1–2 audited behaviour. Round 3 audited what actually **ships** — the example file, the
documentation's promises, and rarely-used flags:

| # | Bug | Severity |
|---|---|---|
| 19 | **The round-2 fix did not protect existing manifests.** Tree entries added earlier kept `min_files = nf//2`; the live `skills` entry could still lose **601 files (50%) undetected**. Added a warning on every check plus a new `swr retighten` command to migrate them | 🔴 incomplete fix |
| 48/49 | The **shipped example manifest taught the anti-pattern**: `min_files: 2000` on a 5,248-file tree tolerated 62% loss. Rewritten to a 4% bound with scoped-path sentinels and a `needs` edge | 🟠 propagates the bug |
| 20 | Docs promised "`--json` on every subcommand" but only `check`/`doctor` implemented it — an agent parsing `--json stats` got a crash. Implemented for `stats`, `why`, `verify` | 🟠 overclaim |
| 18 | 9-character statuses (`SMOKEFAIL`, `BROKENLNK`) collided with the id column | 🟡 cosmetic |

`swr retighten` was run against this workspace: `skills` 601 → 1142 and `llama-bins` 10 → 20,
cutting tolerated loss from ~50% to 4%, manifest re-signed.

### Audit round 4 (v1.3.4) — deployment reality

Round 4 checked how the skill behaves once *installed* rather than run from its dev directory:

| # | Bug | Severity |
|---|---|---|
| 21 | `canary plant` created decoy `build/`, `node_modules/`, `dist/`, `target/`, `__pycache__/` directories in `$HOME` and **had no cleanup command** — permanent litter that also confuses other tooling. Added `swr canary clean` | 🟠 side effects |
| 22 | Script docstrings still announced **v1.2** while the package was 1.3.3, so `--help` reported the wrong version | 🟡 drift |
| 73 | `_meta.json` omitted itself from its own `files` list | 🟡 packaging |

Verified clean in round 4 (no bug found): imports resolve from any cwd, the hook prefers the
installed `~/skills/` copy over `skill_inventions/`, an install at the documented path works
end-to-end, `retighten` is idempotent, **dependency cycles terminate in 0.1 s** instead of
looping, `needs` pointing at a nonexistent id degrades gracefully, and a growing tracked tree
does not trip the lower-bound check.

### Audit round 5 (v1.3.5) — containment and standards conformance

| # | Bug | Severity |
|---|---|---|
| 23 | **Path traversal.** Manifest entries with `../../` or absolute paths resolved outside the workspace. Demonstrated exploitable: `doctor --quarantine` **moved a file out of `/tmp` that the workspace did not own**. Entries are now contained — escaping paths are reported `CORRUPT` and every destructive op refuses them | 🔴 security |
| 24 | `swr add` silently accepted an escaping path, writing (and re-signing) a bad entry into the manifest. Now rejected at authoring time | 🟠 security |

Verified clean in round 5 (no bug found): HKDF matches the RFC 5869 construction on
**200/200 randomized vectors**; `shlex.quote` correctly handles filenames containing spaces,
single quotes, semicolons and `$(...)` with no shell injection; a **1500-entry / 640 KB**
manifest pushes, compresses to 2%, and round-trips byte-identically; the shared verification
cache survives **32-way concurrent** writes without corruption; `retighten`, `audit` and `why`
all behave sanely when escaping entries are present.

### Audit round 6 (v1.3.6) — differential & fuzz testing

Feature probing was exhausted, so round 6 attacked the guarantees directly. It found the
**worst bug of all six rounds — one I introduced myself in round 2**:

| # | Bug | Severity |
|---|---|---|
| 25 | **Signature forgery → RCE.** The round-2 migration fallback trusted `_presig_body`, an attacker-controlled field. Putting the *legitimate* body there and swapping `entries` for a payload made the manifest verify as **valid**; `doctor` then executed `rm -rf /`. Confirmed end-to-end through the real CLI. The fallback now *reconstructs* the pre-migration body from current data and never reads a self-declared field; `_presig_body` is rejected outright | 🔴🔴 critical |
| 26 | **Signature stripping.** Deleting the `sig` field downgraded an authenticated message to "anonymous" while the header still advertised a sender. Found by envelope fuzzing. A header claiming a sender now *requires* a valid signature | 🔴 auth bypass |

Both attacks are now permanent regression tests: `swr attacktest` (4 forgery variants) and two
new cases in `swr_crypto.py selftest`.

Fuzzing results: **2000 manifest mutations → 0 forgeries**; **500 envelope mutations → 0
plaintext forgeries, 0 tracebacks** (18 accepted removals touch only the cosmetic `sig_alg`
label, with the ML-DSA signature still verified — no downgrade is possible since the suite
defines exactly one algorithm). Canonical JSON correctly distinguishes NFC/NFD Unicode and
int-vs-float.

### Audit round 7 (v1.3.7) — 15-minute live soak test

A continuous soak ran **225 cycles over 15 minutes** (check → inject damage → doctor → encrypt →
decrypt → attacktest → stats → audit), with concurrent probes hammering it from outside.

**Soak scorecard:** 0 tracebacks · 0 failed checks (225/225 at 16/16) · 0 invalid signatures ·
0 attacktest failures · 225/225 crypto round-trips correct · 224 successful auto-repairs ·
**resource state identical across all 225 cycles** (`fd=7 tmp=0 shm=0` — no fd, temp-dir, or
tmpfs leaks). The single "still damaged" event was self-inflicted: an external probe truncated a
GGUF mid-cycle, and the soak correctly caught it.

Sustained operation surfaced three defects that no single-shot test could:

| # | Bug | Severity |
|---|---|---|
| 27 | **Unbounded telemetry growth.** `history.jsonl` appends forever — measured ~509 B/record, i.e. **~267 MB/year** at one check per minute, which a snapshot-size-capped sandbox cannot hold. Now rotates at 5000 records | 🟠 resource |
| 28 | **The mtime cache can mask corruption.** With `size`, `mtime_ns` *and* `inode` all preserved, a modified file verified as **OK** while `--no-cache` correctly reported `CORRUPT`. Inherent to mtime caching, but it was undocumented. Entries now expire hourly and the cache is explicitly labelled a speed optimisation, not a tamper boundary | 🟠 correctness |
| 29 | **Crash on read-only/full `~/.swr`.** A cache write raised a bare `PermissionError` traceback and aborted the health check. Cache, telemetry and resume writes are now best-effort with a one-line note | 🟠 robustness |

Also verified live: 7-way concurrent `doctor` runs serialise correctly on the lock with no
corruption; content corruption, blob truncation and tree gutting were each detected and repaired
under load; three consecutive paste pushes succeeded without rate-limiting.

**Seven audits, 29 bugs.** The pattern worth keeping: round 1 (attack the crypto) found 6,
round 2 (run never-executed paths) found 11, round 3 (audit shipped artifacts and doc claims)
found 4 — including a round-2 fix that silently failed to help existing users — round 4
(behaviour once installed) found 3, round 5 (containment + standards conformance) found 2, and
round 6 (differential + fuzz testing) found 2 — the most severe of the entire effort — and
round 7 (a 15-minute live soak) found 3 that only appear under sustained operation.
Each round surfaced a *different class* of defect, which is why "the tests pass" was never
sufficient evidence.

### Honest limits

- **Not audited.** Standard primitives, but this composition has not had third-party review.
  For life-safety threat models use Signal or age, not a workspace utility.
- ChaCha20 comes from OpenSSL; the Poly1305 role is played by HMAC-SHA-512/256 because
  `openssl enc` exposes no AEAD tag. Encrypt-then-MAC is the safe construction, but it is not
  the RFC 8439 AEAD exactly.
- Needs **OpenSSL ≥ 3.5** for ML-KEM/ML-DSA. Falls back to `age`, then redaction.
- Metadata is not hidden: recipient fingerprint, size, and timing are visible on the paste.
- Python-level key material is not zeroized after use (CPython gives no guarantee); on-disk
  temp files *are* overwritten and prefer `/dev/shm` (tmpfs), but if no tmpfs exists they fall
  back to `/tmp`.
- `--i-trust-this-manifest` disables the signature guard on `doctor`, `restore` **and**
  `selftest`. It is a loaded gun; there is no safe default that also allows pulling a peer's
  manifest.

## Files

- `scripts/swr.py` — signed integrity checker + DAG restorer (stdlib only, Python 3.8+)
- `scripts/swr_paste.py` — off-box sync: redaction, encryption, replication (stdlib only)
- `scripts/swr_crypto.py` — hybrid PQ E2E: X25519+ML-KEM-1024, ML-DSA-87 (needs OpenSSL ≥3.5)
- `reference/manifest.example.json` — annotated manifest with all three kinds and tiers
- `reference/turn-start-hook.sh` — drop-in snippet to auto-heal at turn start

### Audit round 8 (v1.4.1) — attacking the new v1.4.0 code

The limitation fixes were the newest, least-tested code, so round 8 targeted them:

| # | Bug | Severity |
|---|---|---|
| 30 | **Decompression bomb in escrow.** `zlib.decompress` was unbounded in three places. 200 MB of zeros compresses to ~204 KB — small enough to fit in a paste and inside a *validly signed* manifest. Now a streaming decompressor with a 64 MB ceiling, cross-checked against the declared size; measured **20 MB peak RSS instead of 200 MB, blocked in 4 ms** | 🔴 DoS |
| 31 | Escrow restore wrote directly to the target, so a failed decompress left a **truncated file** where a good one had been. Now validated in memory, written to a temp file, and `os.replace`d atomically | 🟠 data loss |

Verified clean (no bug found): escrow content **is** covered by both signatures — swapping it
invalidates HMAC and ML-DSA; an attacker self-signing with their own ML-DSA key is rejected as
`untrusted`; **key substitution** (real key declaring a trusted fingerprint) is rejected because
the fingerprint is recomputed from the key, never read from the declaration; **800 fuzz
mutations** of `_pksig`/escrow produced 0 false-valid verdicts and 0 crashes.

`swr attacktest` now covers **7 attack classes** (added: decompression bomb, oversized escrow,
fingerprint substitution).

**Eight audits, 31 bugs.**

## Limitations

*(v1.4.0 resolved the four previously-documented limitations; what remains is stated honestly.)*

**Resolved in v1.4.0**

- ~~HMAC is not a public-key trust system~~ → manifests now carry an **ML-DSA-87 (FIPS 204)
  public-key signature** alongside the HMAC, with a trust store (`swr trust add/list/mine`).
  Verified: a second machine with a *different* HMAC secret and no shared key accepted the
  manifest via ML-DSA and rejected the HMAC — genuine cross-party trust.
- ~~`--i-trust-this-manifest` is a loaded gun~~ → the flag now **requires the manifest digest**,
  so approval is scoped to one exact content. Swapping in `rm -rf /` afterwards is refused with
  a digest mismatch.
- ~~Merkle costs real I/O; the cache covers files, not tree structure~~ → tree verification is
  now cached on a per-file `(size, mtime_ns)` fingerprint. (A cheaper directory-mtime-only key
  was tried first and **masked a real edit** in testing, so it was rejected.)
- ~~Cannot resurrect data with no restore recipe~~ → `swr escrow` embeds small files
  (default ≤256 KB, zlib+base64) directly in the manifest. Demonstrated: a script was deleted
  *and* the local manifest destroyed, then both were recovered **byte-identically from a single
  pastebin URL**.
- ~~Public pastes are public; redaction is a seatbelt~~ → `push` now **encrypts by default**
  (hybrid PQ to your own identity) whenever an identity exists; publishing in the clear requires
  an explicit `--plaintext-ok`. Redaction is skipped for encrypted payloads because rewriting the
  body would invalidate the manifest signature.

**Still true**

- **The crypto composition is unaudited.** Standard primitives (X25519, ML-KEM-1024, ML-DSA-87,
  HKDF-SHA-512, ChaCha20, HMAC), but this particular assembly has had no third-party review. For
  life-safety threat models use Signal or `age`.
- **Escrow is for small files, not gigabytes.** Sync carries the manifest; a 2.2 GB model still
  needs a download recipe. Escrowed content also inflates the manifest — keep an eye on
  `swr audit`.
- **Fingerprints must be verified out-of-band.** Public-key crypto without that is just
  encryption to whoever handed you a key.
- **The mtime cache is a speed optimisation, not a tamper boundary** — an attacker preserving
  `size` + `mtime_ns` + `inode` can defeat it (entries expire hourly; `--no-cache` forces a full
  re-hash).
- **Metadata leaks on public pastes**: recipient fingerprint, payload size, and timing.
- **Python cannot zeroize key material in memory**; on-disk temp files are overwritten and
  prefer tmpfs.
- Requires **OpenSSL ≥ 3.5** for the post-quantum layer; degrades to `age`, then redaction.
