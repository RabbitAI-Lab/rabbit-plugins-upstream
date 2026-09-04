---
name: x402-cli
version: 1.2.4
description: A simple CLI that helps AI agents discover x402 services and make paywalled requests. Become part of the agentic-economy!
metadata:
  x402:
    category: payments
    protocol: x402
    auth: evm-wallet
  openclaw:
    primaryEnv: CLIENT_EVM_WALLET_SECRET
    envVars:
      - name: CLIENT_EVM_WALLET_SECRET
        required: false
        description: >-
          EVM private key (0x...) for the wallet used to sign and send payments. Only required
          for `request pay`; `discover list`, `discover search`, and `request info` work without it.
---

# x402 CLI

A CLI that lets an AI agent discover x402-paywalled services, inspect what they cost, and pay for them — autonomously, with no human confirmation step. `request pay` moves real funds (Base USDC) the instant it runs. The safeguard is bounded wallet funding (see [Setup](#setup)), not a confirmation prompt — if you need a confirmation gate, add it in your own orchestration layer before calling this CLI.

## Skill Files

| File | Purpose |
|------|---------|
| **SKILL.md** (this file) | How to use the CLI |
| **x402_cli.py** | CLI implementation |
| **requirements.txt** | Python dependencies |
| **DISCLOSURES.md** | Detailed risk disclosures and safeguard requirements |
| **NOTICE.md** | Legal notice, liability limitations, and third-party service disclaimers |

## Quick Reference

| Command | Wallet secret required | Moves funds | Writes a file by default | Purpose |
|---|---|---|---|---|
| `discover list` | no | no | no (`--save` to opt in) | Paginated catalog of x402 services |
| `discover search <query>` | no | no | no (`--save` to opt in) | Semantic search over the catalog |
| `request info <url>` | no | no | no (`--save` to opt in) | Inspect payment requirements, no payment sent |
| `request pay <url>` | **yes** | **yes** | no (`--save` to opt in) | Pay and fetch the service response |

Typical flow: `discover` → `request info` → `request pay`. See [Workflow](#workflow).

## Setup

1. **Get a wallet.** This CLI only reads a private key from `CLIENT_EVM_WALLET_SECRET` — it never generates or stores one. Use `create-crypto-wallets` to generate one and `keepass-cli` to store it (see [Integration Guidance](#integration-guidance) for exact commands).
2. **Fund it, deliberately small.** The wallet's balance *is* the security boundary for this skill:
   - Normal use: 5–10 USDC on Base
   - Higher-volume use: up to 50–100 USDC, only if you trust the calling agent's spending behavior
   - Never fund with a personal or high-value key — always a fresh, dedicated wallet
3. **Install deps and export the key** before invoking the CLI:
   ```bash
   python -m pip install -r requirements.txt
   export CLIENT_EVM_WALLET_SECRET="0x..."   # retrieve from keepass-cli at runtime, never hardcode!
   ```
   There is no `--key` flag by design — a CLI argument would leak into shell history, process listings, and logs.

## Commands

### `discover list`

```bash
python x402_cli.py discover list --limit 10 --offset 0 [--save] [--output-dir DIR]
```

| Flag | Default | Meaning |
|---|---|---|
| `--limit` | `50` | Max resources per page (max 100) |
| `--offset` | `0` | Pagination offset |
| `--save` | off | Also write the response to a generated JSON filename |
| `--output-dir` / `-o` | `.` | Directory for `--save` output |

Returns the paginated x402 discovery catalog. See [Discovery Response Schema](#discovery-response-schema) for the shape of each resource.

### `discover search <query>`

```bash
python x402_cli.py discover search "weather data" [--save] [--output-dir DIR]
```

Same flags as `discover list`. `query` is a free-text string matched semantically against service descriptions/tags. Response includes `partialResults: true` if the search timed out with incomplete results.

### `request info <url>`

```bash
python x402_cli.py request info https://example.com/paywalled-endpoint \
	--method post --data '{"foo":"bar"}' --header '{"Authorization":"Bearer ..."}'
```

| Flag | Default | Meaning |
|---|---|---|
| `--method` | `post` | `get` or `post` |
| `--data` | none | JSON object string, sent as request body/params |
| `--header` | none | JSON object string, sent as request headers |
| `--timeout` | `60` | Request timeout in seconds |
| `--save` / `--no-save` | **opt-in (off)** | Write input+response to JSON (see [Saved Request/Response Files](#saved-requestresponse-files)) |
| `--output-dir` / `-o` | `.` | Directory for the saved file |

Sends a plain HTTP request with no payment — the endpoint typically replies `402 Payment Required` with payment instructions. Does **not** require `CLIENT_EVM_WALLET_SECRET`. Always run this before `request pay` to confirm amount, network, and recipient.

### `request pay <url>`

```bash
python x402_cli.py request pay https://example.com/paywalled-endpoint \
  --method post --data '{"foo":"bar"}' --header '{"Authorization":"Bearer ..."}' \
  --spend-limit 1.0
```

Same flags as `request info`, plus it requires `CLIENT_EVM_WALLET_SECRET`. Signs an x402 payment, sends it on Base mainnet, then sends the request and returns the service's response.

| Flag | Default | Meaning |
|---|---|---|
| `--spend-limit` | `1.0` | Maximum USDC to authorize for the payment request |

**⚠️ This authorizes an on-chain payment the moment it runs — there is no confirmation prompt.** A warning is printed to stderr immediately beforehand as a last reminder, but it does not block execution. Always inspect with `request info` first.

## Output Contract

Every invocation prints exactly **one** JSON object to stdout, then exits with:
- `0` — success
- `2` — handled error (bad input, missing env var, network failure)
- `1` — unexpected/internal error

Match errors on `error_code` (stable across versions), not on the human-readable `error` string:

| `error_code` | Meaning |
|---|---|
| `invalid_argument` | Bad CLI arguments |
| `invalid_json` | `--data` / `--header` wasn't valid JSON |
| `missing_env_var` | `CLIENT_EVM_WALLET_SECRET` not set (only for `request pay`) |
| `network_error` | Transport failure — DNS, timeout, connection refused |
| `internal_error` | Unexpected exception; check the accompanying `type` field for the Python exception class |

Security warnings (the `request pay` payment notice) print to **stderr**, never stdout — stdout always contains exactly one JSON object regardless of what's on stderr.

**Success envelopes:**

```json
// discover list / discover search
{"ok": true, "action": "discover-list", "resources": {"...": "..."}}
// + "saved_to": "..." if --save was passed

// request info
{"ok": true, "action": "request-info", "status_code": 402, "data": {"...": "..."}}
// + "saved_to": "..." unless --no-save was passed

// request pay
{"ok": true, "action": "request-pay", "status_code": 200, "data": {"...": "..."}}
// + "saved_to": "..." unless --no-save was passed
```

**Failure envelope (any command):**
```json
{"ok": false, "error": "...", "error_code": "..."}
```

Notes on `request info` / `request pay` specifically:
- `data` is the endpoint's JSON body, or `{"raw": "..."}` if it wasn't valid JSON.
- HTTP 4xx/5xx from the *destination* is still `"ok": true` — it's a valid response, not a CLI failure. Only transport-level failure produces `"ok": false"` / `network_error`.

### Saved Request/Response Files

`request info` and `request pay` can write a JSON file with `--save` (opt-in, disabled by default; `--output-dir`/`-o` to choose where). A stderr notice is printed whenever saving is enabled. Filename pattern: `x402_request_info_<timestamp>.json` / `x402_request_pay_<timestamp>.json`.

```json
{
  "input": {
    "header": {"Authorization": "[REDACTED]"},
    "data": {"foo": "bar"}
  },
  "response": {
    "status_code": 402,
    "data": {"...": "..."}
  }
}
```

- `input.header` / `input.data` are what was passed via `--header` / `--data` (`null` if omitted). Header values matching common auth conventions (`Authorization`, `Cookie`, `Set-Cookie`, `X-API-Key`, etc., case-insensitive) are replaced with `"[REDACTED]"` before writing — **only header values are redacted; the request body/data and the service's response are stored as-is.** If either may carry secrets or sensitive data, omit `--save`.
- `response` is `{"status_code": ..., "data": ...}` on success, or `{"error": "...", "error_code": "..."}` on failure — **the file is written either way**, giving you an audit trail even for failed/rejected payments.
- For `request pay`, treat these files as your local payment ledger.

## Workflow

```
1. discover list / discover search <query>
        → get candidate "resource" URLs
              ↓
2. request info <resource_url>          (no cost, no wallet needed)
        → confirm scheme/network/amount/payTo match what you expect
        → confirm input/output format via extensions.bazaar in the discovery entry
              ↓
3. request pay <resource_url>            (moves real funds — no confirmation prompt)
        → signs payment with CLIENT_EVM_WALLET_SECRET, sends it, returns the service response
```

Skipping step 2 means authorizing a payment blind. Always run `request info` first unless you already know the exact payment requirements for that URL.

## Networks & Security Model

- **Base mainnet only** (`eip155:8453`). Testnets are not supported and will fail — confirm your wallet holds Base-mainnet funds before calling `request pay`.
- **No confirmation gate by design.** This skill is built for autonomous use: an agent can discover, inspect, and pay without stopping for human approval. The risk boundary is the wallet's funding limit, not the CLI. Wrap it in your own orchestration if you need a human-in-the-loop step.

### Capabilities (explicit declaration)

This is a high-impact financial tool. Its full runtime capability surface:

| Capability | Scope | Detail |
|---|---|---|
| Environment read | `CLIENT_EVM_WALLET_SECRET` only | Read once per `request pay` invocation, held in memory only, never written to disk or logs by this CLI. See [`metadata.openclaw`](#) in the frontmatter for the declared env var. |
| Network (fixed) | Coinbase CDP discovery endpoints | `discover list` / `discover search` call `api.cdp.coinbase.com` only. |
| Network (arbitrary) | Any URL passed to `request info` / `request pay` | The URL, HTTP method, `--header`, and `--data` you supply are sent as-is to that third-party endpoint — treat it as untrusted. |
| Blockchain write | Base mainnet (`eip155:8453`) | Only from `request pay`; signs and submits a real, irreversible USDC transfer using `CLIENT_EVM_WALLET_SECRET`. |
| File write | Local disk, opt-in only | Only when `--save` is passed to `discover ...` / `request info` / `request pay`; see [Saved Request/Response Files](#saved-requestresponse-files). No files are written otherwise. |
| Process execution | None | No shell/subprocess execution anywhere in this CLI. |

No other environment variables, files, or subprocesses are touched.

## Discovery Response Schema

Both `discover list` and `discover search` return an array of resources shaped like:

```json
{
  "resource": "https://api.example.com/service",
  "type": "http",
  "description": "Human-readable service description",
  "x402Version": 2,
  "accepts": [
    {
      "scheme": "exact",
      "network": "eip155:8453",
      "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "amount": "1000",
      "payTo": "0x...(recipient_address)",
      "maxTimeoutSeconds": 3600,
      "extra": {"name": "USD Coin", "version": "2"}
    }
  ],
  "lastUpdated": "2026-08-07T15:45:20.968Z",
  "quality": {"l30DaysTotalCalls": 627, "l30DaysUniquePayers": 610, "lastCalledAt": "2026-08-07T06:35:46.22Z"},
  "extensions": {
    "bazaar": {
      "info": {
        "input": {"description": "Expected request format", "example": {"query": "weather"}},
        "output": {"description": "Expected response format", "example": {"temperature": 72, "conditions": "sunny"}}
      }
    }
  }
}
```

| Field | Meaning |
|---|---|
| `resource` | The URL to pass to `request info` / `request pay` |
| `description` | Human-readable summary |
| `quality` | 30-day call volume/unique-payer counts — use to gauge reliability before paying |
| `extensions.bazaar.info` | Example input/output shapes — use to construct `--data`/`--header` correctly before `request pay` |
| `accepts` | Array of payment options for this resource, see below |

**`accepts[]` fields** — a resource may list multiple options (different schemes/networks); pick one matching your wallet's capabilities:

| Field | Meaning |
|---|---|
| `scheme` | Financial semantics — `exact`, `upto`, or `batch-settlement`. See [Payment Schemes](#payment-schemes). |
| `network` | e.g. `eip155:8453` (Base mainnet). The CLI only supports Base mainnet. |
| `amount` | Smallest-unit amount. For `exact`, the fixed price. For `upto`, the authorized maximum. |
| `asset` | Token contract address (e.g. USDC on Base) |
| `payTo` | Recipient wallet address |
| `maxTimeoutSeconds` | Authorization validity window, in seconds |

## Payment Schemes

The `scheme` field in each `accepts[]` entry tells you the financial model in play:

| Scheme | Settlement timing | `amount` meaning | Typical use |
|---|---|---|---|
| `exact` | Synchronous, on-chain, per request | Fixed price you pay | Article paywalls, per-call tool pricing |
| `upto` | Synchronous, on-chain, per request | **Maximum** authorized; actual charge ≤ this, set by the server after usage | LLM token billing, bandwidth metering |
| `batch-settlement` | Deferred — commitment now, transfer later | Per-request cap; running total settled out-of-band | High-volume micropayments, escrow/channel-based billing |

Nuances not captured by the table:
- **`upto`**: the same `amount` field is phase-dependent — at verification it's the max you authorize, at settlement it's what the server actually charges. Your wallet is only ever charged the settlement-time amount, never more than the authorized max.
- **`batch-settlement`**: backed by either **capital** (client's own pre-funded escrow/channel) or **credit** (a network intermediary underwrites and bills later). The CLI handles commitment signing; redemption timing/mechanism is defined by the network binding, not by this CLI.

`scheme` and `network` are independent axes — a resource can advertise the same `scheme` across multiple `network`s (e.g. `exact` on both Base and Solana). The CLI matches whichever combination your wallet supports (currently: `exact`/`eip155:8453` only).

## Integration Guidance

### Setting up with other skills

To securely manage your x402 wallet, combine this skill with `create-crypto-wallets` and `keepass-cli`:

**1. Generate a dedicated wallet** with `create-crypto-wallets`:
```bash
openclaw skills install @beocca/create-crypto-wallets

# Generate a 12-word BIP39 mnemonic
MNEMONIC=$(hdwallet generate mnemonic --client BIP39 --words 12)

# Derive the Ethereum wallet
WALLET=$(hdwallet dump --symbol ETH --hd BIP44 --mnemonic "$MNEMONIC")

# Extract private key and address
PRIVATE_KEY=$(echo "$WALLET" | jq -r '.private_key')
ADDRESS=$(echo "$WALLET" | jq -r '.address')
```

**2. Store securely** with `keepass-cli`:
```bash
openclaw skills install @beocca/keepass-cli

# Store in your KeePass database
python keepass_cli.py add-entry \
  --title "x402-wallet" \
  --username "$ADDRESS" \
  --password "$PRIVATE_KEY" \
  --group "Wallets"
```

**3. Fund the wallet** on Base mainnet with 10–20 USDC

**4. Retrieve and use at runtime:**
```bash
# Retrieve the private key from KeePass
PRIVATE_KEY=$(python keepass_cli.py show-entry --title "x402-wallet" --show-secrets | jq -r '.password')

# Set and use
export CLIENT_EVM_WALLET_SECRET="$PRIVATE_KEY"
python x402_cli.py discover list --limit 5
```

**Reducing shell exposure of the private key:** commands above and in these examples pass the key through shell variables, which can be recovered from shell history, process listings (`ps`), crash dumps, or inherited subprocess environments. To reduce this risk:
- Disable history for the session before exporting secrets (`set +o history`, then `set -o history` afterward), or run the retrieval/export/CLI sequence inside a script instead of an interactive shell.
- Unset the variable as soon as the CLI call completes (`unset CLIENT_EVM_WALLET_SECRET PRIVATE_KEY`).
- Never pass the key as a CLI argument (there is no `--key` flag by design) or print it with `echo`/logging.
- Prefer piping the secret directly into the environment of the single `python x402_cli.py ...` invocation (e.g. `CLIENT_EVM_WALLET_SECRET=$(...) python x402_cli.py ...`) over multi-step `export` so it isn't retained in the shell's exported-variable table for the rest of the session.

### Example workflow: discover, inspect, pay

```bash
# Search for a service
SEARCH=$(python x402_cli.py discover search "your_query")
RESOURCE=$(echo "$SEARCH" | jq -r '.resources.resources[0].resource')

# Inspect what it costs (no payment required)
INFO=$(python x402_cli.py request info "$RESOURCE" --method GET)
echo "$INFO" | jq '.data'

# If satisfied, pay for the service
RESULT=$(python x402_cli.py request pay "$RESOURCE" --method GET)
echo "$RESULT" | jq '.data'
```

## Related Skills

- **keepass-cli** to manage your passwords, credentials, and secrets. Install via `openclaw skills install @beocca/keepass-cli`
- **create-crypto-wallets** is a more sophisticated skill to create crypto wallets using the python-hdwallet library. Install via `openclaw skills install @beocca/create-crypto-wallets`
- **agmsg-cli** allows you to interact with AgMsg — the communication layer for autonomous agents. Install via `openclaw skills install @beocca/agmsg-cli`
- **agnet-cli** allows you to interact with AgNet — the collective brain of the agentic web. There, you can publish, reply to, and react to other agents' content. Install via `openclaw skills install @beocca/agnet-cli`
- **x402-seller** explains to you how to sell your own services using x402. Install via `openclaw skills install @beocca/x402-seller`

## External Documentation

**x402 Protocol & Docs:**
- [x402 Official Site](https://x402.org/) — Main x402 hub
- [x402 Documentation](https://docs.x402.org/introduction) — Complete technical reference
- [x402 GitHub Repository](https://github.com/x402-foundation/x402) — Reference implementations for TypeScript, Go, Python

**CDP (Coinbase Developer Platform):**
- [CDP Getting Started](https://docs.cdp.coinbase.com/get-started/overview) — Set up CDP API keys and wallets
- [CDP x402 Facilitator Docs](https://docs.cdp.coinbase.com/x402/introduction) — Production payment settlement

**Service Discovery & Monitoring:**
- [x402scan](https://www.x402scan.com/) — Service discovery engine; see what's selling
- [x402 GitHub: x402scan](https://github.com/Merit-Systems/x402scan) — Open source service crawler
