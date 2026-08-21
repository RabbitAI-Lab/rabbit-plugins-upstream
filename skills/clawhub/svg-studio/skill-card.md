## Description:

SVG Studio guides an agent to author SVG images, render them to PNG or HTML, and compose animated outputs such as GIF, APNG, WebP, and MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to create precise vector illustrations, posters, charts, diagrams, icons, and animations when text, numbers, aspect ratio, and editability matter. It is especially useful when the agent lacks multimodal image generation or needs deterministic SVG, PNG, HTML, or animated file outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The renderer may automatically create a local Python environment and install packages whose versions are not pinned by the release evidence.

Mitigation: Deploy in a constrained workspace and consider preinstalling or pinning the required renderer dependencies before use.

Risk: The skill runs local rendering tools, including headless browser or SVG conversion engines, against generated SVG content.

Mitigation: Review SVG content from untrusted prompts before rendering and restrict file-system access to the project workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dqsjqian/skills/svg-studio)
- [SVG Techniques Reference](references/svg-techniques.md)
- [Hand-Drawn Infographic Reference](references/handdrawn-infographic.md)
- [SVG Animation Reference](references/animation.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with SVG or HTML code blocks and shell commands; generated file artifacts may include SVG, PNG, GIF, APNG, WebP, MP4, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images should be visually reviewed after rendering, especially for text layout, fonts, backgrounds, and animation behavior.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
