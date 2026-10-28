## Description:

Manages OKX Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn workflows through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to inspect OKX Earn balances and products, compare rates and APRs, and carry out authenticated OKX Earn workflows. It supports Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn actions, including fund-moving operations that require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate against live OKX Earn funds and does not use demo mode.

Mitigation: Use least-privilege OKX credentials, review every confirmation summary before fund-moving commands, and verify account state after writes.

Risk: Some workflows may need Withdraw permission for transfers between OKX accounts.

Mitigation: Avoid granting Withdraw permission unless transfers are intended; if permission is absent, complete transfers manually in the OKX app.

Risk: Recurring monitors can keep checking financial opportunities and sending ongoing notifications.

Mitigation: Enable recurring /loop workflows only when explicitly desired and review the monitor scope, currency, and cadence.

Risk: On-chain Earn products may expose assets to third-party protocol and smart-contract risks.

Mitigation: Show the protocol, lock period, reward details, settlement timing, and required risk disclaimer before confirmation.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/numpy0001/skills/okx-cex-earn)
- [Simple Earn command reference](references/savings-commands.md)
- [Dual Investment command reference](references/dcd-commands.md)
- [On-chain Earn command reference](references/onchain-commands.md)
- [AutoEarn command reference](references/autoearn-commands.md)
- [Flash Earn command reference](references/flash-earn-commands.md)
- [Multi-step workflows](references/workflows.md)
- [Output templates and formatting](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON command output for agent-side parsing and presents user-facing summaries instead of raw terminal output.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
