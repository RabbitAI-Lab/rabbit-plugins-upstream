## Description:

Helps agents manage Microsoft Teams, channels, messages, and meetings through Microsoft Graph with Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an agent to work with Microsoft Teams can list teams and channels, send messages, schedule meetings, and retrieve meeting records through an authorized connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad account permissions or message and meeting data could expose sensitive information.

Mitigation: Review Microsoft authorization scopes, connect only the needed account, and return only task-relevant data.

Risk: Writes, hosted functions, triggers, or destinations can change data or establish ongoing data flows.

Mitigation: Confirm each write and automation with the user, verify where data flows, prefer Maton-hosted destinations, and remove unused connections or automations.

## Reference(s):

- [Microsoft Teams API overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API calls, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe connected Microsoft Teams data or actions; sensitive results should be limited to the task.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
