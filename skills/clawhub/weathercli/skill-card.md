## Description: <br>
Get current weather conditions and forecasts for any location worldwide. Returns structured data with temperature, humidity, wind, precipitation, and more. No API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjtf93](https://clawhub.ai/user/pjtf93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and external users use this skill to retrieve current weather, forecasts, and location metadata for travel planning, activity planning, and weather summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires network access and sends queried locations to Open-Meteo or related geocoding and weather services. <br>
Mitigation: Avoid submitting sensitive locations when that disclosure is not acceptable, and review service use policies for the deployment context. <br>
Risk: The installation guidance fetches weathercli from GitHub and includes an @latest install command. <br>
Mitigation: Review the upstream repository before deployment and prefer a pinned release or commit for stronger supply-chain control. <br>
Risk: The skill cannot operate offline. <br>
Mitigation: Use it only in environments where outbound network access to weather and geocoding services is allowed. <br>


## Reference(s): <br>
- [weathercli releases](https://github.com/pjtf93/weathercli/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON weather output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Weather results include location details, local timestamps, temperature, humidity, wind, precipitation, UV index, and forecast fields when requested.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
