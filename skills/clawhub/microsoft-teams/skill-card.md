## Description:

Helps agents manage Microsoft Teams teams, channels, messages, and meetings through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to find Teams information, manage collaboration spaces, send messages, and arrange meetings through their authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account can grant access to sensitive Teams data.

Mitigation: Connect only with user approval, review OAuth scopes, and prefer read-only access where possible.

Risk: Messages, meeting changes, and other writes can affect other people.

Mitigation: Confirm the target and intended effect with the user before each write.

Risk: Triggers and destinations can keep forwarding future events after setup.

Mitigation: Obtain separate approval for each automation and destination, including what data will be sent and where.

## Reference(s):

- [ClawHub Microsoft Teams skill](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Microsoft Teams API overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with commands and summarized Teams results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain private account and message data.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
