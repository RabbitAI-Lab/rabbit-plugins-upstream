# Error Recovery Runbook

Full recovery procedures for every error code emitted by Agenta-Monero scripts. Every error is emitted to **stderr** as a single-line (compact) JSON object and the script exits non-zero — parse it with `jq`, not line-by-line:

```json
{
  "error": true,
  "code": "WALLET_NOT_LOADED",
  "message": "Wallet 'my_wallet' is not loaded in the RPC server"
}
```

Parse `code` to branch; read `message` for specifics. (The `suggestion` key is reserved in the emitter but not currently populated — use the Recovery column below for guidance.)

## Error codes (full table)

| Code | Meaning | Retryable | Recovery |
|------|---------|:---------:|----------|
| `CONFIG_MISSING` | Required env var not set, or a required `--flag` omitted | No | Run `./setup.sh` to create `.env`, fill required values. For missing flags, supply the required argument (`--address`, `--amount`, `--tx-hash`, `--proof`, etc.). |
| `CONFIG_INVALID` | `.env` contains invalid syntax or shell metacharacters | No | Inspect `.env` for metacharacters or malformed lines; fix and retry. Never `source .env` — it is parsed safely by design. |
| `RPC_UNREACHABLE` | Cannot connect to `monero-wallet-rpc` | Yes | Confirm `monero-wallet-rpc` is running and `MONERO_RPC_URL` is correct; start it if not. **For a send/sweep timeout, this code means the transaction status is UNKNOWN — do NOT treat it as "absent" and do NOT retry the send;** fix connectivity and re-check with `get_transfer.sh --tx-hash`. |
| `WALLET_NOT_LOADED` | Wallet name doesn't match the loaded wallet | No | Open the correct wallet in the RPC server (`open_wallet`); verify `MONERO_WALLET_NAME`. |
| `WALLET_LOCKED` | Wallet file locked by another process | No | Find the holder (`lsof | grep wallet.keys`); kill it or wait for release. |
| `DAEMON_DISCONNECTED` | Wallet RPC can't reach the daemon | Yes | Check daemon status; restart `monerod` if needed. |
| `INSUFFICIENT_BALANCE` | Not enough unlocked funds | No | `check_balance.sh` to see available funds; wait for unlocks or reduce the amount. |
| `AMOUNT_INVALID` | Amount negative, too many decimals (>12), or exceeds balance | No | Correct the amount string (positive decimal, <=12 fractional digits). |
| `INVALID_ADDRESS` | Address format/checksum invalid | No | Re-check the address; do not use it. |
| `NETWORK_MISMATCH` | Address valid but on the wrong network | No | Use an address for the configured `MONERO_NETWORK` (mainnet/stagenet). |
| `INVALID_INPUT` | Bad argument value (priority not 0-4, tx-hash not 64 lowercase hex, label too long/has control chars, `--dest` not a JSON array) | No | Correct the argument value. |
| `SYNC_FAILED` | Wallet sync failed | Yes | Run `sync_status.sh` to diagnose; may need to restart wallet RPC. |
| `REFRESH_FAILED` | Wallet refresh failed | Yes | Run `sync_status.sh`; may need to restart wallet RPC; pass `--no-refresh` to bypass on auto-refreshing ops if you can tolerate stale data. |
| `TX_RELAY_FAILED` | Transaction created but relay failed | No | `get_transfer.sh --tx-hash` to check state; the tx may need manual relay. |
| `RATE_LIMITED` | Too many requests / lock acquisition timeout | Yes | Wait and retry; reduce call frequency. |
| `TX_NOT_FOUND` | Transaction hash not found in wallet | No | Re-check the hash. **For a send-timeout retry-safety check, this specifically means the tx is genuinely absent -> safe to retry the send.** |
| `PROOF_INVALID` | Payment proof verification failed | No | Reject the proof; ask the payer to re-issue with `get_tx_proof.sh`. |

