---
name: agenta-monero
description: "Use when making or receiving Monero (XMR) payments. Generates addresses, sends payments, checks balances, verifies transactions, generates and verifies payment proofs, estimates fees, sweeps funds, and manages wallet operations via a self-hosted monero-wallet-rpc node. Keywords: monero, xmr, cryptocurrency, payments, wallet, send, receive, payment proof."
license: MIT
compatibility: "Requires bash 4+, curl, jq, flock (util-linux), and a running monero-wallet-rpc >= 0.18.0."
metadata:
  hermes:
    category: finance
    tags: [monero, cryptocurrency, payments, wallet, xmr]
    related_skills: []
  version: "0.3.0"
  author: Private Payments
  permissions:
    shell_execution: true
    file_writes:
      - ".env (chmod 600) — RPC credentials + wallet password"
      - "$MONERO_LOCK_DIR/.netrc (chmod 600) — ephemeral RPC auth"
      - "$MONERO_LOCK_DIR/wallet-rpc.pid — process tracking"
      - "$MONERO_LOCK_DIR/wallet-rpc.port — port tracking"
      - "$MONERO_LOCK_DIR/.last_refresh — refresh timestamp"
    process_management: "starts/stops monero-wallet-rpc as a background process"
    network_access: "HTTP POST to $MONERO_RPC_URL/json_rpc (localhost by default)"
    credential_access: "reads .env for RPC + wallet credentials; writes .netrc for curl auth"
---

# Agenta-Monero

Shell wrappers over `monero-wallet-rpc` for autonomous Monero (XMR) payments. All scripts emit JSON to stdout (success) or a structured error JSON to stderr; they compose into receive/send/verify/sweep workflows. Money math is integer piconeros internally; XMR decimal strings appear in output.

> **WARNING — IRREVERSIBLE FINANCIAL OPERATIONS**
>
> - Monero transactions are **irreversible**. Once broadcast, funds cannot be recovered.
> - `send_xmr.sh` and `sweep_all.sh` **require `--confirm` to broadcast**. Without it, they refuse to relay. Use `--dry-run` to preview without `--confirm`.
> - `sweep_all.sh` transfers **all unlocked funds** from the wallet (or subaddress) to a single destination. A mistaken or maliciously triggered sweep can drain the entire balance.
> - Always validate the recipient address (`validate_address.sh`) and confirm the amount before executing a send or sweep.
> - The `.env` file contains `MONERO_WALLET_PASSWORD` and RPC credentials. It is created with `chmod 600`, but on multi-user systems, shared CI, or agent workspaces with broad read access, an attacker who reads `.env` can access the wallet and move funds. Secure the file and the system accordingly.

**Use when:** generating receive addresses, sending/sweeping XMR, checking balance, verifying an incoming payment or a payment proof, estimating fees, or reconciling transactions by hash.

## Prerequisites

- **Install Monero CLI tools** (≥ 0.18.0): download from https://getmonero.org/downloads/ — you need at minimum `monero-wallet-rpc`. Also create a wallet file: `monero-wallet-cli --generate-new-wallet ~/Monero/wallets/main --password 'PASS'` (write down the 25-word seed).
- **Bash ≥ 4**, `curl`, `jq`, `flock` (util-linux) — standard on Linux/macOS (`brew install jq` on macOS).
- **First-time setup:** run `./scripts/interactive_setup.sh` (interactive prompts) **or** tell the Hermes agent "Set up the Agenta-Monero skill" (agent-driven; see First-Time Setup below). Both paths generate RPC credentials, write `.env`, start `monero-wallet-rpc`, and verify readiness.
- After setup, every script runs from the skill root. Invoke `./setup.sh` again after changing `.env`.

## Permissions & Capabilities

This skill performs the following actions. Operators should review these before approving or invoking the skill in automated workflows:

| Capability | Details |
|------------|---------|
| **Shell execution** | Runs `curl`, `jq`, `flock`, `monero-wallet-rpc`, and standard shell utilities |
| **File writes** | `.env` (chmod 600), `.netrc` (chmod 600, ephemeral), PID/port files, lock files, refresh timestamp |
| **Process management** | Starts and stops `monero-wallet-rpc` as a background daemon (PID tracked in `$MONERO_LOCK_DIR`) |
| **Network access** | HTTP POST to `$MONERO_RPC_URL/json_rpc` (localhost by default; can be configured for remote) |
| **Credential access** | Reads `.env` for RPC user/password and wallet password; writes `.netrc` for curl auth; never emits credentials in stdout |

All credential files are created with restrictive permissions (`0600` for files, `0700` for the lock directory). The `.env` file is parsed safely (never sourced) and shell metacharacters are rejected.

