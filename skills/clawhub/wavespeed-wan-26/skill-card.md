## Description:

WaveSpeedAI Wan 2.6 Video Generation helps agents generate text-to-video and image-to-video outputs with Alibaba's Wan 2.6 model through WaveSpeed AI, including audio guidance, prompt expansion, multi-shot mode, configurable seeds, and up to 15 seconds at 720p or 1080p.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to create videos from text prompts or animate source images through the WaveSpeed AI CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the WaveSpeed CLI or MCP package depends on trusting the WaveSpeed package and account flow.

Mitigation: Use a restricted environment and install only when the publisher and package source are trusted.

Risk: Broad environment secrets could be exposed to commands or tools used during video generation.

Mitigation: Keep only the required WaveSpeed credentials in scope and avoid exposing unrelated environment secrets.

Risk: @-prefixed local file inputs upload media to WaveSpeed.

Mitigation: Use @-prefixed local files only when the user intentionally wants that file uploaded.

## Reference(s):

- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide WaveSpeed CLI or MCP calls that return video output URLs and optional downloaded media paths.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
