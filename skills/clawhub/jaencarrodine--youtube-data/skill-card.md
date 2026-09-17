## Description:

YouTube channels, videos, transcripts, and comments for agents - content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and content teams use this skill to query YouTube channel, video, transcript, comment, recommendation, trending, screenshot, and contact-data endpoints through Superagnt-backed API or MCP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube queries and the Superagnt credential are sent to Superagnt.

Mitigation: Install only when this data flow is acceptable, scope the credential to the intended workspace, and rotate or revoke the key if exposure is suspected.

Risk: The MCP server can expose broader tool families beyond the stated YouTube scope.

Mitigation: Enable only the YouTube tool family unless broader Superagnt access is intentionally needed.

Risk: Channel email lookup endpoints may expose sensitive contact data.

Mitigation: Use the email endpoints only in lawful, consent-aware workflows with appropriate review before storage or outreach.

## Reference(s):

- [ClawHub YouTube Data listing](https://clawhub.ai/jaencarrodine/skills/youtube-data)
- [Superagnt YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [Superagnt YouTube MCP server](https://mcp.superagnt.com/mcp/youtube)
- [Superagnt MCP agent setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt API key dashboard](https://superagnt.com/r/ch-youtube-data-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls, JSON]

**Output Format:** [Markdown instructions with curl examples and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API usage; MCP usage may use OAuth or bearer authorization.]

## Skill Version(s):

2.0.2 (source: server release, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
