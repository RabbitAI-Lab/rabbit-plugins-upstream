## Description: <br>
Give your agent a wallet. Fund with Apple Pay. Pay for paywalled content. x402 native. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parkertoddbrooks](https://clawhub.ai/user/parkertoddbrooks) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent pay for paywalled content, mint short-lived payment links, and optionally use Coinbase CDP or Privy wallets for x402 payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent payment authority and spend money through payment and wallet flows. <br>
Mitigation: Require explicit user approval for each payment, keep wallets lightly funded, and enforce spend limits before enabling higher-value or own-wallet transactions. <br>
Risk: The skill can access a local 1Password-backed worker secret and payment-provider credentials. <br>
Mitigation: Use tightly scoped secrets, store them only in approved secret managers, rotate them if exposed, and avoid sharing service-account tokens with unrelated agents or workflows. <br>
Risk: Cloudflare KV-backed one-time payment links may not provide strict global single-use guarantees across all edge locations. <br>
Mitigation: Review or self-host the worker before production use, keep token lifetimes short, and move strict global single-use enforcement to a stronger coordination primitive when higher-value payments are allowed. <br>
Risk: Dormant or optional Privy and user-wallet routes can expand the payment surface if enabled unintentionally. <br>
Mitigation: Enable only the routes and wallet providers required for the deployment, review configuration before release, and test payment, balance, history, and budget behavior in a low-value environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/parkertoddbrooks/skills/wip-agent-pay) <br>
- [README](artifact/README.md) <br>
- [Specification](artifact/SPEC.md) <br>
- [Setup guide](artifact/SETUP.md) <br>
- [Worker reference](artifact/REFERENCE.md) <br>
- [x402 protocol](https://www.x402.org/) <br>
- [Coinbase Developer Platform](https://portal.cdp.coinbase.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON tool-call examples, and JavaScript integration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install and configure a Node.js CLI, MCP server, OpenClaw plugin, Cloudflare Worker, Stripe funding flow, and Coinbase CDP or Privy wallet providers.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata, SKILL.md frontmatter, package.json, CHANGELOG released 2026-07-21) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
