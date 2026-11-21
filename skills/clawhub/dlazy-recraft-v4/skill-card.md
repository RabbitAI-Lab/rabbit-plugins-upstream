## Description:

1MP raster image generation with refined design judgment, suitable for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use the skill to generate raster images from prompts and iterate on aspect ratios. It returns generated image assets and a result summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan was partial: references to the CLI package and endpoints were unresolved, and its guidance recommends review before using the login flow.

Mitigation: Review the complete skill and the CLI dependencies before installation and before entering credentials.

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted API and media service.

Mitigation: Avoid sending sensitive prompts or files, and provide only assets authorized for cloud processing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Raster image assets and a JSON result envelope with output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratio options; asynchronous mode may return a generation ID before the image is ready.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
