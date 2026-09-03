## Description:

This skill helps agents design shift-right validation plans for released or canary features using production monitoring, synthetic checks, user feedback, A/B validation, rollback criteria, and controlled chaos-engineering readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release owners use this skill to plan post-release validation for production or canary releases, including monitoring indicators, synthetic checks, alert thresholds, feedback loops, and rollback triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide production validation, gray releases, monitoring, and chaos-engineering readiness, which may affect live systems if treated as execution approval.

Mitigation: Use the output as a planning artifact only unless explicit authorization, scoped environment approval, privacy review, and a tested rollback plan are in place.

Risk: User behavior analytics and feedback loops can involve personal or regulated data.

Mitigation: Confirm user consent and applicable privacy requirements before collecting or analyzing production behavior data.

Risk: Chaos experiments and canary rollouts can expand incident impact if blast radius and rollback criteria are vague.

Mitigation: Start in non-production or shadow environments, limit blast radius, define alert thresholds, and rehearse rollback before broad rollout.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-shift-right)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured plans, tables, checklists, thresholds, and rollback criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include a shift-right test plan, monitoring dashboard outline, feedback loop, canary strategy, and nine-column test case table.]

## Skill Version(s):

1.7.6 (source: server release evidence; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
