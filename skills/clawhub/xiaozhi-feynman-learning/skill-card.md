## Description:

Helps an agent run Feynman-style learning checks that ask students to explain, give examples, answer why, transfer concepts, and report mastery level and sticking point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, tutors, and education agents use this skill to test whether a learner truly understands a concept after studying, solving a problem, reviewing an AI answer, or preparing to teach someone else. The skill produces a concise mastery assessment and next-step guidance rather than new instruction or a practice set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cross-skill handoff behavior is loose enough to warrant review before installation.

Mitigation: Validate every handoff against the bundled handover schema, restrict recipients to the intended learning DNA or reminder skill, and send only minimal mastery fields after crossSkillSharing or reminderConsent is present.

Risk: Student frustration or safety-related language can appear during tutoring and may exceed the learning workflow.

Mitigation: Run the crisis-signal check before tutoring fallback behavior, stop the learning flow when a crisis signal is present, and follow the bundled crisis referral protocol.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman dialogue patterns](artifact/references/feynman-dialogue-patterns.md)
- [Feynman 4+1 jump state machine](artifact/references/feynman-5jump-statemachine.md)
- [Mastery vocabulary](artifact/shared/vocab.md)
- [Grade band parameters](artifact/shared/grade-bands.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown-style tutoring dialogue and structured assessment text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a mastery level, sticking point, next-step suggestion, optional minimal profile writeback data, or optional reminder handoff when consent is present.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
