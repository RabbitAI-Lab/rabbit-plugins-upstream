## Description:

Screens Amazon categories by market size, competition, concentration, profitability, and opportunities for new products using Qinghu market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product researchers use this skill to compare categories and identify promising markets for new products across supported Amazon sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade npm packages and install Node.js in the user account.

Mitigation: Review setup before running it; install manually or in an isolated environment and pin package versions.

Risk: The integration stores a qhkit API token on the host.

Mitigation: Use a scoped token where possible and limit access to the account and environment storing it.

Risk: Market-data requests are paid and larger result sets may increase charges.

Mitigation: Check the current estimate and obtain user approval before paid calls or large retrievals.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-list)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Concise market analysis with key figures and optional tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Amazon site, analysis period, sample size, and credits used when applicable.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
