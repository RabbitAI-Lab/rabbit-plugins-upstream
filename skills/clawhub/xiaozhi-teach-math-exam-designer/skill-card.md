## Description:

Helps Chinese-language middle and high school math teachers plan assessment blueprints, select and label candidate questions, and review item-level statistics before teacher-approved record updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use this skill to draft assessment blueprints and candidate items for Chinese middle and high school courses, then examine item difficulty, discrimination, and reliability. Teachers verify questions and approve each update to classroom records; the skill does not grade students or make individual diagnoses.

### Deployment Geography for Use:

Global (designed around Chinese-language school math curricula and local examination requirements)

## Known Risks and Mitigations:

Risk: Classroom records could expose student-level information beyond the assessment task.

Mitigation: Limit access to needed fields and tier counts, not per-student tier identities; enforce consent checks before sharing.

Risk: Unverified candidate questions or incorrect item statistics could affect assessment quality.

Mitigation: Have teachers check generated items, calculations, and source attribution before use or record updates.

Risk: Premature disclosure of confidential examination questions or unauthorized reuse of copyrighted items.

Mitigation: Do not provide unreleased examination materials; check permissions and label item sources before reuse.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Assessment blueprint template](references/blueprint-template.md)
- [Assessment design process](references/exam-design-process.md)
- [Item statistics and results rubric](references/result-analysis-rubric.md)
- [AI-generated item checks](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown]

**Output Format:** [Chinese-language text and Markdown tables for assessment blueprints, candidate questions, and item-level statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate questions require teacher verification; classroom record updates require teacher confirmation.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
