## Description:

Adapts web novels into webtoon plot breakdowns and episode scripts, with a separate workflow for dLazy-assisted image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and webtoon creators use this skill to turn novel chapters into episode outlines and scripts in Chinese. The skill also describes an image-generation workflow using the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image workflow may install or run the dLazy CLI and store an API key locally.

Mitigation: Review the CLI before use; prefer npx or a limited environment to avoid a global installation, and protect the local API key.

Risk: Prompts are sent to dLazy services, and user-provided media paths may be uploaded.

Mitigation: Avoid sensitive prompts, files, local paths, or credentials unless you trust the dLazy service and CLI package.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image links]

**Output Format:** [Chinese-language Markdown with episode outlines and scripts; optional image-generation commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Episode-by-episode structure with plot points, visual cues, and cliffhangers.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
