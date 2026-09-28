## Description:

Screens tokens for smart-money activity and cross-references netflows to identify potential early accumulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and researchers use this skill to compare smart-money token screener results with netflow and token-level flows when investigating possible accumulation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the external Nansen CLI requires trusting its package and handling account credentials.

Mitigation: Confirm that you trust the Nansen CLI package and use an explicitly selected API key or authorized browser session.

Risk: API research calls, including calls in loops, may consume credits or incur wallet payments.

Mitigation: Check entitlements, wallet authorization, payment policy, and spending limits before running calls; avoid broad loops unless per-call charges are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-smart-money-alpha)
- [Nansen CLI npm package](https://www.npmjs.com/package/nansen-cli)
- [Nansen CLI repository (linked by skill)](https://github.com/nansen-ai/nansen-cli)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and token-flow summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chain, timeframe, token address, and result limits can be selected for research.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
