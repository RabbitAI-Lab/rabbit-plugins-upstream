## Description:

Generates images from text prompts using Qwen Image 2 Pro through the dLazy service, with optional reference images and support for mixed Chinese and English text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images and mixed-language text-and-image designs from prompts, optionally supplying reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly supplied to the skill are sent to dLazy's hosted service, and generated assets are hosted there.

Mitigation: Send only content you are comfortable sharing with dLazy and review files before supplying them.

Risk: Signing in can save an API key locally, and global installation keeps the CLI on the system.

Mitigation: Use a per-invocation API key and the pinned npx command if you prefer not to store a key or install the CLI globally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown guidance and JSON results containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted by dLazy and can optionally be downloaded locally.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
