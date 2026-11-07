## Description:

把短剧分镜和冻结关键帧写成可直接复制的视频提示词 Markdown，也可按用户要求写时间线配乐或主题曲意图；不生成媒体、不创作歌词、不改分镜边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

短剧编剧、导演和视频创作者可用此技能，将已确认的分镜与关键帧整理成逐镜、可直接复制的视频生成提示词，并按需编写时间线配乐意图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 提示词中的语言要求可能不适合使用者的项目或受众。

Mitigation: 执行前检查语言要求，并按项目需要调整提示词语言。

Risk: 使用参考媒体时，素材可能需要发送给外部视频生成服务。

Mitigation: 提交前确认素材适合分享给所选服务，并遵循项目的素材处理要求。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-video-prompts)
- [目标模型能力档案](references/target-model-profile.md)
- [运动提示词配方](references/motion-recipe.md)
- [生产提示词语法](references/production-prompt-grammar.md)
- [表演与动作时序](references/performance-action-timing.md)
- [摄影与声音连续性](references/camera-audio-continuity.md)
- [交付形态](references/delivery-profile.md)
- [可生成性](references/generability.md)
- [审查与示例](references/review-and-fixtures.md)
- [Seedance 2.0 方言](references/seedance-2.0.md)
- [Seedance 2.5 方言](references/seedance-2.5.md)
- [MiniMax H3 方言](references/minimax-h3.md)
- [Wan 3.0 方言](references/wan-3.0.md)
- [MiniMax H3 视频生成 API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [Seedance 视频生成 API](https://docs.volcengine.com/docs/82379/1520757)
- [Wan 3.0 视频生成 API](https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [中文 Markdown 文档，包含逐镜视频生成提示词和可选的时间线配乐意图]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [提示词遵循已选模型档案与项目语言；不生成媒体或创作歌词。]

## Skill Version(s):

1.0.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
