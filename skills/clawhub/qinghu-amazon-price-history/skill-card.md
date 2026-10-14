## Description:

Queries historical price, sales rank, review, seller, and Buy Box trends for a single Amazon ASIN, along with available FBA costs and product details; it does not provide sales volume.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and analysts use this skill to inspect an ASIN's pricing, ranking, reviews, and seller trends for product research and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating qhkit and Node changes local tooling and may persist shell configuration.

Mitigation: Prefer preinstalled, pinned tooling in a controlled environment; allow shell startup file changes only with explicit approval.

Risk: A Qinghu API token must be configured to access the service.

Mitigation: Use a controlled credential and review token setup before allowing the skill to configure it.

Risk: History lookups are paid calls, and the final charge may increase with result volume.

Mitigation: Review the current estimate and obtain approval before paid calls or large result requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-price-history)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend analysis in text or Markdown, with a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies marketplace and time period; reports credits consumed for paid calls. Sales volume is not included.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
