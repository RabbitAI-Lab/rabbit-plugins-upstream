## Description:

Helps English teachers design listening, speaking, reading, and writing assessments, map student ability with CSE as the primary standard and CEFR as a reference, and produce teaching intervention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

External English teachers use this skill to turn class assessment inputs into four-skill assessment plans, student ability profiles, and follow-up teaching recommendations for upper-primary and middle-school learners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle student assessment records in teacher-facing workflows.

Mitigation: Confirm platform consent controls before use, especially teacher writeback consent and cross-skill sharing controls.

Risk: Broad trigger phrases could be mistaken for a formal assessment workflow.

Mitigation: Ask a clarifying question before reading or writing class assessment records when the user's intent is ambiguous.

Risk: Assessment outputs could be misleading if scores are treated as direct language-proficiency levels.

Mitigation: Require teacher review against CSE descriptors for level judgments and present CEFR only as an international reference.

Risk: Generated assessment items may be used before quality or authorization checks.

Mitigation: Label AI-generated items and require teacher verification before adding them to a resource bank or test paper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [英语综合测评设计模板](references/assessment-template.md)
- ["能做什么"语句与定级流程](references/cefr-can-do-statements.md)
- [CEFR 4 维对照速查](references/cefr-four-skill-descriptors.md)
- [英语 4 维综合评分细则](references/four-skill-rubric.md)
- [学员能力画像模板](references/student-ability-profile-template.md)
- [教学干预建议样板](references/intervention-suggestion-sample.md)
- [Class teaching workspace schema](https://xiaozhi-skills.openclaw.dev/schemas/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance, templates, rubrics, and structured assessment recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference class assessment records when platform consent controls allow it; no executable payloads are disclosed in the release evidence.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
