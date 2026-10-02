## Description:

YouTube channels, videos, transcripts, and comments for agents - content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, research teams, marketing teams, and data teams use this skill to retrieve YouTube video, channel, transcript, comment, search, and recommendation data through superagnt's API for content research and creator intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes creator email lookup through a third-party API without prominent disclosure or controls.

Mitigation: Use email lookup only with clear user intent and a legitimate purpose, and review whether creator email retrieval is appropriate before installing or enabling the skill.

Risk: Channel, video, search, and email lookup targets are sent to superagnt's external API.

Mitigation: Do not submit sensitive or restricted targets unless external API use is acceptable for the workflow.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)
- [Scoped YouTube MCP server](https://mcp.superagnt.com/mcp/youtube)
- [MCP agent setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for the documented API calls.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
