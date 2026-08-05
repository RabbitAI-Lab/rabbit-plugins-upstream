## Description: <br>
Running coach for endurance athletes training with Garmin, Strava, Coros, or Apple Watch. Provides VDOT-based pace zones, session analysis from training screenshots, weekly and periodized season plans (5K through marathon), race strategy, load monitoring via HRV/recovery metrics, injury risk screening, and strength/nutrition guidance grounded in Jack Daniels and Pfitzinger methodology. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for running training support, including workout analysis, pace calibration, weekly and season planning, race review, recovery monitoring, and non-diagnostic injury-risk screening. It is intended for recreational runners who already train consistently and record running data with a watch or fitness app. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses local running and physiological profile data for personalization. <br>
Mitigation: Install only if users are comfortable storing this data locally, and keep profile contents under the user's control. <br>
Risk: Injury and nutrition outputs could be mistaken for medical advice. <br>
Mitigation: Treat outputs as training guidance only, and consult a qualified clinician for pain, worsening symptoms, cardiovascular concerns, pregnancy, medication interactions, or stimulant sensitivity. <br>
Risk: Plans and paces may be inappropriate if watch data, profile values, or recent training context are incomplete or stale. <br>
Mitigation: Confirm the current phase and calibration data before planning, derive paces from recent results or tests, and keep weekly progression conservative. <br>


## Reference(s): <br>
- [Running Coach Skill Page](https://clawhub.ai/haiyangchenbj/skills/running-coach) <br>
- [Injury Assessment Decision Tree](references/injury_check.md) <br>
- [Nutrition & Fueling](references/nutrition.md) <br>
- [Pace System & Fitness Estimation](references/pace_system.md) <br>
- [Periodized Training Phases](references/periodization.md) <br>
- [Profile Schema](references/profile_schema.md) <br>
- [Race Strategy](references/race_tactics.md) <br>
- [Report Templates](references/report_template.md) <br>
- [Session Types](references/session_types.md) <br>
- [Strength Training & Recovery](references/strength_recovery.md) <br>
- [Pre / During / Post: Warm-up / Cool-down / Activation](references/warmup_cooldown.md) <br>
- [Heart Rate Zone Calculation](references/zone_calc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Structured Markdown reports, plans, pace tables, setup guidance, and actionable recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide users to create or update a local running profile and may degrade to an in-conversation text report when logging is unavailable.] <br>

## Skill Version(s): <br>
1.2.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
