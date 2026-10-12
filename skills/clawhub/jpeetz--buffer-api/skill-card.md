## Description:

Schedule, manage and analyze social media posts via the Buffer GraphQL API from any AI agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jpeetz](https://clawhub.ai/user/jpeetz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to schedule, manage, delete, retrieve, and analyze Buffer social media posts and drafts across supported connected channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Buffer API key gives an agent authority over the user's Buffer account and connected social publishing workflows.

Mitigation: Prefer BUFFER_API_KEY or a secret manager, avoid exposing keys in prompts or command history, and confirm the account and channel before making changes.

Risk: The skill can create, edit, reorder, or delete social posts and drafts.

Mitigation: Require explicit user confirmation before mutations that publish, reschedule, reorder, edit, or delete content.

Risk: Media posts depend on public URLs that Buffer can fetch, and untrusted media URLs can create operational or content risk.

Mitigation: Use trusted public hosting domains and verify media URLs with an anonymous HEAD or GET request before creating a post.

## Reference(s):

- [Buffer GraphQL API Reference](references/api-reference.md)
- [Buffer Media and Per-Network Metadata Reference](references/media-and-metadata.md)
- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Explorer](https://developers.buffer.com/explorer.html)
- [Buffer MCP Server](https://mcp.buffer.com/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with GraphQL examples and optional Python helper commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request templates, Buffer GraphQL queries and mutations, media URL verification steps, and status polling guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
