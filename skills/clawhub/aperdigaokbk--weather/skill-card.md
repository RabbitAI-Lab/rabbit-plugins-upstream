## Description:

Gets current weather and forecasts for a named location through wttr.in or Open-Meteo without requiring an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to answer current weather, temperature, precipitation, and forecast questions for a city, region, or airport code during normal workflows such as travel planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather queries are sent to wttr.in and may reveal the city, region, or airport code being checked.

Mitigation: Use coarse locations when possible and avoid sending sensitive exact locations through the weather query.

Risk: The skill is not intended for severe weather alerts, aviation or marine weather, historical weather, or climate analysis.

Mitigation: Use official or specialized sources for safety-critical alerts, aviation or marine operations, historical data, and climate analysis.

Risk: The external weather service may be rate limited or unavailable.

Mitigation: Avoid high-volume repeated requests and retry later or use an alternate weather source when the service is unavailable.

## Reference(s):

- [wttr.in help](https://wttr.in/:help)
- [ClawHub weather skill](https://clawhub.ai/aperdigaokbk/skills/weather)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and URL/query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl; no API key is needed; weather query locations are sent to wttr.in.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
