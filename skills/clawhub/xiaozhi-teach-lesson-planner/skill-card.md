## Description:

教案设计器 helps Chinese-language K12 teachers draft observable UbD-style lesson plans with assessment evidence, competency-aligned objectives, time-boxed lesson segments, question-chain drafts, and A/B/C tier adaptations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 teachers use this skill to turn a lesson topic, curriculum goal, and optional class context into a teacher-reviewed lesson-plan draft. It is intended for planning support, not for autonomous teaching, student evaluation, exam generation, or classroom execution.

### Deployment Geography for Use:

Mainland China defaults; localize curriculum assumptions, consent rules, and crisis-support channels before deployment in other regions.

## Known Risks and Mitigations:

Risk: Real class or student context could be used without the required platform permission and consent controls.

Mitigation: Confirm read/write permissions and consent controls before use with real class data, especially for student tiers, class summaries, parent sharing, and teacher writeback.

Risk: Mainland China curriculum, consent, and crisis-support defaults may be inappropriate in other regions.

Mitigation: Localize curriculum assumptions, legal consent requirements, and emergency or youth-support channels before deploying outside Mainland China.

Risk: AI-generated examples, variants, or classroom exercises may contain errors.

Mitigation: Use the included AI item self-check workflow and require teacher verification before putting generated items into a resource bank, exam, or classroom handout.

Risk: Lesson-plan drafts may be mistaken for final professional judgment or classroom implementation instructions.

Mitigation: Keep outputs teacher-reviewed, avoid promised score gains, and route classroom execution or live questioning strategy to the appropriate teaching workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [lesson-plan-template.md](artifact/references/lesson-plan-template.md)
- [layered-lesson-example.md](artifact/references/layered-lesson-example.md)
- [class-teaching-workspace.schema.json](artifact/shared/class-teaching-workspace.schema.json)
- [platform-conventions.md](artifact/shared/platform-conventions.md)
- [ai-item-check.md](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lesson-plan drafts and structured classWorkspace.lessonPlans guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include UbD objectives, assessment evidence, lesson timing matrices, question-chain drafts, board plans, risk plans, and tiered task variants.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
