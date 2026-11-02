## Description:

把短剧分镜和冻结关键帧写成可直接复制的视频提示词 Markdown，也可按用户要求写时间线配乐/主题曲意图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers and creative teams use this skill to turn approved short-drama storyboards and keyframes into shot-bounded, copy-ready video prompts, or to draft timeline music intent when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous prompt or spoken-dialogue language, or an unreviewed storyboard revision, can lead to prompts that diverge from the creator's intent.

Mitigation: Specify prompt and spoken-dialogue languages, and review proposed storyboard changes before accepting the draft.

Risk: A user may mistake prompt drafting for media generation.

Mitigation: Use this skill for text drafting; handle actual media generation as a separate workflow with confirmation of the exact job.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-video-prompts)
- [Production prompt grammar](artifact/references/production-prompt-grammar.md)
- [Target model capability profile](artifact/references/target-model-profile.md)
- [Motion recipe](artifact/references/motion-recipe.md)
- [Performance and action timing](artifact/references/performance-action-timing.md)
- [Generability guidance](artifact/references/generability.md)
- [Seedance video generation API](https://docs.volcengine.com/docs/82379/1520757)
- [Seedance prompt guide](https://docs.volcengine.com/docs/82379/2607689)
- [MiniMax H3 prompt writing guide](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt)
- [MiniMax video generation API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [Wan 3.0 video generation API](https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copy-ready video prompts and, when requested, timeline music intent; does not generate media or write lyrics.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
