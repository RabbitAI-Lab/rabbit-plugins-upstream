## Description:

1MP raster image generation with refined design judgment, suitable for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to call dLazy's Recraft V4 image generation workflow from a shell-driven agent environment and save or reference generated raster images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes a pinned external npm CLI that calls a hosted cloud API.

Mitigation: Review the @dlazy/cli package or source before installation in sensitive environments, and prefer npx or a non-privileged install when possible.

Risk: Prompts, parameters, and any local files passed to media fields are sent to dLazy services for generation.

Mitigation: Only pass prompts and files intended for upload to dLazy, and avoid including confidential data unless approved for that service.

Risk: The skill requires and may save a dLazy API key in local configuration.

Mitigation: Treat the API key as a credential, restrict local access, and rotate or revoke it from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated image output URLs, and can save generated assets to a local path when requested.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
