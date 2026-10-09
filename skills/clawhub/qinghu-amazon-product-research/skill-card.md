## Description:

Filters Amazon products by marketplace, keyword, category, price, sales, growth, ratings, margin, and fulfillment to support product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product researchers use this skill to shortlist products across supported marketplaces using commercial filters such as sales, competition, price, and estimated margin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading external tooling may change the local environment.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version over automatic npm/npx installation or latest-version upgrades.

Risk: Persistent shell configuration changes may outlast the session.

Mitigation: Do not modify shell startup files without explicit user approval.

Risk: The skill handles an API token for paid service calls.

Mitigation: Provide the token through a secure secret mechanism and confirm estimated credits before authorizing paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-product-research)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown product shortlist with filters, findings, and usage charges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit and a Qinghu API token; tool calls use paid credits and require user approval.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
