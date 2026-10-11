## Description:

Guides Chinese middle- and high-school students through one physics problem at a time using diagrams, modeling, calculation, and reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this Chinese-language tutor to work through a specific middle- or high-school physics problem step by step, with prompts to draw the situation and check the result. It does not offer general study advice or solve an active exam question.

### Deployment Geography for Use:

Mainland China; use elsewhere requires localization of curriculum, emergency contacts, and minor-data practices.

## Known Risks and Mitigations:

Risk: A minor's learning records or reminders could be used without appropriate consent.

Mitigation: Keep profile memory, wrong-answer handoff, and reminders off by default; confirm student and, where required, guardian consent before enabling each feature.

Risk: Curriculum guidance, emergency contacts, and minor-data practices may not fit regions outside mainland China.

Mitigation: Localize these elements before deployment outside mainland China.

Risk: A student may disclose a safety crisis during tutoring.

Mitigation: Stop tutoring and follow the crisis referral protocol, using emergency contacts appropriate to the student's location.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Four-step physics problem-solving guide](artifact/references/physics-4step-statemachine.md)
- [Physics diagram guide](artifact/references/physics-diagram-guide.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese conversational text and Markdown, including stepwise hints, diagram instructions, equations, and answer checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-only by default; profile use, wrong-answer handoff, and reminders require separate opt-in consent.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
