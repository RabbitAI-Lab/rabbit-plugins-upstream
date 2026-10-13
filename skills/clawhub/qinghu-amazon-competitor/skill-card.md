## Description:

Helps Amazon sellers research competing products by marketplace, month, brand, seller, ASIN, category, or keyword and compare sales, revenue, rank, price, and ratings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and market researchers use this skill to find and compare competing products across supported marketplaces using Qinghu AI's competitor lookup service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prompt the agent to install or upgrade external tooling and change the host environment.

Mitigation: Review before installing; require explicit approval for host changes and prefer a preinstalled, pinned qhkit version.

Risk: Configuring API tokens through agent-run commands may expose credentials.

Mitigation: Use a scoped secret mechanism and configure credentials only with explicit user approval.

Risk: Competitor lookups consume paid credits, and even failed remote calls may incur charges.

Mitigation: Check the current credit estimate and obtain consent before making paid calls; limit follow-up calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-competitor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Spreadsheet files]

**Output Format:** [Concise comparison and key product metrics; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies marketplace, period, sample size, and credits charged when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
