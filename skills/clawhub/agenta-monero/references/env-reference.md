# Environment Variables

All configuration is read from `.env` (parsed safely — never sourced) at the skill root. Copy `.env.example` to `.env` and edit; run `./setup.sh` after changing it. Values shown are defaults.

## Connection

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_RPC_URL` | `http://127.0.0.1:18088` | URL of the running `monero-wallet-rpc`. |
| `MONERO_RPC_USER` | _(empty)_ | RPC authentication username. Written into `$MONERO_LOCK_DIR/.netrc` (mode `0600`). |
| `MONERO_RPC_PASSWORD` | _(empty)_ | RPC authentication password. Written into `.netrc`; never passed on the command line. |
| `MONERO_WALLET_NAME` | _(empty)_ | Wallet name; must match the wallet loaded in the RPC server. |

## Network

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_NETWORK` | `mainnet` | `mainnet` \| `stagenet`. `validate_address` compares each address's `nettype` against this to derive `network_match`. |

## Lifecycle

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_LIFECYCLE` | `none` | `none` = assume the wallet RPC is already running (the supported mode). `full` = the agent is expected to manage daemon + wallet lifecycle (reserved). |

## Remote node (optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_REMOTE_NODE` | _(empty)_ | Remote node hostname/IP, if used. |
| `MONERO_REMOTE_PORT` | _(empty)_ | Remote node port. |

## Display

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_CONFIRMATIONS` | `10` | Blocks before a payment is considered `confirmed`. Used by `verify_payment`, `get_transfer`, `list_incoming`. |
| `MONERO_AMOUNT_FORMAT` | `xmr` | `xmr` \| `piconero`. Output amount rendering (scripts emit XMR decimal strings by default). |

## Refresh

There is no `sync` RPC; the wallet refreshes from the daemon via `refresh`, which can take seconds-to-minutes. Refresh is **operation-aware** (see `rpc-reference.md` for the per-op table).

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_AUTO_REFRESH` | `true` | `true` = refresh before balance/transfer/verify ops; `false` = never auto-refresh. |
| `MONERO_REFRESH_MIN_INTERVAL` | `30` | Minimum seconds between refreshes (caching). A refresh is skipped if the last one was more recent than this. Stored in `$MONERO_LOCK_DIR/.last_refresh`. |
| `MONERO_REFRESH_TIMEOUT` | `120` | Maximum seconds for a single `refresh` operation. |

**Override:** any auto-refreshing script accepts `--no-refresh` (works in **any** argument position) to skip the refresh step — useful for fast read-only checks when you can tolerate slightly stale data.

## Retry

The retry helper (`lib/retry.sh`) is **available and unit-tested, but NOT currently applied** to any script RPC call — all scripts call `rpc_call` directly. `send_xmr` and `sweep_all` are intentionally never retried (non-idempotent); `get_transfer` and `check_tx_proof` are intentionally direct so retries don't mask the retry-safety probe / proof classification. Transient codes surface immediately; agents should retry read-only ops themselves (never sends/sweeps). The variables below are reserved for future use and have **no effect today**.

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_RETRY_MAX` | `2` | (Reserved, not currently applied.) Maximum retry attempts for transient errors (`RPC_UNREACHABLE`, `DAEMON_DISCONNECTED`, `SYNC_FAILED`, `REFRESH_FAILED`, `RATE_LIMITED`). |
| `MONERO_RETRY_BACKOFF` | `1` | (Reserved, not currently applied.) Initial backoff in seconds; **doubles per retry** (1, 2, 4, ...). |

## Concurrency

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_LOCK_DIR` | `/tmp/agenta-monero` | Directory for the lock file + netrc. Created with mode `0700`. |
| `MONERO_LOCK_TIMEOUT` | `60` | Maximum seconds to wait to acquire the `flock`. Contention surfaces as `RATE_LIMITED`. |

Every script acquires an exclusive `flock` on `$MONERO_LOCK_DIR/agenta-monero.lock` before any RPC, coordinating multiple local agent processes against the wallet RPC's own serialization. The lock is released on exit.

## Advanced

| Variable | Default | Description |
|----------|---------|-------------|
| `MONERO_RPC_TIMEOUT` | `30` | curl timeout in seconds for individual RPC calls. |
| `MONERO_RPC_SSL_CACERT` | _(empty)_ | Path to a CA cert for self-signed TLS. |
| `MONERO_RPC_SSL_CAPATH` | _(empty)_ | Path to a CA cert directory. |

`setup.sh` warns if `MONERO_RPC_URL` uses `http://` for a non-localhost host.
