## Description:

Turns a product URL, script, or brief into a branded product-launch or promotional video using HyperFrames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to turn product websites, scripts, or briefs into launch videos, feature reveals, product demos, and site showcases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External HyperFrames commands can update global skills or install blocks during setup.

Mitigation: Review updates before running them and verify or pin the HyperFrames CLI and package source.

Risk: URL capture and media-service access can expose source material or credentials.

Mitigation: Use a sandboxed workspace, limit available secrets, and capture only approved URLs and assets.

Risk: Preview and render commands may start background processes and persist preferences.

Mitigation: Review the working environment and stored preferences before use, and stop background jobs when finished.

## Reference(s):

- [ClawHub product-launch-video release](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown plans and scripts, HTML frames, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation and delivery of a rendered MP4 video.]

## Skill Version(s):

1.0.54 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
