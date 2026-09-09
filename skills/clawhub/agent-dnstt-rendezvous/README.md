# 🛰️ Agent DNSTT Rendezvous

**Categories:** operations, agents, communication

**Public tags:** #operations, #dnstt, #agent-coordination, #dns-tunneling, #secure-rendezvous

## ✨ Functionalities

Agent DNSTT Rendezvous is an original, authorization-gated coordination skill
for agents that must prepare a DNSTT client/server link without silently
executing commands or sharing private keys. Its complete functionality is:

- create short-lived `agent-dnstt-rendezvous/v1` server cards;
- bind each card to an authorization reference, purpose, expiry, and nonce;
- include only the server public key and its SHA-256 fingerprint;
- optionally authenticate agent-to-agent card handoff with HMAC-SHA-256;
- detect card editing through a canonical JSON card ID;
- require an independently received server fingerprint before client planning;
- produce DNSTT server key-generation, server, and client commands as JSON argv
  arrays and shell previews without running them;
- plan UDP, DoH, or DoT client transports using one operator-supplied resolver;
- keep server upstreams and client listeners on loopback by default;
- reject broad private-key permissions and never read private-key contents;
- describe the public-key file a client should create without writing it;
- create HMAC-authenticated, secret-free client/server/observer status chains
  with enforced state transitions and predecessor verification;
- provide bounded diagnostics for delegation, key mismatch, no response,
  connected-without-service, and intermittent transport;
- parse cards/status JSON with strict size, depth, duplicate-key, finite-number,
  Unicode, field, endpoint, time, and constraint validation;
- write outputs atomically with mode 0600 while refusing symlinks and accidental
  overwrites;
- emit stable machine-readable error codes and bounded secret-free debug events;
- emit compact single-line JSON envelopes for every command via global `--json`;
- summarize cards read-only with `card-inspect`
  (`agent-dnstt-card-inspect/v1`);
- cross-compare authenticated status chains with `compare-status`
  (`agent-dnstt-compare-status/v1`), with topological head detection,
  partial-chain/diverged-heads issues, and an optional exit-code-5
  consistency gate;
- expose a machine-readable `registry` block in `doctor` (commands, schemas,
  states, transitions, limits, exit codes, safety invariants);
- run a read-only doctor plus unit, regression, property, fuzz, mutation, and
  concurrency checks;
- enforce an explicit authorization acknowledgement and HMAC-by-default policy
  on operational plans;
- run without downloads, subprocesses, DNS changes, firewall changes, active
  probes, resolver sweeps, or network access.

The skill is a planner and handoff protocol—not a DNSTT implementation, VPN,
proxy, anonymity system, or automatic deployment tool.

## 🚀 Usage

Install the skill, run its unit tests, and use the helper's subcommands to
create a server card, verify it on the client, and generate human-reviewed
client/server argv plans. The helper never executes those plans. The examples
below show the complete authorized workflow and the status/diagnostic handoff
agents use to help each other connect safely.

### Install and test

```bash
npx --yes clawhub@latest install @orionshaowswmw/agent-dnstt-rendezvous
cd skills/@orionshaowswmw/agent-dnstt-rendezvous
python3 scripts/rendezvous.py --help
PYTHONDONTWRITEBYTECODE=1 python3 scripts/rendezvous.py doctor
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

For a structured failure report, put global flags before the subcommand:

```bash
python3 scripts/rendezvous.py --debug --json-errors verify-card \
  --card ./state/card.json \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac
```

See `DEBUGGING.md` for the bug matrix and future-fix protocol.

### Server agent workflow

Create a reviewed key-generation plan:

```bash
python3 scripts/rendezvous.py keygen-plan \
  --privkey-file ./state/server.key \
  --pubkey-file ./state/server.pub \
  --ack-authorized \
  --output ./state/keygen-plan.json
```

After a human runs the reviewed external command and protects the private key,
create a 30-minute card:

```bash
export AGENT_LINK_SECRET='use-a-strong-coordination-secret'
python3 scripts/rendezvous.py server-card \
  --agent-id server-agent-a \
  --domain t.example.com \
  --pubkey-file ./state/server.pub \
  --listen 0.0.0.0:5300 \
  --upstream 127.0.0.1:8000 \
  --expires-minutes 30 \
  --authorization-ref LAB-2026-001 \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/card.json
