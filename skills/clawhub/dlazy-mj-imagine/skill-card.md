## Description:

Helps agents create stylized images from prompts using dLazy's Midjourney-style image generation, with aspect-ratio, bot-type, and grid or upscale options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request artistic, strongly stylized images through the dLazy CLI and retrieve generated image links or saved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected local media inputs, and generated outputs are handled by dLazy's hosted service.

Mitigation: Review what you submit and avoid sharing sensitive prompts or media without authorization.

Risk: The CLI stores a dLazy API key on the user's machine.

Mitigation: Use a trusted machine and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Using the skill requires installing or running a third-party CLI package.

Mitigation: Review the pinned @dlazy/cli package before installing it.

## Reference(s):

- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text]

**Output Format:** [CLI commands and JSON responses containing generated image URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be saved as local image files using the CLI.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
