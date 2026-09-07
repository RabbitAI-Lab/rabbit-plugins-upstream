## Description:

教案设计器 helps teachers produce UbD-based lesson plans with observable learning goals, assessment evidence, class-period timing, Bloom-style question-chain drafts, and A/B/C differentiated activities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn a lesson topic, curriculum goal, and optional class learning context into a structured Chinese K12 lesson plan. It is intended for new lessons, reviews, exam-commentary classes, differentiated lesson planning, and draft question-chain design.

### Deployment Geography for Use:

Mainland China primary; deployment elsewhere requires localizing crisis contacts, curriculum assumptions, and minor-data consent rules.

## Known Risks and Mitigations:

Risk: Individual student tier and score-basis notes may be placed into the agent context during differentiated lesson planning.

Mitigation: Prefer aggregate tier counts when possible; otherwise use pseudonyms or seat numbers only and install the skill only where teachers have permission to use that classroom data.

Risk: AI-generated examples, variations, or classroom exercises can be incorrect or unsuitable for the target grade band.

Mitigation: Apply the bundled AI item self-check and keep teacher verification before storing generated items in a resource bank or test.

Risk: The skill is designed around Mainland China K12 curriculum, safety-contact, and minor-data assumptions.

Mitigation: Localize curriculum alignment, crisis contacts, and consent handling before use in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson plan template](artifact/references/lesson-plan-template.md)
- [Layered lesson example](artifact/references/layered-lesson-example.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown lesson plans with structured lesson-plan fields and optional differentiated task-card sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lesson-plan records, question-chain drafts, tier-specific activity variants when student tier data is available, and teacher-facing verification notes for AI-generated exercises.]

## Skill Version(s):

2.1.12 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