```

Generate, but do not execute, the server plan:

```bash
python3 scripts/rendezvous.py server-plan \
  --card ./state/card.json \
  --privkey-file ./state/server.key \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/server-plan.json
```

### Client agent workflow

Receive the server fingerprint through an independent authenticated channel,
then verify the card and generate a client plan:

```bash
python3 scripts/rendezvous.py client-plan \
  --card ./state/card.json \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --transport udp \
  --resolver 192.0.2.53:53 \
  --local-listen 127.0.0.1:7000 \
  --pubkey-file ./state/server.pub \
  --hmac-env AGENT_LINK_SECRET \
  --ack-authorized \
  --output ./state/client-plan.json
```

The output contains a reviewed argv plan and public-key file handoff. The helper
writes neither key file and starts no process.

### Agents help each other

Start an authenticated status chain at `planned`:

```bash
python3 scripts/rendezvous.py status-report \
  --card ./state/card.json \
  --agent-id client-agent-b \
  --role client \
  --state planned \
  --message 'card verified; awaiting approval' \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET \
  --require-hmac \
  --output ./state/client-planned.json
```

Every later state supplies `--previous-report`; invalid jumps are rejected.
`verify-status` checks the HMAC, predecessor ID, agent/role identity, and state
transition. Status messages that resemble passwords, tokens, or private keys
are rejected rather than marked safe.

Use read-only diagnosis when states disagree:

```bash
python3 scripts/rendezvous.py diagnose \
  --card ./state/card.json \
  --symptom no-response \
  --expected-fingerprint 'sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef' \
  --hmac-env AGENT_LINK_SECRET
