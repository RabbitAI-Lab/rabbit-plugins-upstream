# RPC Reference

Full detail for every operation: exact flags, the underlying JSON-RPC `method` + `params`, the complete output object, behavior notes, and whether the script auto-refreshes. All RPC methods are POSTed to `$MONERO_RPC_URL/json_rpc` as `{"jsonrpc":"2.0","id":"...","method":"<m>","params":{...}}` with netrc auth. Amounts inside `params` are integer **piconeros** (1 XMR = 10^12); amounts in script output are XMR decimal strings.

## Refresh classification

| Script | Auto-refresh? | Why |
|--------|:-------------:|-----|
| `create_address` | No | Address creation does not depend on chain state. |
| `send_xmr` | Yes | Needs current balance to validate sufficiency. |
| `estimate_fee` | No | Fee uses current mempool, not a full refresh. |
| `sweep_all` | Yes | Needs current balance to know the sweepable amount. |
| `check_balance` | Yes | Balance depends on chain state. |
| `list_incoming` | Yes | Transfer list depends on chain state. |
| `list_outgoing` | Yes | Transfer list depends on chain state. |
| `verify_payment` | Yes | Confirmation count depends on chain state. |
| `get_transfer` | Yes | Transfer details depend on chain state. |
| `get_tx_proof` | No | Proof generation does not depend on chain state. |
| `check_tx_proof` | Yes | Confirmation count in proof depends on chain state. |
| `list_addresses` | No | Address listing does not depend on chain state (uses `get_address`, not `get_balance`). |
| `validate_address` | No | Validation is purely format/checksum/network. |
| `sync_status` | No | This *is* the status check (point-in-time). |

Every auto-refreshing script accepts `--no-refresh` (works in any argument position).

---

## create_address.sh

**Flags:** `--label "optional label"` (optional), `--account N` (optional, default `0`).

**RPC:** `create_address`
```json
{"method":"create_address","params":{"account_index":0,"label":"Payment from Alice"}}
```

**Output:**
```json
{"address":"88bc...","address_index":5,"account":0}
```
Validates label length (<=255 chars, no control characters). Does not auto-refresh.

## send_xmr.sh

**Flags:**
- Single destination: `--address "ADDR" --amount "1.5"` (required unless `--dest`).
- Multi-destination: `--dest '[{"address":"ADDR1","amount":"1.0"},{"address":"ADDR2","amount":"2.0"}]'` (valid JSON array — bare comma-separated streams are rejected).
- `--priority 0` (default `0`; range 0-4 where **0=default, 1=unimportant, 2=normal, 3=elevated, 4=priority**).
- `--get-tx-key` (return the transaction key; if omitted, `get_tx_key:false`).
- `--dry-run` (calls `transfer` with `do_not_relay:true`; returns fee + tx hash without broadcasting).

**RPC:** `transfer`
```json
{"method":"transfer","params":{"destinations":[{"address":"ADDR","amount":1500000000000}],"priority":0,"get_tx_key":true,"do_not_relay":false}}
```
(`amount` is piconeros.)

**Output:**
```json
{"tx_hash":"7663438...","fee":"0.0000869","amount":"1.5","tx_key":"..."}
```
`tx_key` is present only when `--get-tx-key` is supplied.

**Behavior:** validates each destination via `validate_address` (one RPC per destination — not parallelized); validates amounts (positive, <=12 decimals); pre-checks balance via `get_balance`; converts to piconeros; calls `transfer`. **Not idempotent / not auto-retried.** On timeout, use `get_transfer.sh --tx-hash` before retrying (see SKILL.md retry-safety).

## estimate_fee.sh

**Flags:** same as `send_xmr.sh` (`--address`/`--amount` or `--dest`, `--priority`). Does **not** accept `--get-tx-key` or `--dry-run` (it is always a dry run).

**RPC:** `transfer` with `do_not_relay:true`, `get_tx_key:false`.
```json
{"method":"transfer","params":{"destinations":[{"address":"ADDR","amount":1500000000000}],"priority":0,"get_tx_key":false,"do_not_relay":true}}
```

