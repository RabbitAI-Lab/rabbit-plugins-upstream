## Description:

Analyzes token net flows, labeled sellers, and recent smart-money trades for potential exit signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Token holders and analysts use this skill to examine net flows, seller labels, and recent trades when assessing whether smart-money wallets are exiting a token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, especially in loops, may consume credits or trigger payments from an authorized wallet.

Mitigation: Confirm wallet authorization and spending limits before running calls; avoid unintended loops.

Risk: Cached session details may not prove valid authentication, and session renewal may fail.

Mitigation: Select an API key or saved session, check authentication status, and stop on failed or uncertain authentication rather than retrying anonymously.

## Reference(s):

- [Nansen Exit Signals on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-exit-signals)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a token address and chain; requires a selected Nansen API key or saved browser session.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
