---
name: yield-farm-securepay
version: 2.1.2
author: altoninelli
description: "Zero-cost payment automation on Base (Chain ID 8453) with 100% principal recovery via USDC yield farming (Aave V3 & Morpho). Machine-to-Machine (M2M) API and tool for AI agents and smart accounts. Built-in 0.5% developer fee fully reimbursed by yield."
tags: ["DeFi", "Payments", "Base", "USDC", "Aave", "Morpho", "Yield-Farming", "AI-Agents", "M2M", "EIP-5792", "Zero-Cost"]
price_per_call: "0.5% on-chain fee (min 0.1 USDC, max 50 USDC)"
metadata:
  openclaw:
    emoji: "🌾"
    category: "DeFi Payments"
    reputation_required: "low"
    security_level: "non-custodial"
    network: "Base Mainnet (Chain ID: 8453)"
    token: "USDC (0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913)"
    pricing:
      type: "on-chain-fee"
      rate: "0.5%"
      minimum: "0.1 USDC"
      maximum: "50.0 USDC"
      developer_wallet: "0x785cf69ced4e20a7e975a3391d51321b1528fdfe"
      capital_recovery: "100% of payment and developer fee recovered via collateral yield"
    permissions:
      network:
        - "https://selfpaid.cryptofolio.it"
        - "https://mainnet.base.org"
      wallet: "Non-custodial: generates unsigned EVM calldata and EIP-5792 batch calls. Local pre-signing validation layer required. User/Agent executes and signs in their own wallet. No private keys are ever requested or stored."
---

# 🌾 SelfPaid (YieldFarmSecurepay) Skill v2.1

> **Autonomous Zero-Net-Cost Payments on Base Mainnet**  
> Send USDC to any recipient while recovering **100% of the principal + developer fee** automatically through on-chain collateral yield (Aave V3 & Morpho).

Designed for **autonomous AI agents**, **smart accounts (ERC-4337 / EIP-5792)**, and automated workflows.

---

## 🛡️ Security & Pre-Signing Validation Layer (OpenClaw T09 Compliance)

### 1. Non-Custodial Guarantee
* **No Private Keys**: This skill **never** asks for, stores, or handles private keys, mnemonic phrases, or credentials.
* **Client-Side Signing**: The hosted engine constructs **unsigned raw EVM transaction calldata**. All cryptographic signing is performed locally by the calling agent or user's wallet.

### 2. Mandatory Pre-Signing Validation Protocol
To eliminate risks of unvalidated remote calldata forwarding (OpenClaw Rule T09), any agent or client using this skill **MUST decode and validate the payload locally before invoking the wallet signer**. The included `validate.js` module performs these automated checks:

1. **Chain ID Enforcement**: Verify `chainId === 8453` (Base Mainnet). Reject any mismatch.
2. **Contract Address Allowlist**:
   - Calls 1, 2, and 3 target address MUST be the verified Base USDC token contract: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.
   - Call 4 target address MUST be the verified Aave V3 Pool (`0xA238Dd80C259a72e81d7e4664a9801593F98d1c5`) or Morpho Vault.
3. **Function Selector Allowlist**:
   - Calls 1 & 2 MUST use standard ERC20 `transfer(address,uint256)` selector (`0xa9059cbb`).
   - Call 3 MUST use standard ERC20 `approve(address,uint256)` selector (`0x095ea7b3`).
   - Call 4 MUST use Aave `supply(address,uint256,address,uint16)` selector (`0x617ba037`) or Morpho `deposit(uint256,address)` selector (`0x6e553f65`).
   - All arbitrary or unexpected selectors are strictly rejected.
