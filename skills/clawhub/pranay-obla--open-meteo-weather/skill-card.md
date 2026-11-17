## Description:

Current conditions and a short forecast for any city from the free Open-Meteo API (no API key, no account). Uses web_fetch only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pranay-obla](https://clawhub.ai/user/pranay-obla)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for current conditions and a short forecast for a city, including temperatures, conditions, wind, and precipitation chance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The requested city is sent to Open-Meteo and may be sent to wttr.in if the fallback is used; the security evidence also notes that a privacy notice is missing.

Mitigation: Tell users that the city may be shared with these weather services, and use a less specific location when appropriate.

Risk: The security analysis is partial because a local path-like reference could not be resolved.

Mitigation: Resolve the reference and review the updated security assessment before distributing the skill.

## Reference(s):

- [Open-Meteo](https://open-meteo.com)
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search?name=<city>&count=1&language=en&format=json)
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast)
- [wttr.in fallback](https://wttr.in/)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Concise natural-language weather report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Current conditions and a two-day forecast; defaults to Fahrenheit and mph, with metric units when requested; identifies the source used.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
