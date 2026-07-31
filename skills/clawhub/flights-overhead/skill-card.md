## Description: <br>
See what flights are above you right now. Identify contrails, planes overhead, and nearby air traffic using OpenSky Network (free, no key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to identify nearby aircraft, contrails, and overhead flights from an approximate latitude/longitude. The skill helps present nearby flight details such as callsign, airline, altitude, heading, distance, and optional route context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approximate user coordinates may be sent to OpenSky before the user understands or confirms the location source. <br>
Mitigation: Confirm or ask for the user's location source before querying flights, and use an approximate city or area when that is sufficient. <br>
Risk: Optional route enrichment may read stored user location context or perform extra web searches beyond the core nearby-flight lookup. <br>
Mitigation: Use explicitly provided or permitted location data, and perform route web searches only when the user wants extra flight detail. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/flights-overhead) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown response with optional shell commands and JSON flight data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include nearby aircraft callsigns, airline names, flight numbers, altitude, heading, distance, and location-use guidance.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
