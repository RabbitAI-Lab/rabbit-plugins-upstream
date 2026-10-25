## Description:

Provides location-based weather forecasts, historical conditions, air quality, marine and flood data, alerts, and practical planning advice through Open-Meteo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fbbyqsyea](https://clawhub.ai/user/fbbyqsyea)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can check local forecasts and historical conditions, compare locations, and use weather, air-quality, marine, and flood data to inform daily plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried city names or precise coordinates are sent to Open-Meteo.

Mitigation: Use coarse locations when exact coordinates are unnecessary.

Risk: Recent weather responses are stored in a local cache.

Mitigation: Keep WEATHER_CACHE_DIR in a trusted location and clear cached responses when needed.

Risk: Weather alerts can be unavailable on networks that cannot resolve the alerts service.

Mitigation: Check a local official alert source when severe weather decisions depend on timely warnings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fbbyqsyea/skills/weather-openmeteo)
- [Open-Meteo weather forecast data source](https://api.open-meteo.com/v1/forecast)
- [Open-Meteo air-quality data source](https://air-quality-api.open-meteo.com/v1/air-quality)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown prose or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Location-specific conditions and planning advice; times reflect the queried location's time zone.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
