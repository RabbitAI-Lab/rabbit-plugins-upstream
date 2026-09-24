## Description:

Query current conditions and 1-10 day forecasts for cities, counties, districts, or coordinates in mainland China, Hong Kong, Macao, and Taiwan, including temperature, humidity, precipitation, wind, UV, sunrise, and sunset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lfengwa2](https://clawhub.ai/user/lfengwa2)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer weather questions in Chinese or English for China-region locations, using Open-Meteo current conditions and 1-10 day forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: City names, districts, or coordinates requested by the user are sent to Open-Meteo over HTTPS.

Mitigation: Avoid exact private coordinates unless needed, and use broader place names when that is sufficient.

Risk: Weather forecasts are not official warnings or guarantees.

Mitigation: For severe weather, verify active alerts with the China Meteorological Administration or the relevant local authority.

Risk: The external weather API can be unavailable or return incomplete data.

Mitigation: Report failures plainly and do not substitute fabricated values.

## Reference(s):

- [Weather skill page](https://clawhub.ai/lfengwa2/skills/weather)
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search)
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text weather summary or JSON from the bundled script, typically incorporated into a Markdown response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes resolved location, retrieval time, Open-Meteo source, and official-warning caveat when relevant.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
