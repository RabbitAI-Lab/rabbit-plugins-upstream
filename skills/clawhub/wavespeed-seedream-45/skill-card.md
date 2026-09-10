## Description:

Generate and edit images with ByteDance's Seedream V4.5 model through WaveSpeed AI, including text-to-image generation, multi-image editing, custom resolutions up to 4096x4096, and typography-focused outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to guide agents through WaveSpeed CLI or MCP workflows for text-to-image generation and image editing with Seedream V4.5. It is useful when users need high-resolution images, poster or logo typography, local-file uploads, or multi-image edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on third-party WaveSpeed npm packages and the WaveSpeed platform.

Mitigation: Install only when that trust decision is acceptable; pin package versions where possible and avoid privileged shells.

Risk: Image generation and editing may send prompts, URLs, uploaded local files, and API credentials through third-party services.

Mitigation: Use scoped and rotatable WaveSpeed keys, rely on CLI login instead of chat-pasted secrets, and upload only media intended for WaveSpeed processing.

Risk: Untrusted or unintended media URLs could be passed to the model workflow.

Mitigation: Pass only user-provided media URLs or URLs returned by a previous trusted run, and validate model parameters against the documented schema.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-seedream-45)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key setup](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model IDs, input parameter guidance, authentication notes, and expected output URLs for generated or edited images.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
