## Description: <br>
Track a flight in real time and notify when to leave for airport pickup based on distance to destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to coordinate airport pickups for a named flight by tracking flight progress, estimating drive time, and producing leave-by guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full drive-time mode can send the user's pickup address to Google Maps. <br>
Mitigation: Use basic mode when address disclosure is not desired, and confirm the pickup address with the user before using full drive-time mode. <br>
Risk: Packaging appears incomplete because the documented drive-time helper is missing from the artifact. <br>
Mitigation: Review or add the missing drive-time script before relying on the skill for operational pickup timing. <br>
Risk: Same-callsign or same-flight-number matches can produce incorrect flight tracking. <br>
Mitigation: Pass the origin airport for route sanity checking and verify the flight is on the expected route. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/flight-pickup-tracker) <br>
- [OpenSky Network API](https://opensky-network.org/api) <br>
- [AirLabs API](https://airlabs.co/api/v9) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON status output from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flight tracking polls external services; full drive-time mode may require a Google Maps API key and user-confirmed pickup address.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
