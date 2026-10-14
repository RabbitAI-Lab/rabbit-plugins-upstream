## Description:

Generates 1MP raster images from text prompts for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate raster images from prompts and iterate on visual concepts with selectable aspect ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy services.

Mitigation: Review prompts and files before submission; avoid sensitive content unless approved for the service.

Risk: Installing the CLI and logging in can leave a global package and a saved API key.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before use; use npx or a per-invocation API key if you prefer not to keep a global install or saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI repository (skill metadata link; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs]

**Output Format:** [JSON response with image URL; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [1MP raster output; asynchronous requests may initially return a generation ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
