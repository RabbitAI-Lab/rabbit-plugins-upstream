## Description:

Guides token-transfer analysis with Nansen to identify large transfers, flow trends, and wallet-label patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to examine token transfers, flow trends, and wallet-label breakdowns across supported chains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls may use an API key or saved browser session with account API permissions.

Mitigation: Use only trusted credentials, confirm the selected authentication state before research, and stop on authentication or renewal failure.

Risk: Supported x402 challenges may spend wallet funds on each call, including repeated calls in loops.

Mitigation: Review wallet authorization, payment policy, and spending limits before running calls or loops.

## Reference(s):

- [Nansen Token Transfer Analysis on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-token-transfer-analysis)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with bash command examples and interpretive guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a selected Nansen API key or saved browser session; token-flow queries do not support stablecoins.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
