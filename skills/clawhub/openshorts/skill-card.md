## Description:

Turn long videos (podcasts, webinars, streams) into vertical 9:16 clips with subtitles and publish them to TikTok, Instagram Reels and YouTube Shorts via the OpenShorts API or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mutonby](https://clawhub.ai/user/mutonby)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and automation teams use this skill to turn long videos into vertical clips, add or restyle subtitles, and prepare clips for TikTok, Instagram Reels, or YouTube Shorts. It is useful for asynchronous video clipping pipelines that need quota checks, status polling or webhooks, and explicit approval before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish generated clips to public social platforms.

Mitigation: Require explicit user approval for the exact clip, target account and platforms, title, and schedule before any publish action.

Risk: Video URLs and media may be processed by a third-party OpenShorts instance.

Mitigation: Use only videos the user has rights to, and avoid private or internal URLs unless the configured OpenShorts instance is trusted.

Risk: Generated clips may expire or be unavailable if presigned download links are not handled promptly.

Mitigation: Fetch or forward clip download URLs within the documented 24-hour availability window.

## Reference(s):

- [OpenShorts MCP documentation](https://www.openshorts.app/mcp)
- [OpenShorts MCP server](https://mcp.openshorts.app/mcp)
- [OpenShorts REST API](https://api.openshorts.app)
- [ClawHub skill page](https://clawhub.ai/mutonby/skills/openshorts)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include asynchronous job IDs, clip indexes, platform selections, webhook guidance, and publishing approval steps.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
