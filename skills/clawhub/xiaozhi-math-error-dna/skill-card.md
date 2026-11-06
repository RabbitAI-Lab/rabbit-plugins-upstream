## Description:

面向初高中学生分析数学错题根因与重复模式，并在获得同意后支持弱项追踪和按需月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

初高中学生可用此技能梳理数学错题的根因、识别反复出现的错误类型，并按需查看弱项趋势或生成月报。建立长期记录、跨技能共享或向家长分享须分别获得相应同意。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning records and parent-facing summaries can expose sensitive information about a student.

Mitigation: Choose profile storage, cross-skill sharing, parent summaries, and reminders separately; enable them only with the required consent, and review the host platform and companion skills first.

Risk: AI-generated practice items can contain errors.

Mitigation: Follow the bundled item-check process and verify generated items before presenting them to students or adding them to a resource bank.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Math error dimension table](artifact/references/math-error-dimension-table.md)
- [Concept confusion map](artifact/references/concept-confusion-map.md)
- [Reading habits](artifact/references/reading-habits.md)
- [Consent and platform conventions](artifact/shared/platform-conventions.md)
- [AI-generated item checks](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Chinese text and Markdown summaries or reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are generated on request; persistent records and cross-skill sharing require consent.]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
