## Description:

A Chinese-language middle-school physics lesson-planning skill that helps teachers draft concept-centered lesson plans with lesson segments, questioning chains, differentiation, model-building, application practice, and classroom-summary structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External middle-school physics teachers use this skill to draft Chinese-language physics lesson plans for concept construction, law teaching, model building, application practice, and classroom summaries. It is intended for teacher-reviewed drafts, not direct classroom execution or full experiment procedure design.

### Deployment Geography for Use:

Mainland China; use outside mainland China requires localization of curriculum assumptions, emergency referral guidance, privacy and consent rules, and classroom safety rules.

## Known Risks and Mitigations:

Risk: Lesson plans may contain incorrect, incomplete, or classroom-inappropriate teaching guidance if used without teacher review.

Mitigation: Treat outputs as drafts and require the teacher to review objectives, examples, timing, question chains, and generated items before classroom use.

Risk: Experiment content in a lesson draft may be mistaken for a complete operating procedure.

Mitigation: Keep experiment sections at the lesson-design level, include safetyLevel labels, and route real equipment, operation, and safety procedures to the dedicated experiment-coach skill or school lab policy.

Risk: Use outside mainland China may expose mismatched curriculum, privacy, consent, classroom-safety, or emergency-referral assumptions.

Mitigation: Localize curriculum references, privacy and consent rules, emergency referral guidance, and lab-safety expectations before deployment outside mainland China.

Risk: Class-profile memory can include sensitive classroom observations or student-related teaching records.

Mitigation: Use pseudonyms or seat numbers, respect view/correct/delete/export and sharing controls, and avoid storing unnecessary sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-lesson-planner)
- [Initial physics concepts map](artifact/references/physics-concepts-map.md)
- [Middle-school physics model examples](artifact/references/model-examples.md)
- [Lesson-plan experiment-slot template](artifact/references/lab-design-template.md)
- [Class physics profile template](artifact/references/student-physics-profile-template.md)
- [Shared lab-safety rules](artifact/shared/lab-safety.md)
- [Physics experiment type guidance](artifact/shared/experiment-types.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lesson-plan drafts with structured classroom-workspace fields when memory is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are teacher-reviewed drafts and may include safetyLevel labels, question chains, lesson segments, board plans, and class-profile update fields.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
