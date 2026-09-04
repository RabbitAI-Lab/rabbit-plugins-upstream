## Description:

数学教师的备课工具，帮助将一节数学课的概念建构路径、例题示范、变式训练、课堂小结和错例档案组织成可实施的教案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language middle-school math teachers use this skill to draft lesson plans that connect concept-building, worked examples, variation practice, classroom summaries, and error-case records. It is intended to support teacher preparation and review, not replace teacher judgment.

### Deployment Geography for Use:

Global; adapt crisis-support contacts and student-data practices to local policy outside mainland China.

## Known Risks and Mitigations:

Risk: Student records or cross-skill sharing could expose sensitive classroom information if used without the controls described by the release evidence.

Mitigation: Use aliases, confirm teacher consent before writeback, and honor pause, delete, export, and sharing-control requests before storing or sharing classroom records.

Risk: Crisis-support references may be jurisdiction-specific outside mainland China.

Mitigation: Replace the included contacts with local emergency and youth-support resources before deployment in other regions.

Risk: Generated math exercises or examples may contain calculation, wording, or copyright-status errors.

Mitigation: Require teacher review, self-solve generated items, apply the bundled AI item check, and label AI-generated items before any resource-bank or test reuse.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-lesson-planner)
- [Concept Build Template](references/concept-build-template.md)
- [Variation Design](references/variation-design.md)
- [Error Pattern Rubric](references/error-pattern-rubric.md)
- [AI Item Check](shared/ai-item-check.md)
- [Class Teaching Workspace Schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese-language structured Markdown with schema-aligned JSON snippets when writing lesson-plan workspace records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated math items, lesson-plan records, and resource-bank entries are proposals for teacher review before reuse or storage.]

## Skill Version(s):

2.1.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
