## Description:

Generates WeChat Official Account cover assets from an article or topic by selecting a visual direction, guiding image generation, adding Chinese title text, and producing wide, square, and dual-use formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jondeng11-creator](https://clawhub.ai/user/jondeng11-creator)

### License/Terms of Use:

MIT

## Use Case:

Content creators, publishers, and agent users use this skill to create WeChat article cover images from article drafts or topic descriptions. It supports cover planning, image-generation prompting, title overlay, format conversion, and delivery notes for publication workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cover generation can consume image-generation credits.

Mitigation: Use the skill when cover assets are intentionally needed and confirm the source article or topic before invoking image generation.

Risk: The skill writes generated cover files into an article or selected output folder, which can conflict with existing assets.

Mitigation: Use a dedicated output directory or check existing filenames before running the post-processing script.

## Reference(s):

- [WeChat Cover Rules](references/wechat-cover-rules.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [PNG image files, Markdown notes, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 900x383 wide, 1080x1080 square, and 900x383 dual-use cover variants from a 1:1 master image.]

## Skill Version(s):

1.1.0 (source: config.yaml and SKILL_SkillHub.md frontmatter; matches server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
