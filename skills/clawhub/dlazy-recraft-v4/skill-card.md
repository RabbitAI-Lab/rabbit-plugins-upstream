## Description:

1MP raster image generation with refined design judgment. Suitable for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative practitioners use the skill to generate raster images from prompts and iterate on aspect ratio and output settings through the dLazy Recraft V4 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key, and the security assessment notes that some package and installation references could not be resolved, leaving parts of setup unchecked.

Mitigation: Review the pinned CLI package and installation details before authenticating; use the documented login flow and rotate or revoke the organization key when needed.

Risk: Prompts and supplied local media files are sent to dLazy-hosted services for generation.

Mitigation: Avoid sending sensitive prompts or files unless their transfer to the service is approved.

## Reference(s):

- [dLazy service website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed by the skill](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, API calls]

**Output Format:** [Raster image files (PNG example) returned by URL; optional JSON task/result envelope]

**Output Parameters:** [Prompt and aspect ratio]

**Other Properties Related to Output:** [Generated image URLs are hosted by the service; results can be saved to a local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
