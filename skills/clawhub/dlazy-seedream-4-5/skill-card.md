## Description:

Generates images from text prompts or reference images with Doubao Seedream 4.5 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or transform reference images using a hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy, which also hosts generated files.

Mitigation: Confirm the hosted-service data flow is acceptable before submitting sensitive prompts or media.

Risk: Logging in stores an API key in the local CLI configuration.

Mitigation: Protect local credentials or supply the key per command with DLAZY_API_KEY instead.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and CLI JSON containing generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated images locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.21 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
