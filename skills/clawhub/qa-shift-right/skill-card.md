## Description:

Helps QA and release teams plan post-release validation using canary monitoring, production checks, user feedback, and controlled resilience testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and release teams use this skill to design post-release checks, canary monitoring and alerts, feedback loops, and rollback triggers for production deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production validation or chaos experiments could disrupt live services.

Mitigation: Require explicit authorization, limit the blast radius, test in a non-production or shadow environment first, and use a rehearsed rollback plan.

Risk: Monitoring and user-behavior analysis could expose personal data.

Mitigation: Confirm user consent and applicable privacy requirements before collecting or analyzing production data.

## Reference(s):

- [QA Shift Right on ClawHub](https://clawhub.ai/kokxi/skills/qa-shift-right)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown plan and test-case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes canary metrics, production checks, alert thresholds, feedback handling, and rollback criteria.]

## Skill Version(s):

1.7.7 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
