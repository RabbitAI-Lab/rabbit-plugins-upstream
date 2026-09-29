## Description:

Coordinates consent-based learning reminders for Chinese K–12 students, combining due reviews and tasks into a daily summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to schedule, review, pause, and receive consolidated reminders for study and exploration tasks they explicitly approve.

### Deployment Geography for Use:

Mainland China; localize safeguards before deployment elsewhere

## Known Risks and Mitigations:

Risk: Unwanted reminders or disclosure of a minor's learning data.

Mitigation: Confirm student or guardian consent, honor quiet hours and pause/deletion controls, and share only approved minimum-necessary details.

Risk: Incorrect crisis contacts or consent practices outside the intended region.

Mitigation: Before enabling reminders outside mainland China, localize referral channels and review local consent requirements.

Risk: Promises of proactive delivery when the platform cannot schedule reminders.

Mitigation: Confirm scheduling support; otherwise offer due items on the next user-initiated session and explain the limitation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [Quiet hours and grade bands](shared/grade-bands.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language reminder summaries and conversational responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminders require consent; timing and active delivery depend on platform capabilities.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
