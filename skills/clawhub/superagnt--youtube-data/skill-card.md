## Description:

YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing teams use this skill to find YouTube videos and channels, review transcripts and comments, and monitor creator activity through Superagnt's YouTube data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube queries, channel identifiers, URLs, and the API key are sent to Superagnt.

Mitigation: Use the integration only if you trust Superagnt with these inputs and your credential.

Risk: Channel email lookups can expose creators' personal contact data.

Mitigation: Use contact details only for the user's stated purpose and avoid bulk unsolicited outreach.

Risk: The optional MCP/OAuth connection grants scoped YouTube access to Superagnt.

Mitigation: Enable MCP/OAuth only if you trust Superagnt for that scope.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [Superagnt app and API keys](https://superagnt.com/r/ch-youtube-data-key)
- [YouTube MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [YouTube Data ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with JSON tool schemas and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are structured JSON; the optional MCP connection supports OAuth.]

## Skill Version(s):

2.0.7 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
