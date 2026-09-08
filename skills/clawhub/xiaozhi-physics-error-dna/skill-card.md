## Description:

初中物理错题的根因分析与档案系统，做物理五维（图景/概念/公式/过程/数学工具）子类型定位与弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning assistants use this skill to diagnose recurring junior-secondary physics mistakes, classify them across five physics error dimensions, and produce weak-point records or reports with consent-aware data controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student learning profiles, parent sharing, reminders, and cross-skill writebacks could expose sensitive education data if consent controls are not enforced.

Mitigation: Deploy only on platforms that enforce consent bits and the handover schema server-side, and keep view, correction, deletion, pause, sharing, and export controls available to the student.

Risk: The bundled physics profile schema could be interpreted too broadly across adjacent physics skills.

Mitigation: Keep the profile schema narrowly scoped to physics error-DNA records and clarify boundaries with modeling, experiment, and concept-rebuild skills.

Risk: Weak-point summaries or monthly reports based on sparse records can overstate patterns.

Mitigation: Use the skill's confidence labels and sample-size warnings, and avoid historical counts when cross-session statistics are unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [物理错因维度表](artifact/references/physics-error-dimension-table.md)
- [物理高频概念混淆对照表](artifact/references/physics-concept-confusion-map.md)
- [物理数学工具自检清单](artifact/references/physics-math-tools-checklist.md)
- [四类物理图景绘制追问手册](artifact/shared/physics-diagram-guide.md)
- [档案结构 Schema](artifact/shared/dna-profile.schema.json)
- [交接协议 Schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown responses with structured JSON-compatible profile and handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include confidence labels, sample-size warnings, consent-gated profile updates, reminders, and student-facing weak-point summaries.]

## Skill Version(s):

2.1.12 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
