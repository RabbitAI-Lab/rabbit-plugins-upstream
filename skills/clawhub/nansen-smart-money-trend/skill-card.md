## Description:

Analyzes whether smart-money wallets have held, recently entered, or continued buying a token using Nansen research data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and other users investigating a token use this skill to compare smart-money net flows, holder changes, and trades to distinguish sustained accumulation from recent entry or distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research uses a Nansen API key or saved browser session with account API access.

Mitigation: Confirm an authenticated key or session is selected before research; stop on authentication failures rather than switching to anonymous access.

Risk: Nansen research calls, including repeated calls in loops, may spend funds through configured x402 wallet authorization.

Mitigation: Review wallet authorization, payment policy, and spending limits before making calls or running loops.

## Reference(s):

- [Nansen Smart Money Trend on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-smart-money-trend)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a token address, chain, and selected Nansen API key or saved browser session.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