**Output:**
```json
{"fee":"0.0000869","amount":"1.5","priority":0,"num_destinations":1}
```
Does not broadcast, does not auto-refresh. Validates addresses/amounts identically to `send_xmr`.

## sweep_all.sh

**Flags:** `--address "ADDR"` (required), `--account N` (optional, default `0`), `--subaddress N` (optional — sweep one subaddress; omit for all), `--priority 0` (optional, default `0`), `--dry-run` (optional).

**RPC:** `sweep_all`
```json
{"method":"sweep_all","params":{"address":"ADDR","account_index":0,"priority":0,"do_not_relay":false}}
```
With `--subaddress N`, `params` additionally includes `"subaddr_indices":[N]`.

**Output:**
```json
{"tx_hash":"7663438...","fee":"0.0000869","amount":"8.2"}
```
Validates the destination address before sweeping. **Same non-idempotency caveat as `send_xmr`** — not auto-retried.

## check_balance.sh

**Flags:** `--account N` (optional, default `0`).

**RPC:** `refresh` (if auto-refresh enabled and interval elapsed), then `get_balance`:
```json
{"method":"get_balance","params":{"account_index":0}}
```

**Output:**
```json
{"balance":"10.5","unlocked_balance":"8.2","blocks_to_unlock":42,"time_to_unlock":30240,"account":0}
```
`blocks_to_unlock` and `time_to_unlock` are **read directly from the native `get_balance` response** (the wallet RPC computes them — no client-side derivation).

## get_transfer.sh

**Flags:** `--tx-hash "HASH"` (required; 64 lowercase hex chars).

**RPC:** `refresh` (if enabled), then `get_transfer_by_txid`:
```json
{"method":"get_transfer_by_txid","params":{"txid":"c36258a..."}}
```

**Output:**
```json
{"tx_hash":"c36258a...","amount":"1.5","fee":"0.0000435","direction":"in","confirmations":15,"address":"77Vx9cs...","address_index":3,"timestamp":1535918400,"confirmed":true,"unlock_time":0}
```
`direction` is the wallet's transfer `type` (`in`/`out`/`pool`/`pending`). `confirmed` is `confirmations >= MONERO_CONFIRMATIONS`.

**Failure modes (critical for send retry-safety):**
- `TX_NOT_FOUND` — hash is genuinely absent from the wallet (wallet-side error or empty result). For a send-timeout check, this means "safe to retry".
- `RPC_UNREACHABLE` — transport/daemon down (could not check). The transaction status is **unknown**, not absent. Propagated verbatim; **do not** treat as a "safe to retry" signal.

## verify_payment.sh

**Flags:** either `--tx-hash "HASH"`, **or** `--address "ADDR" --expected-amount "1.5"` (mutually exclusive).

**RPC:**
- tx-hash mode: `get_transfer_by_txid` `{"txid":"HASH"}`.
- address mode: `get_transfers` `{"in":true,"out":false,"pool":true,"pending":true}`, then client-side match on `address` + exact piconero `amount`.

**Output:**
```json
{"verified":true,"confirmations":12,"amount":"1.5","tx_hash":"c36258a...","address":"77Vx9cs...","address_index":3,"confirmed":true}
```
`verified:true` requires the transfer to be incoming **and** at/above `MONERO_CONFIRMATIONS`. `amount` is `null` when no match is found (and `verified:false`).

## get_tx_proof.sh

**Flags:** `--tx-hash "HASH"` `--address "ADDR"` (both required).

**RPC:** `get_tx_proof`
```json
{"method":"get_tx_proof","params":{"txid":"c36258a...","address":"77Vx9cs..."}}
```

**Output:**
```json
{"tx_hash":"c36258a...","address":"77Vx9cs...","proof":"ProofV1..."}
```
Generates a proof shareable with a third party. Does not auto-refresh.

## check_tx_proof.sh

**Flags:** `--tx-hash "HASH"` `--address "ADDR"` `--proof "PROOF"` (all required).

