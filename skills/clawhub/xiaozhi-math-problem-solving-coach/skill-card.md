## Description:

A Simplified Chinese math coach that guides middle-school students through individual problems with questions and progressive hints, then checks understanding with similar exercises.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Middle-school students use this skill to work through math problems, correct mistakes, practice related questions, and review familiar material before exams. It defaults to the current conversation; reading records, sharing across skills, saving mistakes, and scheduling reminders require the student's current-session consent.

### Deployment Geography for Use:

Mainland China by default; deployments elsewhere require localized crisis-support contacts.

## Known Risks and Mitigations:

Risk: A student's problem history or weak areas may be shared or saved without appropriate consent.

Mitigation: Require current-session consent and enforce platform consent flags before reading archives, sharing across skills, saving records, or scheduling reminders; provide deletion and export controls.

Risk: A minor in crisis may receive inappropriate or regionally incorrect support information.

Mitigation: Interrupt tutoring for crisis signals, refer the student to a trusted adult and local emergency support, and localize crisis contacts outside mainland China.

Risk: AI-generated practice problems may contain invalid conditions or incorrect answers.

Mitigation: Check generated questions for a valid solution, suitable grade level, and matching problem type before presenting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Four-step problem-solving workflow](artifact/references/photo-4step-statemachine.md)
- [Math Socratic questioning guide](artifact/references/math-socrates-guide.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Simplified Chinese conversational text and Markdown; optional JSON handoff with consent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise hints, practice problems, and exam-review outlines; no automatic record access or reminders]

## Skill Version(s):

2.4.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