```

## 🔐 Permissions & Requirements

The planner itself needs only Python and narrowly scoped read/write access to
operator-selected files. It performs no subprocess, socket, DNS, HTTP, package,
firewall, or privilege operation. External DNSTT binaries and network access
are required only if a human separately approves and executes the generated
plan on authorized infrastructure.

### Required by this skill

- **Python:** Python 3.10+ standard library.
- **Read access:** user-selected public-key file, rendezvous-card JSON, and—for
  `server-plan` only—the private-key file's existence and permission metadata.
  The private-key contents are never read.
- **Write access:** only paths explicitly supplied with `--output`; files are
  atomically written mode 0600, symlinks are refused, and replacement requires
  `--force-output`.
- **Environment:** optional coordination secret of at least 32 bytes from the
  environment variable named by `--hmac-env`; its value is used in memory and
  never printed.
- **Processes/system calls:** none. The helper uses no subprocess execution.
- **Network:** none. The helper performs no DNS query, HTTP request, scan, or
  socket connection.
- **Privileges:** none. It does not require root or sudo.

### Optional external execution requirements

A human who chooses to execute a reviewed plan separately needs compatible
`dnstt-server`/`dnstt-client` binaries, an authorized delegated subdomain, an
authorized server reachable for DNS, an approved resolver, and a deliberately
scoped TCP upstream. External DNSTT execution may require reviewed UDP/53
routing or firewall configuration; this skill neither requests nor changes it.

## 🔒 Security & Privacy

The helper reads only the selected public-key/card inputs, private-key file
metadata, and optional HMAC secret; it collects no telemetry and sends no data
to any network endpoint. Outputs remain local unless the operator shares them.
Secrets are never embedded or logged. The main risks are unauthorized tunnel
use, open-proxy exposure, key substitution, stale cards, and observable DNS
metadata; mitigations include explicit authorization, loopback defaults,
short expiry, HMAC, out-of-band fingerprint pinning, least privilege, and
review of every generated command before execution.

### Data read and stored

- Reads the public DNSTT key, card JSON, and operator-supplied command options.
- Reads only file mode metadata from the private-key path; never its contents.
- Reads the optional HMAC coordination secret from one named environment
  variable and keeps it only in process memory.
- Stores JSON only when an explicit `--output` path is supplied.

### Data sent off-machine

The helper sends **no data anywhere** and has no network code. If a human later
executes a generated DNSTT plan, tunnel traffic and metadata leave the machine
through the chosen DNS resolver and authorized server. DNS operators may log
query names, timing, volume, source addresses, and the delegated domain even
though DNSTT payloads are encrypted.

### Secret handling

- The server private key never enters cards, plans, status reports, prompts, or
  logs and must remain server-side with mode `0600` or stricter.
- The public key is not secret, but its fingerprint must be compared through an
  independent authenticated channel.
- The HMAC secret must be at least 32 bytes, supplied by environment variable,
  and must not be placed in command arguments, README examples, cards, or chat.
- Rotate keys and coordination secrets after suspected exposure.

### Risks and mitigations

- **Unauthorized tunneling or policy violation:** hard authorization gate,
  authorization reference, no execution, and explicit prohibited-use rules.
- **Open-proxy abuse:** loopback upstream by default; use an authenticated,
  task-scoped service rather than a public general-purpose proxy.
- **Key substitution:** mandatory out-of-band public-key fingerprint on client
  plans plus optional card HMAC.
- **Stale/replayed handoff:** short expiry, nonce, card ID, and state timestamps.
- **LAN exposure:** client listener is loopback-only unless explicitly
  overridden and reviewed.
- **DNS metadata/privacy:** assume resolvers and network operators can observe
  metadata; do not place secrets in domains, status text, or card fields.
- **Resolver abuse:** no scanning or discovery; accept only an operator-supplied
  resolver.
- **Unsigned handoff:** operational plans require HMAC by default; use
  `--allow-unsigned-card` only for an explicitly approved offline workflow.
- **Malformed/tampered files:** bounded no-follow reads, strict JSON/schema
  checks, atomic writes, and card/status HMACs fail closed.
- **Command drift between DNSTT forks:** compare every plan with the installed
  binary's `--help` before execution.

Review `SKILL.md`, `scripts/rendezvous.py`, the tests, and
`references/INSPIRATION.md` before installation. Use only on infrastructure you
own or are explicitly authorized to administer.

## 🧰 Debugging and future bug prevention

Version 1.1.2 applies two full rounds of strict, regression-tested debugging
plus a scanner-hygiene patch for a test-only credential fixture:

- reproduce with documentation values and temporary files—never live traffic;
- add a failing named test before each fix;
- use stable error codes and secret-free JSON diagnostics;
- enforce parser/schema/time/filesystem/HMAC/state-machine invariants;
- run 34 packaged tests covering 500 signed-card round trips, 2,000 endpoint
  fuzz cases, 1,000 malformed JSON cases, top-level mutations, and 64
  concurrent writers;
- run an additional 8,000-example Hypothesis campaign, 12 mutation variants,
  219 state-machine sequences, CPython 3.10–3.13, Mypy strict, Pyright, Ruff,
  Bandit, Pyflakes, and a 20,000-card/1,000-write leak soak;
- require `doctor`, metadata validation, README validation, and regenerated
  TREE-SHA256-v1 before release;
- independently reproduce reviewer claims and reject false positives;
- respect ClawHub scans rather than bypassing warnings.

The second pass hardened future debug redaction, added explicit expired-card
warnings, and prevented a file-type swap to a FIFO/device from blocking input.
`DEBUGGING.md` contains the complete command battery, error matrix, fifteen-bug
regression table, and acceptance criteria for every future fix.

## 🧭 Originality and third-party boundaries

This skill was inspired by high-level client/server, profile, health-state,
key-pinning, and diagnostic concepts observed in projects by anonvector and
WhiteDNS. No source code, assets, branding, UI, profile format, configuration
schema, resolver list, installer, or text was copied. WhiteDNS-Android is
source-available under restrictive terms; this skill does not derive from or
redistribute it. See `references/INSPIRATION.md` for links and license notes.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `ec6273e540864985af970255a2d61ea520b2936e0ab798609457705d54f94b03`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', '.hypothesis', 'htmlcov'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store', '.coverage'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.
