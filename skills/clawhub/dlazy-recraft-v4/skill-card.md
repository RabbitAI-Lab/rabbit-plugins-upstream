## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to generate 1MP raster images through the dLazy hosted Recraft V4 service from text prompts and aspect-ratio parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and any referenced local media files to the dLazy hosted service for image generation.

Mitigation: Avoid sending sensitive content unless the deployment has reviewed the dLazy service terms and data-handling requirements.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate on shared machines, keep local file permissions restricted, and rotate or revoke keys if a machine is shared or compromised.

Risk: The skill depends on installing or running the pinned @dlazy/cli package.

Mitigation: Review the linked dLazy CLI source or npm package before installing in sensitive environments and avoid running npm installs with elevated privileges.

## Reference(s):

- [图像生成 Recraft V4 on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses that reference generated image URLs or saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are hosted on files.dlazy.com unless saved locally with the CLI.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
