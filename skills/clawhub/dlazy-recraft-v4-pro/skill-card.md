## Description:

Generates high-resolution 4MP raster images from text prompts for print-ready and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to request 4MP raster images for print-ready materials and large-format designs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI and saving an API key locally exposes credentials if the environment is not trusted.

Mitigation: Review the CLI before installing; use the on-demand npx option and DLAZY_API_KEY if a persistent global binary or saved API key is undesirable.

Risk: Prompts and intentionally supplied local media are processed by the dLazy cloud service.

Mitigation: Send only prompts and files approved for third-party cloud processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and image-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns image URLs; optional CLI saving downloads the generated image.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
