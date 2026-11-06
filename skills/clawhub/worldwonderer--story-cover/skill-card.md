## Description:

帮助小说作者设计封面提示词，并按需生成和导出适配目标平台的封面图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

小说作者可根据书名、笔名和题材制作封面提示词，并在需要时生成、检查和导出平台适配的封面图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating a cover shares the title, pen name, story-derived prompt, and any reference image with the selected provider; provider-side data handling was not assessed.

Mitigation: Use prompt-only mode for sensitive drafts, share only material suitable for the selected provider, and use a custom API endpoint only when it is trusted.

Risk: The output folder retains prompt and reference records, and API image generation may incur charges.

Mitigation: Review access to the output folder before sharing it, and consider API costs before generating images.

## Reference(s):

- [ClawHub release: story-cover](https://clawhub.ai/worldwonderer/skills/story-cover)
- [Cover style guide](references/cover-styles.md)
- [Image API fallback guide](references/api-fallback.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image files]

**Output Format:** [Image-generation prompts in text or Markdown; generated cover images as PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-sized exports and quality-check notes.]

## Skill Version(s):

1.1.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
