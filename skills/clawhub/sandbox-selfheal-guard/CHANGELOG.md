# Changelog — sandbox-selfheal-guard

## v3.0.1 (2026-09-06 — identical to 3.0.0 plus packaging fix: .clawhubignore added; stray __pycache__/*.pyc removed from the bundle)

### release notes for v3.0.0 line — evidence-based rewrite

Every fix below is grounded in a check run on 2026-09-06 (see `manifest.json.evidence`).

### Fixes (bugs in v2.x, now verified against live sources)
1. **Dead model URL → guaranteed 404 download.** bartowski renamed the file to
   `Qwen_Qwen3-0.6B-Q4_K_M.gguf`; the old name returns HTTP 404 with a 15-byte
   body — the exact corruption v2 claimed to guard against. Fixed URL + bytes
   re-verified (484,220,320) via HEAD + range request.
2. **Unreachable download branch.** v2 used `case $f in Coder*)` — a glob that
   anchors at byte 0, so `Qwen2.5-Coder-*` never matched; the coder model could
   never download. URL selection is now manifest-driven; the bug class is gone.
3. **Dead build flags.** `-DLLAMA_NATIVE=ON`/`-DLLAMA_BUILD_SERVER=OFF`/`-DLLAMA_SERVER=OFF`
   are unused/deprecated (llama.cpp renamed options to `GGML_*`). Now
   `-DGGML_NATIVE=ON` + automatic portable fallback (`-DGGML_NATIVE=OFF`).
