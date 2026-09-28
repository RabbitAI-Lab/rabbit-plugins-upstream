## Description:

Generates evidence-based portfolio audits, candidate scorecards, privacy classifications, consolidation plans, and a persistent execution queue with dependency-linked tasks for Skill portfolio management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to inventory Skill portfolios, find duplicates or stale versions, classify sharing risk, and produce prioritized maintenance and publication roadmaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad scan range could expose sensitive projects, memories, or private Skill material during an audit.

Mitigation: Define the scan range before running the skill and exclude sensitive projects or memories that should not be reviewed.

Risk: The persistent execution queue writes follow-up work to a task ledger, which could be placed in an unintended location.

Mitigation: Choose and confirm the task-ledger location before writing audit follow-up tasks.

Risk: Audit recommendations may misclassify sharing readiness or miss context in large Skill portfolios.

Mitigation: Review the evidence boundaries, privacy classifications, and proposed P0 actions before acting on publication or maintenance recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-portfolio-audit)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown report with scorecards, classifications, roadmap sections, and a task ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include evidence boundaries, risk locations without credential values, dependency-linked tasks, and next-action status.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
