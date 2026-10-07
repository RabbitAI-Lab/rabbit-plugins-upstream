## Description:

Helps agents use a user-deployed MetaTrader 5 bridge to inspect account and market data, run analysis and backtests, and manage trades with explicit confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who already operate mt5-httpapi use this skill to query their MetaTrader 5 account, market data, and backtests, and to request individually confirmed trade or terminal actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade changes can affect a real brokerage account.

Mitigation: Start with a demo account and require fresh, explicit confirmation of the account and trade details for each order, cancellation, or position change; do not automatically retry uncertain trade calls.

Risk: An exposed or untrusted bridge endpoint can reveal account information or permit unauthorized trades.

Mitigation: Use only a trusted local or protected MT5_API_URL and configure a strong API token before any network exposure.

Risk: Terminal shutdown or restart interrupts access to the selected terminal.

Mitigation: Require fresh confirmation naming the target terminal and exact operation before shutdown or restart.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [Setup guide](references/setup.md)
- [Project homepage (skill metadata; import provenance unavailable)](https://github.com/psyb0t/mt5-httpapi)
- [Wickworks indicator reference](https://github.com/psyb0t/docker-wickworks#available-indicators)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and account or trade summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and a token when authentication is enabled; trade and terminal changes require explicit confirmation.]

## Skill Version(s):

4.16.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
