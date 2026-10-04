## Description:

Turns a student's weekly learning records into an evidence-based review with a focused next step and guided self-reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators in a simplified-Chinese K12 setting use this skill to review a week of learning, identify evidence of progress and difficulty, and select one priority for the following week. A family-facing report requires the student's consent.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent requirements, and crisis-support contacts before student use elsewhere.

## Known Risks and Mitigations:

Risk: Curriculum, minor-consent rules, and crisis contacts may be inappropriate outside mainland China.

Mitigation: Localize these requirements and contacts before use with students in another region.

Risk: A family report or learning-summary handoff could disclose a student's personal information without permission.

Mitigation: Confirm the student's identity and current consent before sharing or writing back; honor refusal and pause controls.

Risk: Incomplete learning history could make weekly statistics or conclusions misleading.

Mitigation: State data gaps, avoid unsupported historical numbers, and use a conversational review when persistent records are unavailable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report template](references/review-report-template.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral guidance](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly student report or shorter three-question review for younger students; optional consented family report, growth-summary handoff, and reminder request.]

## Skill Version(s):

2.10.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
