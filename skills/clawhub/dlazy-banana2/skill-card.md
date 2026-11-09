## Description:

Generate and edit high-quality images with Nano Banana 2.0 using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate or edit images by sending a prompt and, optionally, reference images to the dLazy hosted service. The skill returns generated image links and can save results to a local path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence is incomplete and reports a mismatch between the image-generation purpose and a login-only operation.

Mitigation: Review the referenced CLI and its authentication requirements before installing or using the skill.

Risk: Prompts and local reference files are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or images, and review dLazy's service terms before use.

Risk: The skill requires a dLazy API key, which is stored in the user's CLI configuration when using the login or auth commands.

Mitigation: Keep the key private and rotate or revoke it from the dLazy dashboard if it is exposed.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, URLs, JSON]

**Output Format:** [JSON result data with generated image URLs; image files can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and up to 14 reference images, with selectable aspect ratio and image size; asynchronous jobs can return a task identifier.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
