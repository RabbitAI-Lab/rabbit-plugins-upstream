## Description:

初高衔接规划师 helps students from the end of middle-school entrance exams through early Grade 10 diagnose transition gaps in math, physics, chemistry, and English, then produce a staged bridge plan for the summer and first school weeks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning-support agents use this skill to identify the prerequisite gaps that may affect the first chapters of Grade 10 math, physics, chemistry, and English, then plan what to review first, what to preview lightly, and when to hand off to subject-specific skills. It is intended for Chinese-language K12 transition planning with consent-gated profile reading and reminder handoff.

### Deployment Geography for Use:

Mainland China by default; localize curriculum assumptions, minor-data consent requirements, and crisis-contact guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Student profile fields or reminder queues may involve student data and should not be used without appropriate consent.

Mitigation: Keep profile reading and reminder enqueueing disabled unless the current session includes explicit consent and any required guardian consent; otherwise rely only on current-session information and provide a text plan.

Risk: Use outside Mainland China may expose students to mismatched curriculum assumptions, consent requirements, or crisis-contact guidance.

Mitigation: Localize curriculum references, minor-data consent rules, and emergency or youth-support contact channels before deployment outside Mainland China.

Risk: Transition planning can become misleading if it pretends to cover unsupported high-school content or guarantees outcomes.

Mitigation: State coverage limits, route detailed subject instruction to the appropriate subject skills, preserve rest days, and avoid guarantees that the plan will prevent falling behind.

## Reference(s):

- [Bridge checklist reference](artifact/references/bridge-checklists.md)
- [Platform capability and localization conventions](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Student profile schema](artifact/shared/dna-profile.schema.json)
- [Skill handoff protocol schema](artifact/shared/handover-protocol.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-bridge-planner)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with diagnostic questions, weekly planning structure, consent-gated handoff notes, and references to subject-specific skills.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reminder_enqueue handoff content when the student explicitly consents; does not directly write student profiles or promise active reminders.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
