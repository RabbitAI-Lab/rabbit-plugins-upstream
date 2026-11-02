## Description:

Generates 2K, 3K, or 4K Doubao Seedream images from prompts and optional reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can generate high-resolution images for key visuals, posters, and print, using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's hosted service, and local image files may be uploaded for processing.

Mitigation: Send only prompts and images you are comfortable sharing with dLazy.

Risk: The CLI stores an API key in the user's local configuration, and image generation may incur costs.

Mitigation: Use the recommended login flow, keep the key private, rotate or revoke it if exposed, and review the cost estimate before generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON result containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolutions and selectable aspect ratios; asynchronous requests can return a task ID.]

## Skill Version(s):

1.2.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
