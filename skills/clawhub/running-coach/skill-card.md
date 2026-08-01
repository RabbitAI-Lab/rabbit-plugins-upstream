## Description: <br>
Running Coach analyzes running screenshots and training context to produce session reviews, VDOT-based pace guidance, weekly and season plans, load monitoring, injury-risk screening, warm-up, strength, nutrition, and race-strategy advice for recreational runners. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and recreational runners use this skill to interpret watch or app run data, calibrate training paces, plan workouts and race preparation, monitor recovery signals, and receive non-diagnostic running guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and persists health-related profile and training-log data. <br>
Mitigation: Install only when comfortable with local profile access, recent training-log use, and storing key parameters in memory; keep profile and log permissions limited to the user's intended storage locations. <br>
Risk: Running, injury, caffeine, and maximal-effort test guidance can be inappropriate for users with pain, medical conditions, pregnancy, medication interactions, cardiovascular concerns, or uncertain symptoms. <br>
Mitigation: Treat outputs as educational coaching guidance, keep injury screening non-diagnostic, and seek clinician guidance for red-flag symptoms or medical uncertainty. <br>
Risk: Broad activation triggers may cause the agent to process sensitive fitness screenshots or training context when running-related inputs are shared. <br>
Mitigation: Review shared screenshots and profile fields before use, and avoid providing unrelated sensitive data in running-coach interactions. <br>


## Reference(s): <br>
- [Running Coach ClawHub release](https://clawhub.ai/haiyangchenbj/skills/running-coach) <br>
- [Session Types](references/session_types.md) <br>
- [Heart Rate Zone Calculation](references/zone_calc.md) <br>
- [Periodized Training Phases](references/periodization.md) <br>
- [Injury Assessment Decision Tree](references/injury_check.md) <br>
- [Report Templates](references/report_template.md) <br>
- [Profile Schema](references/profile_schema.md) <br>
- [Pace System & Fitness Estimation](references/pace_system.md) <br>
- [Pre / During / Post: Warm-up / Cool-down / Activation](references/warmup_cooldown.md) <br>
- [Strength Training & Recovery](references/strength_recovery.md) <br>
- [Nutrition & Fueling](references/nutrition.md) <br>
- [Race Strategy](references/race_tactics.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Configuration] <br>
**Output Format:** [Structured Markdown reports, tables, plans, and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May suggest updates to the user's local running profile or training log after confirmation; degrades to text reports when storage is unavailable.] <br>

## Skill Version(s): <br>
1.2.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
