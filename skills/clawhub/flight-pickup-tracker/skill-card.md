## Description: <br>
Track a flight in real-time and notify when to leave for airport pickup based on distance to destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People coordinating airport pickups use this skill to monitor an arriving flight, estimate airport drive time, and decide when to leave for pickup. Agents use it to gather flight, destination, pickup-origin, and timing details before proposing scheduled monitoring and user alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a saved home address or pickup origin and send route requests to Google Maps. <br>
Mitigation: Confirm the pickup origin and Google Maps API use with the user before each monitoring session, and avoid reusing a saved home address without explicit consent. <br>
Risk: The skill may set up repeated flight checks without a clear monitoring window. <br>
Mitigation: Confirm the flight, destination airport, start time, polling cadence, and stop condition before scheduling repeated checks. <br>
Risk: Flight status and leave-by estimates can be wrong when live position data is stale, the flight number maps to multiple legs, or traffic changes quickly. <br>
Mitigation: Treat leave-by times as estimates, verify the route and airport for the intended flight, and recalculate before sending pickup alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/flight-pickup-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require a flight code, destination airport, pickup origin, scheduled timing, and a Google Maps API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
