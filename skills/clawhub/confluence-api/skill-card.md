## Description:

Helps agents access Confluence Cloud to read and manage pages, spaces, blog posts, comments, and attachments through a user-authorized connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to retrieve and organize Confluence content, or to make approved changes to pages, spaces, comments, and attachments. It also describes optional automations for approved Confluence actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the wrong account or granting broader Confluence access than needed.

Mitigation: Confirm the intended account and requested scopes before authorizing a connection.

Risk: Changes or deletions could affect shared Confluence content.

Mitigation: Confirm each write or delete with the user before proceeding.

Risk: Hosted functions, triggers, or destinations could continue acting or forwarding data after setup.

Mitigation: Require explicit approval for the intended ongoing action, event data, and destination before enabling automation.

## Reference(s):

- [Confluence skill on ClawHub](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton](https://maton.ai)
- [Companion API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with commands and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the authorized Confluence account and its permissions.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
