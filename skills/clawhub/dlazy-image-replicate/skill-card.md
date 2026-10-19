## Description:

Analyzes a source image's composition, colors, lighting, and style to guide generation of a similar image with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate an image resembling the visual style of a supplied image through the dLazy image-replication service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to dLazy cloud services.

Mitigation: Send only media you are comfortable sharing with the service; avoid sensitive images.

Risk: The dLazy CLI can persist an API key on the local device.

Mitigation: Use a per-invocation API key when persistence is unwanted, and rotate or revoke exposed keys.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image files]

**Output Format:** [JSON response with generated image URL; optional downloaded image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image URL.]

## Skill Version(s):

1.3.32 (source: ClawHub release; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
