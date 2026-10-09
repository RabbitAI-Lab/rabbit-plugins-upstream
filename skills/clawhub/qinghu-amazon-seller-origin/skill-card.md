## Description:

Analyzes seller countries and regions within an Amazon category, including their shares of listings, sales volume, and revenue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and market researchers use this skill to compare seller-origin shares within a specified category and marketplace, including whether local or Chinese sellers dominate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup or upgrades can install Node and qhkit and modify local PATH or shell configuration.

Mitigation: Obtain explicit approval before installation, upgrades, or environment changes; prefer a preinstalled, pinned qhkit in a contained environment.

Risk: Configuring the Qinghu service token places a credential on the user's machine.

Mitigation: Ask permission before token configuration and keep the token out of reports and logs.

Risk: Qinghu tool calls can consume paid credits.

Mitigation: Estimate credit costs and obtain user consent before paid calls.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-seller-origin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown analysis with an optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identify the marketplace, period, sample size, and credits consumed by paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
