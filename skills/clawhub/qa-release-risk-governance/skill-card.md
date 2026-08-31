## Description:

Helps teams assess release risk, design canary rollout and rollback plans, and define production monitoring before a software release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, release managers, and DevOps teams use this skill to decide whether a release is ready, plan staged rollout gates, prepare rollback steps, and identify monitoring signals for production validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release, canary, or rollback recommendations could be acted on without sufficient approval or operational review.

Mitigation: Treat outputs as release-governance guidance and review any suggested release, canary, or rollback plan through the appropriate approval process before acting.

Risk: Incorrect or incomplete release risk analysis could miss production impact, rollback cost, or monitoring gaps.

Mitigation: Validate the assessment against current test strategy, risk assessment inputs, release scope, and production monitoring data before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-release-risk-governance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown release risk assessment with checklists and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a release decision recommendation, risk summary, blocking issues, rollback plan, monitoring recommendations, and traceability ID.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
