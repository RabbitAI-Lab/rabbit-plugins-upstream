## Description:

数学测评设计帮助数学教师用双向细目表规划测评目标、题目覆盖、难度梯度和考后逐题统计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 math teachers use this skill to design diagnostic, formative, and summative math assessments, prepare blueprint tables, label item sources, and summarize item-level statistics for teacher review. It is scoped to assessment design and item statistics, not student ranking, diagnosis, remediation planning, grading, or parent communication.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The security review reports that the data contract gives the skill and downstream handoffs more student assessment data access than the stated limits justify.

Mitigation: Require a platform-enforced projection that exposes only the fields needed for assessment design, such as aggregate tier counts and relevant knowledge-point names.

Risk: Cross-skill handoffs could share assessment data beyond the intended task boundary.

Mitigation: Check crossSkillSharing and related consent flags before handoff, and pass only the minimum fields named for the receiving skill.

Risk: The distributed schema and the stated write-back behavior are not fully aligned.

Mitigation: Align the schema with the write-back fields before persistent storage, or keep write-back outputs session-only until the schema authorizes those writes.

Risk: The skill is localized for Mainland China curriculum, consent defaults, and emergency-resource behavior.

Mitigation: Before use elsewhere, localize curriculum assumptions, consent handling, and emergency-resource guidance for the target region.

Risk: Candidate AI-generated math items or copied source items may be incorrect or unsuitable for reuse.

Mitigation: Require item self-checks, teacher verification, and the declared copyright status before any item enters a worksheet, exam, or resource library.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [双向细目表模板](references/blueprint-template.md)
- [数学测评设计流程](references/exam-design-process.md)
- [数学测评题目统计模板](references/result-analysis-rubric.md)
- [测评题目统计报告模板（班级）](references/class-report-sample.md)
- [测评统计卡模板（学员）](references/student-report-sample.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [班级教学工作空间 Schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese Markdown tables, reports, and JSON-compatible workspace field proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are draft assessment artifacts and statistics for teacher confirmation; AI-generated item candidates must be labeled and manually verified before use.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
