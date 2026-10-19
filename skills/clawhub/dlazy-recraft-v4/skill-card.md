## Description:

Generates 1MP raster images from prompts through the dLazy Recraft V4 service for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate raster images from text prompts and try different aspect ratios through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service sends prompts and any explicitly selected input files to dLazy-hosted endpoints.

Mitigation: Confirm the service is appropriate for the data before submitting prompts or selecting files.

Risk: The CLI stores a dLazy API key locally and may require installing a third-party npm package.

Mitigation: Protect the local API key and review the pinned @dlazy/cli package before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI package (declared in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON response with hosted image URLs; optional locally saved PNG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous tasks return a generation ID for polling.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
