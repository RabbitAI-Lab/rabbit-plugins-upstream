## Description:

Helps agents discover statistically validated patterns in tabular data through Disco and explain the findings with effect sizes, significance measures, and available citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Data analysts and developers use Disco to identify feature interactions, subgroup effects, and relationships in tabular datasets, then communicate validated findings and links to interactive reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded datasets and analysis results may be sent to Disco or cloud storage, and public analyses publish results.

Mitigation: Obtain permission before uploading data and explicitly select private visibility for confidential or regulated datasets.

Risk: Agent-accessible billing tools can attach payment methods, purchase credits, or change plans.

Mitigation: Require explicit human approval before any payment-method, purchase, or subscription action.

## Reference(s):

- [Discovery on ClawHub](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco developer documentation](https://disco.leap-labs.com/developers)
- [Disco Python SDK](docs/python-sdk.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of patterns and interactive report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings may include conditions, effect sizes, adjusted p-values, and citations when available.]

## Skill Version(s):

0.2.179 (source: ClawHub release and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
