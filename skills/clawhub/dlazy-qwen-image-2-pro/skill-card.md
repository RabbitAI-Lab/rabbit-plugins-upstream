## Description:

Generates images with Alibaba Bailian's Qwen Image 2.0 Pro, with support for complex text rendering, multilingual layouts, photorealistic detail, and semantic adherence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts, optionally with reference images, and retrieve or save the resulting image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review could not resolve several references or inspect the CLI package used by the skill.

Mitigation: Review the pinned CLI installation and login steps, and confirm you trust the CLI package and dLazy service before use.

Risk: The CLI stores an API key in the local user configuration when you log in or set a key.

Mitigation: Use a trusted device, protect access to your user account, and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [CLI repository link listed in skill metadata (release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON response with generated image URLs and task status; optionally a saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to three reference images; supports five image sizes.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