4. **Fragile binary assumption.** Prefer `llama-completion` (upstream moved
   llama-cli's deterministic mode there, discussion #17618), fall back to
   `llama-cli`; probe `--version` before trusting `-x`.
5. **Library poisoned its host.** v2 ran `set -e` + global `cd` in a file meant
   to be *sourced* → could kill the caller's shell. v3: POSIX sh functions only,
   subshell isolation, explicit return codes.
6. **Hallucinated advertised files shipped nothing.** v2's SKILL.md promised
   `prompt_cache_layer.py`, `run_max_speed.sh`, `test_selfheal.sh` — absent from
   the bundle. v3 actually ships `prompt_cache.py`, `run_guarded.sh`,
   `test_selfheal.sh` (13 hermetic tests).
7. **Missing-flag hallucination risk.** Optional flags are now feature-detected
   from `--help` instead of asserted.
8. **Hang-by-sudo.** v2 ran plain `sudo apt-get` — blocks forever on
   stdin-closed sandboxes if a password is needed. Now `sudo -n` probe, else skip+warn.
9. **Hang-by-budget division.** Budget math guards t/s near zero; caps enforced.
10. **Duplicate-context README.** v2 README reprinted the entire SKILL.md body
    (~2× token cost for every reading agent). v3 README is a thin pointer.

### New features
- **Circuit breaker** on model downloads (3 fails → 30 min cooldown → degrade
  gracefully instead of re-downloading 484 MB every call).
- **Self-improving budgets:** `run_guarded.sh` logs wall-clock per call;
  `selfheal_tune.sh` measures real t/s and EMA-updates `state/state.json`;
  budgets converge to this host's truth. Defaults labeled "unmeasured".
- **Real prompt cache** (`prompt_cache.py`): sha256 key, TTL, size-based
  eviction, stats. Cache-hit path avoids the binary entirely.
- **`run_guarded.sh`**: light-swarm auto routing (≤8 words → scout, n≤96),
  cache → preflight → timeout → fallback chain → latency log.
- **Integrity upgrade:** model verify = exact bytes + `GGUF` magic (range-verified).
- **Machine-readable core:** `manifest.json` as single source of truth with an
  `evidence` block (verification method + date per fact).
- **Token-lean SKILL.md** (~40% smaller than v2 body) + progressive-disclosure
  file table; README no longer duplicates it.

### Multi-model debug round (how v3.0.0 was reviewed)
Distributed review across independent providers via the workspace router —
5 parallel specialist passes (shell correctness, fact-grounding, security/least-privilege,
docs/cross-model clarity, robustness/edge-cases) → fix → 2-model consensus re-review
of the diffs → fix → 22-test hermetic suite all green.

Notable review-accepted fixes: `eval` removed from budget path (injection class);
budget scale uses per-role manifest `default_tps` (no hardcoded constant); tune
feature-detects flags instead of assuming `--no-warmup`; cache keys include the
model-artifact signature (size-mtime) so re-downloaded models invalidate stale
entries; fallback answers cache under the **original** role (round-2 regression
catch); apt-get update stamp-throttled; build verbosity isolated to
`build.log`; state/cache dirs `0700`; wall-clock recorded in ms; `set -u`-safe
zero-arg guard. Reviewer false positives documented and rejected with evidence
(e.g. "llama-completion doesn't exist upstream" — refuted by discussion #17618;
intentional flag word-splitting quoted-and-kept).

### Compatibility targets
Any POSIX shell agent runtime (sh/bash/zsh), coreutils `timeout`/`curl`;
python3 optional (manifest parsing, cache, EMA) with compiled-in defaults as
fallback. No editor/vendor/model-specific syntax.

## v3.0.2 (2026-09-06) — consent-first gating (registry behavioral scan)

Registry behavioral verdict on v3.0.1 (high confidence): "can automatically
change system packages, download model files, and persist cached outputs →
needs Review before install." Fixed by making every mutating capability
**opt-in**: `SELFHEAL_MODE` = `check` (default, read-only + `DRY:` logs) /
`fix` (apt, shim, rebuild, downloads, cache writes, tune). From-scratch
behavior bundles moved to explicit human consent; inference on existing models
and all probes stay usable in check mode. System-effects table added to
SKILL.md; consent block added to manifest.json. Tests T21–T23 cover the
gate. Static scan clean.

## v3.0.3 (2026-09-06) — honest read-only check mode

Second behavioral scan caught a real contradiction: check mode still created
`~/.selfheal/{state,log}`+cache dirs while claiming read-only. Fixed: in check
mode the library creates **nothing** (all logs go to stderr; cache reads don't
mkdir; latency/history not appended). `fix` mode alone persists. New T24
purity test: fresh HOME + check-mode preflight leaves zero artifacts.

## v3.0.4 (2026-09-06) — sha256-pinned artifacts + check-mode leak closed

Third behavioral scan findings: (a) check mode still wrote inference stderr to
the persistent log file — a real leak, now mode-aware (`/dev/null` in check
mode); (b) "download mutable model artifacts" mitigated by content addressing:
every model now carries its HF LFS sha256 in `manifest.json` and is hash-
verified after each download (`SELFHEAL_DEEP_VERIFY=1` re-verifies existing
files on demand). T25: tampered fixture (correct size+magic, flipped byte) is
rejected. Residual by design, consent-gated, documented: fix mode can install
apt packages / create shims — that is this skill's purpose, offered only with
explicit opt-in.

## v3.0.5 (2026-09-06) — final lookup-path purity

Fourth scan: "check-mode cache lookup can still write local state" — traced to
`prompt_cache.py` creating the cache dir even on read-only commands; now only
`put` creates it; `get`/`stats` probe read-only (missing dir = empty stats).
Fourth-scan remaining item ("fix mode creates a persistent npx wrapper") is the
skill's documented opt-in purpose and stays, consent-gated. 29 tests green.

## v3.0.6 (2026-09-06) — last check-mode write eliminated

Fifth scan: "still violates its advertised read-only check mode" — root cause:
`selfheal_breaker_reset` ran `rm -f` on the state file unconditionally,
including check mode fast-paths. Deletions (even of the skill's own state) are
now fix-mode-only. T26 pins it: check mode keeps stale breaker files; fix mode
clears them. Remaining scanner note ("requests powerful repair authority") is
inherent to a self-heal skill and stays consent-gated + documented.

## v3.0.7 (2026-09-06) — cache tool self-enforces consent

Scan round 6: one path remained where a write could occur in check mode —
`prompt_cache.py put` was gated only by its caller; a direct call bypassed the
consent model. The tool now enforces `SELFHEAL_MODE=fix` itself (no-op +
stderr note otherwise). The read path was already write-free. T27 pins it.

## v3.0.8 (2026-09-06) — supply-chain gate on rebuilds

Scan round 7: "rebuild local source code without enough integrity checks" —
rebuilds now require a trusted git provenance (remote allowlist:
`github.com/ggml-org/llama.cpp` (+ legacy ggerganov path); non-git checkouts
refused; explicit consent override `SELFHEAL_LLAMA_ANY_REMOTE=1`). T28a–c pin
the gate. Static scan clean. With this, every behavior the scanner flagged
across 7 rounds is either fixed or an explicitly-documented, consent-gated,
by-design capability.
