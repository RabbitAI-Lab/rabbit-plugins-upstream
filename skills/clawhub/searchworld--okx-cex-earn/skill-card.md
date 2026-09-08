## Description:

Guides agents through OKX Earn workflows for Simple Earn, Fixed Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn using the okx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External OKX users and agents use this skill to inspect Earn balances and products, prepare subscriptions or redemptions, manage lending rates and AutoEarn settings, and monitor earn positions against a live OKX account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate subscriptions, redemptions, lending-rate changes, transfers, and other actions against live OKX funds.

Mitigation: Require a fresh explicit yes/no confirmation before every write action, show the amount, currency, product, rate or term, and verify the result after execution.

Risk: Credential and profile checks may expose sensitive account configuration details if handled carelessly.

Mitigation: Never accept credentials in chat, guide users through okx config init, prefer least-privilege API keys, and confirm auth/status commands do not print secrets before sharing output.

Risk: Recurring monitors or transfer workflows can create broad financial exposure, especially when withdrawal permissions are enabled.

Mitigation: Avoid withdrawal permission unless a specific transfer workflow requires it, and set explicit duration, frequency, and stop conditions for any periodic monitoring.

Risk: Some products include lockups or timing limits, such as fixed-term lock periods and AutoEarn's 24-hour disable restriction.

Mitigation: Preview fixed-term orders before execution, state lockup and early-redemption limits clearly, and warn about the 24-hour AutoEarn restriction before enabling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-earn)
- [OKX homepage](https://www.okx.com)
- [Simple Earn command reference](references/savings-commands.md)
- [Dual Investment command reference](references/dcd-commands.md)
- [On-chain Earn command reference](references/onchain-commands.md)
- [AutoEarn command reference](references/autoearn-commands.md)
- [Flash Earn command reference](references/flash-earn-commands.md)
- [Multi-step workflows](references/workflows.md)
- [Templates and formatting reference](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON command output where the skill requires structured results; no additional post-processing constraints are specified.]

## Skill Version(s):

1.4.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
