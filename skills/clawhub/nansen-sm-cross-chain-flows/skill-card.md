## Description:

Guides cross-chain smart-money netflow analysis to identify potential token capital rotation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to compare smart-money token netflows across chains and spot possible capital rotation over 24-hour and seven-day periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, especially in loops, can consume API credits or trigger configured wallet payments.

Mitigation: Review payment policy, wallet authorization, spending limits, and expected call volume before running the workflow.

Risk: Missing or failed account authentication can prevent research calls.

Mitigation: Select an authorized API key or browser session and check authentication status before starting; stop on authentication failures rather than switching to anonymous paid access.

Risk: A token absent from chain results may have activity below the reporting threshold.

Mitigation: Avoid treating absent results as zero activity or an unsupported chain; use the documented result limit when comparing chains.

## Reference(s):

- [Nansen SM Cross-Chain Flows on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-sm-cross-chain-flows)
- [nansen-devops publisher profile](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 24-hour and seven-day netflows; missing results do not prove no activity.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