4. **Strict Call Order & Count**: Enforce exactly 4 calls in documented order: `DEVELOPER_FEE` → `PAYMENT` → `APPROVE_POOL` → `SUPPLY_YIELD`. Reject duplicated or injected calls.
5. **Zero Native-Token Value**: Every call MUST have `value === "0x0"`. Reject any call attempting native ETH transfers.
6. **Recipient & Payer Integrity**: Verify decoded Step 2 recipient and payer addresses exactly match user-approved values.
7. **Developer Fee Integrity**: Recalculate the fee locally: $0.5\%$ of payment, clamped between $0.1\text{ USDC}$ and $50.0\text{ USDC}$. Verify Step 1 sends exactly this amount to `0x785cf69ced4e20a7e975a3391d51321b1528fdfe`.
8. **No Unlimited Approvals**: Step 3 approval amount MUST match the exact required collateral deposit. Infinite (`uint256.max`) approvals are rejected.
9. **Yield Beneficiary Integrity**: Call 4 calldata is strictly decoded to enforce that the collateral position is credited to the sender (`onBehalfOf === sender` for Aave, `receiver === sender` for Morpho), preventing remote position redirection.
10. **Decoded Confirmation**: Display a human/agent-readable summary of all decoded parameters before forwarding to the signer.

### 3. Developer Fee & Transparency
* **Developer Wallet**: `0x785cf69ced4e20a7e975a3391d51321b1528fdfe`
* **Rate**: 0.5% (min 0.1 USDC, max 50 USDC) in Step 1 (`DEVELOPER_FEE`).
* **Zero Net Cost to Payer**: The developer fee is included in the collateral yield calculation. Accrued yield from Aave V3 / Morpho reimburses **both** the recipient payment and the developer fee back to the payer over time.

---

## ⚡ How It Works (Machine-to-Machine)

When an agent needs to pay a recipient (e.g. paying for an API, human service, or agent-to-agent task):

1. **Discovery / Yield Optimization**: Query `GET /api/v1/payment/rates` to see real-time APYs across Aave V3 and Morpho on Base.
2. **Build Payment Batch**: Send a single `POST` request to `https://selfpaid.cryptofolio.it/api/v1/payment/build` with payment parameters.
3. **Receive 4 Sequential Transactions**:
   - **Step 1 (`DEVELOPER_FEE`)**: Transfer 0.5% fee to developer wallet (`0x785c...fdfe`).
   - **Step 2 (`PAYMENT`)**: Transfer payment amount to recipient wallet.
   - **Step 3 (`APPROVE_POOL`)**: Authorize USDC collateral deposit to the selected yield protocol.
   - **Step 4 (`SUPPLY_YIELD`)**: Deposit collateral into Aave V3 / Morpho on behalf of the payer (`sender`).
4. **Local Verification**: The client/agent runs `validatePaymentBatch(response, { amount, recipient, sender })` using `validate.js` to decode and enforce all allowlists.
5. **Execution & Signing**:
   - **Standard Wallets**: Sign and execute the 4 verified transactions in sequence.
   - **Smart Accounts / EIP-5792**: Execute the 4 calls in a single atomic 1-click batch via `batchCalls`.
6. **100% Capital Recovery**: The deposited collateral generates yield until 100% of the funds spent (payment + developer fee) have been accrued and recovered.

---

## 🤖 AI Agent Integration Guide

No API key, registration, or local setup is required. The API is completely public and frictionless for agents.

### Endpoint 1: Live Yield Oracle
Get current APYs and see which protocol is currently offering higher yields:

```bash
curl -s https://selfpaid.cryptofolio.it/api/v1/payment/rates
```

**Response:**
```json
{
  "aave": 0.0422,
  "morpho": 0.0389,
  "best": "aave",
  "bestApy": 0.0422,
  "lastUpdated": "2026-10-09T08:27:49.700Z"
}
```

---

### Endpoint 2: Calculate Quote
Check collateral requirements and estimated recovery time:

```bash
curl -s "https://selfpaid.cryptofolio.it/api/v1/payment/quote?amount=25"
```

**Response:**
```json
{
  "amountToPay": "25",
  "collateralTotal": "540",
  "feeAmount": "0.125",
  "yieldDepositAmount": "515",
  "totalRequiredAmount": "540.125",
  "selectedProtocol": "aave",
  "estimatedAPY": 0.0422,
  "estimatedRecoveryDays": 426
}
```

