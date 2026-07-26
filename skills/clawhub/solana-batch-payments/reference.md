# API Reference — Spraay Solana Gateway

Base URL: `https://gateway-solana.spraay.app`
Network: check `GET /health` → `network` (`devnet` or `mainnet-beta`)
Payment: USDC on Solana via x402 v2, scheme `exact`

## POST /solana/batch-send-sol — $0.01

Build unsigned transactions batch-sending SOL to up to 1,000 recipients.

**Body**

```json
{
  "sender": "string (base58 public key, required — fee payer & source)",
  "recipients": [
    { "address": "string (base58)", "amount": "number (SOL)" }
  ]
}
```

**Response 200**

```json
{
  "success": true,
  "custodial": false,
  "sender": "…",
  "recipients": 100,
  "feeBps": 30,
  "feeLamports": 3000000,
  "feeSol": 0.003,
  "transactionCount": 8,
  "transactions": ["<base64 unsigned tx>", "…"],
  "blockhash": "…",
  "lastValidBlockHeight": 123456789,
  "note": "Sign each transaction with the sender wallet and submit."
}
```

Chunking: max 14 transfer instructions per tx (the 30 bps fee instruction rides in the first chunk and shares the cap).

**Errors:** `400` missing `sender` / invalid recipients · `402` payment required (x402 challenge) · `500` build failure with `details`.

## POST /solana/batch-send-token — $0.01

Same as above for any SPL token. Adds ATA creation for recipients missing a token account (rent ≈ 0.00204 SOL per created ATA, paid by sender).

**Body:** as batch-send-sol plus `"mint": "string (base58 SPL mint)"`. `amount` in human-readable token units.

Chunking: max 7 transfer instructions per tx (ATA creation overhead).

## GET /solana/quote — $0.001

Query params: `recipients` (number, required), `token` (symbol, optional, default SOL).

Returns estimated tx count, network fees (~5,000 lamports/tx), and worst-case ATA rent for token sends.

## GET /solana/status/:txid — $0.001

**Response 200**

```json
{
  "signature": "…",
  "status": "confirmed | finalized | unknown",
  "err": null,
  "slot": 312345678,
  "blockTime": 1783300000,
  "fee": 5000,
  "explorer": "https://explorer.solana.com/tx/…"
}
```

`404` if signature not found.

## Free endpoints

- `GET /health` — service, version, network, x402Network, treasury, timestamp
- `GET /.well-known/x402` — full machine-readable manifest (endpoints, prices, payment details)
- `GET /` — human-readable service summary

## x402 flow (manual)

1. `POST /solana/batch-send-sol` with no `X-PAYMENT` header.
2. Receive `402` with payment requirements: amount (e.g. $0.01 USDC), `payTo` treasury address, CAIP-2 network (`solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp` mainnet, `solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1` devnet).
3. Construct and settle the USDC payment per the x402 `exact` SVM scheme (or let an x402 client library do it).
4. Retry the identical request with the base64 payment proof in `X-PAYMENT`.
5. Gateway verifies via facilitator and returns the result.

Facilitators: devnet `https://x402.org/facilitator` · mainnet `https://facilitator.payai.network`.

## Signing the returned transactions

Each entry in `transactions[]` is a base64-serialized legacy `Transaction` with `feePayer = sender` and a recent blockhash. Deserialize, sign with the sender keypair, submit:

```js
import { Transaction, Connection, Keypair } from '@solana/web3.js';

const conn = new Connection(RPC_URL, 'confirmed');
for (const b64 of res.transactions) {
  const tx = Transaction.from(Buffer.from(b64, 'base64'));
  tx.sign(senderKeypair);                    // local — key never leaves your machine
  const sig = await conn.sendRawTransaction(tx.serialize());
  await conn.confirmTransaction({ signature: sig, blockhash: res.blockhash,
    lastValidBlockHeight: res.lastValidBlockHeight });
}
```

If the blockhash expires before submission, re-call the build endpoint — quotes and builds are cheap by design.

## Related Solana endpoints (main gateway)

Base URL: `https://gateway.spraay.app` — same x402 payment model (USDC on Base or Solana).

| Endpoint | Price | Notes |
|---|---|---|
| `GET /api/v1/solana/jupiter/quote` | $0.005 | params: inputMint, outputMint, amount |
| `POST /api/v1/solana/jupiter/swap-tx` | $0.01 | returns unsigned swap tx — same sign-locally pattern |
| `GET /api/v1/solana/helius/assets-by-owner` | $0.003 | full portfolio via Helius DAS |
| `GET /api/v1/solana/helius/asset` | $0.002 | single asset |
| `GET /api/v1/solana/pyth/price` | $0.005 | single feed |
| `GET /api/v1/solana/pyth/prices` | $0.008 | batch feeds |

Full catalog (192 endpoints): https://docs.spraay.app