## First-Time Setup

When a user asks to set up the Agenta-Monero skill, follow this workflow.

**Path A — Agent-driven (recommended):**
1. Ask: "What's the path to your wallet file?"
2. Ask: "What's the wallet password?"
3. Ask: "Local daemon or remote node?"
   - If remote: "What's the daemon address? (e.g. node.example.com:18081)"
4. Check: `command -v monero-wallet-rpc` — if missing, print install guidance (https://getmonero.org/downloads/) and stop.
5. Run: `./scripts/interactive_setup.sh --wallet-path "PATH" --wallet-password "PASS" --network mainnet --daemon-type local [--daemon-address "HOST:PORT" if remote] --force`
6. Read the JSON output. If `ready:true` → done. If `ready:false` → check `warnings` and troubleshoot.
7. To check wallet-rpc status later: `./scripts/wallet_rpc_status.sh`. To stop it: `./scripts/stop_wallet_rpc.sh`.

**Path B — Manual interactive script:**
Tell the user to run `./scripts/interactive_setup.sh` and follow the prompts.

**Both paths:**
- Generate random RPC credentials (12-char user, 24-char password).
- Write `.env` (chmod 600) with all values including `MONERO_WALLET_PASSWORD`.
  - **Caution:** `.env` persists on disk and contains the wallet password. On multi-user systems or CI, ensure the file is not world-readable, not committed to version control, and not included in backups or log captures.
- Start `monero-wallet-rpc` as a background process (PID stored in `$MONERO_LOCK_DIR/wallet-rpc.pid`).
- Run `./setup.sh` and report readiness.
- **Credentials are not emitted in stdout JSON.** They exist only in `.env` (chmod 600). If the user needs to see them, read from `.env` directly.

## Quick reference

One compact block per operation. **Load `references/rpc-reference.md` when you need exact JSON-RPC params, full output field lists, or per-operation refresh classification.**

```text
create_address.sh  --label "Payment from Alice" [--account 0]   -> {address, address_index, account}
send_xmr.sh        --address ADDR --amount "1.5"                -> {tx_hash, fee, amount[, tx_key]}
                   [--priority 0] [--get-tx-key] [--dry-run] [--confirm]
                   [--dest '[{"address":"A","amount":"1.0"}]']
estimate_fee.sh    --address ADDR --amount "1.5" [--priority 0] -> {fee, amount, priority, num_destinations}
sweep_all.sh       --address ADDR [--account 0] [--subaddress N]-->{tx_hash, fee, amount}
                   [--priority 0] [--dry-run] [--confirm]
check_balance.sh   [--account 0]                                -> {balance, unlocked_balance, blocks_to_unlock, time_to_unlock, account}
get_transfer.sh    --tx-hash HASH                               -> {tx_hash, amount, fee, direction, confirmations, address, address_index, timestamp, confirmed, unlock_time}
verify_payment.sh  --tx-hash HASH | --address ADDR --expected-amount "1.5" -> {verified, confirmations, tx_hash, address, address_index, confirmed, amount}
get_tx_proof.sh    --tx-hash HASH --address ADDR                -> {tx_hash, address, proof}
check_tx_proof.sh  --tx-hash HASH --address ADDR --proof PROOF  -> {verified, confirmations, amount, tx_hash, address}
list_incoming.sh   [--confirmed-only|--all] [--since-block N]   -> [{tx_hash, amount, confirmations, address, address_index, timestamp, confirmed, unlock_time}]
                   [--since-timestamp N] [--limit 100] [--account 0]
list_outgoing.sh   [--since-block N] [--since-timestamp N]      -> [{tx_hash, amount, fee, timestamp, address, address_index, unlock_time}]
                   [--limit 100] [--account 0]
list_addresses.sh  [--account 0]                                -> [{index, address, label, balance, unlocked_balance}]
validate_address.sh --address ADDR                              -> {valid, network, network_match, subaddress, integrated}
sync_status.sh                                                   -> {height, daemon_connected, wallet_version}
```

Concrete output examples (stdout; success is one JSON object per line):

```json
// create_address.sh
{"address":"88bc...","address_index":5,"account":0}
// send_xmr.sh --address ... --amount "1.5"
{"tx_hash":"7663438...","fee":"0.0000869","amount":"1.5"}
// estimate_fee.sh --address ... --amount "1.5"
{"fee":"0.0000869","amount":"1.5","priority":0,"num_destinations":1}
// sweep_all.sh --address DEST --dry-run
{"tx_hash":"","fee":"0.0000869","amount":"8.2"}
// check_balance.sh
{"balance":"10.5","unlocked_balance":"8.2","blocks_to_unlock":42,"time_to_unlock":30240,"account":0}
// get_transfer.sh --tx-hash ...
{"tx_hash":"c36258a...","amount":"1.5","fee":"0.0000435","direction":"in","confirmations":15,"address":"77Vx9cs...","address_index":3,"timestamp":1535918400,"confirmed":true,"unlock_time":0}
// verify_payment.sh --tx-hash ...
{"verified":true,"confirmations":12,"tx_hash":"c36258a...","address":"77Vx9cs...","address_index":3,"confirmed":true,"amount":"1.5"}
// get_tx_proof.sh --tx-hash ... --address ...
{"tx_hash":"c36258a...","address":"77Vx9cs...","proof":"ProofV1..."}
// check_tx_proof.sh --tx-hash ... --address ... --proof ...
{"verified":true,"confirmations":15,"amount":"1.5","tx_hash":"c36258a...","address":"77Vx9cs..."}
// validate_address.sh --address ...
{"valid":true,"network":"mainnet","network_match":true,"subaddress":false,"integrated":false}
// sync_status.sh
{"height":1523651,"daemon_connected":true,"wallet_version":196613}
// list_incoming.sh (array element)
{"tx_hash":"c36258a...","amount":"1.5","confirmations":15,"address":"77Vx9cs...","address_index":3,"timestamp":1535918400,"confirmed":true,"unlock_time":0}
```

Amounts in outputs are XMR decimal strings (e.g. `"1.5"`). `--dry-run` and `estimate_fee` preview without broadcasting.

## Gotchas (verified facts — get these right)

- **No `sync` RPC.** The wallet refreshes from the daemon via `refresh`, which can take seconds-to-minutes. Refresh is **operation-aware**: balance/transfer/verify ops auto-refresh; address-management, `validate_address`, `estimate_fee`, `get_tx_proof`, and `sync_status` do not. Override with `--no-refresh` on any auto-refresh op (**`--no-refresh` works in any argument position**).
- **`blocks_to_unlock` / `time_to_unlock` are native `get_balance` fields.** Read them directly — never derive them. `check_balance` surfaces both. They are `0` when no funds are locked, or `null` if the wallet omits them — treat `0`/`null` as "nothing locked".
- **Priority values: `0=default, 1=unimportant, 2=normal, 3=elevated, 4=priority`.** The default is **`0`** (wallet decides). Do **not** default to `1` — that literally means "unimportant". Send/sweep/estimate accept `--priority 0-4`.
- **Single `/json_rpc` endpoint.** Every wallet method this skill uses — including `get_height` and `get_version` — is POSTed to `$MONERO_RPC_URL/json_rpc`. There is no root-path call anywhere.
- **`validate_address` uses real RPC fields.** The RPC is called with `any_net_type:true` so the real `nettype` is returned; `network_match` is derived client-side by comparing `nettype` to `MONERO_NETWORK`. There is **no `checksum_valid` field** (the checksum is part of `valid`). This keeps `INVALID_ADDRESS` (bad format/checksum) distinct from `NETWORK_MISMATCH` (valid but wrong network).
- **Money is integer piconeros (1 XMR = 10^12).** Never use floating-point for amounts. All arithmetic is integer piconero; the XMR decimal strings in output come from the scripts' string-based conversion. Amounts must be positive and have <=12 decimals.
- **Sends and sweeps are not idempotent and are NOT auto-retried.** On timeout/uncertain result, check `get_transfer.sh --tx-hash` **before** retrying (see retry-safety workflow). Use `--dry-run` / `estimate_fee` to preview.
- **Credentials use netrc (never `curl -u`); `.env` is parsed, never sourced.** The netrc lives at `$MONERO_LOCK_DIR/.netrc` (mode `0600`). All user values are passed to the RPC via `jq --arg`/`--argjson` — never by string interpolation.

## Workflows

Workflows are rendered as checklists. Money/identity paths (send, sweep, verify) are prescriptive: follow the order. Every destructive workflow ends with a verify-after-act step.

### Receive a Payment

- [ ] `scripts/create_address.sh --label "Payment from Alice"` — note the returned `address`.
- [ ] Share `address` with the payer.
- [ ] `scripts/check_balance.sh` (or `scripts/list_incoming.sh --since-block <height>`).
- [ ] `scripts/verify_payment.sh --address "ADDR" --expected-amount "1.5"` — wait until `verified:true`.
- [ ] `scripts/get_tx_proof.sh --tx-hash "HASH" --address "ADDR"` — hand the payer the `proof` for their records.

### Send a Payment (plan -> validate -> execute)

> **Irreversible:** `send_xmr.sh` requires `--confirm` to broadcast. Use `--dry-run` to preview without `--confirm`. Always validate the address and confirm the amount before executing.

- [ ] **Plan:** `scripts/estimate_fee.sh --address "RECIPIENT" --amount "2.5"` — preview `fee`.
- [ ] **Validate:** `scripts/validate_address.sh --address "RECIPIENT"` — confirm `valid:true` and `network_match:true`.
- [ ] **Balance:** `scripts/check_balance.sh` — confirm `unlocked_balance >= 2.5`.
- [ ] **Preview (optional):** `scripts/send_xmr.sh --address "RECIPIENT" --amount "2.5" --dry-run` — confirm fee/amount without broadcasting.
- [ ] **Execute:** `scripts/send_xmr.sh --address "RECIPIENT" --amount "2.5" --confirm` — note the `tx_hash`.
- [ ] **Verify:** `scripts/get_transfer.sh --tx-hash "<tx_hash>"` — confirm it was recorded (and `confirmed` once enough blocks pass).

### Send a Payment — retry safety (DECISION GATE)

Sends are not idempotent. **Never retry blindly on timeout.** Run this gate first:

- [ ] Attempt: `scripts/send_xmr.sh --address "RECIPIENT" --amount "2.5" --confirm`.
- [ ] If it returns a `tx_hash` (success) -> **done; do NOT re-send.**
- [ ] If it **times out / returns an uncertain result**, whether you can use `get_transfer` depends on having a hash:
  - **You have a `tx_hash`** (from the send response, or a prior attempt you're unsure about) -> call `scripts/get_transfer.sh --tx-hash "<tx_hash>"` and branch on the **error code**:
    - `TX_NOT_FOUND` -> the transaction is genuinely absent from the wallet -> **safe to retry the send.**
    - `RPC_UNREACHABLE` -> the wallet RPC / daemon could not be reached -> the transaction status is **unknown**, not absent -> **do NOT retry the send;** fix connectivity (`sync_status.sh`, restart `monero-wallet-rpc`/`monerod`) and re-check `get_transfer` before doing anything else.
    - any success result -> the tx exists -> **do NOT re-send.**
  - **You have NO `tx_hash`** (pure transport failure / `RPC_UNREACHABLE` with no payload) -> there is nothing to look up; status is **unknown**. **Do NOT retry the send.** Fix connectivity first, then reconcile with `scripts/list_outgoing.sh` (match by amount/timestamp) to detect any tx that may have been created before re-evaluating.

### Verify a Payment Proof

- [ ] Collect from the payer: `tx_hash`, `address`, and `proof` string.
- [ ] `scripts/check_tx_proof.sh --tx-hash "HASH" --address "ADDR" --proof "PROOF"`.
- [ ] Act on `verified`: `true` => proof is cryptographically valid (read `amount`, `confirmations`). `false` / `PROOF_INVALID` => reject and ask the payer to re-issue.

### Sweep Funds (plan -> validate -> execute)

> **Irreversible and high-impact:** `sweep_all.sh` requires `--confirm` to broadcast. Use `--dry-run` to preview without `--confirm`. A mistaken address can drain the entire wallet.

- [ ] `scripts/check_balance.sh` — read `unlocked_balance` (the sweepable amount).
- [ ] `scripts/validate_address.sh --address "DESTINATION"` — `valid:true` + `network_match:true`.
- [ ] `scripts/sweep_all.sh --address "DESTINATION" --dry-run` — preview `amount` + `fee` without sending.
- [ ] `scripts/sweep_all.sh --address "DESTINATION" --confirm` — execute; note `tx_hash`.
- [ ] (Optional) `scripts/get_transfer.sh --tx-hash "<tx_hash>"` — confirm. Same retry-safety caveat as sends applies.

### Check for Payments (with filtering)

- [ ] `scripts/sync_status.sh` — confirm `daemon_connected:true` and that `height` is recent (else data may be stale). `list_incoming` auto-refreshes unless `MONERO_AUTO_REFRESH=false` or you pass `--no-refresh`; if auto-refresh is off and you need fresh data, re-enable it (there is no standalone refresh script).
- [ ] `scripts/list_incoming.sh --since-block <height> --limit 50` — recent incoming transfers.
- [ ] Read `confirmations` / `confirmed` per row (threshold = `MONERO_CONFIRMATIONS`, default `10`).
- [ ] To pin a specific payment: `scripts/verify_payment.sh --tx-hash "HASH"` (or `--address` + `--expected-amount`).

## Error codes

Every error is a JSON object on **stderr** plus a non-zero exit. It is **compact (single-line)** — but always parse it with `jq`, never line-by-line. The object has exactly `error`, `code`, and `message` (the `suggestion` key is reserved in the emitter but not currently populated; use the table below for recovery text):

```json
{
  "error": true,
  "code": "TX_NOT_FOUND",
  "message": "no transfer found for txid 7663438…"
}
```

**Load `references/error-runbook.md` when a script returns an error code and you need detailed, per-code recovery steps.**

| Code | Meaning | Retryable | One-line recovery |
|------|---------|:---------:|-------------------|
| `CONFIG_MISSING` | Required env var / arg not set | No | Run `./setup.sh`; supply the missing `--flag`. |
| `CONFIG_INVALID` | `.env` has bad syntax/metachars | No | Inspect `.env`; fix malformed lines; do not source it. |
| `CONFIRM_REQUIRED` | `--confirm` not provided for destructive operation | No | Add `--confirm` to broadcast, or `--dry-run` to preview without broadcasting. |
| `RPC_UNREACHABLE` | Cannot reach monero-wallet-rpc | Yes | Start/check `monero-wallet-rpc`; re-check. (Do NOT treat a send timeout with this code as "tx absent".) |
| `WALLET_NOT_LOADED` | Wallet name != loaded wallet | No | `open_wallet` the right wallet; check `MONERO_WALLET_NAME`. |
| `WALLET_LOCKED` | Wallet file locked elsewhere | No | Find/kill the holder (`lsof \| grep wallet.keys`) or wait. |
| `DAEMON_DISCONNECTED` | Wallet RPC can't reach daemon | Yes | Check/restart `monerod`. |
| `INSUFFICIENT_BALANCE` | Not enough unlocked funds | No | `check_balance.sh`; wait for unlocks or reduce amount. |
| `AMOUNT_INVALID` | Amount <=0 / >12 decimals / >balance | No | Correct the amount string. |
| `INVALID_ADDRESS` | Bad format/checksum | No | Re-check the address; do not use. |
| `NETWORK_MISMATCH` | Valid address, wrong network | No | Use an address for `MONERO_NETWORK` (mainnet/stagenet). |
| `INVALID_INPUT` | Bad flag value (e.g. priority 0-4, tx-hash, label) | No | Correct the argument value. |
| `SYNC_FAILED` / `REFRESH_FAILED` | Wallet sync/refresh failed | Yes | `sync_status.sh`; may need to restart wallet RPC. |
| `TX_RELAY_FAILED` | Tx created but not broadcast | No | `get_transfer.sh --tx-hash`; may need manual relay. |
| `RATE_LIMITED` | Lock acquisition timed out / daemon busy | Yes | Wait; reduce call frequency. |
| `TX_NOT_FOUND` | Hash unknown to this wallet | No | Re-check the hash; for sends this means "safe to retry" (see retry-safety). |
| `PROOF_INVALID` | Payment proof verification failed | No | Reject; ask payer to re-issue proof. |

Transient codes (`RPC_UNREACHABLE`, `DAEMON_DISCONNECTED`, `SYNC_FAILED`, `REFRESH_FAILED`, `RATE_LIMITED`) surface **immediately** — they are **not** auto-retried by the scripts. The retry helper (`lib/retry.sh`) exists and is unit-tested, but is **not** currently applied to any script RPC call (all scripts call `rpc_call` directly). `send_xmr`/`sweep_all` are intentionally never retried (non-idempotent). `get_transfer` and `check_tx_proof` are intentionally direct so they don't mask the retry-safety probe / proof classification. If a read-only op returns a transient code, **the agent should retry it itself** (never retry sends/sweeps — drive those via the decision gate above).

## Refresh & concurrency

- **Refresh:** controlled by `MONERO_AUTO_REFRESH` (default `true`) and `MONERO_REFRESH_MIN_INTERVAL` (default `30`s; a refresh is skipped if one happened within this window). Auto-refreshing ops accept `--no-refresh` to skip. The last-refresh timestamp lives in `$MONERO_LOCK_DIR/.last_refresh`.
- **Concurrency:** every script takes an exclusive `flock` on `$MONERO_LOCK_DIR/agenta-monero.lock` (timeout `MONERO_LOCK_TIMEOUT`, default `60`s) before any RPC; lock contention surfaces as `RATE_LIMITED`. The lock is released on exit, coordinating multiple local agent processes against the wallet RPC's own serialization.

**Load `references/env-reference.md` when you need the full environment-variable table (connection, network, refresh, retry, concurrency, TLS knobs) or the complete refresh-strategy / retry-backoff details.**
