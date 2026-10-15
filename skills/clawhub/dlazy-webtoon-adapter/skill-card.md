## Description:

Adapts web novels into Chinese-language webtoon plot breakdowns and episode scripts, with optional dLazy image-generation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creative teams use this skill to turn web-novel chapters into plot outlines, episode assignments, and visual-first webtoon scripts; its optional image workflow uses dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths supplied to the dLazy CLI may be sent to dLazy services.

Mitigation: Review inputs and command previews; avoid sensitive prompts and local file paths before approving a call.

Risk: dLazy API keys may persist in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per run when persistence is unwanted, and rotate or revoke keys as needed.

Risk: The image-generation requirement broadens this writing skill's scope, and its documented install versions conflict.

Mitigation: Use the CLI only when image generation is intended; review its package/source and resolve the version mismatch before global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Chinese-language Markdown outlines and scripts, with optional command previews and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Episode scripts target 500–800 Chinese characters each; the skill also requests user confirmation before image generation.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; embedded versions differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
