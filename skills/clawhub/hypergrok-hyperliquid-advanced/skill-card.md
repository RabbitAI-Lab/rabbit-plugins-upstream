## Description:

Guides approved Hyperliquid trading-desk workflows for advanced orders, protective cancellation, API-wallet use, and sub-account or vault addressing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk operators and developers use this reference to assess and implement less common Hyperliquid actions, including TWAP and spot orders, on approved tickets. It also identifies actions the desk does not support, such as transfers and withdrawals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trading actions can affect real funds if an agent acts without authorization or limits.

Mitigation: Use a dedicated API wallet, approved tickets, clear limits, and the designated execution role; keep main-wallet keys off the desk.

Risk: A triggered dead-man's switch cancels protective stops along with other orders.

Mitigation: Obtain explicit approval before arming it; if it fires with an open position, treat the position as unprotected and follow the incident playbook.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, API calls]

**Output Format:** [Markdown with Python and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trading actions require an approved ticket and the designated execution role.]

## Skill Version(s):

1.6.1 (source: ClawHub release; bundled skill metadata states 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
