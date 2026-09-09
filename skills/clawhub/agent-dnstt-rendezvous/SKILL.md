---
name: agent-dnstt-rendezvous
description: "Authorization-gated coordination skill for agents that need to plan, verify, and troubleshoot a DNSTT client/server link without sharing private keys, scanning resolvers, changing DNS/firewalls, or auto-executing tunnel commands. Uses short-lived rendezvous cards, out-of-band public-key fingerprints, optional HMAC authentication, loopback-by-default services, deterministic argv plans, and secret-free status handoffs. Use only on domains, resolvers, servers, and services the operator owns or is explicitly authorized to administer."
version: 1.2.0
license: MIT-0
categories: [operations, agents, communication]
topics: [operations, dnstt, agent-coordination, dns-tunneling, secure-rendezvous]
metadata:
  openclaw:
    emoji: "🛰️"
    requires:
      bins: [python3]
---

# 🛰️ Agent DNSTT Rendezvous

A distinct, original agent-coordination layer for **authorized DNSTT links**.
It does not implement DNSTT, copy another project's code, download binaries,
scan the public Internet, change DNS/firewalls, or start processes. It helps a
server agent, client agent, and optional observer agent agree on the same
short-lived connection facts and produce commands for a human to review.

## When to use

Use this skill when all of the following are true:

1. The operator owns or has written authorization for the tunnel domain,
   server, resolver, and upstream service.
2. A compatible `dnstt-server` and `dnstt-client` are already obtained from a
   trusted source and verified separately.
3. Agents need a safe handoff: domain, server public key, fingerprint,
   listener, loopback upstream, expiry, purpose, and authorization reference.
4. A human will review and execute any generated command.

Do **not** use it for covert access, policy evasion, unauthorized proxying,
data exfiltration, public-resolver sweeps, open proxies, or hiding activity from
network owners. DNSTT traffic is observable in DNS logs and is not an anonymity
system.

## Distinct design

This skill is a coordination protocol rather than a tunnel implementation:

- **Short-lived rendezvous cards** expire automatically.
- **Out-of-band key pinning** is mandatory for client plans.
- **Optional HMAC authentication** protects agent-to-agent card handoff.
- **No private key ever enters a card or client plan.**
- **Loopback by default:** server upstream and client listener are local-only.
- **No automatic execution:** commands are emitted as JSON argv arrays.
- **No network scanning:** only an operator-supplied resolver may be planned.
- **Secret-free status reports** let agents help each other diagnose which side
  is failing without exchanging credentials.

## Roles and cooperation protocol

### 🖥️ Server agent

1. Confirms written authorization and the intended single TCP service.
2. Generates a DNSTT keypair locally using a reviewed plan.
3. Keeps the private key mode `0600`; shares only the public key.
4. Creates a rendezvous card with an expiry and authorization reference.
5. Sends the card and public-key fingerprint through separate channels.
6. Produces a server command plan but never executes it automatically.

### 💻 Client agent

1. Receives the card and independently receives the public-key fingerprint.
2. Verifies card integrity, expiry, fingerprint, and optional HMAC.
3. Uses only the operator-approved UDP, DoH, or DoT resolver.
4. Keeps its local DNSTT listener on loopback unless LAN access was explicitly
   approved.
5. Produces a client plan and public-key-file handoff for human review.

### 👁️ Observer/helper agent

1. Compares client/server status reports by `card_id`.
2. Confirms timestamps and state transitions.
3. Runs only the bounded diagnostic checklist—never broad scans.
4. Helps classify a failure as delegation, key pinning, DNS path, listener,
   upstream service, or intermittent transport.

### State machine

`planned → authorized → configured → reachable → connected → verified → closed`

Failures use the `failed` state with a secret-free observation. Agents do not
advance state based on claims alone; each transition needs observable evidence.

## Installation

The skill helper uses Python's standard library only:

```bash
python3 scripts/rendezvous.py --help
python3 -m unittest discover -s tests -v
```

DNSTT binaries are optional external runtime dependencies for executing a
reviewed plan. This skill never downloads them.

## Debugging preflight

Run the read-only doctor and complete regression suite before any release or
when diagnosing unexpected behavior:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/rendezvous.py doctor
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

For structured, secret-free diagnostics, put global flags before the
subcommand:

```bash
python3 scripts/rendezvous.py --debug --json-errors verify-card \
  --card ./state/rendezvous-card.json \
  --expected-fingerprint 'sha256:<64-lowercase-hex>' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac
```

See `DEBUGGING.md` for the bug matrix, error codes, reproduction protocol,
property/fuzz/concurrency testing, and future-fix acceptance criteria.

## Authorized lab workflow

The examples use reserved documentation names and addresses. Replace them only
with infrastructure you are authorized to operate.

### 1. Server: request a key-generation plan

```bash
python3 scripts/rendezvous.py keygen-plan \
  --privkey-file ./state/server.key \
  --pubkey-file ./state/server.pub \
  --ack-authorized \
  --output ./state/keygen-plan.json
```

