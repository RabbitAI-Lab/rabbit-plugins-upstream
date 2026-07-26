## Description: <br>
Fetch productivity analytics from RescueTime for screen time, productivity score, app usage, time tracking, daily or weekly activity reports, and computer activity summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rusynandriy](https://clawhub.ai/user/rusynandriy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, developers, and other RescueTime users use this skill to ask an agent for productivity summaries, app and site usage reports, category breakdowns, and screen-time trends from their RescueTime account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RescueTime reports can reveal work habits, app usage, screen time, and daily routines. <br>
Mitigation: Request only the reports and date ranges needed for the task, and avoid sharing outputs beyond the intended audience. <br>
Risk: The RescueTime API key can expose private productivity data if stored or shared carelessly. <br>
Mitigation: Store the API key securely, do not commit it to shared files, and remove it from prompts or logs that do not need it. <br>


## Reference(s): <br>
- [ClawHub RescueTime skill page](https://clawhub.ai/rusynandriy/skills/rescuetime) <br>
- [RescueTime API key management](https://www.rescuetime.com/anapi/manage) <br>
- [RescueTime analytic data API example](https://www.rescuetime.com/anapi/data?key=API_KEY&format=json&perspective=rank&restrict_kind=activity) <br>
- [RescueTime daily summary feed example](https://www.rescuetime.com/anapi/daily_summary_feed?key=API_KEY) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include RescueTime query parameters, date ranges, productivity categories, and converted time totals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
