## Description:

用"讲给小智听"来检验学生是否真的学会了某个概念，并产出掌握度判定、卡住位置和下一步建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, tutors, and learning agents use this skill to run a Feynman-style self-check after studying a concept. It guides the student through explanation, examples, reasoning, transfer, and age-appropriate critical verification, then reports mastery level and blind spots.

### Deployment Geography for Use:

Mainland China by default; other regions require localized safety contacts, curriculum review, and minors-data consent checks before student-facing deployment.

## Known Risks and Mitigations:

Risk: Student mastery data can be saved or shared if platform consent boundaries are too loose.

Mitigation: Install only on platforms that enforce Learning DNA authorization checks, guardian consent where required, and writes limited to extensions.understanding after an explicit save request.

Risk: Reminders, weekly reports, or parent-visible summaries could expose learning assessment data without clear consent.

Mitigation: Treat reminders, weekly reports, and parent-visible summaries as opt-in sharing flows rather than automatic outputs.

Risk: Safety guidance is designed around mainland China and may give inappropriate referral channels elsewhere.

Mitigation: Localize emergency and youth-support contacts before use outside mainland China, and ask the student's region before giving location-specific crisis numbers.

Risk: Generated transfer checks or practice items may be incorrect or outside the student's grade band.

Mitigation: Apply the bundled AI item self-check before presenting generated questions, and require teacher review before teacher-facing item reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman 4+1 jump state machine](artifact/references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](artifact/references/feynman-dialogue-patterns.md)
- [Platform conventions and degradation paths](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational guidance and a Markdown-style Feynman test assessment report; optional structured handover payloads when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose mastery records for extensions.understanding only after an explicit save request and valid cross-skill sharing consent.]

## Skill Version(s):

2.1.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
