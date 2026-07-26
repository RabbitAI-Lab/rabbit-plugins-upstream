## Description: <br>
Search for Israel Rail train schedules using the railil CLI, including routes between stations, fuzzy station search, date and time filters, and JSON, Markdown, table, or text output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lirantal](https://clawhub.ai/user/lirantal) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to look up Israel Rail train schedules through the railil CLI, selecting origin and destination stations and optionally filtering by date, time, result limit, and output format. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on installing and running the third-party railil npm CLI globally. <br>
Mitigation: Install it only in environments where that third-party CLI is approved, and review the package before use when organizational policy requires dependency review. <br>
Risk: Schedule lookups depend on the railil CLI and its upstream train schedule data being available and current. <br>
Mitigation: Treat results as travel-planning assistance and confirm critical itinerary details against an authoritative rail schedule source before acting. <br>


## Reference(s): <br>
- [Railil GitHub project](https://github.com/lirantal/railil) <br>
- [ClawHub Railil skill page](https://clawhub.ai/lirantal/skills/skill-railil) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, JSON, Markdown, Text] <br>
**Output Format:** [Markdown guidance with railil CLI examples and optional CLI output in JSON, Markdown, table, or text format.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the third-party railil npm CLI to be available as a global command.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
