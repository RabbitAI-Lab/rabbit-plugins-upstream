## Description:

面向语文老师的现代文阅读教学设计工具。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese language teachers use this skill to design modern-text reading lessons, guide text interpretation, select reading strategies, create staged reading tasks, and prepare teacher-confirmed reading-ability records.

### Deployment Geography for Use:

China Mainland by default; localize curriculum assumptions, consent rules, and crisis-contact guidance before student-facing use elsewhere.

## Known Risks and Mitigations:

Risk: The security review flags an access-scope mismatch around student and class weakness records.

Mitigation: Resolve the weaknessRank contract before installation: either add the read scope clearly with minimization and consent controls, or remove the prose instruction to read it.

Risk: Reading-performance records may expose sensitive student information if written or shared too broadly.

Mitigation: Use pseudonyms or seat IDs, keep only the minimum necessary reading-performance data, and require teacher confirmation before any record writeback.

Risk: AI-generated reading questions or exercises may be incorrect, misleveled, or unsupported by the source text.

Mitigation: Apply the bundled AI item self-check and label AI-generated items for manual teacher verification before classroom, homework, or resource-bank use.

Risk: Modern textbook, teaching-aid, or book excerpts may raise copyright issues if copied into outputs.

Mitigation: Require copyrightStatus on selected texts and keep restricted textbook or teaching-aid material as source indexes rather than reproduced full text.

Risk: Student reading reflections can contain crisis signals outside normal learning support.

Mitigation: Stop the teaching workflow when crisis signals appear, avoid diagnostic labels, direct the student to trusted adults or local emergency help, and record only the referral fact when permitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-reading-guide)
- [文本三解模板](references/text-three-solve.md)
- [阅读 6 大策略卡片](references/six-strategies-card.md)
- [群文阅读设计模板](references/group-text-design.md)
- [文本三解填写样板](references/three-solve-sample.md)
- [阅读策略使用样板](references/strategy-use-sample.md)
- [三阶练习设计填写样板](references/three-stage-practice-sample.md)
- [群文阅读童年议题样板](references/group-text-sample-childhood.md)
- [学员阅读力档案模板](references/reading-ability-profile-template.md)
- [班级教学工作区数据契约](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机例外](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown teaching designs, reading-analysis frameworks, discussion questions, task plans, and pending structured record entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before classroom use, resource-bank storage, parent-visible sharing, or student-record writeback.]

## Skill Version(s):

2.1.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
