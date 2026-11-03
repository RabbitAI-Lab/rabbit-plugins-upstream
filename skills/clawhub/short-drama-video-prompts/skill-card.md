## Description:

将已确认的短剧分镜和关键帧整理为可复制的视频提示词，并可按需编写时间线音乐意图；不生成媒体或歌词，也不更改镜头边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

短剧创作者和制作团队可用它把已确认的分镜、关键帧与声音要求写成逐镜视频提示词；需要时也可整理配乐或主题曲的时间线意图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts may contain minor language or workflow inconsistencies.

Mitigation: Review the generated language and require upstream acceptance of shot-boundary changes.

Risk: Images, recordings, or scripts used in separate media generation may be shared with the provider.

Mitigation: Check the exact job and confirm whether its inputs may be shared with the provider before generating media.

Risk: Companion production skills and the referenced checker are not bundled or assessed here.

Mitigation: Assess those companion tools separately before relying on them.

## Reference(s):

- [目标模型能力档案](artifact/references/target-model-profile.md)
- [运动提示词配方](artifact/references/motion-recipe.md)
- [生产提示词语法](artifact/references/production-prompt-grammar.md)
- [摄影与声音连续性](artifact/references/camera-audio-continuity.md)
- [交付形态](artifact/references/delivery-profile.md)
- [Seedance 2.0 提示词指南](artifact/references/seedance-2.0.md)
- [Seedance 2.5 提示词指南](artifact/references/seedance-2.5.md)
- [MiniMax H3 提示词指南](artifact/references/minimax-h3.md)
- [Wan 3.0 提示词指南](artifact/references/wan-3.0.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [逐镜视频提示词文档，可选时间线配乐或主题曲意图章节]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [文本输出；不生成媒体或歌词，并保留已确认的镜头边界。]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