Review `command_argv`, run it manually, then protect the private key:

```bash
chmod 600 ./state/server.key
```

### 2. Server: create a short-lived card

```bash
export AGENT_LINK_SECRET='replace-with-a-strong-shared-coordination-secret'
python3 scripts/rendezvous.py server-card \
  --agent-id server-agent-a \
  --domain t.example.com \
  --pubkey-file ./state/server.pub \
  --listen 0.0.0.0:5300 \
  --upstream 127.0.0.1:8000 \
  --expires-minutes 30 \
  --authorization-ref LAB-2026-001 \
  --purpose 'authorized agent message service' \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/rendezvous-card.json
```

The card contains a public key, never a private key. Send the displayed
`sha256:<64hex>` public-key fingerprint to the client through a separate,
authenticated channel. Operational plans require an HMAC-authenticated card by
default; `--allow-unsigned-card` is an explicit offline-workflow waiver, not a
normal convenience flag.

### 3. Server: generate a reviewed server plan

```bash
python3 scripts/rendezvous.py server-plan \
  --card ./state/rendezvous-card.json \
  --privkey-file ./state/server.key \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/server-plan.json
```

The helper refuses private key files with group/world permissions. It does not
modify DNS, firewall rules, services, or systemd.

### 4. Client: verify the card

```bash
python3 scripts/rendezvous.py verify-card \
  --card ./state/rendezvous-card.json \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET
```

Use the real fingerprint received out of band. A mismatch is a hard stop.

### 5. Client: generate a reviewed client plan

```bash
python3 scripts/rendezvous.py client-plan \
  --card ./state/rendezvous-card.json \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --transport udp \
  --resolver 192.0.2.53:53 \
  --local-listen 127.0.0.1:7000 \
  --pubkey-file ./state/server.pub \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/client-plan.json
```

The output contains the public-key file content and a DNSTT client argv array.
It writes neither file and starts no process.

### 6. Agents exchange authenticated status chains

Start with `planned`:

```bash
python3 scripts/rendezvous.py status-report \
  --card ./state/rendezvous-card.json \
  --agent-id client-agent-b \
  --role client \
  --state planned \
  --message 'card verified; awaiting operator approval' \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac \
  --output ./state/client-planned.json
```

Each later state must provide the previous report. For example:

```bash
python3 scripts/rendezvous.py status-report \
  --card ./state/rendezvous-card.json \
  --agent-id client-agent-b \
  --role client \
  --state authorized \
  --message 'operator approval recorded' \
  --previous-report ./state/client-planned.json \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac \
  --output ./state/client-authorized.json
```

Verify a chained report with its predecessor:

```bash
python3 scripts/rendezvous.py verify-status \
  --card ./state/rendezvous-card.json \
  --status ./state/client-authorized.json \
  --previous-report ./state/client-planned.json \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac
```

Status messages containing token/password/private-key patterns or control
characters are rejected. The HMAC tag authenticates the report but is not the
secret itself.

## Read-only diagnostics

```bash
python3 scripts/rendezvous.py diagnose \
  --card ./state/rendezvous-card.json \
  --symptom no-response \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET
```

Available symptoms:

- `dns-delegation`
- `key-mismatch`
- `no-response`
- `connects-no-service`
- `intermittent`

Diagnostics print bounded checks. They never probe hosts or resolver ranges.

## DNSTT compatibility notes

DNSTT is a userspace TCP tunnel over delegated DNS, not a full VPN. A typical
server forwards incoming streams to a single TCP endpoint, while a client
opens a local TCP listener. Exact flags differ by build/fork; always compare the
plan with the installed binary's `--help` before execution.

A tunnel DNS zone normally needs an NS delegation to a nameserver hostname with
A/AAAA records for the authorized server. This skill does not create records.
The server plan defaults to UDP port 5300 so DNSTT need not run as root; an
operator may separately review port-53 forwarding. No firewall command is
created here.

## v1.1.0 debugging and hardening

A full adversarial audit reproduced and fixed twelve bug classes:

1. short HMAC secrets;
2. permissive card schemas/endpoints/constraints;
3. future-issued or overlong-lived cards;
4. duplicate/non-finite/oversized/over-complex JSON;
5. output symlink overwrite and partial-write risk;
6. DoH URLs containing credentials/query/fragment data;
7. private-key symlink and ownership/mode risks;
8. secret-bearing status messages marked safe;
9. unsigned operational cards accepted without an explicit waiver;
10. LAN listeners overriding a signed loopback-only card;
11. status reports skipping state transitions;
12. test-only dynamic imports triggering static security scans.

The fix set adds strict schemas, bounded no-follow reads, atomic mode-0600
writes, 32-byte HMAC minimum, safe binary/path parsing, dual-consent LAN
listeners, authenticated status chains, structured error codes, secret-free
debug events, a read-only doctor, and fail-closed CLI handling.

