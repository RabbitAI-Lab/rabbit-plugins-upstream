## Description:

化学解题教练面向初高中化学学习场景，按定物质、三重表征、写式列式、守恒检验的四步法引导学生完成当前一道化学题，并默认只在当前会话内工作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and tutoring agents use this skill to guide junior high and early high school chemistry problem solving through Socratic hints, substance identification, equation setup, and conservation checks. It can optionally prepare consent-gated wrong-answer handoff or reminder data when the student and required guardian have explicitly opted in.

### Deployment Geography for Use:

Global; intended for Chinese K12 chemistry-learning contexts unless localized for curriculum, safety, consent, and crisis-referral requirements.

## Known Risks and Mitigations:

Risk: Student profile memory, cross-skill sharing, parent visibility, and reminders can expose or persist minor student data when enabled without clear consent.

Mitigation: Keep memory, sharing, and reminders disabled by default; enable them only after the student and any required guardian explicitly opt in, and preserve the provided privacy control entries.

Risk: The skill is designed for Chinese K12 chemistry contexts, so direct use elsewhere can misstate curriculum scope, consent expectations, or crisis-referral channels.

Mitigation: Localize curriculum references, legal consent defaults, and safety or crisis contact guidance before deploying outside the intended context.

Risk: Chemistry tutoring may involve lab-safety topics or student requests for at-home experiment steps.

Mitigation: Use the bundled lab-safety guidance: avoid dangerous at-home procedures, do not provide unsafe chemical-mixing instructions, and defer supervised experiments to teachers or laboratories.

Risk: A learner may disclose self-harm, bullying, severe distress, or other crisis signals while using a learning skill.

Mitigation: Stop the tutoring flow, avoid diagnosis, encourage contact with trusted adults, and provide localized emergency or youth-support channels as specified by the crisis protocol.

Risk: Generated practice items or worked examples can contain incorrect conditions, answers, or grade-level mismatches.

Mitigation: Apply the bundled AI item self-check before presenting generated items, and mark teacher-facing generated items for human verification before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-problem-coach)
- [四步化学解题法细则](references/chemistry-4step-guide.md)
- [化学错因维度表](shared/chemistry-error-dimension-table.md)
- [实验安全约定](shared/lab-safety.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown with optional structured JSON handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate consent-gated wrong-answer handoff or reminder data; does not write long-term records by default.]

## Skill Version(s):

2.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
