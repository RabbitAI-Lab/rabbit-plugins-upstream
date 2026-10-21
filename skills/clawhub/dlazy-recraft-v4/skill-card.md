## Description:

Generates 1MP raster images with Recraft V4 for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate raster images from text prompts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to dLazy cloud services.

Mitigation: Avoid submitting sensitive prompts or files without approval.

Risk: The external dLazy CLI stores an API key locally.

Mitigation: Review the CLI before installation, use the on-demand pinned package if preferred, and rotate or revoke the key when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can also be saved locally on request.]

## Skill Version(s):

1.3.32 (source: ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
