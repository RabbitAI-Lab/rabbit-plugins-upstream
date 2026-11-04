## Description:

多视角对抗式审查。full/lean 模式在已部署 reviewer agents 时并行 spawn；缺失/异常 agents 或 spawn 失败时自动降级 solo，参考文件不可读时使用内置 rubric fallback。触发方式：/story-review、/审查、「审查一下」「帮我审一下」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

小说作者可用此技能从结构、角色、文字和设定等角度审查章节，并获得带有原文依据的修改建议，帮助发现影响故事连贯性和阅读体验的问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full and lean reviews can change saved continuity records without asking for approval.

Mitigation: Back up the book and approve proposed tracking changes before full or lean reviews; use solo mode to avoid automatic tracking changes.

Risk: Deployed reviewer agents and companion writing tools can affect review results or make additional changes.

Mitigation: Review the deployed reviewer agents and companion writing tools separately before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-review)
- [Quality rubric](references/quality-rubric.md)
- [Solo review guidance](references/solo.md)
- [Project link declared in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with quoted evidence and revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are prioritized by severity; full and lean reviews may save local continuity-tracking progress.]

## Skill Version(s):

1.1.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
