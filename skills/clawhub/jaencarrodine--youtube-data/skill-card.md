## Description:

YouTube channels, videos, transcripts, and comments for agents - content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, marketing teams, and creator-intelligence teams use this skill to retrieve YouTube video, channel, transcript, comment, search, trending, recommendation, and screenshot data through Superagnt API and MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Superagnt API access for YouTube data and can include creator contact lookup.

Mitigation: Install only when users intend to authorize Superagnt API access; use email lookup with explicit user intent and privacy, consent, and anti-spam controls.

Risk: The MCP setup can expose broader Superagnt tool families than the YouTube skill alone.

Mitigation: Review MCP setup and enabled tool families before use; enable only the YouTube-related tools needed for the workflow.

Risk: The security scan verdict is suspicious due to unclear upfront disclosure of email lookup and platform expansion capabilities.

Mitigation: Review the skill behavior and user-facing disclosure before deployment, especially for environments handling personal or contact data.

## Reference(s):

- [Superagnt YouTube Data Documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [Superagnt YouTube MCP Server](https://mcp.superagnt.com/mcp/youtube)
- [Superagnt MCP Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub YouTube Data Listing](https://clawhub.ai/jaencarrodine/skills/youtube-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API and MCP calls may return live YouTube data and creator contact lookup results.]

## Skill Version(s):

2.0.5 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
