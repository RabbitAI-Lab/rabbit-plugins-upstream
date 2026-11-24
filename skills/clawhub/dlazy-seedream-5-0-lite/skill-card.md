## Description:

Generate images with Doubao Seedream 5.0 Lite from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create images from text prompts or use reference images to guide image generation through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a mismatch between the image-generation purpose and login-only behavior, with incomplete coverage and medium confidence.

Mitigation: Before installation, check that the login behavior is expected, review the padded section of the Chinese-language file, and verify the referenced CLI package and any missing local paths.

Risk: Prompts and supplied local images are sent to dLazy hosted services for inference and media storage.

Mitigation: Do not submit sensitive prompts or images unless their use with the hosted service is allowed by your data-handling requirements.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link declared in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)

## Skill Output:

**Output Type(s):** [Images, JSON, Files]

**Output Format:** [Image assets and JSON responses containing generated image URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and up to 10 reference images; supports 2K or 3K resolution and several aspect ratios.]

## Skill Version(s):

1.3.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
