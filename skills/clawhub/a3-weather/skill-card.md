## Description:

Weather for daily briefings and meeting alerts (OpenWeatherMap) - today's one-line summary or the forecast at a meeting time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rusheel080703](https://clawhub.ai/user/rusheel080703)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use an agent to add a concise local weather summary to a daily briefing or a forecast for a meeting time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags network access and environment settings whose permissions are not declared.

Mitigation: Review the suspicious verdict before installation, and install only when access to the OpenWeatherMap destination and the required API key is explicitly limited and declared.

Risk: Weather lookups send a location and units to OpenWeatherMap together with the API key; a meeting city may be included when supplied.

Mitigation: Use only a trusted API key and pass a plain city location only when its disclosure is acceptable; otherwise use the configured default location.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rusheel080703/skills/a3-weather)
- [OpenWeatherMap API endpoint](https://api.openweathermap.org)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text weather summary or JSON weather data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides current conditions and a next-24-hour summary, or a forecast near a requested time within the five-day forecast window. Results are cached for 30 minutes.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
