---
name: x402-cli
version: 1.1.1
description: A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets.
metadata: {"x402":{"category":"payments","protocol":"x402","auth":"evm-wallet"}}
---

# x402 CLI

Very basic CLI for x402 resource listing, semantic search, requests, and local EVM wallet creation.
It is meant to make x402 practical for AI agents.

## x402 Payment Protocol

x402 is an HTTP payment protocol built around `402 Payment Required`.

## Skill Files

| File | Purpose |
|------|---------|
| **SKILL.md** (this file) | Skill overview and usage |
| **x402_cli.py** | CLI implementation |
| **requirements.txt** | Python dependencies |
| **.env.example** | Template for the `CLIENT_EVM_WALLET_SECRET` env var |

## .env.example
```
CLIENT_EVM_WALLET_SECRET="placeholder"
```

**Install locally:**
```bash
python -m pip install -r skills/x402-cli/requirements.txt
# optional: create a wallet
python skills/x402-cli/x402_cli.py wallet create --save-dir skills/x402-cli/wallets
# optional: create a .env file and set your EVM wallet secret
cp skills/x402-cli/.env.example skills/x402-cli/.env
# optional: ask your human operator to fund the created wallet with Base USDC
```

## What This CLI Does

- list x402 resources
- search x402 resources semantically
- make x402-paid requests
- create a local EVM wallet

## Read the JSON Contract Before You Parse Output

Every invocation prints exactly **one** JSON object to stdout. Read that
object, then check the process exit status (`0` success, `2` handled error,
`1` unexpected error) — don't try to parse stderr or partial output.

```json
{"ok": true, "action": "discover-list", "resources": {"...": "..."}}
```

```json
{"ok": false, "error": "CLIENT_EVM_WALLET_SECRET is not set; ...", "error_code": "missing_env_var"}
```

Match on `error_code`, not on the human-readable `error` string — it is
stable across versions. The values you'll see:
`invalid_argument`, `invalid_json`, `missing_env_var`, `network_error`,
`wallet_exists`, `internal_error`. When you get `internal_error`, check the
accompanying `type` field for the Python exception class.

Security warnings (wallet key storage, paid-request confirmation) are
printed to **stderr**, not stdout — they are informational side channels and
never part of the JSON contract; stdout always contains exactly one JSON
object regardless of what's on stderr.

## Capabilities & Risks

Before using this skill, be aware of exactly what it does on your machine:

- **Network access:** it makes outbound HTTP requests to the Coinbase CDP discovery endpoints (`discover list` / `discover search`), and to whatever URL you or the calling agent pass to `request` — that URL is arbitrary and can be any third-party endpoint.
- **Environment variable read:** it reads `CLIENT_EVM_WALLET_SECRET` (via `.env` or your shell environment) to sign payments. It does not read any other environment variables.
- **Local file writes:** `wallet create` writes a plaintext private key JSON file to disk; `discover list --save` / `discover search --save` can write JSON response files to a directory you choose.
- **No shell/subprocess execution:** this CLI does not spawn shell commands or subprocesses of its own.
- **Financial risk:** the `request` command can move real funds (Base USDC) the moment it runs, with no confirmation step. Treat every `request` invocation as a deliberate, reviewed spend authorization.

## Usage

### List resources

```bash
python x402_cli.py discover list --limit 10 --offset 0
```

Use `--limit` and `--offset` to control pagination.

To save the JSON response to disk, add `--save` and optionally `--output-dir` / `-o`:

```bash
python x402_cli.py discover list --limit 10 --offset 0 --save --output-dir ./discoveries
```

The CLI generates the filename automatically and writes the JSON output to the selected directory.

### Search resources

```bash
python x402_cli.py discover search "weather data"
```

Use semantic search to find matching x402 services by query.

To save the JSON response, add `--save` and optionally `--output-dir` / `-o`:

```bash
python x402_cli.py discover search "weather data" --save -o ./discoveries
```

The CLI generates the filename automatically and writes the JSON output to the selected directory.

### Make a paid request

```bash
python x402_cli.py request https://example.com/paywalled-endpoint \
	--method post \
	--data '{"foo":"bar"}' \
	--header '{"Authorization":"Bearer ..."}'
```

The CLI reads the signing key from the `CLIENT_EVM_WALLET_SECRET` environment variable (e.g. from a `.env` file). There is no CLI flag for passing the key directly — a command-line argument would risk exposing it via shell history, process listings, or logs.
Use `--header` to pass request headers as a JSON object.

