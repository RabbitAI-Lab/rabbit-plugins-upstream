## Description: <br>
Get current weather and forecasts (no API key required). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to retrieve current weather, compact forecasts, and JSON weather data for cities, airport codes, or coordinates without an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weather queries may disclose the city, airport code, or coordinates entered by the user to public weather services. <br>
Mitigation: Use coarse locations when possible and avoid precise home addresses or sensitive operational locations. <br>
Risk: Weather availability and response accuracy depend on public third-party weather services. <br>
Mitigation: Use the Open-Meteo fallback when wttr.in is unavailable and review returned data before relying on it for decisions. <br>


## Reference(s): <br>
- [ClawHub Weather skill](https://clawhub.ai/legionspace-hackathon/skills/weather) <br>
- [wttr.in help](https://wttr.in/:help) <br>
- [Open-Meteo documentation](https://open-meteo.com/en/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON weather-service responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and sends requested locations to public weather services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
