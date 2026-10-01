## Description:

Guides agents through OKX CEX spot, swap, futures, options, and event-contract trading workflows, including order placement, cancellation, amendment, leverage changes, position closure, and related safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help an agent operate the OKX trading CLI for authenticated trading and order-management tasks across spot, derivatives, options, and event-contract products. It is intended for workflows where the user remains responsible for trading decisions and confirms write actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated CLI use can execute live financial trades or irreversible account actions.

Mitigation: Prefer demo mode first, verify the active profile before every trade, and require explicit user confirmation before any order, cancellation, amendment, leverage change, or position close.

Risk: Credential handling can expose sensitive OKX authentication material.

Mitigation: Do not accept credentials in chat; guide users to the OKX CLI configuration flow and stop on authentication failures until re-authentication is complete.

Risk: Directional trading recommendations or automatic account-data behavior can influence financial decisions.

Mitigation: Treat recommendations as informational only, present relevant checks and parameters, and leave the final trading decision to the user.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [Spot Command Reference](artifact/references/spot-commands.md)
- [Swap / Perpetual Command Reference](artifact/references/swap-commands.md)
- [Futures / Delivery Command Reference](artifact/references/futures-commands.md)
- [Options Command Reference](artifact/references/options-commands.md)
- [Event Contract Commands](artifact/references/event-commands.md)
- [Trade Workflows and Examples](artifact/references/workflows.md)
- [Event Contract Workflows](artifact/references/event-workflows.md)
- [MCP Tool Reference and Output Conventions](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trading-mode labels, confirmation prompts, and follow-up checks for authenticated OKX CLI actions.]

## Skill Version(s):

1.4.8 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
