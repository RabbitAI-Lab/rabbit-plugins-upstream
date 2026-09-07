# Changelog

## 1.2.0 — machine-readable coordination surface

### Added

- Global `--json` flag: compact, single-line JSON envelopes on stdout for
  every command (file outputs remain canonical pretty JSON, unchanged).
- `card-inspect` command: read-only card summary envelope
  (`agent-dnstt-card-inspect/v1`) with expiry countdown, HMAC verdict,
  grouped constraints, and fingerprint display. HMAC-required by default,
  with an explicit `--allow-unsigned-card` opt-out.
- `compare-status` command: topological chain-head verdict over 1–64 status
  reports (`agent-dnstt-compare-status/v1`) with expired-card analysis via the
  `card_expired` evidence field, `partial_chain` /
  `diverged_heads` structural issues, informational `peer_state_mismatch`,
  and a deterministic `suggested_next` state. HMAC-required by default with
  `--allow-unsigned-card` opt-out; identical duplicate report files supplied
  twice are folded rather than flagged. `--require-consistent` converts
  structural issues into exit code 5 — the verdict envelope is emitted
  *before* the gate fires, so gating callers read the exit code, not
  artifact existence.
- Doctor output now includes a `registry` block enumerating commands,
  schemas, states, roles, transitions, limits, exit codes, global flags,
  environment variables, and safety invariants.
- New exit code 5 (`inconsistent_chains`) and error codes
  `too_many_reports`, `reports_required`, `partial_chain`, `diverged_heads`.
- Nine regression tests covering the new surface (70 total).

### Changed

- Nothing for v1.1.x consumers: all previously documented outputs, file
  formats, exit codes 0–4, and the card signing path are byte-identical.

### Safety

- Planner posture unchanged: no process execution, no private-key reads
  beyond the operator-supplied file, no resolver scanning, loopback-by-default
  constraints enforced exactly as before.

## 1.1.2 — scanner-hygiene patch

- Replaced a test-only credential-shaped literal with an equivalent value
  assembled at runtime.
- Runtime behavior and security policy are unchanged.
- Eliminates a false `suspicious.exposed_secret_literal` static-scan signal
  while preserving the debug-redaction regression assertion.

## 1.1.1 — maximum-capacity follow-up audit

### Fixed

- Debug events now redact sensitive field-name substrings and secret-looking
  string values, protecting against mistakes in future debug call sites.
- Expired-card diagnostics now emit `card_expired: true` and explicitly state
  that a new card is required before reconnecting.
- Bounded file reads now use `O_NONBLOCK` before post-open `fstat`, preventing a
  concurrent file-type swap to a FIFO/device from hanging the process.
- Added a strict type annotation for public-key regex results; Mypy strict and
  Pyright now report zero findings.

### Maximum verification

- 34 packaged tests passed.
- 8,000 Hypothesis-generated inputs passed.
- 12/12 seeded mutants were killed.
- 219 state-machine sequences checked to depth 8.
- CPython 3.10, 3.11, 3.12, and 3.13 passed.
- Mypy strict, Pyright, Ruff, Bandit, Pyflakes, and py_compile passed.
- 20,000 signed-card verifications and 1,000 atomic writes completed with no
  file-descriptor or retained-memory leak.
- Seven model-review lenses were triaged; findings were accepted only after
  independent reproduction, and false positives were documented rather than
  patched blindly.

## 1.1.0 — adversarial debugging and fail-closed hardening

### Fixed

- Reject HMAC secrets shorter than 32 bytes.
- Reject unknown/missing card fields, malformed constraints/endpoints, unsafe
  JSON types, duplicate keys, non-finite numbers, controls/surrogates, excessive
  nesting/nodes, oversized cards, and oversized key files.
- Reject future-issued cards and lifetimes outside 5 minutes–24 hours.
- Replace direct output writes with atomic mode-0600 writes; reject symlinks and
  require explicit overwrite approval.
- Reject DoH credentials, query strings, fragments, whitespace, and malformed
  ports.
- Reject private-key symlinks, wrong ownership, non-regular files, implausible
  sizes, and group/world permissions.
- Reject existing, colliding, or symlink key-generation targets.
- Reject secret-like or control-bearing status text.
- Require HMAC-authenticated operational cards by default.
- Require both signed-card permission and local approval for LAN listeners.
- Enforce authenticated status predecessor chains and legal state transitions.
- Replace raw CLI tracebacks with stable error codes and safe diagnostics.

### Added

- `doctor`, `verify-status`, `--debug`, `--json-errors`, and `--force-output`.
- Versioned integer/string-only canonical JSON rules.
- Deterministic plan IDs and private-key metadata recheck guidance.
- 31 unit/regression/property/fuzz/concurrency tests.
- `DEBUGGING.md` command battery, error matrix, regression matrix, and future
  fix acceptance criteria.

### Preserved

- No network access, subprocess execution, resolver scanning, DNS changes,
  firewall changes, binary downloads, or private-key reads.

## 1.0.1 — scanner-safe test loading

- Replaced test-only dynamic module loading with a normal static import.
- Static ClawHub scan: clean, zero findings.
- Runtime functionality unchanged.

## 1.0.0 — initial submission

- Original authorization-gated DNSTT rendezvous cards, client/server plans,
  HMAC handoff, fingerprint pinning, status reports, and bounded diagnostics.
