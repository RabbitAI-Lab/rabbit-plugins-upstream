---
name: x402card-agent
description: Discover, issue, and manage an x402card wallet-owned virtual card through Base-USDC x402 payments, including capability checks, wallet authentication, idempotent card issuance, card status, balance, and secure credential reveal. Use when an owner wants a virtual card or an agent needs the x402card card contract without exposing a private key.
---

# x402card agent

Install the public CLI with `curl -sSL https://x402card.org/install | sh`, or use the local runtime in `packages/agent` from a source checkout. Use the public MCP only for discovery because it has no wallet authority.

## Safe workflow

1. Run `x402card status` and read `https://api.x402card.org/api/agent` before a money action. From a source checkout, also run `x402card-agent capabilities` and `x402card-agent config`.
2. Configure `X402CARD_SIGNER_COMMAND` to a user-owned signer executable. Never request, export, log, or store its private key or seed phrase.
3. Run `x402card-agent status` to establish or recover the wallet session.
4. Run `x402card-agent issue` once. Let its stable idempotency key recover the same order on retry.
5. Verify the fixed economics before signing: wallet pays 25 USDC on Base, card starts at $25, card platform fee is $10, expected available balance is $15.
6. Read progress with `x402card-agent operation <order-id>`, `cards`, or `balance <card-id>`.
7. Reveal credentials only with `x402card-agent reveal <card-id>` to the controlling TTY, or with explicit `--clipboard`. Never return credentials through MCP, chat, logs, stdout, or files.

The local MCP command is `x402card-mcp`. It may use the signer for bounded owner and issue operations, but it intentionally exposes no generic signing tool and no credential-reveal tool.

Treat unknown settlement state as pending/operator review. Never generate a second payment or change an idempotency key to bypass a pending operation.
