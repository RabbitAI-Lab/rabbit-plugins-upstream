## Description:

Helps agents draft, review, schedule, and publish content through Automate It while managing related workspace tasks and resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[workingdevshero](https://clawhub.ai/user/workingdevshero)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams and agents use this skill to prepare social posts, submit them for human review, manage schedules and automations, and retrieve publishing results in an Automate It workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked API key could allow unauthorized access or publishing within its granted scopes.

Mitigation: Use a narrowly scoped key, keep it in a secret store, and rotate it if exposed.

Risk: Reviewer or admin access can approve, schedule, publish, or reorganize workspace content without the intended oversight.

Mitigation: Require explicit operator direction for approvals, no-review publishing, automations, and public posts; use human review where available.

Risk: Deleting tasks, content, automations, folders, or skills can permanently remove workspace material.

Mitigation: Confirm each specifically requested deletion with the operator before executing it.

## Reference(s):

- [Automate It agent information](https://automate.it.com/agents)
- [Automate It skill on ClawHub](https://clawhub.ai/workingdevshero/skills/automate-it)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown content with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing outcomes depend on the API key's scopes, workspace role, and review process.]

## Skill Version(s):

0.5.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
