## Description:

Helps agents read and manage Confluence Cloud pages, spaces, blog posts, comments, and attachments through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to find and manage Confluence content and, with approval, connect an account or configure related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account can read or change Confluence content.

Mitigation: Select the narrowest available scopes, start with read-only operations, and confirm the target and effect before every change or deletion.

Risk: Credentials or private content could be exposed through raw API calls or overly broad connections.

Mitigation: Prefer OAuth login, avoid raw API keys unless necessary, and remove unused connections.

Risk: Automations may continuously forward matching event data to a destination.

Mitigation: Get separate approval for triggers and destinations, limit forwarded data, and periodically remove unused automations.

## Reference(s):

- [Confluence skill listing](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Confluence REST API v2 documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize Confluence content or API results, depending on the request.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
