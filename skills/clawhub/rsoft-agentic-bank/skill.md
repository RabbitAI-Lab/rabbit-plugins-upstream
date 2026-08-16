---
name: rsoft-agentic-bank
description: AI-native lending on Base MAINNET for autonomous agents. Check credit, request USDC loans (EIP-712 signed), and repay autonomously. Real money.
version: 2.0.0
requires:
  bins:
    - curl
  skills:
    - payment
metadata:
  openclaw:
    homepage: https://rsoft-agentic-bank.com/
---

# RSoft Agentic Bank

Official skill for **RSoft Agentic Bank** — an AI-native lending service for autonomous agents on **Base mainnet** (Coinbase L2).

Agents can check their creditworthiness, request USDC loans, receive funds on-chain, and repay autonomously. Every repaid loan earns a bank-signed, portable **ERC-8004 reputation mark** — verifiable on-chain credit history.

> ⚠️ **REAL MONEY.** This bank operates on Base MAINNET with real USDC. Defaults are recorded on-chain against your agent's reputation. Borrow only what your agent can repay.

## Prerequisites

- **Payment skill** installed and configured for **Base mainnet** with a funded wallet (a few cents of ETH for gas; USDC arrives when the loan disburses).
- If the payment skill is not installed:
```bash
npx clawhub install payment
```
- Configure for Base mainnet:
```bash
~/.openclaw/skills/payment/scripts/payment-config set network.name "base" network.chain_id 8453 network.rpc_url "https://mainnet.base.org" payment.default_token "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913" payment.default_token_symbol "USDC" payment.default_token_decimals 6
```
- If you don't have a wallet yet:
```bash
~/.openclaw/skills/payment/scripts/create-wallet
```

## Setup: Know Your Wallet Address

```bash
~/.openclaw/skills/payment/scripts/get-address
```
Use the `address` field as your `agent_id` in all bank commands.

## Base URLs

```
Reads & repay (free, no key):  https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws
Loan origination (API key):    https://rsoft-agentic-bank.com/api/v1
```

## Available Commands

### 1. Check Interest Rates (free)

```bash
curl -s https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws/api/interest-rates
```

### 2. Check Credit Score (free)

Replace `{agent_id}` with your wallet address:
```bash
curl -s https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws/api/creditworthiness/{agent_id}
```

### 3. Request a Loan (API key + your signature)

Two things are required — both are security features, not red tape:

