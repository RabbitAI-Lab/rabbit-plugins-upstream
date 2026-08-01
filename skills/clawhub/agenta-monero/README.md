# Agenta-Monero

> Autonomous Monero (XMR) payments for Hermes and Openclaw agents via shell. JSON-in, JSON-out wrappers over `monero-wallet-rpc` for sending, receiving, verifying, and sweeping. Composable into agent-driven workflows.

> **WARNING — Irreversible Financial Operations**
>
> Monero transactions are **irreversible**. `send_xmr.sh` and `sweep_all.sh` broadcast by default — use `--dry-run` to preview. `sweep_all.sh` transfers **all unlocked funds** to one destination; a mistaken or maliciously triggered sweep can drain the entire wallet balance. Always validate addresses and confirm amounts before executing.

## What It Does

| Command | Description |
|---------|-------------|
| `create_address.sh` | Generate a receive address with label |
| `send_xmr.sh` | Send XMR (requires `--confirm`, supports `--dry-run`) |
| `sweep_all.sh` | Sweep **all** wallet funds to a destination (requires `--confirm`, supports `--dry-run`) |
| `check_balance.sh` | Check balance + unlock status |
| `estimate_fee.sh` | Preview fees before sending |
| `validate_address.sh` | Verify address format and network |
| `get_transfer.sh` | Look up a transaction by hash |
| `verify_payment.sh` | Confirm a payment was received |
| `get_tx_proof.sh` / `check_tx_proof.sh` | Generate or verify payment proofs |
| `list_incoming.sh` / `list_outgoing.sh` | List transactions with filtering |
| `list_addresses.sh` | List subaddresses with balances |
| `sync_status.sh` | Check daemon connection + wallet height |
| `interactive_setup.sh` | First-time setup wizard |
| `wallet_rpc_status.sh` / `stop_wallet_rpc.sh` | Manage the RPC daemon |

## Prerequisites

- **OS:** Linux or macOS (Windows not supported)
- **Monero CLI tools** >= 0.18.0 ([download](https://getmonero.org/downloads/)) - at minimum `monero-wallet-rpc`
- **Bash** >= 4, `curl`, `jq`, `flock` (util-linux)

## Installation

**Hermes:**
```bash
git clone https://github.com/tibbar-etihw/agenta-monero.git ~/.hermes/skills/finance/agenta-monero
```

**OpenClaw:**
```bash
git clone https://github.com/tibbar-etihw/agenta-monero.git ~/.openclaw/workspace/skills/finance/agenta-monero
```

Or tell your agent:
> "Install the agenta-monero skill from https://github.com/tibbar-etihw/agenta-monero"

**New to this?** See the [Getting Started guide](docs/GETTING_STARTED.md) for a detailed walkthrough covering wallet creation, daemon setup, and first-time configuration.

## Configuration

Your agent configures everything. Simply prompt it with:

> "Set up the Agenta-Monero skill."

---

<details>
<summary>Manual configuration (advanced)</summary>

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Required variables:
- `MONERO_RPC_URL` - wallet RPC endpoint (default: `http://127.0.0.1:18088`)
- `MONERO_RPC_USER` / `MONERO_RPC_PASSWORD` - RPC credentials
- `MONERO_WALLET_NAME` - must match the loaded wallet
- `MONERO_WALLET_PASSWORD` - wallet password
- `MONERO_NETWORK` - `mainnet` or `stagenet`

> **Caution:** `.env` contains `MONERO_WALLET_PASSWORD` and RPC credentials. It is created with `chmod 600`, but on multi-user systems, shared CI, or agent workspaces with broad read access, anyone who reads this file can access the wallet and move funds. Do not commit `.env` to version control or include it in backups/log captures.

</details>

## Usage Examples

```bash
# Create a receive address
./scripts/create_address.sh --label "Payment from Alice"

# Check your balance
./scripts/check_balance.sh

# Send XMR (dry run first)
./scripts/send_xmr.sh --address "RECIPIENT" --amount "1.5" --dry-run
./scripts/send_xmr.sh --address "RECIPIENT" --amount "1.5" --confirm

# Verify a payment
./scripts/verify_payment.sh --tx-hash "HASH" --expected-amount "1.5"

# Estimate fees
./scripts/estimate_fee.sh --address "RECIPIENT" --amount "1.5"

# List recent incoming transactions
./scripts/list_incoming.sh --since-block 1500000 --limit 50
```

## How It Works

All scripts communicate with `monero-wallet-rpc` via a single `/json_rpc` endpoint. Credentials are stored in a netrc file (never passed via command line). The `.env` file is parsed safely - never sourced.

- **Auto-refresh**: Balance/transfer/verify operations auto-refresh the wallet. Use `--no-refresh` to skip.
- **Concurrency**: Scripts use file locking (`flock`) to coordinate multiple processes.
- **Money math**: All amounts are integer piconeros internally (1 XMR = 10^12). XMR decimal strings appear in output.

## Error Handling

Errors are JSON on stderr with an error code:

```json
{"error":true,"code":"INSUFFICIENT_BALANCE","message":"not enough unlocked funds"}
```

Common codes: `CONFIG_MISSING`, `RPC_UNREACHABLE`, `WALLET_NOT_LOADED`, `INSUFFICIENT_BALANCE`, `INVALID_ADDRESS`, `NETWORK_MISMATCH`, `TX_NOT_FOUND`

See `references/error-runbook.md` for detailed recovery steps.

## Testing

Tests use an in-process Python mock RPC server - no daemon or network required.

```bash
bats tests/                    # Run all tests
bats tests/send_xmr.bats      # Run single test file
```

Requires: `bats`, `python3`

## Documentation

- `SKILL.md` - Full agent-facing reference
- `references/rpc-reference.md` - RPC method details
- `references/error-runbook.md` - Per-error recovery steps
- `references/env-reference.md` - Environment variable table
- `docs/GETTING_STARTED.md` - Install walkthrough

## WARNING
Never fund your agent's Monero wallet with more than what you are willing to potentially lose. Agents make mistakes and misunderstand instructions all the time.

## License

MIT

## Donations

If you find this useful, donations are appreciated:

**Monero:**
```
82fPMdPyWS5jEvW3TzH8ibWmrj2Uu1hmNNo7n1W2bdyMEGTDEUN6ecXYHjn6TnAxan9N3LhDS678KfzagsVuMYYk3hXZ2gR
```
