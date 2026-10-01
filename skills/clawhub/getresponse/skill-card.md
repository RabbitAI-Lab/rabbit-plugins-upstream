## Description:

Guides agents in managing GetResponse marketing contacts, campaigns, messaging, and automation through an authenticated Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to inspect and manage GetResponse contacts, campaigns, newsletters, SMS, and related automations. Sending messages or changing business data requires explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending newsletters or SMS may reach real contacts or change business data.

Mitigation: Start with read-only checks and confirm each write or send, including its audience, content, and timing.

Risk: Connections and API keys can grant access to customer and campaign data.

Mitigation: Prefer OAuth, authorize only needed access, and avoid exposing long-lived API keys.

Risk: Functions, triggers, and destinations can continue running or forwarding data after setup.

Mitigation: Review their behavior and destinations before approval, and remove automations when no longer needed.

## Reference(s):

- [GetResponse skill on ClawHub](https://clawhub.ai/byungkyu/skills/getresponse)
- [Maton](https://maton.ai)
- [GetResponse API documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI specification](https://apireference.getresponse.com/open-api.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated requests follow the user's connection permissions; writes and sends require approval.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
