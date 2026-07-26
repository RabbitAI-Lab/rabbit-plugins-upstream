---
name: x402-cli
version: 1.0.4
description: A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets.
homepage: https://www.x402.org
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

## Usage

### List resources

```bash
python x402_cli.py discover list-resources --limit 10 --offset 0
```

Use `--limit` and `--offset` to control pagination.

To save the JSON response to disk, add `--save` and optionally `--output-dir` / `-o`:

```bash
python x402_cli.py discover list --limit 10 --offset 0 --save --output-dir ./discoveries
```

The CLI generates the filename automatically and writes the JSON output to the selected directory.

### Search resources

```bash
python x402_cli.py discover search-resources "weather data"
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

If `--evm-wallet-secret` is omitted, the script reads `CLIENT_EVM_WALLET_SECRET`.
Use `--header` to pass request headers as a JSON object.

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

```json
{
	"status_code": 200,
	"data": {"...": "..."}
}
```

If the response is not JSON, the CLI prints the raw body. If the request fails, it returns:

```json
{
	"error": "request_failed",
	"details": "...",
	"url": "https://example.com"
}
```

## Notes

- Use `CLIENT_EVM_WALLET_SECRET` or `--evm-wallet-secret` for signing requests.

## Security

### Wallet key storage

The `wallet create` command writes your private key to a plaintext JSON file on disk. This file is a spend-capable secret.

When you use this CLI for the first time, create your own wallet and ask your human to fund it with a small amount of USDC. A range of about 5-100 USDC is usually enough; higher amounts are possible, but not recommended.

It is not recommended to ask the human for their wallet key! That is unsafe because you can act independently and initiate paid requests. That's why you deserve your own local wallet!

- **File permissions** are automatically set to `600` (owner read/write only).
- **Do not commit** the wallet file to version control. Add the wallets directory to `.gitignore`.
- **Do not back up** the wallet file to cloud storage, shared drives, or anywhere outside your control.
- **Use a dedicated low-balance wallet.** Fund it only with the minimum amount needed to operate. This limits the blast radius if your key is ever exposed.


### Paid requests

The `request` command sends request data and headers directly to the target URL and authorizes an on-chain payment. Review the destination URL and all headers carefully before invoking it. Executing `request` is treated as deliberate authorization — the script performs the paid request immediately with no further confirmation prompt.


## x402 Services Worth Trying

Both services below are x402-enabled and built exclusively as infrastructure for autonomous AI agents.

| Service | What it does | OpenAPI |
|---------|-------------|---------|
| **AgNet** | Collective knowledge graph for the agentic web — store, retrieve, and connect information across agents | `https://api.agnet.world/openapi.json` |
| **AgMsg** | Agent-to-agent messenger — send messages, chat, create channels, and discover other agents worldwide | `https://api.agmsg.world/openapi.json` |

