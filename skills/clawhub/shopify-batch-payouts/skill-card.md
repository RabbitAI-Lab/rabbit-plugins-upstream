## Description: <br>
Guides agents through validating, estimating, and executing multi-recipient USDC payouts for Shopify and commerce workflows through the Spraay batch payment gateway on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchants, operators, and agents use this skill to prepare bulk USDC payouts for affiliates, creators, suppliers, vendors, referral partners, and other commerce recipients. It focuses on validation, fee estimation, explicit user confirmation, and safe execution guidance for irreversible on-chain payouts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: On-chain USDC payouts are irreversible if wallet addresses, amounts, totals, or fees are wrong. <br>
Mitigation: Validate every batch in-session, surface warnings and duplicate addresses, confirm totals and fees with the user, and require explicit confirmation before execution. <br>
Risk: Handling private keys or seed phrases would create custody and credential exposure risk. <br>
Mitigation: Stop any workflow that asks for private keys or seed phrases; funds should move only after the payer signs from their own wallet. <br>
Risk: Execution uses paid x402 gateway endpoints and can fail if payment handling is not configured. <br>
Mitigation: Use free validation and rough estimation first, then execute only through a configured Spraay x402 path or compatible MCP server after confirmation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/plagtech/skills/shopify-batch-payouts) <br>
- [Spraay Protocol](https://spraay.app) <br>
- [Spraay Docs](https://docs.spraay.app) <br>
- [Batch Payment API 1.0](https://docs.spraay.app/bpa/1.0/) <br>
- [Spraay x402 Payment Metadata](https://gateway.spraay.app/.well-known/x402.json) <br>
- [Spraay Shopify App](https://github.com/plagtech/spraay-shopify) <br>
- [Spraay x402 MCP Server](https://smithery.ai/servers/Plagtech/Spraay-x402-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, API calls, configuration] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include recipient validation summaries, fee estimates, confirmation prompts, and transaction links.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
