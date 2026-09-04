## Description:

A Chinese-language junior middle school math coaching skill that locates a student's current five-level practice tier, generates progressively harder exercises, and records confirmed growth milestones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and learning-support agents use this skill to practice junior middle school math through tiered diagnostics, adaptive exercise sequences, hint-ladder coaching, and concise growth summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning profile sharing, reminders, or parent/guardian visibility may be inappropriate without clear consent.

Mitigation: Confirm profile sharing, reminder, and parent/guardian visibility settings before use; honor the provided view, correct, delete, pause, sharing-control, and export controls.

Risk: Crisis hotline wording may be inappropriate outside mainland China.

Mitigation: Replace crisis referral wording with local emergency and support resources before using the skill in other regions.

Risk: Generated math exercises can contain flawed conditions, unsuitable difficulty, or incorrect solutions.

Mitigation: Apply the bundled AI item self-check before presenting generated exercises, and require human review before teacher-facing generated items are reused as resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang)
- [Initial Math Gradient-Level Reference](references/gradient-levels.md)
- [AI Item Self-Check Protocol](shared/ai-item-check.md)
- [Hint Ladder and Worked Example Exit](shared/hint-ladder.md)
- [Platform Capability Conventions](shared/platform-conventions.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)
- [Handover Protocol Schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese coaching dialogue, math practice prompts, Markdown summaries, and JSON handover objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated learning profile updates, training log entries, and reminder queue handoffs when the hosting platform supports them.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
