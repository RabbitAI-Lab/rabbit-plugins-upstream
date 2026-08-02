## Description: <br>
Purchase physical products through SP3ND with USDC on Solana by registering an agent, creating server-priced carts, placing idempotent orders, handling manual-review and shipping-quote lifecycles, paying payment-ready orders through x402, and tracking fulfillment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kent-x1](https://clawhub.ai/user/kent-x1) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an agent to SP3ND for approved physical-goods purchases, USDC payment, quote handling, shipping selection, and fulfillment tracking. It is intended for workflows where the agent follows server-priced order and payment gates rather than trusting caller-supplied prices or payment details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can support real purchases and USDC payments when connected to SP3ND credentials and a funded wallet. <br>
Mitigation: Use a dedicated low-balance wallet, set spending and approval limits, and confirm recipient, shipping, and order details before creating or paying an order. <br>
Risk: SP3ND API credentials, wallet files, and shipping details are sensitive. <br>
Mitigation: Keep API keys, API secrets, wallet key material, and private shipping information out of logs, commits, and unrelated agent context. <br>
Risk: Stale quotes, manual-review states, or uncertain payment settlement can cause incorrect or duplicate payment attempts. <br>
Mitigation: Use stable idempotency keys, pay only when SP3ND reports payment readiness, honor quote expiration and shipping selection, and read the order before retrying after an uncertain response. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kent-x1/skills/sp3nd) <br>
- [SP3ND API Documentation](https://sp3nd.shop/partner-api/docs) <br>
- [SP3ND Agent Card](https://sp3nd.shop/.well-known/agent-card.json) <br>
- [Published SP3ND Skill](https://sp3nd.shop/skill.md) <br>
- [SP3ND Partner Dashboard](https://sp3nd.shop/partner-api/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with HTTP, JSON, JavaScript, shell, and text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SP3ND API credentials and may use a Solana wallet file for USDC payment.] <br>

## Skill Version(s): <br>
1.8.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
