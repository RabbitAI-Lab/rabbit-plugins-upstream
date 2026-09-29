## Description:

Coordinates selected perspectives to review open-source project decisions and produce a consensus, disagreement, and recommendation report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qikairo7](https://clawhub.ai/user/qikairo7)

### License/Terms of Use:

MIT-0

## Use Case:

Open-source project maintainers and developers use this skill at decision points to compare perspectives on pull requests, documentation, repository setup, architecture, and governance, then receive a reasoned recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision reviews depend on other installed perspective skills and may delegate analysis to parallel subagents.

Mitigation: Confirm the required perspective skills are installed and review delegated analysis before acting on the recommendation.

Risk: Simulated viewpoints and synthesized recommendations may misstate a person's position or obscure consequential disagreement.

Mitigation: Use only documented public reasoning models, preserve material disagreements, and independently verify consequential decisions.

## Reference(s):

- [oss-perspective-council on ClawHub](https://clawhub.ai/qikairo7/skills/oss-perspective-council)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown report with consensus, disagreements, and a recommendation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are weighted by the selected perspectives' relevance to the decision.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
