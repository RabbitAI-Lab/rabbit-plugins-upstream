## Description:

Remove watermarks, logos, captions, and text overlays from images and videos using WaveSpeed AI for media the user owns or is licensed to modify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to remove watermarks, captions, logos, or text overlays from images and videos they own or are licensed to modify. It guides setup, responsible-use checks, model invocation, pricing awareness, and result handling through WaveSpeed CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be misused to remove copyright, attribution, or ownership marks from media the user is not authorized to modify.

Mitigation: Confirm the user owns the media or has a license that permits removing the mark before running the model, and refuse unclear or infringing requests.

Risk: Selected media is uploaded to WaveSpeed for processing.

Mitigation: Use the skill only when the user is comfortable sending the media to WaveSpeed, and avoid arbitrary URLs or media sources not provided by the user.

Risk: Global CLI installation can introduce environment-wide package and version exposure.

Mitigation: Use a pinned package version or isolated environment when tighter control is required.

## Reference(s):

- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed Access Key](https://wavespeed.ai/accesskey)
- [WaveSpeed Terms of Service](https://wavespeed.ai/static/terms)
- [ClawHub Skill Page](https://clawhub.ai/wavespeed/skills/wavespeed-watermark-remover)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, model identifiers, parameter tables, and JSON-output handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WaveSpeed-hosted output URLs or downloaded media files after CLI or MCP execution.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
