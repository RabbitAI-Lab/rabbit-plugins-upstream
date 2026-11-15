## Description:

Automatically selects a dLazy CLI image model for image-generation requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can request image generation in natural language; the skill selects a dLazy CLI model and returns generated media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the skill's documented scope may include video and speech workflows beyond image generation, and scanner coverage is partial.

Mitigation: Review the requested workflow and the relevant CLI behavior before use, especially for video or speech tasks.

Risk: Prompts and supplied local media are sent to dLazy hosted services for processing and storage.

Mitigation: Avoid submitting sensitive prompts or files unless their use with the dLazy service is approved.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated images, SVG graphics, Hosted media URLs, JSON results]

**Output Format:** [Hosted media URLs in JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected model and request options determine the media returned.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
