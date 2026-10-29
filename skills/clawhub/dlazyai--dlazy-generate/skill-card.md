## Description:

A comprehensive generation skill that selects an appropriate dLazy CLI model to generate images, videos, and audio from the user's intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request image, video, or audio generation in natural language; the skill selects a suitable dLazy CLI model and returns generated media or its result URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and local media files may be uploaded for processing.

Mitigation: Use the skill only for explicit media requests and provide only files you intend to upload to dLazy.

Risk: The CLI stores an API key in the user's configuration, where exposure could permit account use.

Mitigation: Review the external CLI before installation and use an organization API key that can be rotated or revoked.

Risk: Generation requests can consume service credits.

Mitigation: Confirm the requested media and generation choice before starting a run.

## Reference(s):

- [dLazy CLI repository (linked by the skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated images, Generated videos, Generated audio, Generation result URLs]

**Output Format:** [Media outputs and URLs, with JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available formats and quality depend on the selected model; requests can consume dLazy service credits.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
