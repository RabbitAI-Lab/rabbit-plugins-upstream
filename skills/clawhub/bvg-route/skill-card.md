## Description: <br>
Plans Berlin public-transport routes and next departures using the public v6.bvg.transport.rest API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jaysonsantos](https://clawhub.ai/user/jaysonsantos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travelers, residents, and agents use this skill to plan Berlin public-transit trips, check upcoming departures, and produce concise step-by-step route options with real-time refresh tokens when available. <br>

### Deployment Geography for Use: <br>
Germany (Berlin public-transport coverage) <br>

## Known Risks and Mitigations: <br>
Risk: Route planning can send origin, destination, timing, and stop details to the public BVG transport API. <br>
Mitigation: Avoid highly sensitive exact home, workplace, medical, or appointment locations when that privacy exposure matters. <br>
Risk: Transit recommendations can become stale as live departures, delays, and service conditions change. <br>
Mitigation: Refresh journeys or departures before relying on a route, especially near departure time. <br>
Risk: Running the helper script directly depends on local shell tooling. <br>
Mitigation: Use it only in an environment with bash, python3, curl, and jq available, and review command inputs before execution. <br>


## Reference(s): <br>
- [v6.bvg.transport.rest API](https://v6.bvg.transport.rest/api.html) <br>
- [Artifact API reference](references/API.md) <br>
- [ClawHub skill page](https://clawhub.ai/jaysonsantos/skills/bvg-route) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown route summaries with optional JSON journey details and shell/API command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include journey refresh tokens, stop IDs, departure and arrival times, transfers, walking distances, and step-by-step transit legs.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
