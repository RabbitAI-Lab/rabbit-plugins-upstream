## Description:

Running coach for endurance athletes training with Garmin, Strava, Coros, or Apple Watch. Provides VDOT-based pace zones, session analysis from training screenshots, weekly and periodized season plans (5K through marathon), race strategy, load monitoring via HRV/recovery metrics, injury risk screening, and strength/nutrition guidance grounded in Jack Daniels and Pfitzinger methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External recreational endurance runners use this skill to analyze watch or app training data, calibrate paces, plan weekly and season training, review races, monitor load, and get general strength, nutrition, recovery, and injury-risk guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a local running profile that may contain sensitive fitness, injury, heart-rate, lactate-threshold, recovery, and goal data.

Mitigation: Review profile.json before use, keep only necessary fields, and avoid sharing profile or training-log contents outside the intended agent session.

Risk: The skill remembers selected training parameters across sessions, which can retain sensitive or stale fitness information.

Mitigation: Review stored memory periodically, remove sensitive or outdated parameters, and keep profile.json as the authoritative source.

Risk: Injury screening and caffeine or recovery guidance could be mistaken for medical advice.

Mitigation: Treat outputs as general training guidance and seek medical care for rest pain, swelling, sharp running pain, night pain, or symptoms lasting more than two weeks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/running-coach)
- [Session Types](artifact/references/session_types.md)
- [Heart Rate Zone Calculation](artifact/references/zone_calc.md)
- [Periodized Training Phases](artifact/references/periodization.md)
- [Injury Assessment Decision Tree](artifact/references/injury_check.md)
- [Report Templates](artifact/references/report_template.md)
- [Profile Schema](artifact/references/profile_schema.md)
- [Pace System & Fitness Estimation](artifact/references/pace_system.md)
- [Pre / During / Post: Warm-up / Cool-down / Activation](artifact/references/warmup_cooldown.md)
- [Strength Training & Recovery](artifact/references/strength_recovery.md)
- [Nutrition & Fueling](artifact/references/nutrition.md)
- [Race Strategy](artifact/references/race_tactics.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, tables, plans, checklists, and profile setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose updates to a local running profile and memory only with user confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
