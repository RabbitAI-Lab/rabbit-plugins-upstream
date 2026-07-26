## Description: <br>
Austrian rail travel planner for planning journeys, checking station arrivals and departures, and viewing service disruptions via ÖBB Scotty. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manmal](https://clawhub.ai/user/manmal) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and travel-planning agents use this skill to look up Austrian public transport stations, plan routes, check station boards, and review service disruptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel-search details such as station names, routes, dates, and times are sent to the ÖBB Scotty API. <br>
Mitigation: Use normal station, date, and time inputs and avoid entering sensitive personal context into travel searches. <br>
Risk: The shell helpers rely on local bash, curl, and jq behavior when making external API calls. <br>
Mitigation: Run the skill with trusted system versions of bash, curl, and jq and review commands before execution. <br>


## Reference(s): <br>
- [ÖBB Scotty HAFAS API endpoint](https://fahrplan.oebb.at/bin/mgate.exe) <br>
- [ClawHub skill page](https://clawhub.ai/manmal/skills/oebb-scotty) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bash, curl, and jq; outputs station search, trip, station board, and disruption data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
