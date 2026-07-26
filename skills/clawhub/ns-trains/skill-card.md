## Description: <br>
Check Dutch train schedules, departures, disruptions, and plan journeys using the NS API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eggressive](https://clawhub.ai/user/eggressive) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travelers and commute-focused agents use this skill to look up Dutch rail departures, arrivals, disruptions, station matches, and journey options from the NS API. <br>

### Deployment Geography for Use: <br>
Global, for Netherlands rail information. <br>

## Known Risks and Mitigations: <br>
Risk: Station, route, and optional commute locations are sent to the NS API. <br>
Mitigation: Use the skill only when sharing those travel details with the NS API is acceptable. <br>
Risk: The NS subscription key is required for API calls and could be exposed if pasted into files, commits, or chat logs. <br>
Mitigation: Keep NS_SUBSCRIPTION_KEY in runtime secrets or environment injection, and rotate the key in the NS API portal if exposure is suspected. <br>
Risk: Travel results depend on live NS API availability and response accuracy. <br>
Mitigation: Treat returned schedule and disruption information as current API data and verify critical journeys with an official NS channel when needed. <br>


## Reference(s): <br>
- [NS API Portal](https://apiportal.ns.nl/) <br>
- [NS API Starter Guide](https://apiportal.ns.nl/startersguide) <br>
- [NS Trains ClawHub Release](https://clawhub.ai/eggressive/skills/ns-trains) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal text and agent-facing guidance with command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include station names, departure and arrival times, delays, duration, transfers, platform numbers, disruption warnings, and crowdedness forecasts when returned by the NS API.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
