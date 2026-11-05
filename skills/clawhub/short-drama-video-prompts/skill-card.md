## Description:

把短剧分镜和冻结关键帧写成可直接复制的视频提示词 Markdown，也可按用户要求写时间线配乐/主题曲意图。用户提到文生/图生视频动作、人物表演、运镜、口型、环境运动、镜头时长、起止状态、把分镜转成视频提示词或写配乐提示词时使用；不生成媒体、不创作歌词、不改分镜边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和制作团队可用此技能把已确认的分镜、关键帧和声音要求整理成逐镜视频生成提示词，或按需撰写时间线配乐意图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A later media-generation step may send selected images, video, or audio to an external provider.

Mitigation: Review the proposed generation job and its selected media before confirming it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/short-drama-video-prompts)
- [生产提示词语法](artifact/references/production-prompt-grammar.md)
- [摄影与声音连续性](artifact/references/camera-audio-continuity.md)
- [目标模型能力档案](artifact/references/target-model-profile.md)
- [Seedance 视频生成 API](https://docs.volcengine.com/docs/82379/1520757)
- [MiniMax 视频生成 API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [Wan 3.0 视频生成 API](https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with per-shot copyable video prompts and optional timeline music direction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates prompt text and production guidance; does not generate media or lyrics.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
