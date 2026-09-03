## Description:

Generate exquisite images with Kling o1 model, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate images through dLazy's hosted Kling o1 workflow from text prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local image paths can be sent to dLazy services for hosted generation.

Mitigation: Avoid confidential prompts or files unless the user trusts dLazy's retention and privacy practices.

Risk: The CLI may store an API key in the user's local configuration.

Mitigation: Use environment variables, npx, dry-run, and key rotation or revocation when reducing persistence or exposure is important.

Risk: API calls can consume dLazy credits and may fail when credits are insufficient.

Mitigation: Use dry-run where appropriate and confirm account balance before running costly generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing generated image output URLs, with optional local image file output when saved by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with --no-wait; local image inputs may be uploaded to dLazy media storage.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
