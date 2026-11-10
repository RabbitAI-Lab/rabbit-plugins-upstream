## Description:

Running coach for endurance athletes training with Garmin, Strava, Coros, or Apple Watch. Provides VDOT-based pace zones, session analysis from training screenshots, weekly and periodized season plans (5K through marathon), race strategy, load monitoring via HRV/recovery metrics, injury risk screening, and strength/nutrition guidance grounded in Jack Daniels and Pfitzinger methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Recreational endurance runners use this skill to interpret watch or app data, estimate training paces from their own results, plan training for 5K through marathon races, and review race, recovery, strength, and nutrition questions. It provides non-diagnostic injury risk screening rather than medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a possibility of persistent weekly review updates without required notice.

Mitigation: Review proposed weekly review changes and require clear notice and user confirmation before persisting updates.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/running-coach)
- [Pace system](references/pace_system.md)
- [Heart rate zone calculation](references/zone_calc.md)
- [Session types](references/session_types.md)
- [Periodization](references/periodization.md)
- [Weekly review](references/weekly_review.md)
- [Race strategy](references/race_tactics.md)
- [Injury screening](references/injury_check.md)
- [Runner profile schema](references/profile_schema.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance, Training plans]

**Output Format:** [Structured Markdown with tables and concise coaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided running data and calibration; may provide text reports when no training-log system is configured.]

## Skill Version(s):

1.2.11 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
