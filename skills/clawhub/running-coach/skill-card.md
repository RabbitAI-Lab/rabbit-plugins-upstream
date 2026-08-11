## Description:

Running coach for endurance athletes training with Garmin, Strava, Coros, or Apple Watch. Provides VDOT-based pace zones, session analysis from training screenshots, weekly and periodized season plans (5K through marathon), race strategy, load monitoring via HRV/recovery metrics, injury risk screening, and strength/nutrition guidance grounded in Jack Daniels and Pfitzinger methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and running-focused agents use this skill to analyze watch or app training data, produce structured training reports, calculate calibrated pace and heart-rate zones, and generate weekly or season training guidance for 5K through marathon goals. It is intended for recreational runners with running-specific context and is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or create a local running profile, persist key fitness parameters, and write training summaries to a configured log.

Mitigation: Review the profile path, MEMORY.md usage, and training-log destination before installation; limit stored data to fields needed for running guidance.

Risk: Injury screening guidance could be mistaken for medical care.

Mitigation: Treat injury output as non-diagnostic risk screening and seek a qualified clinician for severe, worsening, persistent, swelling, night, rest, or sharp pain symptoms.

Risk: Training plans and pace zones can be misleading when based on stale, missing, or uncalibrated fitness data.

Mitigation: Confirm the current training phase and calibrate paces from a recent race, lactate-threshold test, or time trial before relying on personalized prescriptions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/running-coach)
- [README_zh.md](artifact/README_zh.md)
- [Session Types](artifact/references/session_types.md)
- [Heart Rate Zone Calculation](artifact/references/zone_calc.md)
- [Periodized Training Phases](artifact/references/periodization.md)
- [Injury Assessment Decision Tree](artifact/references/injury_check.md)
- [Report Templates](artifact/references/report_template.md)
- [Profile Schema](artifact/references/profile_schema.md)
- [Pace System & Fitness Estimation](artifact/references/pace_system.md)
- [Warm-up / Cool-down / Activation](artifact/references/warmup_cooldown.md)
- [Strength Training & Recovery](artifact/references/strength_recovery.md)
- [Nutrition & Fueling](artifact/references/nutrition.md)
- [Race Strategy](artifact/references/race_tactics.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown reports, tables, training plans, and optional profile or log update guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for missing calibration, profile, or training-log details before producing personalized guidance.]

## Skill Version(s):

1.2.5 (source: server release metadata; artifact frontmatter reports 1.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