**RPC:** `check_tx_proof`
```json
{"method":"check_tx_proof","params":{"txid":"c36258a...","address":"77Vx9cs...","signature":"ProofV1..."}}
```
(`proof` maps to the RPC's `signature` param.)

**Output:**
```json
{"verified":true,"confirmations":15,"amount":"1.5","tx_hash":"c36258a...","address":"77Vx9cs..."}
```
On failure (wallet rejects the proof, `good=false`, or RPC error other than `RPC_UNREACHABLE`) returns `PROOF_INVALID`. `RPC_UNREACHABLE` is surfaced as-is (connectivity failure, not an invalid proof).

## list_incoming.sh

**Flags:**
- (default): confirmed + unconfirmed.
- `--all`: explicit alias for default.
- `--confirmed-only`: only `confirmations >= MONERO_CONFIRMATIONS` (takes precedence over `--all` if both given).
- `--since-block N`, `--since-timestamp N`, `--limit N` (default `100`), `--account N` (default `0`).

**RPC:** `refresh` (if enabled), then `get_transfers`:
```json
{"method":"get_transfers","params":{"in":true,"out":false,"pool":true,"pending":true,"filter_by_height":true,"min_height":1523000,"account_index":0}}
```

**Output** (array; empty `[]` when none):
```json
[{"tx_hash":"c36258a...","amount":"1.5","confirmations":15,"address":"77Vx9cs...","address_index":3,"timestamp":1535918400,"confirmed":true,"unlock_time":0}]
```

## list_outgoing.sh

**Flags:** `--since-block N`, `--since-timestamp N`, `--limit N` (default `100`), `--account N` (default `0`).

**RPC:** `refresh` (if enabled), then `get_transfers` with `out:true` (and `in:false`).

**Output** (array; empty `[]` when none):
```json
[{"tx_hash":"a1b2c3...","amount":"0.5","fee":"0.0000435","timestamp":1535918500,"address":"77Vx9cs...","address_index":3,"unlock_time":0}]
```

## list_addresses.sh

**Flags:** `--account N` (optional, default `0`).

**RPC:** `get_address` `{"account_index":0}` (uses `get_address`, not `get_balance`'s `per_subaddress`, because the latter only lists addresses with activity).

**Output** (array):
```json
[{"index":0,"address":"55LTR8...","label":"Primary account","balance":"0.5","unlocked_balance":"0.5"}]
```
Does not auto-refresh.

## validate_address.sh

**Flags:** `--address "ADDR"` (required).

**RPC:** `validate_address` **with `any_net_type:true`** so the real `nettype` is returned:
```json
{"method":"validate_address","params":{"address":"ADDR","any_net_type":true,"allow_openalias":false}}
```
RPC returns `valid`, `nettype`, `subaddress`, `integrated`, `openalias_address`.

**Output:**
```json
{"valid":true,"network":"mainnet","network_match":true,"subaddress":false,"integrated":false}
```
`network`/`network_match` are derived client-side: `network` is the RPC's `nettype`; `network_match` is `nettype == MONERO_NETWORK`. There is **no `checksum_valid` field** — the checksum is part of `valid`. This keeps `INVALID_ADDRESS` (`valid=false`) distinct from `NETWORK_MISMATCH` (`valid=true`, `network_match=false`). Does not auto-refresh.

## sync_status.sh

**Flags:** none.

**RPC:** `get_height` and `get_version`, both via `/json_rpc`.

**Output:**
```json
{"height":1523651,"daemon_connected":true,"wallet_version":196613}
```
`daemon_connected` is a **real reachability proxy**: `true` iff both `get_height` and `get_version` succeeded (if either fails the script exits `RPC_UNREACHABLE`). `wallet_version` is the raw integer from `get_version` (a packed integer such as `196613`, **not** a dotted string). The wallet RPC cannot honestly report the daemon's `target_height` or sync progress, so `synced`/`target_height` are intentionally **not** emitted (a prior version reported an always-true `synced`, which gave false confidence). Point-in-time; does not auto-refresh (it is the status check itself).
