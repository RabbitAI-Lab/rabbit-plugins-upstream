## Description:

Turn long videos (podcasts, webinars, streams) into vertical 9:16 clips with subtitles, re-cut them, and publish them to TikTok, Instagram Reels and YouTube Shorts via the OpenShorts API or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mutonby](https://clawhub.ai/user/mutonby)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and media operators use this skill to let an agent create short-form clips from longer videos, refine captions or edits, and schedule or publish approved clips through OpenShorts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish content to connected social accounts, and Instagram or YouTube posts may go live directly.

Mitigation: Require explicit user confirmation of the target platforms, title, caption, and timing before publishing.

Risk: The skill may send video URLs or uploaded video content to OpenShorts for processing.

Mitigation: Use it only for videos the user has rights to process and only when sharing the source with OpenShorts is acceptable.

Risk: The hosted OpenShorts API requires an API key.

Mitigation: Store OPENSHORTS_API_KEY in the agent host's normal secret storage and avoid exposing it in prompts, logs, or generated files.

## Reference(s):

- [OpenShorts MCP documentation](https://www.openshorts.app/mcp)
- [OpenShorts API documentation](https://api.openshorts.app/docs)
- [OpenShorts HTTP reference](reference.md)
- [Agent Skills standard](https://github.com/agentskills/agentskills)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration]

**Output Format:** [Markdown guidance with REST, MCP, and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce asynchronous job instructions, polling or webhook guidance, and publishing confirmation prompts.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
