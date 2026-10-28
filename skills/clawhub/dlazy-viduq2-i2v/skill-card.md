## Description:

Convert static images into dynamic videos with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use the skill to turn reference images or start and end frames into short videos with Vidu Q2. It accepts a prompt and generation settings, then returns generated media or an asynchronous task result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images and other media are uploaded to dLazy's hosted service for generation.

Mitigation: Submit only media you are comfortable uploading to dLazy.

Risk: Video generation uses paid cloud processing.

Mitigation: Review generation costs and available credits before submitting a request.

Risk: The CLI uses an API key for account access.

Mitigation: Use the environment-variable option if preferred, protect the local configuration file, and revoke the key when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy service](https://dlazy.com)
- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video assets, JSON results, Usage guidance]

**Output Format:** [JSON results with generated asset URLs or task status; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation settings include prompt, input images or frames, duration, aspect ratio, resolution, and optional audio.]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
