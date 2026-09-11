## Description:

帮初中物理老师把讲题升级为系统化的解题教学，使用审题、建模、过程分析、列式、求解反思的五步法，并支持变式训练与班级解题档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to prepare and guide middle-school physics problem-solving instruction, including model selection, process analysis, equation setup, reflection prompts, and variant-practice design. It also helps maintain low-sensitivity class problem-solving records and draft teacher-reviewed updates when consent allows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Class problem-solving records may expose sensitive information about minors if real names, private details, or public critiques are included.

Mitigation: Use aliases or seat numbers, keep records low sensitivity, provide view/correct/delete/export controls, and avoid public student-specific error displays.

Risk: Generated physics questions or variants may contain calculation errors, unsuitable difficulty, or misleading explanations.

Mitigation: Label AI-generated items, run the item self-check, and require teacher review before assigning, saving, or sharing generated materials.

Risk: Copyrighted textbook, tutoring, or exam questions could be retained or reused beyond permitted indexing.

Mitigation: Require copyrightStatus labels and store original teaching-aid or exam questions only as indexes unless rights allow broader use.

Risk: Student writeback could update learner records without valid consent.

Mitigation: Send teacher_writeback data only after confirming teacherWritebackConsent, and restrict the payload to aliases, weak knowledge-point updates, mastery status, and a short low-sensitivity note.

Risk: Learner distress or safety signals may appear during problem-solving support.

Mitigation: Stop the teaching flow when crisis signals appear, avoid recording sensitive details, and provide location-appropriate referral guidance according to the bundled crisis protocol.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-problem-guide)
- [five-step-template.md](references/five-step-template.md)
- [five-step-worked-examples.md](references/five-step-worked-examples.md)
- [model-selection.md](references/model-selection.md)
- [multi-solution-example.md](references/multi-solution-example.md)
- [student-solving-profile-template.md](references/student-solving-profile-template.md)
- [variation-physics.md](references/variation-physics.md)
- [ai-item-check.md](shared/ai-item-check.md)
- [platform-conventions.md](shared/platform-conventions.md)
- [vocab.md](shared/vocab.md)
- [crisis-exception.md](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown teaching guidance with optional structured class-workspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher review is required before saving, sharing, or writing back class or student records.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
