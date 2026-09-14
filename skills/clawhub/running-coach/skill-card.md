## Description:

Running coach for endurance athletes training with Garmin, Strava, Coros, or Apple Watch. Provides VDOT-based pace zones, session analysis from training screenshots, weekly and periodized season plans (5K through marathon), race strategy, load monitoring via HRV/recovery metrics, injury risk screening, and strength/nutrition guidance grounded in Jack Daniels and Pfitzinger methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External runners and coaching assistants use this skill to analyze training screenshots, calibrate paces from race or time-trial results, build weekly and season plans, review races, monitor recovery signals, and receive running-specific advisory guidance. It is aimed at recreational endurance runners training consistently for distances from 5K through marathon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health and performance details may be copied into persistent memory without clear opt-in or deletion controls.

Mitigation: Before use, decide whether heart-rate, injury, race, goal, and training-phase details should be stored outside the local profile; remove or narrow the persistent-memory instruction if that storage is not desired.

Risk: Injury, nutrition, supplement, and recovery guidance can be mistaken for medical advice.

Mitigation: Keep the skill's non-diagnostic framing, immediate-stop red flags, doctor-referral triggers, and health disclaimer active in medical-adjacent responses.

Risk: Training plans can become unsafe when based on stale phase, recovery, or calibration data.

Mitigation: Confirm the current training phase, recent load, and pace calibration before generating plans, and keep weekly volume or intensity increases conservative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/running-coach)
- [Pace System & Fitness Estimation](references/pace_system.md)
- [Heart Rate Zone Calculation](references/zone_calc.md)
- [Session Types](references/session_types.md)
- [Periodized Training Phases](references/periodization.md)
- [Injury Assessment Decision Tree](references/injury_check.md)
- [Report Templates](references/report_template.md)
- [Profile Schema](references/profile_schema.md)
- [Nutrition & Fueling](references/nutrition.md)
- [Strength Training & Recovery](references/strength_recovery.md)
- [Warm-up / Cool-down / Activation](references/warmup_cooldown.md)
- [Race Strategy](references/race_tactics.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown reports, tables, setup prompts, training plans, and advisory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May personalize responses from a local runner profile and may suggest opt-in training-log updates.]

## Skill Version(s):

1.2.8 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
