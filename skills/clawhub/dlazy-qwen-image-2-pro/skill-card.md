## Description:

Helps agents create images from text prompts with Qwen Image 2 Pro through the dLazy service, including designs with detailed text and mixed Chinese-English layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent to generate images from text, optionally using reference images and layout or size preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Avoid submitting sensitive content without reviewing dLazy's data handling and account terms.

Risk: The third-party CLI may store a dLazy API key locally.

Mitigation: Review the pinned CLI package before installing and protect or revoke the API key as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns JSON containing hosted image URLs; the CLI can optionally save generated images locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
