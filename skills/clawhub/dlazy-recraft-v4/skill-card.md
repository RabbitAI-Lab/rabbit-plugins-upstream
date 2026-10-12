## Description:

Generates 1MP raster images from prompts using Recraft V4 through dLazy for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate raster images from text prompts and iterate on visual ideas with selectable aspect ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly provided for generation may be sent to dLazy; generated files are hosted by dLazy.

Mitigation: Avoid submitting sensitive prompts or files, and review dLazy's service terms before use.

Risk: The CLI may store a dLazy API key locally.

Mitigation: Use a per-invocation key if preferred, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source (skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Image URLs, JSON]

**Output Format:** [JSON response with a generated image URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratios and asynchronous generation.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
