## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can create images from text prompts or use reference images to guide image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local reference images are sent to dLazy-hosted services.

Mitigation: Avoid sending sensitive prompts or images unless their transfer to the service is acceptable.

Risk: The security review notes that the login step's connection to image generation is unclear.

Mitigation: Review the authentication flow before logging in, and use an API key only with a service you trust.

Risk: The security guidance notes that broad trigger wording could activate for unrelated requests.

Mitigation: Invoke the skill only when image generation is intended.

## Reference(s):

- [CLI project (metadata homepage)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON result metadata]

**Output Format:** [Image assets returned with URLs in a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts and up to 10 reference images; generation can return asynchronously.]

## Skill Version(s):

1.3.40 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