1. **A pilot API key.** Message [@RSoft-Agentic-Bank on Moltbook](https://www.moltbook.com/u/RSoft-Agentic-Bank) to get one. Export it as `BANK_API_KEY`.
2. **Your wallet's EIP-712 signature.** The bank only originates loans signed by the borrowing wallet itself — nobody (including this skill) can borrow in your name.

**Step 3a — sign the loan terms** with the same private key your payment skill uses (`PRIVATE_KEY` env var):
```bash
# npm install ethers  (once)
node -e '
const { Wallet } = require("ethers");
const w = new Wallet(process.env.PRIVATE_KEY);
const domain = { name: "RSoft Agentic Bank", version: "1", chainId: 8453,
                 verifyingContract: "0x8004A169FB4a3325136EB29fA0ceB6D2e539a432" };
const types = { LoanRequest: [
  { name: "agentWallet",     type: "address" },
  { name: "loanAmountUsdc6", type: "uint256" },
  { name: "nonce",           type: "string"  },
  { name: "deadline",        type: "uint256" } ] };
const amount = 5.0;                                   // USDC, min 5
const nonce = "oc-" + Date.now();
const deadline = Math.floor(Date.now() / 1000) + 900; // 15 min
const message = { agentWallet: w.address,
                  loanAmountUsdc6: Math.round(amount * 1e6), nonce, deadline };
w.signTypedData(domain, types, message).then(sig => console.log(JSON.stringify(
  { agent_wallet: w.address, loan_amount: amount, nonce, deadline, signature: sig })));'
```

**Step 3b — submit the signed request** (use the JSON printed above as the body):
```bash
curl -s -X POST -H "Content-Type: application/json" -H "X-API-Key: $BANK_API_KEY" \
  -d '{"agent_wallet": "<your 0x…>", "loan_amount": 5, "nonce": "<nonce>", "deadline": <deadline>, "signature": "0x…"}' \
  https://rsoft-agentic-bank.com/api/v1/loan/request
```
Save the `request_id`. The bank's 5-agent pipeline evaluates risk and, if approved, sends real USDC to your wallet on Base within seconds.

**Step 3c — track it** (free, no key):
```bash
curl -s https://rsoft-agentic-bank.com/api/v1/loan/status/{request_id}
```

### 4. Verify the Loan Arrived

Check your wallet on [BaseScan](https://basescan.org/) (search your address) or with your payment skill's balance command.

### 5. Repay a Loan (3 steps — do all 3 in order)

**Step 1: Check how much you owe**
```bash
curl -s https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws/api/repay-info/{agent_id}
```
Save the `request_id`, `repayment_amount`, and `pay_to` from the response.

**Step 2: Send USDC payment on-chain — the EXACT amount**
```bash
~/.openclaw/skills/payment/scripts/pay --to <pay_to> --amount <repayment_amount>
```
Pay **exactly** `repayment_amount` — not more, not less. Save the transaction hash from the output.

**Step 3: Confirm repayment with the bank**

WARNING: The URL is `/api/repay` — do NOT change it to any other URL.
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"request_id": "<request_id>", "tx_hash": "<tx_hash>"}' https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws/api/repay
```
Safety net: if your agent dies after Step 2, the bank auto-detects exact treasury payments within ~10 minutes. An agent that paid is never marked in default.

## Full Workflow Example

```
1. Get your wallet address         → get-address
2. Check interest rates            → curl /api/interest-rates
3. Check your credit score         → curl /api/creditworthiness/{wallet}
4. Sign the loan terms             → node signing snippet (step 3a)
5. Request the loan                → curl POST /api/v1/loan/request (with key + signature)
6. Verify USDC received            → BaseScan / balance
7. Check repayment info            → curl /api/repay-info/{wallet}
8. Send EXACT USDC to bank         → pay --to {pay_to} --amount {repayment_amount}
9. Confirm repayment               → curl POST /api/repay
```

## Important Notes

- **Network:** Base MAINNET — real USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`), real consequences.
- **Loan size:** 5 USDC minimum. Your ceiling starts at the $5 floor and climbs the credit ladder with each repaid loan ($5 → $10 → $25 → …).
- **One active loan at a time.** Repay before requesting a new one. An unpaid default blocks new loans until you cure it (repay in full via the same repay flow).
- **Gas:** your wallet needs a small amount of ETH on Base for transaction fees.
- All transactions are verifiable on [BaseScan](https://basescan.org/).

## MCP Server (recommended for MCP-capable agents)

If your agent speaks MCP, skip the curls — the same bank is one config line away, no API key needed:
```
https://7mavs5vu7ggbhtxvbavdgs26qa0cbawg.lambda-url.us-east-1.on.aws/mcp
```
Tools: `get_creditworthiness`, `request_loan` (carries your EIP-712 signature), `get_repayment_info`, `confirm_repayment`. Full docs: [rsoft-agentic-bank.com/docs](https://rsoft-agentic-bank.com/docs).

## Verification

- **Official Website:** [rsoft-agentic-bank.com](https://rsoft-agentic-bank.com/)
- **Publisher:** RSoft Latam
- **Protocol:** REST API via curl + payment skill for on-chain transfers; MCP server for tool-native agents
- **Network:** Base mainnet (Coinbase L2)

---
*Developed by RSoft Latam — Empowering the Agentic Economy.*
