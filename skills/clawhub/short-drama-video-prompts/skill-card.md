## Description:

把已确认的短剧分镜和冻结关键帧整理成可复制的视频提示词，并可按需编写时间线配乐意图；不生成媒体或歌词，也不改动分镜边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向短剧创作者与视频制作团队，用于依据已确认的镜头边界和关键帧撰写可直接复制的视频生成提示词，并在需要时规划时间线配乐意图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project language, target-model dialect, or storyboard-boundary requirements may differ from the skill's prompt rules.

Mitigation: Before use, confirm the project's prompt language and target model, then check prompts against accepted shot boundaries.

Risk: Security scan coverage is partial, so some referenced local guidance may not be represented in the scan evidence.

Mitigation: Confirm referenced files are present and review the relevant guidance before adopting the workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-video-prompts)
- [Target model capability profile](references/target-model-profile.md)
- [Production prompt grammar](references/production-prompt-grammar.md)
- [Performance and action timing](references/performance-action-timing.md)
- [Review and fixtures](references/review-and-fixtures.md)
- [Seedance video generation API](https://docs.volcengine.com/docs/82379/1520757)
- [Seedance prompt guide](https://docs.volcengine.com/docs/82379/2607689)

## Skill Output:

**Output Type(s):** [Text, Markdown, Prompt guidance]

**Output Format:** [Copy-ready video prompt Markdown, with timeline music intent when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follows accepted shot boundaries and keyframes; does not generate media or lyrics.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