Verification in v1.1.0 included 31 unit/regression/property/fuzz/concurrency
tests: 500 signed-card round trips, 2,000 endpoint fuzz cases, 1,000 malformed
JSON cases, mutation checks, and 64 concurrent atomic writers.

## v1.1.1 maximum-capacity follow-up audit

A second independent audit added three more regression fixes:

- debug events now filter sensitive field-name substrings and secret-looking
  values, preventing future call sites from accidentally logging credentials;
- diagnostics now report `card_expired: true` and explicitly prohibit reuse of
  an expired card for reconnection;
- bounded input opens now include `O_NONBLOCK`, so a concurrent regular-file to
  FIFO/device swap cannot hang before post-open `fstat` rejects it.

The maximum audit ran 34 packaged tests, 8,000 Hypothesis examples, 12 mutation
variants (12/12 killed), 219 state sequences to depth 8, CPython 3.10–3.13,
Mypy strict, Pyright, Ruff, Bandit, Pyflakes, a 20,000-card/1,000-atomic-write
soak, and seven independent model-review lenses. The soak retained 17 KB after
garbage collection, kept file descriptors at 7→7, and found no leak.

Reviewer findings were independently reproduced before acceptance. False
positives—including the intentional `failed → planned` retry and conservative
hostname handling—were rejected rather than patched blindly.

## v1.2.0 machine-readable coordination surface

Additive release for multi-agent orchestration. No v1.1.x output or file
format changed; the canonical pretty-JSON signing path is byte-identical.

- **Global `--json`** (place before the subcommand, like `--debug` and
  `--json-errors`): every command emits one compact JSON envelope on stdout
  (canonical separators, deterministic key order of the schema). With
  `--output`, the canonical file is still written unchanged; the compact
  envelope replaces the printed path line. Without `--output`, behavior is
  the existing plain Python-JSON print — `--json` only changes the printed
  form.
- **`card-inspect`**: read-only card summary envelope
  `agent-dnstt-card-inspect/v1` — card_id, tunnel_domain, listener, upstream,
  expiry countdown, HMAC verdict, grouped safety constraints, grouped
  (colon-separated) fingerprint display. Runs the same `verify_card`
  fail-closed checks; no new trust surface. HMAC authentication is required
  by default on this observer path; pass `--allow-unsigned-card` to adopt an
  unsigned offline card explicitly.
- **`compare-status`**: observer-side verdict envelope
  `agent-dnstt-compare-status/v1` over 1–64 status reports sharing one
  card_id. Historical (expired) cards remain analyzable, their staleness
  surfaced as `card_expired: true` evidence rather than a hard gate.
  Rebuilds authenticated chains by `previous_status_id` links,
  reports the *topological* head per (agent_id, role) — never just the newest
  timestamp — and flags `partial_chain` (missing predecessor in the supplied
  set) and `diverged_heads` (two unlinked heads for one identity).
  Cross-role disagreement between server and client heads is surfaced as the
  informational `peer_state_mismatch`, never as a chain fault. HMAC
  authentication is required by default; `--allow-unsigned-card` opts out
  for offline reviews. Duplicate report files supplied more than once are
  folded (identical content) — they never fabricate a `diverged_heads` alarm.
  With `--require-consistent`, any structural issue exits with code **5**
  (`inconsistent_chains`) so orchestrators can gate on it. Gate semantics:
  the verdict envelope is emitted (stdout and/or `--output` file) *before*
  the exit code is raised, so a failing gate still leaves diagnostic evidence
  behind — callers must key their decision on the exit code, not on file
  existence. Filesystem failures dominate: a verdict-write error exits 3 and
  no consistency gate fires.
- **`doctor` registry block**: machine-readable enumeration of commands,
  schemas, states, roles, transitions, limits, exit codes, global flags, env
  vars, and safety invariants. Lets an orchestrator discover the callability
  contract without parsing prose.
- New [ERROR REFERENCE] codes: `too_many_reports`, `inconsistent_chains`,
  `reports_required`, `partial_chain`, `diverged_heads`.

## Safety boundaries

- Never expose an unauthenticated general-purpose proxy.
- Keep the server upstream loopback-bound and application-authenticated.
- Keep client listeners loopback-bound unless LAN access is explicitly needed.
- Limit card lifetime, sessions, query rate, and upstream scope.
- Treat DNS resolvers and network operators as able to observe tunnel metadata.
- Never include private keys or coordination secrets in cards, logs, status
  reports, prompts, issue reports, or chat.
- Do not use a DNS tunnel where policy or law forbids it.
- Stop and close the session after the authorized task.

## Originality and inspiration

No source code, UI, configuration format, profile URI, branding, assets, or text
was copied from the referenced projects. Architectural lessons were studied at
a high level: client/server role separation, resolver-aware health, explicit
profiles, key pinning, bounded service management, and clear diagnostics. This
skill's card schema, HMAC handoff, state machine, safety gates, planner, tests,
and documentation are original.

See `references/INSPIRATION.md` for project links, license boundaries, and the
specific ideas that were transformed rather than copied.
