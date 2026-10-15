## Description:

Generates 2K, 3K, or 4K images from text prompts and optional reference images through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution key visuals, posters, and print-ready imagery from prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected reference media are sent to the third-party dLazy service.

Mitigation: Use only prompts and reference files you are comfortable sharing with dLazy; verify you trust the service before installing.

Risk: CLI login can save a dLazy API key in local configuration.

Mitigation: Use an on-demand npx invocation and DLAZY_API_KEY for less persistent local setup; protect any stored key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include generated image URLs; optional --save downloads an image locally.]

## Skill Version(s):

1.2.25 (source: ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