Additional codes that may surface from RPC plumbing: `DEST_JSON_INVALID` (`--dest` is not a valid JSON array of `{address,amount}`) and `RPC_ERROR` (generic wallet-side RPC error not matching a specific code).

## Edge cases

- **Wallet RPC not running:** `rpc_check_connection` fails fast with `RPC_UNREACHABLE`.
- **Wallet file locked:** detected via RPC error message; mapped to `WALLET_LOCKED`.
- **Wrong network:** `validate_address` returns `network_match=false` -> `NETWORK_MISMATCH` (distinct from a malformed address -> `INVALID_ADDRESS`).
- **Zero balance:** `check_balance` returns `0.0` values gracefully.
- **No transactions:** `list_incoming`/`list_outgoing` return `[]`.
- **Partial sync:** `sync_status` reports only wallet `height` + `daemon_connected` (`true` iff the wallet RPC responded to both probes). It deliberately does **not** claim synced/not-synced — the wallet RPC cannot honestly report the daemon's sync target — so it never gives false confidence. For daemon sync progress, query `monerod` directly.
- **Timeout:** curl timeout `30`s default (`MONERO_RPC_TIMEOUT`); refresh timeout `120`s (`MONERO_REFRESH_TIMEOUT`).
- **Large amount precision:** all internal arithmetic is integer piconeros; XMR decimal conversion is string-based, never floating-point.
- **Concurrent access:** scripts take an exclusive `flock` on `$MONERO_LOCK_DIR/agenta-monero.lock` (timeout `MONERO_LOCK_TIMEOUT`); lock contention surfaces as `RATE_LIMITED`.

## Retry logic (available, but NOT currently applied)

The retry helper (`lib/retry.sh`) is **available and unit-tested, but is NOT currently applied to script RPC calls** — all scripts call `rpc_call` directly.

- `MONERO_RETRY_MAX` (default `2`) — maximum retry attempts for transient errors.
- `MONERO_RETRY_BACKOFF` (default `1`) — initial backoff in seconds; **doubles per retry** (1, 2, 4, ...).

These variables are reserved for future use and have **no effect today**. `is_retryable` classifies the transient codes above (`RPC_UNREACHABLE`, `DAEMON_DISCONNECTED`, `SYNC_FAILED`, `REFRESH_FAILED`, `RATE_LIMITED`), but no script routes its calls through `retry_with_backoff`. Transient codes therefore surface **immediately**.

This is intentional for the destructive paths: **`send_xmr` and `sweep_all` must never be auto-retried** (non-idempotent — an automatic retry could double-spend). Drive their retry manually via the retry-safety decision gate in SKILL.md (timeout -> `get_transfer.sh --tx-hash` -> retry only on `TX_NOT_FOUND`; never on `RPC_UNREACHABLE`). `get_transfer` and `check_tx_proof` are also intentionally direct so that an automatic retry would not mask the retry-safety probe or proof classification. For read-only ops that surface a transient code, **the agent should retry them itself**.

## Send retry-safety decision gate (recap)

```text
send_xmr timed out / uncertain
        |
        v
Do you have a tx_hash?
        |
        +-- NO (pure transport failure / RPC_UNREACHABLE, no payload)
        |       -> status UNKNOWN: do NOT retry; fix connectivity, then
        |          reconcile via list_outgoing.sh (match amount/timestamp)
        |
        +-- YES -> get_transfer.sh --tx-hash <hash>
                |
                +-- success (tx present)         -> DONE  (do NOT re-send)
                +-- code == TX_NOT_FOUND         -> SAFE to retry the send
                +-- code == RPC_UNREACHABLE      -> STOP: status UNKNOWN, fix connectivity, re-check
                +-- (any other code)             -> STOP: diagnose before acting
```

The asymmetry is deliberate: `TX_NOT_FOUND` is a wallet-side "this hash is not here" answer; `RPC_UNREACHABLE` means "I could not ask the wallet at all". Treating the latter as "absent" risks a double-spend.
