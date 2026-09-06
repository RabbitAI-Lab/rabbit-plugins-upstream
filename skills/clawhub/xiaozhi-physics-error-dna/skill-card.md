## Description:

Analyzes middle-school physics mistakes into physics-specific error dimensions, subtype labels, weak-point profiles, and student-facing reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and education agents use this skill to identify recurring root causes in middle-school physics mistakes, distinguish physics-picture issues from concept, formula, process, and math-tool errors, and produce weak-point summaries or monthly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records and analyzes student learning-profile data.

Mitigation: Deploy only with clear student and guardian consent requirements, profile deletion/export controls, and cross-skill or parent-sharing controls enabled.

Risk: A student may express self-harm, severe distress, bullying, or other crisis signals while discussing physics anxiety.

Mitigation: Stop the tutoring and profile-analysis flow, state the AI boundary, and route the student to trusted adults and localized crisis-support channels.

Risk: Weak-point conclusions may be misleading when based on too few mistakes or unavailable history.

Mitigation: Mark conclusions as sample-insufficient when data is limited and avoid historical counts unless the platform provides them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [物理错因维度表](references/physics-error-dimension-table.md)
- [物理高频概念混淆对照表](references/physics-concept-confusion-map.md)
- [物理数学工具自检清单](references/physics-math-tools-checklist.md)
- [四类物理图景绘制追问手册](shared/physics-diagram-guide.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text, with JSON-compatible profile and handover fields when records are stored by the platform.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable payloads; long-term profiles, reminders, and parent-facing summaries depend on consent and available platform memory.]

## Skill Version(s):

2.1.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
