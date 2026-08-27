# x402-cli Disclosures

## 1. Real Money Transactions

This CLI enables autonomous spending of real cryptocurrency (USDC on Base mainnet). When you invoke `request pay`, funds are moved irreversibly. This is not a simulation or test environment—transactions are final and cannot be reversed.

## 2. No Confirmation Gate in the CLI

The CLI itself provides no confirmation prompt or approval workflow before sending payment. A warning is printed to stderr before payment, but this does not block execution. If you require human approval, implement that gate in your agent orchestration layer *before* calling the CLI.

## 3. Irreversible Blockchain Transactions

Blockchain transactions are final and immutable. Funds sent to a wrong address, at an incorrect amount, on the wrong network, or to a malicious service cannot be recovered. The CLI does not validate the recipient, confirm the network, or audit the service before payment.

## 4. Third-Party Service Risks

The CLI discovers and pays third-party APIs that you or your agent selects. These services are not authored, endorsed, audited, or vetted by the authors of this software. Each is subject to its own terms, fees, availability, acceptable-use policies, legal restrictions, and compliance requirements. You are solely responsible for determining whether any service is lawful, accurate, secure, and suitable for your use case.

## 5. Agent Misunderstanding and Misdirection

Autonomous or semi-autonomous agents may misinterpret user instructions, select the wrong service, use the wrong network, send funds to an incorrect address, overpay, or interact with a malicious or defective endpoint. No safeguard in this CLI prevents these errors—they are prevented only by your external controls.

## 6. Wallet and Key Management

The CLI requires a private key via the `CLIENT_EVM_WALLET_SECRET` environment variable. This key is never stored by the CLI but is live in memory during execution. Exposure of the environment variable leaks full wallet control. Never:
- Hardcode keys in scripts or config files
- Pass keys as command-line arguments (they appear in shell history and process listings)
- Use a personal or high-value wallet
- Use the same key across multiple agents or untrusted contexts

Always use a fresh, dedicated wallet with minimal, intentional funding.

## 7. Wallet Funding as Security Boundary

This CLI has a configurable per-invocation spend limit, but it does not implement allowlists. The wallet's on-chain balance *is* your ultimate security boundary. If the wallet holds 10 USDC, the agent can spend at most 10 USDC before subsequent transactions fail. If it holds 100 USDC and you made an error, 100 USDC is at risk.

- Minimal use: 5–10 USDC
- Higher-volume use: up to 50–100 USDC (only if you trust the agent's orchestration)
- High-value wallets: never use this CLI with them

## 8. External Safeguards Required

You are responsible for implementing wallet-level policies, spend limits, service allowlists, address allowlists, network restrictions, transaction previews, approvals, monitoring, incident-response procedures, and any other external controls appropriate for your use case. The CLI provides none of these.

## 9. Discovery Service Limitations

The `discover list` and `discover search` commands return a catalog of x402-enabled services. This catalog is not vetted or endorsed by the authors of this software. A service appearing in the catalog does not mean it is safe, legitimate, or suitable for your use. Apply the same due diligence as you would for any third-party API.

## 10. No Affiliation or Endorsement

x402-cli is an independent agent skill. It is not affiliated with, endorsed by, or sponsored by Coinbase, the Linux Foundation, the x402 project, or any x402 Foundation entity. The presence of this CLI or its documentation does not imply endorsement of x402, any x402 service, or any third-party integration.

## 11. No Legal or Compliance Advice

This software is provided as-is and without legal, financial, tax, AML, sanctions, money-transmission, securities, or compliance advice. You are solely responsible for determining whether your use of this software complies with applicable law in your jurisdiction.

