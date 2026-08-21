## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images through the dLazy hosted Seedream 4.5 service from text prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the skill are sent to dLazy cloud endpoints.

Mitigation: Use the skill only when the user intends to use dLazy Seedream 4.5, and avoid submitting confidential prompts or media unless the account and service terms permit that use.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Prefer user-scoped credentials, use the DLAZY_API_KEY environment variable for per-invocation access when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Generic image-generation trigger phrases could route ordinary image requests to this provider.

Mitigation: Invoke by the dLazy provider and Seedream 4.5 model name when this specific service is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects containing generated image URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local image paths may be uploaded to dLazy media storage for image-to-image generation.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
