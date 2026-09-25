## Description:

Get current weather and forecasts (no API key required).

This skill is ready for commercial/non-commercial use.

## Publisher:

[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve current weather, compact conditions, forecasts, or JSON weather data without requiring API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather requests contact third-party services and may reveal the queried city, airport code, or coordinates.

Mitigation: Use a nearby city, airport code, or coarse coordinates instead of an exact private address when privacy matters.

## Reference(s):

- [ClawHub Weather skill page](https://clawhub.ai/legionspace-hackathon/skills/weather)
- [wttr.in help](https://wttr.in/:help)
- [Open-Meteo documentation](https://open-meteo.com/en/docs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, text, JSON, files]

**Output Format:** [Markdown guidance with bash commands and possible plain-text, JSON, or PNG service responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and contacts public weather services; no API key is required.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
