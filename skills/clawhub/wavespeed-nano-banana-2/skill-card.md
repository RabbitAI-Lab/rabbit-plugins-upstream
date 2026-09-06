## Description:

Generate and edit images using Google's Nano Banana 2 model via WaveSpeed AI, including text-to-image generation and natural-language edits with flexible aspect ratios, up to 4K resolution, multilingual text rendering, and camera-style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate new images from prompts or edit existing images through WaveSpeed's CLI or MCP tooling. It is suited for workflows that need controllable image outputs, multiple aspect ratios, selectable resolution, and prompt-driven image transformations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running unpinned npm or npx packages can introduce ordinary supply-chain exposure.

Mitigation: Verify the WaveSpeed CLI or MCP package and version before use, and avoid running npm or npx with administrator privileges.

Risk: Prompts, image URLs, and uploaded local images are sent to WaveSpeed for image generation or editing.

Mitigation: Upload only images and URLs intended for WaveSpeed processing, and prefer a revocable WaveSpeed key where possible.

Risk: API credentials can be exposed if copied into chat or stored carelessly.

Mitigation: Use wavespeed login or the WAVESPEED_API_KEY environment variable instead of sharing keys in conversation.

## Reference(s):

- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)
- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-nano-banana-2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples, parameter guidance, and output URL handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of WaveSpeed CLI or MCP calls and handling of generated image URLs or downloaded files.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
