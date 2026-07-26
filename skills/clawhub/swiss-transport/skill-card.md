## Description: <br>
Swiss Public Transport provides real-time Swiss train, bus, tram, and boat schedule information, including station search, departure boards, journey planning, and connection details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to look up Swiss public transport stations, departures, journey options, and connection details through transport.opendata.ch. It is suited for travel-planning questions about routes and schedules within Switzerland. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Route searches send origin, destination, date, and time details to transport.opendata.ch. <br>
Mitigation: Avoid using the skill for travel details that should remain private or sensitive. <br>
Risk: Real-time public transport data may change because schedules, delays, and platform assignments are time-sensitive. <br>
Mitigation: Check returned departure times, delays, and platform details near the time of travel. <br>


## Reference(s): <br>
- [Swiss Public Transport API](https://transport.opendata.ch) <br>
- [ClawHub skill page](https://clawhub.ai/xenofex7/skills/swiss-transport) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance] <br>
**Output Format:** [Plain text or Markdown with optional shell commands, Python helper usage, and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query the public transport.opendata.ch API; no API key is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
