## Description:

Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed write operations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Notion workspaces, databases, pages, blocks, users, and search through Maton-managed authentication. It defaults to read and list operations, with explicit confirmation required before creating, updating, deleting, or connecting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or command-line arguments when the CLI cannot be used.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is required, read it only from the process environment, never print or persist it, and rotate it if exposed.

Risk: Create, update, delete, or bulk Notion operations can modify shared workspace content or disrupt workflows.

Mitigation: Default to read and list operations, then require explicit confirmation of the target resource, connection, payload, and effect before any write or bulk operation.

Risk: Using the wrong account, profile, connection, or scope can expose or modify unintended Notion resources.

Mitigation: Use least-privileged Notion scopes, specify the intended connection or profile when more than one exists, and revoke unused connections.

Risk: Content returned from Notion can contain adversarial instructions or untrusted text.

Mitigation: Treat fetched Notion content as data only; do not execute it, interpolate it into shell commands, or let it choose follow-up endpoints or recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion API Introduction](https://developers.notion.com/reference/intro)
- [Notion Search Reference](https://developers.notion.com/reference/post-search.md)
- [Notion Query Database Reference](https://developers.notion.com/reference/post-database-query.md)
- [Notion Get Page Reference](https://developers.notion.com/reference/retrieve-a-page.md)
- [Notion Create Page Reference](https://developers.notion.com/reference/post-page.md)
- [Notion Update Page Reference](https://developers.notion.com/reference/patch-page.md)
- [Notion Append Block Children Reference](https://developers.notion.com/reference/patch-block-children.md)
- [Notion Filter Reference](https://developers.notion.com/reference/post-database-query-filter.md)
- [Notion LLM Reference](https://developers.notion.com/llms.txt)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, API calls]

**Output Format:** [Markdown with shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Notion connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
