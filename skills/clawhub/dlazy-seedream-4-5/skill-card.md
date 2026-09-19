## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to call dLazy's hosted Seedream 4.5 image generation service for text-to-image and image-to-image tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected input files, generated outputs, and API usage are handled by dLazy's hosted service.

Mitigation: Avoid sending sensitive prompts or files, review dLazy's service terms, and use an appropriate dLazy organization API key.

Risk: The skill installs or invokes an external @dlazy/cli package.

Mitigation: Review the external package before installing and use the pinned npx invocation when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as hosted URLs and may be saved locally with the CLI.]

## Skill Version(s):

1.3.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
