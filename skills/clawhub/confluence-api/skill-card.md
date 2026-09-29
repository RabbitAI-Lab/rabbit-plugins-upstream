## Description:

Helps agents read and manage Confluence Cloud pages, spaces, blog posts, comments, and attachments through a managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to find, read, and update content in an authorized Confluence Cloud account. It also documents optional automations that require separate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes or new connections may change or expose Confluence content.

Mitigation: Start with read-only actions; confirm the exact account, target, and change before connecting or writing.

Risk: Hosted functions, triggers, and destinations can create persistent automation or forward data to third parties.

Mitigation: Approve each automation and destination separately, including the host, data fields, connected account, and persistence; avoid untrusted destinations.

Risk: API keys and locally executed event handlers can expose credentials or act on untrusted data.

Mitigation: Keep credentials out of logs and saved files; separately approve any local event handler after reviewing its behavior.

## Reference(s):

- [Confluence skill on ClawHub](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Confluence Cloud REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Confluence API responses from the authorized account.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
