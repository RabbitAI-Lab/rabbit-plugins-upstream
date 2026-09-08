## Description:

Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed write operations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect to Notion through Maton, inspect users, pages, databases, data sources, and blocks, and make scoped changes after confirming the target connection and resource.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Notion workspace content through an authorized Maton connection.

Mitigation: Install only when Notion access is intended, prefer OAuth, use the narrowest available Notion scopes, and confirm the exact connection and target resource before create, update, archive, delete, or bulk operations.

Risk: Credential exposure could occur if tokens or API keys are printed, persisted, or passed through unsafe command lines.

Mitigation: Use Maton's OAuth flow and operating system credential storage where possible; do not print, log, export, or persist provider credentials.

Risk: Content returned from Notion may include untrusted text that attempts to influence the agent's next action.

Mitigation: Treat fetched Notion content as data, validate it before reuse, and do not let it choose follow-up endpoints, recipients, commands, or write payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Notion API Introduction](https://developers.notion.com/reference/intro)
- [Notion Search API](https://developers.notion.com/reference/post-search.md)
- [Notion Query Database API](https://developers.notion.com/reference/post-database-query.md)
- [Notion Get Page API](https://developers.notion.com/reference/retrieve-a-page.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and request examples for Maton-mediated Notion API access; write operations require explicit confirmation.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
