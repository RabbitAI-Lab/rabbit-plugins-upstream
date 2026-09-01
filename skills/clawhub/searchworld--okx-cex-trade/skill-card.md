## Description:

Enables agents to help users place, cancel, amend, and monitor OKX spot, swap, futures, options, and event contract orders through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate OKX centralized-exchange trading workflows from an agent, including order placement, amendment, cancellation, leverage changes, conditional orders, option workflows, and event contract workflows. It is intended for authenticated OKX CLI use and requires explicit care around live versus demo trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live OKX trading actions involving real funds.

Mitigation: Use demo mode first and require explicit confirmation of live/demo mode, instrument, side, size, order type, price, leverage, cost, and maximum loss before any write action.

Risk: Users may expose OKX credentials during setup or troubleshooting.

Mitigation: Configure credentials only through the OKX CLI and never provide API keys, secrets, passphrases, or OAuth tokens in chat.

Risk: Directional event-contract or market commentary may be mistaken for financial advice.

Mitigation: Treat UP/DOWN and market commentary as unverified information, not financial advice, and require the user to choose and confirm any trade direction.

Risk: Derivative contract sizing, leverage, and margin settings can produce orders different from the user's intent.

Mitigation: Verify contract face value, leverage, margin mode, notional value, cost, and maximum loss before submission, and ask for clarification when amount units are ambiguous.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-trade)
- [Trade workflows and examples](references/workflows.md)
- [MCP tool reference and output conventions](references/templates.md)
- [Spot command reference](references/spot-commands.md)
- [Swap and perpetual command reference](references/swap-commands.md)
- [Futures and delivery command reference](references/futures-commands.md)
- [Options command reference](references/options-commands.md)
- [Event contract commands](references/event-commands.md)
- [Event contract workflows](references/event-workflows.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, Markdown, Text]

**Output Format:** [Markdown text with OKX CLI commands and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include mode labels, order identifiers, tabular command results, and safety confirmations for write actions.]

## Skill Version(s):

1.4.5 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
