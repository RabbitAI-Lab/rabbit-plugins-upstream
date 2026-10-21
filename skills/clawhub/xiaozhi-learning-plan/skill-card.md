## Description:

Creates tailored study schedules for Chinese K–12 students, with weekly plans for upper-primary students and 30-day plans for older students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to turn learning goals and, with consent, existing learning-profile summaries into achievable study and exam-preparation schedules. It can help adjust plans after weekly check-ins and prepare a parent-facing task board when authorized.

### Deployment Geography for Use:

Mainland China (Chinese K–12 context; localize curricula, emergency contacts, and consent rules before use elsewhere)

## Known Risks and Mitigations:

Risk: Learning-profile use, parent sharing, or reminder queueing could expose student information without consent.

Mitigation: Keep each action off by default; obtain separate explicit consent and allow students to decline or revoke it.

Risk: Curriculum, emergency contacts, and minor-consent expectations are specific to mainland China.

Mitigation: Use in the intended Chinese K–12 setting or localize those requirements before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study-plan templates](references/plan-templates.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown study schedules, weekly progress summaries, and optional printable family task boards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper-primary students receive weekly rather than 30-day schedules; parent-facing boards and reminder queueing require separate consent.]

## Skill Version(s):

2.11.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
