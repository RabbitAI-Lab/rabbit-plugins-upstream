## Description:

Designs differentiated, time-bounded homework task cards with rubrics, feedback templates, and aggregate completion writeback guidance for teachers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn a topic, class learning profile, or existing assignment into differentiated A/B/C homework cards, scoring rubrics, student feedback, and aggregate completion summaries. It is intended for classroom assignment design, not review scheduling, exam generation, or automated grading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom learning records may be used to design homework and write aggregate completion summaries.

Mitigation: Enable parent-facing output and cross-skill sharing only when the relevant consents are present, and keep completion writebacks aggregate and de-identified.

Risk: AI-generated homework items may be incorrect, unsuitable for the declared grade band, or not ready for formal assignment use.

Mitigation: Apply the bundled AI item self-check, label teacher-facing generated items as requiring human validation, and do not place unverified items into formal homework.

Risk: The skill may encounter student crisis disclosures while handling homework feedback or parent-facing summaries.

Mitigation: Stop the homework workflow, follow the crisis exception protocol, contact trusted adults or local emergency channels as appropriate, and avoid storing sensitive details beyond the referral fact.

Risk: Excessive homework volume can displace sleep, movement, or other subjects.

Mitigation: Default to concise assignments, include estimated minutes for every task, and confirm added workload before increasing assignment volume.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Assignment rubric and leveled task card template](artifact/references/assignment-rubric.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown task cards, rubrics, feedback templates, and structured workspace-field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated minutes per task, aggregate completion-summary fields, and teacher-facing labels for AI-generated items requiring human validation.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