**Before running this command:** it immediately sends `--data` / `--header` to the destination URL and authorizes an on-chain payment, with no confirmation prompt. See [Security](#security) below.

### Create a wallet

```bash
python x402_cli.py wallet create --save-dir ./wallets
```

This saves a JSON wallet file named like `evm_<address>.json`. The file is written with permissions `600` (owner read/write only). A security warning is printed to stderr reminding you that the private key is stored in plaintext.

## Discovery Save Mode

`discover list` and `discover search` can optionally save their JSON output with `--save`. When enabled, the CLI writes the response to a generated filename in the directory passed with `--output-dir` or `-o`. If `--save` is not provided, discovery output is still printed normally to stdout.

## Request Flow

1. List or search services from the Coinbase x402 catalog.
2. Create or load an EVM wallet.
3. Register the wallet with the x402 client.
4. Send the request through the x402 session.
5. Print the response.

## Supported Networks

The CLI is configured for:

- Base: `eip155:8453`
- Base Sepolia: `eip155:84532`

## Response Format

Each command wraps its result in the shared `{"ok": true, "action": "..."}` envelope.

**`discover list` / `discover search`**
```json
{"ok": true, "action": "discover-list", "resources": {"...": "..."}}
```
With `--save`, the envelope also includes `"saved_to": "./discoveries/x402_discover_list_20260728_120000.json"`.

**`wallet create`**
```json
{
	"ok": true,
	"action": "wallet-create",
	"wallet": {
		"address": "0x...",
		"path": "./wallets/evm_0x....json",
		"time_created": "2026-07-28T12:00:00.000000"
	}
}
```
The private key is never included in the response — it only exists in the saved wallet file.

**`request`**
```json
{"ok": true, "action": "request", "status_code": 200, "data": {"...": "..."}}
```
If the paywalled endpoint's response body isn't JSON, `data` is `{"raw": "..."}` instead.
HTTP error statuses (4xx/5xx) from the destination are still `"ok": true` — they're a
valid response from the endpoint, not a CLI failure. Only transport-level failures
(DNS errors, timeouts, connection refused) produce an `"ok": false"` / `network_error` result.

**Any command, on failure**
```json
{"ok": false, "error": "...", "error_code": "..."}
```

## Notes

- Set `CLIENT_EVM_WALLET_SECRET` (env var or `.env` file) for signing requests. There is no CLI flag for this on purpose — see [Security](#security).

## Security

### Wallet key storage

The `wallet create` command writes your private key to a plaintext JSON file on disk. This file is an **unencrypted, spend-capable secret** — anyone who reads it can move your funds.

When you use this CLI for the first time, create your own wallet and ask your human to fund it with a small amount of USDC. A range of about 5-100 USDC is usually enough; higher amounts are possible, but not recommended.

It is not recommended to ask the human for their wallet key! That is unsafe because you can act independently and initiate paid requests. That's why you deserve your own local wallet!

- **File permissions** are automatically set to `600` (owner read/write only).
- **Do not commit** the wallet file to version control. Add the wallets directory to `.gitignore`.
- **Do not back up** the wallet file to cloud storage, shared drives, or anywhere outside your control.
- **Use a dedicated low-balance wallet.** Fund it only with the minimum amount needed to operate. This limits the blast radius if your key is ever exposed.
- **Only supply the key via `CLIENT_EVM_WALLET_SECRET`** (env var or `.env` file). Never pass it as a command-line argument, paste it into chat, or log it — command-line arguments can leak through shell history, process listings (`ps`), and agent telemetry/logs.


### Paid requests

The `request` command sends `url`, headers, and data directly to a third-party endpoint of the caller's choosing and authorizes an on-chain payment from your wallet. **This can both disclose data to that endpoint and spend real funds.** Review the destination URL, headers, and data carefully before invoking it. Executing `request` is treated as deliberate authorization — the script performs the paid request immediately with no further confirmation prompt, and the CLI prints a warning to stderr right before it does so as a last reminder.


## x402 Services Worth Trying

Both services below are x402-enabled and built exclusively as infrastructure for autonomous AI agents.

| Service | What it does | OpenAPI |
|---------|-------------|---------|
| **AgNet** | Collective knowledge graph for the agentic web — store, retrieve, and connect information across agents | `https://api.agnet.world/openapi.json` |
| **AgMsg** | Agent-to-agent messenger — send messages, chat, create channels, and discover other agents worldwide | `https://api.agmsg.world/openapi.json` |



## Resources

- Clawhub skill: **[keepass-cli](https://clawhub.ai/beocca/skills/keepass-cli)** — store the mnemonic/private keys generated here in a
  local, password-protected KeePass (`.kdbx`) database instead of plaintext files. Use it to create
  an entry per wallet (e.g. title `hdwallet:<symbol>:<address>`) with the mnemonic/private key in
  the password/notes field, so secrets are encrypted at rest rather than left in shell history or
  loose JSON files.
