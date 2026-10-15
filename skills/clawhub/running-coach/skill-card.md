## Description:

Helps endurance runners analyze workouts, estimate training paces, plan weeks and race seasons, and review recovery and race strategy using watch data and recent results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Recreational runners preparing for 5K through marathon events use this skill to interpret training records, build calibrated training plans, and get race, recovery, and non-diagnostic injury-risk guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A running profile may contain sensitive heart-rate, goal, and injury-history information.

Mitigation: Provide only fields needed for personalized advice; review the local profile before sharing or syncing it.

Risk: Training summaries may be sent to a configured log system.

Mitigation: Opt in to log writes only if comfortable with the destination; revoke or avoid log_write for text-only reports.

Risk: Injury and recovery guidance could be mistaken for a medical assessment.

Mitigation: Treat screening as non-diagnostic and seek medical care for persistent or severe symptoms or urgent warning signs.

## Reference(s):

- [Running Coach release](https://clawhub.ai/haiyangchenbj/skills/running-coach)
- [Pace system](references/pace_system.md)
- [Weekly review](references/weekly_review.md)
- [Injury screening](references/injury_check.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown reports, tables, and training plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local running profile with confirmation or write training summaries to a configured log after opt-in; otherwise provides text-only reports.]

## Skill Version(s):

1.2.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
