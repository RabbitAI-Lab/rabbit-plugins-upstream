## Description:

A Chinese-language middle-school math coaching skill that guides students through individual math problems with Socratic questions, staged hints, similar practice problems, and exam-review support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students use this skill to work through Chinese middle-school math problems without immediately receiving the answer: the agent asks for the student's current thinking, escalates hints through a defined ladder, generates similar problems for transfer practice, and prepares short exam-review structures. Host platforms can also use it to create consent-gated wrong-answer handoff records for related learning-profile skills.

### Deployment Geography for Use:

China Mainland Chinese K12 context; localize curriculum assumptions, consent requirements, and safety referral channels before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill handles student learning records and cross-skill handoffs, and the server security summary says routing and retention rules are broader than the stated scope.

Mitigation: Deploy only where the host platform enforces consent, recipient authorization, and retention limits for profile reads, wrong-answer handoffs, reminders, deletion/export requests, and parent-sharing controls.

Risk: The security verdict is suspicious even though no malicious behavior was found.

Mitigation: Review the release before student use and confirm that platform controls implement the security guidance rather than relying on instructional text alone.

Risk: The artifact is designed for Chinese K12 use and includes China Mainland safety-channel assumptions.

Mitigation: For other regions, localize curriculum alignment, minor-consent requirements, and crisis referral channels before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang)
- [Math four-step photo workflow state machine](artifact/references/photo-4step-statemachine.md)
- [Math Socratic questioning guide](artifact/references/math-socrates-guide.md)
- [Intent-branch prompt extensions](artifact/references/claw-templates-extended.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [AI-generated item self-check protocol](artifact/shared/ai-item-check.md)
- [Platform conventions and localization constraints](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese conversational tutoring guidance, short markdown-style study structures, generated math exercises, and JSON handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on host-provided OCR, persistent memory, cross-session statistics, consent state, and reminder workflows; missing capabilities trigger documented degradation paths.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
