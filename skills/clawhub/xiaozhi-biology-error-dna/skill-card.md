## Description:

帮助初高中学生按六类生物学错因分析错题、定位薄弱知识点，并在需要时生成弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking middle- and high-school students use this skill to diagnose recurring biology mistakes and plan targeted practice. With the student's consent, it can track weak points in a learning profile and share summaries with related learning skills.

### Deployment Geography for Use:

Global (Chinese-language K12 learning; crisis referrals depend on location)

## Known Risks and Mitigations:

Risk: Persistent biology weak-point data and cross-skill summaries may disclose a student's learning history.

Mitigation: Review profile and sharing controls with the student or guardian; obtain consent before saving or sharing, and honor pause, deletion, and sharing restrictions.

Risk: Sparse or unavailable history may make a weak-point report misleading.

Mitigation: Report only supported observations, label small samples, and avoid precise historical counts without access to reliable records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [Biology error dimension table](artifact/references/biology-error-dimension-table.md)
- [Learning profile schema](artifact/shared/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational analysis and optional Markdown weak-point report; structured profile or handoff records when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile updates and sharing require consent; historical statistics depend on available records.]

## Skill Version(s):

2.4.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
