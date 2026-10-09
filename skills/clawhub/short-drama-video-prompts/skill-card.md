## Description:

将已确认的短剧分镜与关键帧转为逐镜可复制的视频提示词，并按需编写时间线配乐或主题曲意图，不生成媒体或歌词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和制作团队使用已确认的分镜、关键帧与模型档案，编写镜头动作、表演、运镜和声音的视频提示词；需要时补充时间线配乐意图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboards, keyframes, and specifications may contain sensitive project material.

Mitigation: Review source access and generated prompts before sharing them outside the production team.

Risk: Local checks do not establish that prompts will generate usable media.

Mitigation: Confirm reference images and target-model constraints, then have a creator review the output before production.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-video-prompts)
- [Motion prompt recipe](artifact/references/motion-recipe.md)
- [Target model profile](artifact/references/target-model-profile.md)
- [Video prompt output template](artifact/assets/video-prompts.md)
- [Timeline music specification](artifact/assets/music-spec.jsonl.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSONL, Guidance]

**Output Format:** [Per-shot Markdown prompts and optional timeline music JSONL specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follows confirmed shot boundaries and target-model capabilities; does not generate video, audio, or lyrics.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
