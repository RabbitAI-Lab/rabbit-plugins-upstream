## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn text prompts, optionally with reference images, into Jimeng-generated images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied media are sent to dLazy services; local media paths may be uploaded for processing.

Mitigation: Avoid sending sensitive prompts or files unless they are approved for use with the service.

Risk: The pinned @dlazy/cli package was not included in the security scan, and the scanner review was partial.

Mitigation: Review the package and its project documentation before installation, and use the pinned version declared by the skill.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page (listed in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with generated image URLs and metadata; image files when saved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images can be provided; generated assets are returned as hosted URLs or saved to a local path.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
