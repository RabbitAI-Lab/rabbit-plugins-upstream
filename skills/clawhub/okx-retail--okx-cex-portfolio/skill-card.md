## Description:

Helps users review OKX balances, positions, profit and loss, account history, fees, and limits, and guides confirmed transfers or position-mode changes; requires API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External OKX users can use the skill to check balances across account types, review open and closed positions, account activity, fees, account settings, and available limits. It can guide transfers and position-mode changes after the user confirms the account and action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A command could use the wrong live or demo account.

Mitigation: Start in demo mode for account-information tasks, confirm the selected account and mode, and state which mode was used.

Risk: Transfers or account-setting changes can affect funds or position behavior.

Mitigation: Before a write command, confirm the account, mode, amount, and destination; check positions before changing position mode.

Risk: Credentials and returned account details are sensitive.

Mitigation: Do not accept credentials in chat; use read-only credentials for information-only access and configure credentials through the CLI.

Risk: Live use may rely on missing preflight guidance or an unexpected CLI version.

Mitigation: Obtain the shared preflight instructions and verify the installed CLI version before live use.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-portfolio)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands]

**Output Format:** [Markdown with account summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account balances, positions, transaction history, and other sensitive financial information.]

## Skill Version(s):

1.5.0 (source: evidence.json release version, artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