---

### Endpoint 3: Build Payment Transactions (M2M)
Generate ready-to-sign EVM transaction calldata:

```bash
curl -s -X POST https://selfpaid.cryptofolio.it/api/v1/payment/build \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 25,
    "recipient": "0x2222222222222222222222222222222222222222",
    "sender": "0x1111111111111111111111111111111111111111",
    "protocol": "auto"
  }'
```

#### Request Parameters
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Number | **Yes** | Amount of USDC to pay to the recipient (e.g. `25`). |
| `recipient` | String | **Yes** | EVM address receiving the payment (`0x...`). |
| `sender` | String | **Yes** | EVM address of payer / agent executing transactions (`0x...`). |
| `protocol` | String | No | `'auto'` (default, picks best APY), `'aave'`, or `'morpho'`. |
| `collateral` | Number | No | Collateral multiplier (default `20` = 20x). |
| `buffer` | Number | No | Safety buffer percentage (default `8` = 8%). |

#### Output Structure
The endpoint returns:
* **`summary`**: Full financial summary (fees, deposits, estimated days to 100% recovery).
* **`transactions`**: Array of 4 EVM transaction objects `{ step, name, description, to, data, value }`.
* **`batchCalls`**: Array of calls formatted for **EIP-5792** (`wallet_sendCalls`) for atomic 1-click execution.
* **Security Validation**: Always validate the payload through `validate.js` before signing.

---

## 🧮 Mathematical Model & Recovery Economics

### Capital Recovery Formula
* **Collateral Total**: $\text{amount} \times \text{multiplier} \times (1 + \text{buffer})$
* **Developer Fee**: $\text{clamp}(\text{amount} \times 0.5\%, 0.1\text{ USDC}, 50\text{ USDC})$
* **Yield Deposit**: $\text{Collateral Total} - \text{amount}$
* **Annual Accrued Yield**: $\text{Yield Deposit} \times \text{APY}$
* **Recovery Days**: $\frac{\text{amount} + \text{Developer Fee}}{\text{Daily Yield}}$

### Comparison: Collateral Multiplier vs Recovery Time (at ~4.2% APY)
| Multiplier | Collateral Total | Yield Deposit | Est. Recovery Time |
| :--- | :--- | :--- | :--- |
| **5×** | 5.40 USDC / unit | 4.40 USDC | ~5.3 years |
| **10×** | 10.80 USDC / unit | 9.80 USDC | ~2.4 years |
| **20× (Recommended)** | 21.60 USDC / unit | 20.60 USDC | **~1.1 years** |

*Higher collateral multiplier generates faster daily yield, recovering the spent principal sooner.*

---

## 📦 OpenClaw Agent Usage

An OpenClaw agent invokes this skill using a safe, validated execution pipeline:

```markdown
User: "Pay 10 USDC to 0xAlice... with full capital recovery."
Agent:
1. Queries GET https://selfpaid.cryptofolio.it/api/v1/payment/quote?amount=10
2. Confirms recovery timeline (~426 days at 4.2% APY, 0.1 USDC developer fee).
3. Calls POST https://selfpaid.cryptofolio.it/api/v1/payment/build with recipient and sender wallet.
4. Executes Local Validation via validate.js:
   - Verifies Chain ID is 8453 (Base Mainnet)
   - Verifies target contracts are allowlisted (USDC and Aave V3)
   - Verifies zero native ETH value across all calls
   - Verifies recipient is 0xAlice and fee is 0.1 USDC to developer
   - Verifies approval is bounded strictly to the collateral deposit
5. Presents verified transaction summary to user/policy:
   "Payment of 10 USDC verified. Collateral deposit: 206 USDC into Aave V3. Est. recovery: 426 days."
6. Passes verified batchCalls to local Web3 signer for execution.
```

---

## 📄 License & Attribution

* **Author**: `@altoninelli`
* **License**: MIT
* **Security**: Compliant with OpenClaw T09 safe transaction construction standard. Non-custodial, zero credentials requested.
