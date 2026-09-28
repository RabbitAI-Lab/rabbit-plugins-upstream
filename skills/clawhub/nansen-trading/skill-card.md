## Description:

Guides agents through DEX swaps and cross-chain bridges on Solana and Base, Solana limit orders, and Hyperliquid perpetual trading via the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent in obtaining trade quotes, previewing or executing swaps and bridges, managing Solana limit orders, and managing Hyperliquid perpetual positions.

### Deployment Geography for Use:

Global, subject to applicable trading and compliance restrictions.

## Known Risks and Mitigations:

Risk: Agent-run trading commands can broadcast irreversible transactions without a fresh human confirmation.

Mitigation: Require a quote or dry run first, show the exact chain, tokens, amount, recipient, fees, approvals, slippage and quote ID, then obtain fresh explicit approval before any execution or trading mutation.

Risk: Agent access to Nansen credentials and a wallet signing password can expose funds.

Mitigation: Install only if comfortable granting the agent access to those credentials; keep wallet signing authorization separate from account login and require approval before signing.

## Reference(s):

- [Nansen Trading on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-trading)
- [Nansen CLI npm package](https://www.npmjs.com/package/nansen-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes quote and dry-run steps before execution.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
