## Description:

Generates images with Alibaba Bailian Qwen Image 2.0 Pro through dLazy, with support for detailed layouts and mixed Chinese and English text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to turn text prompts and up to three reference images into image assets, including designs with detailed layouts or rendered text. Results can be returned as image URLs or saved locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to dLazy services for generation, and local image files may be uploaded to its media storage.

Mitigation: Send only prompts and images you are authorized to share, and review dLazy's media-retention terms before use.

Risk: The CLI stores an organization API key in the local user configuration, and image generation may incur costs.

Mitigation: Protect the stored key, rotate or revoke it if exposed, and check generation costs before submitting requests.

Risk: The skill relies on an external CLI package to make API requests and handle files.

Mitigation: Review the CLI package and its source before installation, as the skill guidance recommends.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON metadata, Image URLs]

**Output Format:** [JSON result envelope with image URLs and metadata; optionally a saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation may return a task identifier when run asynchronously.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
