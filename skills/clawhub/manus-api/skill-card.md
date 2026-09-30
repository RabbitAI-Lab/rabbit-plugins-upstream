## Description:

Connects an agent to the Manus API through Maton to manage tasks, projects, files, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Manus users can ask an agent to run tasks, manage projects and files, and set up webhooks or approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection or write actions could affect Manus tasks, files, and webhooks.

Mitigation: Confirm the specific connection and each requested write; review the connection's authorization scope.

Risk: Hosted functions, triggers, and destinations can run persistent actions through the connected account.

Mitigation: Approve each function, trigger, and destination explicitly before creating or enabling it.

## Reference(s):

- [Manus skill on ClawHub](https://clawhub.ai/byungkyu/skills/manus-api)
- [Maton](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code blocks; API results may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Manus connection.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
