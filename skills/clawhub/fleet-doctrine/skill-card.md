## Description:

Fleet Doctrine provides model routing guidance for choosing model classes for sub-agents, scheduled jobs, coding delegation, and task handling in a multi-model AI fleet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to choose an appropriate model class for orchestration, implementation, scheduled work, second opinions, image or video tasks, and long-context analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model routing guidance can influence an agent toward higher-cost or more capable model classes than a task requires.

Mitigation: Review routing decisions against task sensitivity, cost, and capability needs before deployment.

Risk: Routing guidance can become stale as model classes and available provider models change.

Mitigation: Treat aliases as model classes and update local mappings to current models rather than hardcoding dated model IDs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/fleet-doctrine)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transparent routing guidance; no code execution, persistence, or unusual data handling.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
