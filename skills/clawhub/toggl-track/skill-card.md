## Description:

Guides agents through authorized Toggl Track time tracking and management of projects, clients, and tags via Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Toggl Track can ask an agent to view and manage time entries, projects, clients, and tags. Optional automation can run approved tasks on a schedule or in response to supported events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Maton grants access to Toggl Track account data.

Mitigation: Authorize the connection only with the user's approval and use read/list operations by default.

Risk: Writes or connection changes can alter account data or access.

Mitigation: Obtain explicit approval before each write or connection change.

Risk: Functions, triggers, destinations, and local watches can persist or forward data.

Mitigation: Treat each automation feature as a separate opt-in and remove it when no longer needed.

## Reference(s):

- [Toggl Track skill release](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Toggl Track API documentation](https://engineering.toggl.com/docs/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized Maton connection for Toggl Track operations.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
