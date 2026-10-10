## Description:

Helps users assess Amazon keyword demand through search volume, purchases, purchase rate, and year-over-year, month-over-month, and three-month trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product researchers use this skill to assess keyword search and purchase trends across supported marketplaces and periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may install or upgrade Node and qhkit, or modify PATH without clear per-step approval.

Mitigation: Approve each installation, upgrade, and environment change explicitly; pin the qhkit version where practical.

Risk: Configuring a Qinghu API token may expose a credential if handled carelessly.

Mitigation: Obtain explicit consent before configuring the token and keep it out of logs and shared files.

Risk: Keyword data queries consume credits, and actual costs can rise with result volume.

Mitigation: Confirm the estimated cost and scope before each paid call, especially bulk queries, and report the credits charged.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend summary with supporting figures; table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, period, sample size, and credits charged for paid queries.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
