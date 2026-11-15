## Description:

GPT Image 2.5 Sunburst supports text-to-image generation and image editing for detailed creative work, including in-image text, composition, reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use this skill to generate or edit images from prompts, optionally guiding the result with reference images and aspect ratio or quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login step is not clearly tied to the advertised image task, and some referenced paths were unavailable for review.

Mitigation: Review the linked CLI package before installing, protect the local configuration and API key, and rotate or revoke the key if exposed.

Risk: Prompts and local reference images are sent to dLazy hosted services for generation.

Mitigation: Use only prompts and images that are appropriate to share with the service; avoid sensitive inputs.

## Reference(s):

- [CLI repository (linked in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON metadata]

**Output Format:** [Generated image assets (PNG URLs or saved files) with a JSON result envelope]

**Output Parameters:** [Prompt, optional reference images, aspect ratio, quality, and synchronous or asynchronous generation settings]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy; local reference images are uploaded to its media storage.]

## Skill Version(s):

1.2.30 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
