## Description: <br>
Weather and pollen reports for any location using free APIs. Get current conditions, forecasts, and pollen data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to fetch current weather conditions, a short forecast, and pollen information for a configured location. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may display a requested location name while querying configured/default coordinates rather than geocoding arbitrary cities. <br>
Mitigation: Set WEATHER_LAT, WEATHER_LON, and WEATHER_LOCATION for the intended area, and do not rely on the location argument for arbitrary-city accuracy unless geocoding is added. <br>
Risk: Weather and pollen reports depend on Open-Meteo and Pollen.com availability and responses. <br>
Mitigation: Treat unavailable or stale API responses as incomplete information and confirm important weather or allergy decisions with an authoritative source. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thesethrose/skills/weather-pollen) <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [Pollen.com Current Forecast](https://www.pollen.com/forecast/current/pollen/75409) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, guidance] <br>
**Output Format:** [Markdown text report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Weather and pollen data are fetched from external free APIs; the displayed location can be configured with environment variables.] <br>

## Skill Version(s): <br>
1.0.3 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
