## Description:

Current weather and forecasts with web_fetch, falling back to wttr.in curl for locations, rain, temperature, travel planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

People can ask an agent for current conditions, rain and temperature checks, short forecasts, or weather information for travel planning. Provide a city, region, airport code, or coordinates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather lookups send the supplied location to an external weather service.

Mitigation: Use a city-level location when sufficient, and avoid sharing precise coordinates unless you are comfortable transmitting them.

## Reference(s):

- [wttr.in help](https://wttr.in/:help)
- [wttr.is fallback service](https://wttr.is/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown weather summaries with current conditions and forecast details; shell command examples for fallback lookups.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weather results depend on the supplied location and available service data.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
