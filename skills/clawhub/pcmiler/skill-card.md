## Description: <br>
PC*Miler provides REST API examples for retrieving route coordinates and geocoding addresses with an authenticated PC*Miler API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nchoudhury-trimble](https://clawhub.ai/user/nchoudhury-trimble) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and logistics teams use this skill as a quick reference for making authenticated PC*Miler REST API calls that return route path coordinates or geocode an address. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the examples sends route stops, coordinates, or addresses to PC*Miler. <br>
Mitigation: Submit location data only when authorized and when the provider's handling terms are acceptable for the use case. <br>
Risk: The skill requires access to a PC*Miler API key. <br>
Mitigation: Use a dedicated or restricted API key where possible and avoid exposing the key in prompts, logs, or shared command history. <br>


## Reference(s): <br>
- [PC*Miler ClawHub Skill Page](https://clawhub.ai/nchoudhury-trimble/skills/pcmiler) <br>
- [PC*Miler Route Reports API Example](https://pcmiler.alk.com/apis/rest/v1.0/Service.svc/route/routeReports?stops=-75.173297%2C39.942892%3B-74.83153%2C39.61703%3B-74.438942%2C39.362469&reports=RoutePath) <br>
- [PC*Miler Locations API Example](https://pcmiler.alk.com/apis/rest/v1.0/Service.svc/locations?street=1%20Independence%20Way&city=princeton&state=nj&country=US&postcode=08540&postcodeFilter=us&region=NA&dataset=Current) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and a valid PCMILER_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
