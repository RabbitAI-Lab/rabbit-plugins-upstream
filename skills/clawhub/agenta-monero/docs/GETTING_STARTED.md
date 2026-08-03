# Getting Started with Agenta-Monero

A guide for **new users** to install the Agenta-Monero skill and connect it to Monero (local node or remote node).

---

## How this skill fits together (read this first)

```
┌─────────────┐    JSON-RPC     ┌────────────────────┐    P2P     ┌──────────────┐
│   Agent     │ ─────────────▶ │ monero-wallet-rpc  │ ─────────▶ │   monerod    │
│  + skill    │   127.0.0.1    │  (you run this)    │            │ (the daemon) │
└─────────────┘    :18088       └────────────────────┘            └──────────────┘
                     ▲                                                     ▲
                     │                                                     │
              the skill talks                                        can be LOCAL
              to THIS (the wallet                  (you run `monerod`)  ── or REMOTE ──
              RPC, always on your                                       (a public node)
              machine)
```

---

## Quick Start — Choose Your Path

### Path 1: Agent-Driven (recommended)

Tell your Hermes agent: **"Set up the Agenta-Monero skill."** The agent will:
1. Ask for your wallet file path and password.
2. Ask: local daemon or remote node?
3. Generate secure credentials, write `.env`, start `monero-wallet-rpc`, and verify readiness.

The agent passes flags: `--wallet-path`, `--wallet-password`, `--network`, `--daemon-type`, `--force`

