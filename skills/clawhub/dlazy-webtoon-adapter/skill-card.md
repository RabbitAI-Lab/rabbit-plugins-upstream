## Description:

Adapts web novels into Chinese-language webtoon plot breakdowns and episode scripts, with optional dLazy cloud image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creative teams use this skill to turn web-novel chapters into episodic webtoon outlines and scripts; its additional CLI instructions support cloud image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes webtoon writing with cloud image generation, so its actual scope may exceed the expected writing workflow.

Mitigation: Review the image-generation instructions and enable the CLI only if that additional capability is wanted.

Risk: The image-generation CLI sends prompts and supplied media to dLazy services, including uploads of local media files.

Mitigation: Avoid providing sensitive prompts or media paths unless uploading that content to dLazy is acceptable.

Risk: Global CLI installation and locally stored API keys create persistent software and credential state.

Mitigation: Review the CLI package before installation; consider npx and a per-run DLAZY_API_KEY instead of a global installation or saved key.

Risk: The ClawHub release, embedded skill definitions, and CLI install statements specify conflicting versions.

Mitigation: Resolve the version mismatch and confirm the intended CLI package version before running commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source linked in skill metadata (not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Chinese-language Markdown and CLI guidance, with image links when generated]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plot breakdowns, episode scripts, and optional image-generation prompts.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; embedded frontmatter reports 1.3.5 and 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
