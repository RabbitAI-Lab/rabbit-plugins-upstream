## Description:

Generate and edit images with ByteDance Seedream 5.0 Pro through WaveSpeed AI, including multi-reference edits and image layer decomposition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create images from prompts, edit images with one or more references, or separate an image into a base image and transparent layers using Seedream 5 Pro.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to WaveSpeed, and image generation uses account credits.

Mitigation: Submit only appropriate images and review current pricing and run settings before generating.

Risk: API credentials could be exposed if pasted into chat.

Mitigation: Authenticate through the CLI or use an environment variable; keep API keys out of chat.

Risk: The security review covers the bundled instructions, not the external software or hosted service.

Mitigation: Review the provider's current service information and terms before use.

## Reference(s):

- [Seedream 5.0 Pro text-to-image model](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro)
- [Seedream 5.0 Pro image-editing model](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro/edit)
- [Seedream 5.0 Pro layer-decomposition model](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro/layer-decomposition)

## Skill Output:

**Output Type(s):** [Images, Image URLs, Transparent image layers]

**Output Format:** [JPEG or PNG images and result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Layer decomposition can return a base image and multiple transparent layers.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
