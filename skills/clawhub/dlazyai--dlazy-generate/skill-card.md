## Description:

Routes image, video, and audio generation requests to an appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate images, videos, and audio by routing requests to a suitable dLazy model through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and reported broad triggers plus a mismatch between the stated media-generation purpose and authentication setup.

Mitigation: Review the install and authentication instructions and the skill content before enabling it; confirm a request is intended to invoke generation.

Risk: Prompts and supplied local media are sent to dLazy hosted services for processing.

Mitigation: Avoid sending confidential or personal content unless it is approved for that service.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, Media URLs, JSON]

**Output Format:** [Hosted media URLs in a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects a model based on the request; generated media is returned by URL.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
