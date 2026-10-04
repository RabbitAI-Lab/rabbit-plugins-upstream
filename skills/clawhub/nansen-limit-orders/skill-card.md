## Description:

Guides price-triggered Solana limit orders and best-effort settlement alerts for orders placed on other chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to manage real Solana limit orders or set up settlement alerts for orders placed on other chains.

### Deployment Geography for Use:

Global, subject to applicable service eligibility, sanctions and geographic checks.

## Known Risks and Mitigations:

Risk: Credentialed CLI access can place, change or cancel real trades.

Mitigation: Trust the CLI before installing and confirm the wallet, tokens, amount, trigger price, slippage and expiry before running commands.

Risk: A transfer alert can miss a fill or match an unrelated transfer; it does not track order state.

Mitigation: Filter alerts by wallet, chain, token and side, review the destination and verify fills with the trading venue or order history.

Risk: An invalid or anonymous authentication state may lead to unauthorized or unintended requests.

Mitigation: Check the selected credentials and stop on authentication failure; do not fall back to anonymous payment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-limit-orders)
- [Nansen CLI package](https://www.npmjs.com/package/nansen-cli)
- [Nansen CLI documentation](https://github.com/nansen-ai/nansen-cli)
- [Browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Order details and alert destinations require user review before execution.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
