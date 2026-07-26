## Description: <br>
Get the weather — current conditions, forecasts, and historical data for any location. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tongguanghai](https://clawhub.ai/user/tongguanghai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer weather questions for named places, postal codes, or coordinates, including current conditions, forecasts, historical weather, air quality, and practical travel or clothing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weather queries may disclose the requested location to Open-Meteo services. <br>
Mitigation: Avoid submitting sensitive locations unless sharing them with the weather API is acceptable. <br>
Risk: Weather and lifestyle guidance may be incomplete or stale for high-impact decisions. <br>
Mitigation: Use official local alerts and professional judgment for safety-critical travel or severe-weather decisions. <br>


## Reference(s): <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search) <br>
- [Open-Meteo Air Quality API](https://air-quality-api.open-meteo.com/v1/air-quality) <br>
- [Open-Meteo Historical Weather API](https://archive-api.open-meteo.com/v1/archive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown weather summaries with structured conditions, forecasts, advice, and warnings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt language and temperature units based on the queried location.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
