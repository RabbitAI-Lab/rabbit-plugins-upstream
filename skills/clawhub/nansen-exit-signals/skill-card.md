## Description:

Guides token holders through Nansen CLI research to assess smart-money exit signals using net flows, seller labels, and recent trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Token holders and analysts use this skill to inspect net flow direction, labeled sellers, and recent smart-money trades when assessing whether a token is seeing exits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research queries may consume account entitlements or credits, and supported x402 challenges may spend authorized wallet funds, including on repeated calls.

Mitigation: Review the selected credential, wallet payment policy, and spending limits before running queries or loops.

Risk: An unverified or failed authentication state can prevent the intended research workflow.

Mitigation: Check authentication status first and stop on anonymous selection, authentication failure, or uncertain session renewal; do not fall back to anonymous paid access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-exit-signals)
- [Nansen CLI browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and exit-signal interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses token address and chain; reports flows, seller labels, and recent trades.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
