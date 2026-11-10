## Description:

Generates 1MP raster images with Recraft V4 for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can submit prompts and aspect-ratio options through the dLazy CLI to generate Recraft V4 raster images, then retrieve the image URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags authentication steps whose connection to the image-generation purpose is unclear.

Mitigation: Review the CLI authentication flow before use, confirm the dLazy account and service are expected, and use an account-scoped key that can be rotated or revoked.

Risk: Prompts and any supplied image, video, or audio files are sent to dLazy-hosted services for processing.

Mitigation: Avoid sending sensitive prompts or media unless the service is approved for that data.

## Reference(s):

- [CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Raster images, JSON]

**Output Format:** [Generated image assets with a JSON response containing result URLs and image metadata; asynchronous requests can return a task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are returned from dLazy media storage; an optional save path can download the result locally.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
