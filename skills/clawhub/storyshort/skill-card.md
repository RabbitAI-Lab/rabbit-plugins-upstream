## Description:

Create, render and publish AI videos with StoryShort, plus standalone AI images and clips, with option discovery, credit estimates, and direct publishing to TikTok, YouTube, and Instagram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuelrondot](https://clawhub.ai/user/samuelrondot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and content teams use this skill to create, render, inspect, and publish short-form StoryShort media through the StoryShort MCP server while checking available options and credit costs before spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a StoryShort API key that can create media, consume credits, and access connected publishing workflows.

Mitigation: Install it only when that access is intended, keep STORYSHORT_API_KEY private, and review the target account before use.

Risk: Media generation and rendering can spend credits.

Mitigation: Check the account balance and quote the estimated credit cost before starting a generation or expensive render.

Risk: Publishing or scheduling can post generated media to connected social accounts.

Mitigation: Require explicit approval before any publish action and use restricted or test visibility settings when validating a workflow.

## Reference(s):

- [StoryShort MCP documentation](https://storyshort.ai/mcp)
- [StoryShort REST API documentation](https://storyshort.ai/api-docs)
- [StoryShort API key settings](https://storyshort.ai/app/settings/api)
- [ClawHub skill page](https://clawhub.ai/samuelrondot/skills/storyshort)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires STORYSHORT_API_KEY and may initiate asynchronous StoryShort media generation, rendering, or publishing workflows.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
