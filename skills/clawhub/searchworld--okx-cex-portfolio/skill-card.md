## Description:

Helps agents inspect OKX account balances, positions, P&L, bills, fees, configuration, and withdrawal limits, and execute explicitly confirmed account transfers or position-mode changes through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review OKX portfolio state, account history, fees, and position information, with support for explicitly confirmed transfers and position-mode changes. It requires OKX credentials and is intended for account-management workflows rather than market data, order placement, or bot management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses OKX account data and can perform limited write actions on account state.

Mitigation: Install only when this access is intended, use demo mode first when possible, and confirm live versus demo mode before each action.

Risk: Credentials or command output could expose sensitive account information if shared in chat.

Mitigation: Configure credentials through the OKX CLI flow and avoid entering API keys or secret-bearing command output into chat.

Risk: Transfers and position-mode changes can affect real account funds or trading configuration.

Mitigation: Require explicit confirmation before write commands and verify balances or account configuration after the command completes.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-portfolio)
- [Publisher profile](https://clawhub.ai/user/searchworld)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should state whether live or demo mode was used; CLI commands may return OKX account data and JSON when requested.]

## Skill Version(s):

1.4.4 (source: server release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
