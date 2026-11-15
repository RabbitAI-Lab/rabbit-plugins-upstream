## Description:

Generate and edit high-quality images with Nano Banana 2.0 from text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts or edit images using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review did not establish the behavior of the `dlazy login` authentication flow.

Mitigation: Review the CLI login flow and account requirements before authenticating; use an API key that can be rotated or revoked.

Risk: Prompts and local reference images are sent to dLazy-hosted services for generation or editing.

Mitigation: Avoid submitting sensitive prompts or images unless your organization approves the service's data handling.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing generated image URLs or an asynchronous task identifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image files can be saved locally with the CLI; asynchronous tasks can return before image generation is complete.]

## Skill Version(s):

1.3.40 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
