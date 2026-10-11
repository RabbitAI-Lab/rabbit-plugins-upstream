## Description:

Helps agents generate images with Qwen Image 2 Pro through the dLazy CLI, including designs with complex text and layout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request images from text prompts, optionally supplying reference images for text-heavy or mixed-media designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication requires a dLazy API key that may be saved locally by the CLI.

Mitigation: Protect the local CLI configuration and rotate or revoke the key through dLazy if needed.

Risk: Prompts are sent to dLazy; local media explicitly supplied for generation is uploaded.

Mitigation: Only submit prompts and media you are comfortable sharing with the service.

Risk: A global CLI install persists on the device.

Mitigation: Review the CLI before installation, or use the documented npx option for on-demand execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON result guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results contain image URLs; generated files can be downloaded on request.]

## Skill Version(s):

1.3.27 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
