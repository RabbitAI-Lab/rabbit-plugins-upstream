## Description: <br>
AI-powered shopping API guidance for product search, order creation, and USDC checkout on Solana or Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[purch-agent](https://clawhub.ai/user/purch-agent) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to search Amazon and Shopify products, create purchase orders, and complete USDC checkout flows with Solana or Base wallets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask users to pass raw wallet private keys to command-line scripts and can submit irreversible crypto payments. <br>
Mitigation: Prefer browser checkout or a trusted wallet or hardware-wallet flow, avoid command-line private keys, and use a dedicated low-balance wallet for testing. <br>
Risk: A payment may be signed before the user has fully checked merchant, chain, amount, recipient or contract, fees, and product details. <br>
Mitigation: Require explicit human review of merchant, item, amount, chain, recipient or contract, and fee details before signing or submitting any transaction. <br>
Risk: Checkout requests send personal contact and shipping information to api.purch.xyz. <br>
Mitigation: Review the email and shipping data before submission and send only the information needed to complete the purchase. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/purch-agent/skills/agentic-commerce) <br>
- [Purch API Base URL](https://api.purch.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON API examples, shell commands, and Python or TypeScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces product search guidance, order creation examples, transaction signing instructions, and CLI output examples; live checkout results depend on api.purch.xyz, wallet state, network fees, and user-provided order details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
