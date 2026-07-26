## Description: <br>
Creates personalized triathlon, marathon, and ultra-endurance training plans with sport-specific workouts, training zones, and race-day strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shiv19](https://clawhub.ai/user/shiv19) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External athletes and endurance coaches use this skill to assess training history, validate goals and constraints, and generate periodized plans for triathlon, marathon, and ultra-endurance events. The skill can work from manually provided fitness data or Strava-backed local analysis when the user authorizes that workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive athlete data, goals, schedules, health context, and private coaching notes may be retained under ~/.endurance-coach. <br>
Mitigation: Ask the user before Strava authorization or persistent local storage, disclose the local files involved, and periodically review or delete Athlete_Context.md, coach.db, and saved notes when retention is not desired. <br>
Risk: The Strava-backed workflow uses an external endurance-coach npm CLI and may sync private activity data. <br>
Mitigation: Run Strava authorization and sync commands only after the user confirms they are comfortable with that account access and local data sync. <br>
Risk: Race nutrition, caffeine, field testing, and high-volume training guidance may be inappropriate for some athletes. <br>
Mitigation: Treat the guidance as general coaching support, validate plans with the athlete, and involve a qualified coach or clinician for injury, medical, nutrition, or unusually high-load concerns. <br>


## Reference(s): <br>
- [Athlete Assessment Guide](reference/assessment.md) <br>
- [Training Load Management](reference/load-management.md) <br>
- [Periodization & Progressive Overload](reference/periodization.md) <br>
- [Athlete Assessment Commands](reference/queries.md) <br>
- [Race Execution & Nutrition Strategy](reference/race-day.md) <br>
- [Database Schema Reference](reference/schema.md) <br>
- [Workout Templates Reference](reference/templates.md) <br>
- [Workout Library](reference/workouts.md) <br>
- [Training Zones & Field Testing](reference/zones.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with compact YAML v2.0 training plans, shell commands, and rendered HTML plan output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local athlete context, coach notes, compact YAML plans, and HTML renders when the user authorizes those workflows.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
