## Description:

Uses a user-configured mt5-httpapi bridge to retrieve MetaTrader 5 account and market data, run backtests, and perform explicitly confirmed trade, chart-deployment, and terminal actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill with an already configured mt5-httpapi instance to inspect MetaTrader 5 accounts and market data, retrieve backtest reports, and manage trades or chart deployments with action-specific confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious with medium confidence, citing possible unauthenticated desktop exposure and setup, file, and system operations beyond the declared scope; the scan was partial because some referenced paths could not be resolved.

Mitigation: Verify the setup instructions, network exposure, and files being handled before use; avoid installation if those cannot be verified.

Risk: The bridge can expose brokerage account data and real-money trade or chart-deployment actions, and server authentication may be optional.

Mitigation: Use a trusted, restricted endpoint with authentication enabled when supported, check whether the account is live, and require fresh action-specific confirmation for every trade, deployment, or terminal change.

## Reference(s):

- [Setup guide](references/setup.md)
- [mt5-httpapi project](https://github.com/psyb0t/mt5-httpapi)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Shell commands, Configuration instructions]

**Output Format:** [JSON request and response data, text summaries, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user-provided MT5_API_URL; trade and other live mutations require per-action confirmation.]

## Skill Version(s):

4.34.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
