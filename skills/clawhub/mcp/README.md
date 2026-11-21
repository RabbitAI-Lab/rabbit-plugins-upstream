# `@cryptoslip/mcp` — PocketSlip MCP Server for Autonomous Agents

Non-custodial Model Context Protocol (MCP) server for **CryptoSLIP Protocol V3.2** (`v33`: `0x3f80aa68Fb4834d6E119EE1cf932C14419Cf63EB`) on **Base Mainnet (`8453`)**.

Instead of handing an LLM standing authority over a master private key, hand it a bounded `$5.00 USDC` (`ETH`, `cbBTC`, or `NARA`) `#` Slip URL via `CRYPTOSLIP_URL`.

## Security Architecture

- **`V-01` `<1s` Boot Auto-Keep Rotation:** On startup (`bootAndRotate()`), if the slip is unrotated (`nonces == 0`), `PocketSlipVault` immediately executes an on-chain `Keep` (`0%` protocol fee), rotating `claimSigner` to a fresh local key persisted with `0600` permissions. The original `.env` link is invalidated on-chain, bounding prompt-injection risk strictly to that single slip.
- **`V-02` Out-of-Context `BoundedAgentPolicy` Firewall:** Deterministically enforces `maxPerCallUsdMicro`, `maxSpendsPerMinute`, `maxDailyUsdMicro`, `assertSafeDestination` (blocking burn addresses, token contracts, vaults, routers, and known public test addresses), optional recipient/domain allowlists, `redactSecretsFromToolOutput`, and `100%` Uniswap V4 `NARALiquidityHookV5` (`0x07d8F2Dfd121B10dE3176DeAb6A8C0eaa2646aCC`) swap enforcement.
- **`V-03` Per-Slip Mutex & `$0.10` Remainder Guard:** Serializes concurrent tool calls via `SlipMutex` and prevents sub-minimum change reverts (`$0.10 USDC`, `100 sats` cbBTC, `0.000001` ETH/NARA).
- **`V-04` Circle `TokenPaymasterV08` Default:** Headless agent operations default to self-funded `USDC` network fees via Circle `TokenPaymasterV08` (`0x0578cFB241215b77442a541325d6A4E6dFE700Ec`) + `Simple7702Account` (`0xe6Cae83BdE06E4c305530e199D7217f42808555B`).

## Quick Start

```bash
CRYPTOSLIP_URL="<YOUR_SLIP_URL>" npx @cryptoslip/mcp
```

### Claude Desktop / Claude Code / Cursor Configuration

```json
{
  "mcpServers": {
    "cryptoslip": {
      "command": "npx",
      "args": ["-y", "@cryptoslip/mcp"],
      "env": {
        "CRYPTOSLIP_URL": "<YOUR_SLIP_URL>",
        "CRYPTOSLIP_MAX_PER_CALL_USD": "0.50",
        "CRYPTOSLIP_MAX_DAILY_USD": "5.00",
        "CRYPTOSLIP_MAX_SPENDS_PER_MIN": "3"
      }
    }
  }
}
```

## Tools Exposed Over Stdio

| Tool | Purpose |
| :--- | :--- |
| `cryptoslip_status` | Redacted slip & wallet balance, active vault (`v33`), rotation status, and policy caps (zero raw keys). |
| `cryptoslip_pay_human` | Splits or creates a `#startapp=slip_...` link (or 12-char `scrypt` code) for X/Telegram/SMS human bounties (`No take-back` or revocable). |
| `cryptoslip_batch_payout` | 1-tx `Multicall3` batch dispenser (`1..500` items) returning JSON or CSV `#` links with `bc_ea68lz8s` Builder Code. |
| `cryptoslip_pay_x402_or_merchant` | Pays an HTTP `402` endpoint or merchant wallet via `splitAndPay` under `BoundedAgentPolicy` + `SlipMutex`. |
| `cryptoslip_verify_or_export_receipt` | Verifies or exports a cryptographic `PaymentReceiptBundleV1` (`JSON`, `CSV`, or printable HTML). |
| `cryptoslip_reclaim_unclaimed` | `0%`-fee `refundSlipDirect` recovery for unclaimed revocable (`cancelLockedUntil == 0`) DM slips. |
| `cryptoslip_withdraw_referrals` | Claims `0.25%` (`50/50` share) lifetime `referralCredits` on Base Mainnet. |

## Environment Variables

| Variable | Default | Description |
| :--- | :--- | :--- |
| `CRYPTOSLIP_URL` | *(required for PocketSlip)* | `#startapp=slip_...` pocket-funds URL; rotated on boot via `Keep` (`0%` fee). |
| `CRYPTOSLIP_STATE_PATH` | `~/.cryptoslip-mcp/pocket-state.json` | `0600` local file storing rotated local signer state across restarts. |
| `CRYPTOSLIP_RPC_URL` | `https://mainnet.base.org` | Base Mainnet (`8453`) JSON-RPC endpoint. |
| `CRYPTOSLIP_MAX_PER_CALL_USD` | `"0.50"` | Maximum USD-equivalent value allowed per single spend call. |
| `CRYPTOSLIP_MAX_DAILY_USD` | `"5.00"` | Maximum rolling 24-hour USD-equivalent spend limit. |
| `CRYPTOSLIP_MAX_SPENDS_PER_MIN` | `"3"` | Sliding-window per-minute spend count limit. |
| `CRYPTOSLIP_ALLOWED_RECIPIENTS` | *(unset)* | Optional comma-separated `0x...` recipient allowlist. |
| `CRYPTOSLIP_ALLOWED_DOMAINS` | *(unset)* | Optional comma-separated HTTPS hostname allowlist for HTTP `402` endpoints. |

## OpenClaw / Skill Manifest

See [`SKILL.md`](./SKILL.md) for the ready-to-drop skill manifest.
