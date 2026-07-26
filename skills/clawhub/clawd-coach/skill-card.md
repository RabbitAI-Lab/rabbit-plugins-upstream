## Description: <br>
Create personalized triathlon, marathon, and ultra-endurance training plans from Strava-linked or manually supplied fitness data, including periodized schedules, sport-specific workouts, zones, and race-day strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shiv19](https://clawhub.ai/user/shiv19) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External athletes and coaches use this skill to assess endurance training history, validate constraints and goals, and generate personalized plans for triathlon, marathon, and ultra-endurance events. It can work from manual fitness inputs or from Strava-synced activity history stored locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Strava connection flow asks users to provide sensitive OAuth material in chat, including a Client Secret and full redirect URL. <br>
Mitigation: Prefer manual entry or a safer OAuth flow when available; do not paste Strava secrets or full redirect URLs into ordinary chat unless transcript and log exposure risk is acceptable. <br>
Risk: The skill can store detailed fitness history from Strava in a local SQLite database. <br>
Mitigation: Install only if local storage of training history is acceptable, and protect or delete the local database according to the user's privacy needs. <br>
Risk: Training and nutrition recommendations can affect health, injury risk, and race-day fueling decisions. <br>
Mitigation: Treat outputs as coaching suggestions rather than medical advice, validate zones and plans with the athlete, and seek qualified medical guidance for injuries or health concerns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shiv19/skills/clawd-coach) <br>
- [Athlete Assessment Guide](artifact/reference/assessment.md) <br>
- [Training Load Management](artifact/reference/load-management.md) <br>
- [Periodization & Progressive Overload](artifact/reference/periodization.md) <br>
- [SQL Queries for Athlete Assessment](artifact/reference/queries.md) <br>
- [Race Execution & Nutrition Strategy](artifact/reference/race-day.md) <br>
- [Sport-Specific Workout Library](artifact/reference/workouts.md) <br>
- [Training Zones & Field Testing](artifact/reference/zones.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Files, Shell commands] <br>
**Output Format:** [Conversational coaching guidance with structured JSON training plans, optional rendered HTML files, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local plan JSON/HTML files and query or sync a local SQLite fitness database when Strava is connected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
