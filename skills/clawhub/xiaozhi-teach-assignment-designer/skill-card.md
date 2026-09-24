## Description:

Designs differentiated Chinese K12 homework task cards with estimated completion time, scoring rubrics, feedback templates, and teacher-reviewed follow-up records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn a lesson topic, learning evidence, or existing homework set into differentiated A/B/C task cards, scoring criteria, concise feedback, and aggregate completion summaries. It is intended for Chinese-language K12 homework design and requires teacher review before student or parent use.

### Deployment Geography for Use:

China mainland by default; deployments in other regions require localization of curriculum, privacy, and crisis-referral assumptions before student-facing use.

## Known Risks and Mitigations:

Risk: The skill is designed around China-specific K12 curriculum, privacy, and crisis-referral assumptions.

Mitigation: Confirm the deployment geography before use and localize curriculum expectations, data-consent rules, and emergency referral channels outside China mainland.

Risk: AI-generated homework items or rubrics may contain incorrect, unsolvable, or misaligned material.

Mitigation: Require teacher review and item self-check before any generated question enters a formal assignment or resource bank.

Risk: Homework feedback can expose sensitive student information if copied directly into parent- or class-facing outputs.

Mitigation: Use pseudonyms or aggregate summaries, omit names, rankings, and individual score comparisons, and respect parent-sharing consent controls.

Risk: Active unified exam questions, answer keys, or scoring standards may be confidential.

Mitigation: Do not input or generate active exam materials; use only general methods, blueprint structures, or self-authored practice until the exam is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Assignment rubric and differentiated task-card template](artifact/references/assignment-rubric.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI-generated item self-check protocol](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text with structured tables, task cards, rubric sections, and JSON-compatible field names.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing drafts only; generated items require manual verification and the skill does not automatically grade student work.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
