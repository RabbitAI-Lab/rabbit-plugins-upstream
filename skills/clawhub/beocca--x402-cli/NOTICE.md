================================================================================
NOTICE
Copyright (c) beocca 2026
================================================================================

## x402-cli: HTTP 402 Payment Service Discovery and Execution

This software enables AI agents to discover and pay HTTP 402 / x402-enabled services using blockchain transactions on Base mainnet (USDC). Payment execution is autonomous and final.

## CRITICAL RISK NOTICE

**Blockchain transactions are irreversible. Loss of funds is possible and may be permanent.**

This software may cause an autonomous or semi-autonomous agent to:
- Initiate, sign, and submit blockchain transactions
- Transfer cryptocurrency to third-party addresses
- Interact with unaudited or malicious endpoints
- Spend funds based on agent misunderstanding or misdirection

Blockchain transactions cannot be reversed once submitted. Agents can:
- Misinterpret user instructions
- Select the wrong service or network
- Send funds to incorrect or unrecoverable addresses
- Overpay for a service
- Interact with defective, unavailable, or malicious endpoints

**Users are solely responsible for implementing appropriate safeguards outside this software**, including but not limited to:
- Wallet-level spend limits and policies
- Service allowlists and address allowlists
- Network restrictions and RPC provider selection
- Transaction previews and human approval workflows
- Comprehensive monitoring and incident-response procedures

This software cannot guarantee that any agent orchestrator, wallet provider, RPC endpoint, payment facilitator, service discovery provider, or third-party API will enforce these safeguards.

## THIRD-PARTY HOSTED SERVICES

Operation of this software may require or use third-party hosted services, including:
- Payment facilitators and x402 discovery catalogs
- Blockchain RPC providers (Base mainnet)
- Wallet providers and key management services
- QR code generation services
- Any x402-enabled API endpoint your agent selects

These services are **not provided, endorsed, audited, or vetted by the authors of this software**. Each is subject to its own:
- Terms of service and acceptable-use policies
- Fees and pricing structures
- Availability limits and rate limits
- Geographic restrictions and sanctions compliance
- Privacy policies and data handling practices
- Disclaimers and dispute-resolution provisions

Use of this software does not imply endorsement, approval, security audit, or fitness assessment of any third-party service.

## NO ENDORSEMENT OF THIRD-PARTY APIS

This software is generic and may allow agents to pay any service supporting the x402 standard. The authors:
- Do **not** endorse any service, API, or catalog listing
- Do **not** monitor or audit paid services
- Do **not** guarantee the legality, accuracy, or security of any service
- Provide **no** vetting or suitability analysis

Users are solely responsible for reviewing and assessing the terms, legality, accuracy, security, and suitability of any service their agent pays for.

## QR CODE GENERATION SERVICE

This software may generate QR codes for public deposit addresses or payment URIs using the third-party QR Code API at `api.qrserver.com` operated by Foundata GmbH.

When QR codes are generated, encoded data (such as wallet addresses and payment URIs) is transmitted to the third-party service. **Do not encode private keys, seed phrases, authentication secrets, or other sensitive information in QR codes.** QR codes should be used only for public addresses and non-sensitive funding instructions.

The authors of this software:
- Do not operate or control the QR code service
- Do not guarantee availability, correctness, scannability, privacy, or security
- Do not guarantee that encoded data is kept confidential

Users should verify the displayed address, network, token, and amount before sending funds.

## LICENSE AND THIRD-PARTY DEPENDENCIES

x402-cli source code is licensed under the MIT-0 License. Third-party dependencies remain subject to their own license terms (see LICENSE-THIRD-PARTY.txt if present).

Certain optional or transitive wallet-provider dependencies may include WalletConnect / Reown software, which is subject to the WalletConnect Community License Agreement and is not licensed under the primary license for this software.

## INDEPENDENT PROJECT NOTICE

x402-cli is an independent agent skill for interacting with x402-compatible HTTP 402 payment services. It is **not**:
- Affiliated with Coinbase, Inc.
- Affiliated with the Linux Foundation or LF Projects
- Endorsed by, sponsored by, or part of the x402 project
- Endorsed by, sponsored by, or affiliated with any x402 Foundation entity

## NO LEGAL, FINANCIAL, OR COMPLIANCE ADVICE

This software is provided as-is and without:
- Legal, financial, tax, or investment advice
- Sanctions, AML, or anti-money-laundering guidance
- Money-transmission or financial-services advice
- Securities or commodities trading guidance
- Data protection, privacy, or GDPR compliance advice
- Consumer-protection or dispute-resolution guidance

Users and integrators are solely responsible for determining whether their use, distribution, integration, and operation of this software complies with applicable law in their jurisdiction.

## NO WARRANTY AND LIMITATION OF LIABILITY

The authors, contributors, and maintainers of this software are **not liable** for any direct, indirect, incidental, special, exemplary, or consequential damages, including:
- Loss of cryptocurrency or other assets
- Loss of profits or revenue
- Disruption of business operations
- Data loss or corruption
- Unauthorized access or theft
- Service unavailability or poor performance

This limitation applies even if the authors have been advised of the possibility of such damages.
