## Description:

Schedules and combines consented study reviews and learning tasks into a daily reminder digest for Chinese-speaking K–12 students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use the skill to request, review, pause, and manage reminders for revision, missed questions, study plans, and exploration tasks. With consent, it groups scheduled items into a low-interruption daily summary.

### Deployment Geography for Use:

Mainland China; adapt language, school assumptions, consent rules, and crisis resources before use elsewhere.

## Known Risks and Mitigations:

Risk: Reminders or cross-skill learning data could be shared or retained without the student's or guardian's consent.

Mitigation: Require explicit consent and provide clear controls to view, pause, delete, export, and limit sharing of reminders.

Risk: Chinese school assumptions and crisis contacts may be unsuitable outside mainland China.

Mitigation: Localize the language, school context, legal consent rules, and help channels before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [Platform capabilities and fallback behavior](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language text reminders, daily summaries, and control confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminders require consent; scheduling and delivery depend on platform capabilities.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
