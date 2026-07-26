## Description: <br>
Accept payments on websites with moneydevkit for checkout, paywall, Next.js, or Replit integrations, including fixed pricing, pay-what-you-want, products, customers, orders, and Bitcoin Lightning payments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satbot-mdk](https://clawhub.ai/user/satbot-mdk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to add hosted checkout, product payments, customer collection, and payment confirmation flows to Next.js or Replit web applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires wallet seed phrase and API credentials that could expose funds or payment account access if mishandled. <br>
Mitigation: Store MDK_MNEMONIC and MDK_ACCESS_TOKEN only in a secrets manager or environment variable system, never in chat, logs, source control, or generated application output. <br>
Risk: Payment-account actions such as rotating keys or changing product, customer, checkout, or order data can affect live commerce workflows. <br>
Mitigation: Use non-production credentials for initial testing and require explicit user confirmation before changing or deleting payment-account data or rotating keys. <br>
Risk: Using this skill requires trusting Moneydevkit as the payment and wallet provider. <br>
Mitigation: Install and use the skill only after reviewing Moneydevkit's service, endpoints, and security posture for the intended application. <br>


## Reference(s): <br>
- [Next.js Integration](references/nextjs.md) <br>
- [Replit Integration](references/replit.md) <br>
- [moneydevkit documentation](https://docs.moneydevkit.com) <br>
- [moneydevkit MCP server](https://mcp.moneydevkit.com) <br>
- [moneydevkit npm organization](https://www.npmjs.com/org/moneydevkit) <br>
- [ClawHub skill page](https://clawhub.ai/satbot-mdk/skills/moneydevkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference required environment variables, external endpoints, and framework-specific setup steps.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
