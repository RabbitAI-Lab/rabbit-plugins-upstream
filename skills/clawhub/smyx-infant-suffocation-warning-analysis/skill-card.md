## Description:

Analyzes infant sleep media for prone positioning and facial covering, and returns a structured risk report with recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers can submit infant sleep media for a structured risk report and review historical reports. The reports support monitoring and do not replace adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised continuous alarm behavior exceeds what the bundled workflow implements.

Mitigation: Treat reports as supplemental, maintain adult supervision, and verify any alerting separately.

Risk: Sleep footage is uploaded to a remote service, while processing, retention, and deletion practices are unclear.

Mitigation: Obtain explicit consent before upload and confirm who processes recordings and how they can be deleted.

Risk: Account and token handling may lack clear user control.

Mitigation: Require explicit account choices, secure credentials per user, and keep API secrets separate from identity fields.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured text or JSON reports; Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include identified sleep position, face covering, risk level, recommendations, and report links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata; artifact frontmatter lists 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
