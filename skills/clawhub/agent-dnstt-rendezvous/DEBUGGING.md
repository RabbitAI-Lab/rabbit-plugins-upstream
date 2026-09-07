# 🧰 Debugging and bug-fixing standard

This guide is mandatory for every Agent DNSTT Rendezvous change. It favors
small reproducible failures, fail-closed behavior, structured diagnostics, and
proof that safety invariants still hold.

## 1. First-response command battery

Run from the skill directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/rendezvous.py doctor
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/rendezvous.py tests/test_*.py
python3 /home/user/tools/validate_skill_metadata.py .
python3 /home/user/tools/validate_skill_readme.py .
```

If `pyflakes` is available:

```bash
pyflakes scripts/rendezvous.py tests/test_*.py
```

Do not debug by running a real tunnel first. Reproduce card, parser, planner,
status, or output behavior locally with documentation addresses and temporary
files.

## 2. Safe diagnostics

Global flags must precede the subcommand:

```bash
python3 scripts/rendezvous.py --debug --json-errors verify-card \
  --card ./state/card.json \
  --expected-fingerprint 'sha256:<64-lowercase-hex>' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac
```

- `--debug` emits bounded JSON events to stderr.
- Debug events omit messages, keys, public-key material, and secrets.
- `--json-errors` emits a stable error code and safe explanation.
- Never attach raw private keys, HMAC secrets, resolver credentials, or cards
  containing internal authorization details to bug reports.

Useful error classes include:

| Code | Meaning | First check |
|---|---|---|
| `duplicate_json_key` | Ambiguous card/status JSON | Regenerate with this tool; do not hand-edit |
| `object_id_mismatch` | Content changed after ID creation | Compare card copies and regenerate |
| `hmac_mismatch` | Wrong secret or modified card/status | Verify secret source and handoff channel |
| `hmac_required` | Operational plan received unsigned card | Use HMAC or explicitly approve offline waiver |
| `fingerprint_mismatch` | Server key differs from out-of-band pin | Stop; re-verify with server operator |
| `future_card` / `expired_card` | Clock or stale handoff | Check UTC clocks; issue a new card |
| `invalid_card_ttl` | Lifetime outside 5 min–24 h | Use a short task-appropriate lifetime |
| `output_symlink` | Unsafe output destination | Choose a regular file in a trusted directory |
| `private_key_permissions` | Private key is too broadly readable | Set mode 0600 or stricter |
| `sensitive_status_message` | Report may leak a secret | Replace with a non-secret observation |
| `too_many_reports` | compare-status got >64 reports | Split the batch per chain |
| `reports_required` | compare-status with no `--report` | Supply at least one status ops file |
| `inconsistent_chains` | `--require-consistent` set and a structural issue found | Inspect `issues`; reconcile agents off-band. The verdict envelope is still emitted before rc5 fires |

Two entries inside the `compare-status` `issues` array are **labels, not
process error codes**: `partial_chain` (a supplied report references a
predecessor outside the supplied set) and `diverged_heads` (one agent/role
produced unlinked chain heads). They are fatal only via `--require-consistent`.

| `invalid_state_transition` | Status chain skipped/rewound state | Supply the correct previous report |
| `internal_error` | Unexpected CLI-boundary failure | Reproduce with tests and report error type only |

Exit codes: 0 success; 2 rendezvous/domain error; 3 filesystem error;
4 unexpected internal error; 5 consistency failure raised only by
`compare-status --require-consistent` or a `ConsistencyError`. Exit-code
precedence: filesystem failures (3) dominate the consistency gate — if the
verdict write itself fails, rc3 fires and no rc5 decision was possible.

## 3. Reproduction protocol

For every bug:

1. Record the skill version, Python version, command/subcommand, exit code, and
   structured error code.
2. Reduce the failure to the smallest card/status/input possible.
3. Replace real domains, IPs, keys, paths, and authorization references with
   documentation values.
4. Add a failing regression test before changing production code.
5. Confirm the test fails for the intended reason—not because of unrelated
   environment state.
6. Fix the narrowest invariant and rerun the complete suite.
7. Regenerate README `TREE-SHA256-v1`; never edit the digest manually.

## 4. Bug-class checklist

### Parsing and schema

- Cap file sizes before decoding.
- Reject symlinks and non-regular files.
- Reject duplicate JSON keys, NaN/Infinity, floats in signed objects, unsafe
  Unicode/control characters, excess depth, and excess node count.
- Reject unknown/missing card or status fields.
- Validate every field again after parsing; never trust a matching hash alone.

### Authentication and cryptography

- Use at least 32 bytes for the HMAC-SHA-256 coordination secret.
- Compare IDs, HMACs, and fingerprints with `hmac.compare_digest`.
- Treat unkeyed `card_id` as accidental-change detection, not authentication.
- Require HMAC on operational plans by default.
- Require a separately received server public-key fingerprint on clients.
- Never read or transmit the DNSTT server private key.

### Time and replay

- Reject issue times more than five minutes in the future.
- Limit cards to 5 minutes–24 hours.
- Reject expired cards for live operations.
- Chain status reports through `previous_status_id` and validate transitions.

### Filesystem

- Write JSON through same-directory temporary files, mode 0600, `fsync`, and
  `os.replace`.
- Refuse output symlinks and accidental overwrites.
- Refuse existing/symlink key-generation targets.
- Reject private-key symlinks, non-regular files, wrong ownership, empty/huge
  files, and group/world permissions.

### Commands and URLs

- Keep plans as argv arrays; never invoke a shell or subprocess.
- Permit only simple binary names or safe filesystem paths.
- Keep shell previews informational and correctly quoted.
- Reject DoH userinfo, queries, fragments, whitespace, and malformed ports.
- Require both a signed-card allowance and a local explicit override for LAN
  client listeners.

### Logging and reports

- Never log credentials, HMAC secrets, private keys, tokens, passwords, or raw
  sensitive cards.
- Reject control characters and secret-like status messages.
- Keep diagnostics read-only and resolver-list-free.

## 5. Test strategy

The suite combines:

- unit tests for each parser, validator, planner, and safety gate;
- regression tests for every discovered bug;
- 500 signed-card round trips;
- 2,000 randomized endpoint inputs;
- 1,000 malformed JSON inputs;
- top-level card mutation checks;
- 64-way atomic-writer contention;
- state-machine invariants;
- secret-detection corpus;
- end-to-end client/server/status handoff with no network or execution.

Maximum-capacity follow-up checks additionally include 8,000 Hypothesis
examples, 12 seeded mutants, 219 state sequences to depth 8, CPython 3.10–3.13,
Mypy strict, Pyright, Ruff, Bandit, Pyflakes, and a 20,000-card/1,000-write
resource soak with file-descriptor and retained-memory assertions.

All tests must pass with `PYTHONDONTWRITEBYTECODE=1` so test caches do not enter
the published artifact.

## 6. Current regression matrix

| ID | Former defect | Permanent regression |
|---|---|---|
| B1 | 16-byte HMAC accepted | 32-byte minimum test |
| B2 | Malformed endpoints/constraints/unknown fields accepted | strict schema tests |
| B3 | Future-issued cards accepted | clock-skew/TTL tests |
| B4 | Duplicate JSON keys silently overwrote | strict JSON duplicate test |
| B5 | Output symlink target could be overwritten | atomic/symlink test |
| B6 | DoH URL could contain credentials | URL userinfo/query/fragment tests |
| B7 | Private-key symlink passed mode check | lstat/symlink test |
| B8 | Secret-bearing status marked safe | secret corpus/control-character tests |
| B9 | Operational unsigned card accepted silently | HMAC-by-default/explicit-waiver test |
| B10 | LAN listener override contradicted signed card | dual-consent constraint test |
| B11 | Status states could skip transitions | chained state-machine tests |
| B12 | Test dynamic import triggered scanner | static import and static-scan gate |
| B13 | Future debug call could log a sensitive-looking field/value | substring/value redaction test |
| B14 | Expired-card diagnostics did not prominently forbid reconnection | explicit expiry warning test |
| B15 | File could change to FIFO between `lstat` and `open` and block | `O_NONBLOCK` + post-open `fstat` race test |

## 7. Future-fix acceptance criteria

A fix is complete only when:

- the original failure has a named regression test;
- all unit/property/fuzz/concurrency tests pass;
- py_compile and pyflakes pass;
- `doctor` passes;
- no network/subprocess import has appeared;
- metadata and README validators pass;
- non-secret debug/error output is actionable;
- `TREE-SHA256-v1` is regenerated;
- ClawHub static and asynchronous security scans are respected, never bypassed.

## 8. Sources behind these practices

- Python JSON hooks and repeated-name behavior:
  https://docs.python.org/3/library/json.html
- OWASP Logging Cheat Sheet (exclude tokens, passwords, keys, sensitive data;
  sanitize untrusted event text):
  https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Logging_Cheat_Sheet.md
- RFC 2104 HMAC design:
  https://www.rfc-editor.org/rfc/rfc2104
- RFC 8785 canonical-JSON design principles (this skill uses a narrower,
  versioned integer/string-only canonical form rather than claiming full JCS):
  https://www.rfc-editor.org/rfc/rfc8785
- Atomic replacement discussion and failure modes:
  https://bugs.python.org/issue8604
- Upstream DNSTT setup and MTU/delegation behavior:
  https://www.bamsoftware.com/software/dnstt/
