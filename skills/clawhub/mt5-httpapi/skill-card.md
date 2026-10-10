## Description:

Helps agents use a user-configured MetaTrader 5 HTTP bridge to inspect account and market data, run backtests, and perform explicitly confirmed trading and terminal operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading operators who already run mt5-httpapi use this skill to query their MetaTrader 5 account, review market data and backtests, and carry out individually confirmed account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Orders, position changes, and live EA deployments can affect real brokerage funds.

Mitigation: Start with a demo account and confirm the exact account and action, including trade size and protective levels or deployment target, before every mutation.

Risk: An exposed API without authentication can allow unauthorized access to account data and trading controls.

Mitigation: Set a strong token before network exposure and keep the service bound to localhost or behind strong authentication.

Risk: Terminal restarts and file writes or deletes can interrupt trading or alter a running environment.

Mitigation: Require confirmation of the target terminal, file, and exact operation before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [mt5-httpapi project homepage](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [Chart deployments documentation](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/chart-deployments.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with HTTP requests and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses may include account and market data; actions affecting live accounts require explicit per-action confirmation.]

## Skill Version(s):

4.28.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
