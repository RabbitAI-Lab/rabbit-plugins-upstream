## Description:

根据小说信息设计封面提示词，并按需生成与导出小说封面图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

小说作者和创作者可用它根据书名、笔名、题材和发布平台设计封面提示词；需要成图时生成并按平台规格导出封面。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpublished book details or reference images may be sent to the configured image provider during image generation.

Mitigation: Share only material the author is comfortable sending to the selected provider.

Risk: The security review was partial because a local path referenced by the skill was unavailable for checking.

Mitigation: Review the unavailable referenced material when it is available.

## Reference(s):

- [小说封面视觉风格库](references/cover-styles.md)
- [API 回退生图](references/api-fallback.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-cover)

## Skill Output:

**Output Type(s):** [Text, Image files]

**Output Format:** [Chinese-language cover prompts and generated PNG cover images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include saved image paths, platform-sized exports, and a brief visual quality check.]

## Skill Version(s):

1.1.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
