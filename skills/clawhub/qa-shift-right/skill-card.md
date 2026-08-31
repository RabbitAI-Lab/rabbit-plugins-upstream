## Description:

QA Shift Right helps agents design post-release validation plans using production monitoring, synthetic checks, A/B validation, canary metrics, alert thresholds, rollback triggers, and chaos engineering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release teams use this skill to plan production validation after a release or during canary rollout. It guides the agent to produce monitoring metrics, synthetic test cases, alert thresholds, feedback loops, rollback triggers, and chaos experiment safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production monitoring, canary release, user behavior analysis, or chaos experiment guidance could affect live systems if applied without authorization.

Mitigation: Require explicit organizational approval before use on real systems.

Risk: User behavior analysis and feedback collection can create privacy or regulatory exposure.

Mitigation: Confirm user consent and applicable privacy compliance before collecting or analyzing production user data.

Risk: Canary rollout or chaos experiment plans can increase incident impact if blast radius and rollback paths are not controlled.

Mitigation: Start with narrow scope, define measurable rollback triggers, use circuit breakers where appropriate, and validate rollback procedures before expanding exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-shift-right)
- [ClawHub publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured tables, checklists, metrics, thresholds, and rollout guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a shift-right validation plan covering canary strategy, monitoring dashboard, feedback loop, synthetic checks, alert thresholds, rollback triggers, and chaos engineering controls.]

## Skill Version(s):

1.7.5 (source: server release metadata and skill frontmatter, released 2026-08-30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
