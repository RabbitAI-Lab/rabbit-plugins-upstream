## Description:

Guides Chinese-speaking students to explain and apply a concept in their own words, then identifies their level of understanding and where they are stuck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese-speaking K–12 learning settings use this skill to test their understanding of a concept through explanation, examples, and age-appropriate follow-up questions. It returns a mastery assessment and the point where their explanation breaks down, rather than teaching new material or assigning a full exercise set.

### Deployment Geography for Use:

Mainland China; other regions require localization of curriculum, minor-consent rules, and crisis-support contacts.

## Known Risks and Mitigations:

Risk: Deploying outside mainland China without adaptation could provide mismatched curriculum, consent practices, or crisis contacts.

Mitigation: Localize the curriculum, minor-consent rules, and crisis-support contacts before use in another region.

Risk: A child's learning assessment or retest reminder could be shared or retained without appropriate consent.

Mitigation: Keep assessments in the current session by default; require an explicit request and enabled sharing or reminder consent before writing a profile entry or arranging a reminder.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman five-step state machine](references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and a structured Markdown assessment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a mastery level, sticking point, and next step; optional profile updates and retest reminders require the student's request and applicable consent.]

## Skill Version(s):

2.4.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
