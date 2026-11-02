## Description:

Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT

## Use Case:

People creating visual summaries use this skill to turn an article, document, URL, or topic into a professional infographic, with options for layout, visual style, aspect ratio, and language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source material may contain confidential information that is sent to OpenRouter and the selected model provider.

Mitigation: Review prompts and source content before generation; do not rely on secret-stripping instructions as an automated redaction guarantee.

Risk: Image generation and retries may incur charges, and source copies and backups remain locally.

Mitigation: Consider model costs before generating and review local working files and backups after use.

Risk: Documented OpenCode-specific paths may need adjustment when using OpenClaw.

Mitigation: Adapt those paths to the OpenClaw environment before running the workflow.

## Reference(s):

- [Upstream project reference listed in metadata](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Layout definitions](artifact/references/layouts/)
- [Style definitions](artifact/references/styles/)

## Skill Output:

**Output Type(s):** [Images, Markdown, Guidance]

**Output Format:** [PNG infographic image with Markdown analysis, structured content, and generation prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Layout and style are selectable; aspect ratio and language can be specified.]

## Skill Version(s):

1.56.1 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
