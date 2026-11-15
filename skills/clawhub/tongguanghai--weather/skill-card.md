## Description:

Get the weather - current conditions, forecasts, and historical data for any location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tongguanghai](https://clawhub.ai/user/tongguanghai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for current, forecast, historical, and air-quality weather information for named places, postal codes, or coordinates. It also supports weather-aware lifestyle advice such as clothing, travel, UV, rain, and severe-weather guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather requests may send queried places or coordinates to Open-Meteo APIs.

Mitigation: Avoid precise private locations when that is sensitive, or use coarser locations and preferred language handling.

Risk: Weather summaries and lifestyle advice can be incomplete or unsuitable for safety-critical decisions.

Mitigation: Check authoritative local alerts before travel, outdoor work, or severe-weather response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tongguanghai/skills/weather)
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast)
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search)
- [Open-Meteo Air Quality API](https://air-quality-api.open-meteo.com/v1/air-quality)
- [Open-Meteo Historical Weather API](https://archive-api.open-meteo.com/v1/archive)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown or plain text weather summaries with current conditions, forecast details, and practical recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May adapt language and temperature units by region.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