**Prerequisites:** `monero-wallet-rpc` installed + a wallet file created.
- Download Monero CLI tools: https://getmonero.org/downloads/
- Create a wallet: `monero-wallet-cli --generate-new-wallet ~/Monero/wallets/main --password 'PASS'`
- (Stagenet for testing: add `--stagenet`, use https://stagenet-faucet.xmr-tw.org/ for free funds)

### Path 2: Interactive Script

```bash
./scripts/interactive_setup.sh
```
Follow the prompts — it does the same as Path 1 but you drive it yourself.

### Path 3: Step-by-Step (Advanced)

See the detailed walkthrough below. Use this if you want full control over each component.

---

Two things to understand:

1. **The skill always talks to `monero-wallet-rpc` on your own machine** (`http://127.0.0.1:18088`). You run `monero-wallet-rpc`; it holds your wallet file and keys.
2. **`monero-wallet-rpc` talks to a `monerod` daemon**, which can be:
   - **Local** — you run `monerod` yourself (full node, best privacy, slow first sync), or
   - **Remote** — a public node (fast setup, lighter). Use `--untrusted-daemon` for privacy.

So "**connect to a remote node**" means telling your *wallet-rpc* to use a remote daemon — **not** pointing the skill at a remote server. The skill's `MONERO_RPC_URL` stays `http://127.0.0.1:18088`.

> **First time? Use stagenet** (`--stagenet`, ports `38xxx`). Mainnet syncs for hours–days and real funds are at risk. See the stagenet path below.

---

## Prerequisites

- **OS:** Linux or macOS (Windows not supported)
- **Monero CLI tools** (`monerod`, `monero-wallet-cli`, `monero-wallet-rpc`) ≥ **0.18.0** — from https://getmonero.org/downloads/ or your package manager.
- **Bash ≥ 4**, `curl`, `jq`, `flock` (util-linux) — standard on Linux/macOS (`brew install jq` on macOS).
- **Agent:** Hermes or OpenClaw installed.

Check:
```bash
monero-wallet-rpc --version
bash --version | head -1
command -v curl jq flock
```

---

## Step 1 — Create a wallet (once)

Create a wallet file with `monero-wallet-cli`. **Write down the 25-word seed** it shows — that's the only way to recover funds.

**Mainnet:**
```bash
mkdir -p ~/Monero/wallets
monero-wallet-cli --generate-new-wallet ~/Monero/wallets/main --password 'WALLET_PASS'
# ... note the seed mnemonic, then type `exit`
```

**Stagenet (recommended for testing):**
```bash
mkdir -p ~/Monero/stagenet
monero-wallet-cli --stagenet --generate-new-wallet ~/Monero/stagenet/wallet --password 'WALLET_PASS'
```

> Fund a stagenet wallet free at https://stagenet-faucet.xmr-tw.org/ (or search "monero stagenet faucet").

---

## Step 2 — Start the daemon (choose local OR remote)

### Option A — Local node (full node, best privacy)

**Mainnet** (sync takes a long time the first run):
```bash
monerod --detach              # or run in a foreground terminal
```
**Stagenet:**
```bash
monerod --stagenet --detach
```
Daemon RPC ports: **mainnet `18081`**, **stagenet `38081`**. Check progress: `monerod -- status` or `tail -f ~/.bitmonero/bitmonero.log`.

### Option B — Remote node (fast, no local sync)

Skip running `monerod`; instead point `monero-wallet-rpc` at a public node in Step 3 with `--daemon-address <host>:<port> --untrusted-daemon`. Public nodes: https://monero.fail/ (pick one on your network — mainnet `:18081`, stagenet `:38081`).

> **Privacy:** always use `--untrusted-daemon` with a remote node so your wallet doesn't reveal more than necessary to a third party.

---

## Step 3 — Start `monero-wallet-rpc` (the thing the skill talks to)

Run this in its own terminal (or `--detach`). It loads your wallet and listens on `127.0.0.1:18088`.

**Mainnet + LOCAL daemon:**
```bash
monero-wallet-rpc \
  --wallet-file ~/Monero/wallets/main --password 'WALLET_PASS' \
  --rpc-bind-port 18088 --rpc-login username:password \
  --daemon-address 127.0.0.1:18081 --trusted-daemon
```

**Mainnet + REMOTE daemon (no local `monerod`):**
```bash
monero-wallet-rpc \
  --wallet-file ~/Monero/wallets/main --password 'WALLET_PASS' \
  --rpc-bind-port 18088 --rpc-login username:password \
  --daemon-address node.example.com:18081 --untrusted-daemon
```

**Stagenet + LOCAL daemon (recommended for first run):**
```bash
monero-wallet-rpc --stagenet \
  --wallet-file ~/Monero/stagenet/wallet --password 'WALLET_PASS' \
  --rpc-bind-port 38088 --rpc-login username:password \
  --daemon-address 127.0.0.1:38081 --trusted-daemon
```

Notes:
- `--rpc-login username:password` — choose your own username and a strong password; the skill authenticates with these (via a netrc file, never on the command line).
- `--rpc-bind-ip 127.0.0.1` is the default (loopback only). Do **not** expose the wallet RPC to the network without TLS + auth.
- **Remote wallet-RPC** (uncommon — wallet-rpc on another server): add `--rpc-ssl enabled --rpc-ssl-autodetect`, bind to `0.0.0.0`, and set the skill's `MONERO_RPC_URL=https://server:port` plus `MONERO_RPC_SSL_CACERT` if self-signed.

Leave it running, then verify it responds:
```bash
curl -u username:password --digest \
  -X POST http://127.0.0.1:18088/json_rpc \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}' -H 'Content-Type: application/json'
```

---

## Step 4 — Install the skill (manual copy — recommended)

**Do I tell the agent to install it?** No. Hermes and OpenClaw **auto-discover** any skill directory containing a `SKILL.md` under their skills folder. So you place the skill there yourself; the agent picks it up automatically.

**Why manual copy (not `hermes skills install`)?** `hermes skills install <url>` is for skills published to a hub/URL and pulls only `SKILL.md` + detected references. This skill is **script-heavy** (`scripts/*.sh`, `lib/*.sh`); a manual copy guarantees every file lands in place.

**Hermes:**
```bash
mkdir -p ~/.hermes/skills/finance
cp -r agenta-monero ~/.hermes/skills/finance/agenta-monero
cd ~/.hermes/skills/finance/agenta-monero
```

**OpenClaw:**
```bash
mkdir -p ~/.openclaw/workspace/skills/finance
cp -r agenta-monero ~/.openclaw/workspace/skills/finance/agenta-monero
cd ~/.openclaw/workspace/skills/finance/agenta-monero
```

(If you've published the skill to a GitHub repo and prefer the CLI: `hermes skills install https://your-repo/SKILL.md` — but verify `scripts/` and `lib/` came along afterwards.)

---

## Step 5 — Configure `.env`

```bash
# Hermes:
cd ~/.hermes/skills/finance/agenta-monero

# OpenClaw:
cd ~/.openclaw/workspace/skills/finance/agenta-monero

cp .env.example .env
chmod 600 .env
```

Edit `.env` — set at least these:
```bash
MONERO_RPC_URL="http://127.0.0.1:18088"   # 127.0.0.1:38088 for stagenet
MONERO_RPC_USER="username"               # same as --rpc-login username from Step 3
MONERO_RPC_PASSWORD="password"            # same as --rpc-login password from Step 3
MONERO_NETWORK="mainnet"                  # mainnet | stagenet
```
Leave the rest at defaults. Keep `.env` out of version control (the skill's `.gitignore` already excludes it).

---

## Step 6 — Run `setup.sh` (readiness check)

```bash
./setup.sh
```
Expect:
```json
{"ready":true,"deps_ok":true,"config_ok":true,"connection_ok":true,"wallet_loaded":true,"version":196613,"warnings":[]}
```
- `ready:true` → you're set.
- `connection_ok:false` → wallet-rpc isn't running / wrong port or creds (see Troubleshooting).
- `wallet_loaded:false` → wallet-rpc is up but no wallet is loaded. Fix by starting wallet-rpc with `--wallet-file` (Step 3), then re-run `setup.sh`.

---

## Step 7 — Use it

You can now either **ask the Hermes agent** in plain language, or **run scripts directly**.

Ask the agent, e.g.:
> "Generate a Monero subaddress labelled 'invoice 42'."
> "Send 1.5 XMR to 88bc…, dry-run first to preview the fee."
> "Check my balance and how many blocks are locked."

Or run a script directly (from the skill directory):
```bash
./scripts/sync_status.sh
./scripts/create_address.sh --label "invoice 42"
./scripts/estimate_fee.sh --address 88bc… --amount 1.5
./scripts/send_xmr.sh --address 88bc… --amount 1.5 --dry-run    # preview, no broadcast
./scripts/send_xmr.sh --address 88bc… --amount 1.5              # actually send
./scripts/get_transfer.sh --tx-hash <hash>                      # confirm it landed
./scripts/check_balance.sh
```

Every script prints JSON on stdout and structured errors on stderr. Full per-operation details: see `SKILL.md` and `references/`.

---

## Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `RPC_UNREACHABLE` | wallet-rpc not running, wrong `MONERO_RPC_URL` port, or wrong `--rpc-login` creds. Re-run the curl check in Step 3. |
| `connection_ok:false` from setup | same as above. |
| `wallet_loaded:false` | wallet-rpc is up but no wallet open — start it with `--wallet-file … --password …`. |
| `CONFIG_INVALID` on `.env` | a line has shell metacharacters (`$ \` ( ) { } ; | & < >`) — the parser rejects them on purpose; simplify the value. |
| Send times out / unsure if it sent | **do not just retry.** Run `./scripts/get_transfer.sh --tx-hash <hash>`. `TX_NOT_FOUND` → safe to retry. `RPC_UNREACHABLE` → status unknown, fix connectivity first, do **not** retry. |
| Huge `daemon_connected`/stale balance | wallet isn't synced. Let `monerod` finish syncing (or wait for `monero-wallet-rpc` to refresh). |
| Remote node rejected / slow | pick a different node from https://monero.fail/; keep `--untrusted-daemon`. |

More: `references/error-runbook.md`.

---

## Lifecycle Management

After setup, `monero-wallet-rpc` runs in the background. Manage it with the following.

### Start

Run `./scripts/interactive_setup.sh --force` to restart with the existing `.env`, or start `monero-wallet-rpc` manually (see Step 3).

### Stop

```bash
./scripts/stop_wallet_rpc.sh
# or: kill $(cat $MONERO_LOCK_DIR/wallet-rpc.pid)
```

### Check status

```bash
./scripts/wallet_rpc_status.sh
```

Emits JSON: `running`, `pid`, `port`.

---

## Security checklist

- ✅ `.env` is `chmod 600` and not committed.
- ✅ wallet-rpc bound to `127.0.0.1` (default); strong `--rpc-login` secret.
- ⚠️ **Process-table exposure:** `monero-wallet-rpc` accepts the wallet password only via `--password` (CLI), so it is visible in `ps aux` / `/proc/<pid>/cmdline` for the daemon's lifetime. This is an upstream limitation. Run on a single-user system, or restrict process-table visibility (dedicated user account, container, or PID namespace).
- ✅ `--untrusted-daemon` for any remote node.
- ✅ Test on **stagenet** before touching mainnet funds.
- ✅ `--dry-run` / `estimate_fee.sh` before every real send.
- ✅ Back up the 25-word wallet seed offline.

## Next steps
- Day-to-day usage & workflows: `SKILL.md`.
- RPC details / error recovery / env vars: `references/`.
