## Description:

Generates high-resolution 4MP raster images from text prompts for print and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, creators, and developers use this skill to request high-resolution images through the dLazy service for print and large-format projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided files are sent to a third-party cloud service; generated images are hosted there.

Mitigation: Avoid submitting sensitive prompts or files unless their upload and hosting are intended.

Risk: The npm CLI can be installed globally, and login saves an API key locally.

Mitigation: Use the pinned on-demand npx invocation if a persistent global installation is undesirable, and protect the local API key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing a hosted PNG image URL; an optional flag saves the image locally.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
