## Description:

将已确认的短剧分镜和关键帧整理为逐镜视频生成提示词，并可按需编写时间线配乐意图；不生成媒体或歌词，也不更改分镜边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和视频制作人员可将已确认的分镜与关键帧转换为逐镜、可复制的视频提示词，也可整理跨镜头的时间线配乐意图。该技能用于准备提示词，不负责生成媒体、创作歌词或更改已确认的分镜边界。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 生成的提示词、语言或对白可能不准确，或不适合目标视频模型。

Mitigation: 执行前核对提示词与对白，尤其检查 Seedance 2.0 的语言和对白内容。

Risk: 项目文件访问或后续外部生成可能超出当前提示词准备任务的范围。

Mitigation: 仅访问相关项目脚本和参考素材；外部媒体生成应走独立流程并取得明确确认。

## Reference(s):

- [目标模型档案](references/target-model-profile.md)
- [提示词语法](references/production-prompt-grammar.md)
- [镜头与音频连续性](references/camera-audio-continuity.md)
- [表演与动作时序](references/performance-action-timing.md)
- [交付配置](references/delivery-profile.md)
- [审查与测试样例](references/review-and-fixtures.md)
- [Seedance 2.0 指南](references/seedance-2.0.md)
- [Seedance 2.5 指南](references/seedance-2.5.md)
- [MiniMax H3 指南](references/minimax-h3.md)
- [Wan 3.0 指南](references/wan-3.0.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [逐镜视频提示词文档；可选时间线配乐意图章节]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [引用已确认的镜头边界与参考素材；不生成媒体或歌词。]

## Skill Version(s):

1.0.9

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
