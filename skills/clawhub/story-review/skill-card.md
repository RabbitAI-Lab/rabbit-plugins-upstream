## Description:

为中文小说提供多视角的结构、人物、文字与设定审查，并在审稿助手不可用时改用单人审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

小说作者和编辑用它审查章节或整部作品，获取有原文依据、按严重程度整理的修改建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review may read private manuscript and planning files.

Mitigation: Limit access to the intended project and review the selected files before running.

Risk: Full and lean reviews may update project-local tracking files; batch reviews may save review state.

Mitigation: Back up tracking data before review, or choose solo mode to avoid tracking-file maintenance.

## Reference(s):

- [通用网文内容审查标准](references/quality-rubric.md)
- [叙事逻辑审查参考](references/story-logic.md)
- [平台审查标准：知乎](references/rubrics/zhihu.md)
- [平台审查标准：番茄](references/rubrics/fanqie.md)
- [平台审查标准：起点](references/rubrics/qidian.md)
- [Publisher-provided source link (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with cited findings and revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are grouped by severity; the skill does not rewrite story prose.]

## Skill Version(s):

1.1.37 (source: server release; artifact frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
