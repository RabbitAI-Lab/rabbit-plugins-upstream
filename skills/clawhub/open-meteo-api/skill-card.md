## Description: <br>
Fetch weather forecasts, current conditions, historical weather, and air quality with the free Open-Meteo API (no API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer weather, climate, air quality, and related location-based data questions through Open-Meteo endpoints or the bundled Python helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weather queries may send place names, coordinates, dates, and requested variables to Open-Meteo over HTTPS. <br>
Mitigation: Avoid precise sensitive locations unless needed, and disclose external API use where users or deployment policy require it. <br>
Risk: The bundled script covers common forecasts, while historical, air quality, marine, flood, climate, and other advanced tasks require direct API calls. <br>
Mitigation: Use the documented endpoint references for advanced tasks and validate required parameters, date ranges, timezones, and API error reasons. <br>
Risk: Commercial deployments may need Open-Meteo customer endpoints or an API key rather than the no-key free path. <br>
Mitigation: Confirm Open-Meteo terms for the deployment and configure approved customer endpoints or credentials when required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nanookai/skills/open-meteo-api) <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search) <br>
- [Open-Meteo Other APIs](artifact/references/other-apis.md) <br>
- [Open-Meteo Forecast API Variable Catalog](artifact/references/weather-variables.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with API URLs, code examples, shell commands, and optional JSON output from the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled helper performs HTTPS requests to Open-Meteo and can emit either formatted text or raw JSON.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
