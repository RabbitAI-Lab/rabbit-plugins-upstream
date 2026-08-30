## Description:

Schedule, manage and analyze social media posts via the Buffer GraphQL API from any AI agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jpeetz](https://clawhub.ai/user/jpeetz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing operators, and automation agents use this skill to schedule, manage, and analyze Buffer social media posts across connected channels. It supports account and channel discovery, post creation and scheduling, media attachment guidance, post updates and deletion, ideas, metrics, and Buffer GraphQL troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Buffer API key can be used to create, edit, reorder, or delete scheduled and draft social posts.

Mitigation: Use a limited Buffer API key where possible, store it only in a controlled environment variable, and require explicit human confirmation before create, edit, move, or delete operations.

Risk: Media assets must be fetched from public URLs, which can expose private files or fail later if signed links expire.

Mitigation: Host only intended public assets, verify anonymous reachability before scheduling, and avoid URLs that expire before the scheduled post time.

## Reference(s):

- [ClawHub Buffer API skill page](https://clawhub.ai/jpeetz/skills/buffer-api)
- [Buffer GraphQL API reference](https://developers.buffer.com/reference.html)
- [Buffer API Explorer](https://developers.buffer.com/explorer.html)
- [Buffer MCP server](https://mcp.buffer.com/mcp)
- [API reference](references/api-reference.md)
- [Media and metadata reference](references/media-and-metadata.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with GraphQL, JSON, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request templates, Buffer GraphQL mutations and queries, environment variable setup, and verification commands.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
