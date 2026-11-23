## Description:

Generate or edit images with Nano Banana Pro using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the skill to create images from text prompts or edit images using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan does not establish what the CLI login step authorizes or why it is needed for image generation.

Mitigation: Before running dlazy login, review its purpose and proceed only if you are comfortable with the account access it requests.

Risk: Prompts and local reference images are sent to dLazy hosted services for processing.

Mitigation: Avoid submitting sensitive prompts or images unless you are comfortable with their handling by the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI source link declared in skill metadata (not verified provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files or hosted image URLs, with a JSON result/status payload.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and optional reference images; supports aspect ratio and 1K, 2K, or 4K size settings.]

## Skill Version(s):

1.2.47 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
