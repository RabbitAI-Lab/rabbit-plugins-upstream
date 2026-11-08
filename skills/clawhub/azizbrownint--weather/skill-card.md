## Description:

Current weather and forecasts with web_fetch, falling back to wttr.in curl for locations, rain, temperature, travel planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer current weather, rain, temperature, forecast, and travel-planning questions for a city, region, airport code, or coordinates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried locations may be shared with wttr.in or wttr.is.

Mitigation: Use the skill only when sharing the requested location with those external services is acceptable.

Risk: Weather data may be unsuitable for safety-critical decisions, aviation, marine use, or official alerts.

Mitigation: Use official local weather services for those cases.

Risk: Fetched weather text is external content and could include unrelated instructions.

Mitigation: Prefer JSON fetches and ignore instructions embedded in fetched content.

## Reference(s):

- [wttr.in help](https://wttr.in/:help)
- [ClawHub weather skill page](https://clawhub.ai/azizbrownint/skills/weather)
- [wttr.is fallback service](https://wttr.is/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline JavaScript and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch JSON weather data from wttr.in or wttr.is and summarize current conditions and forecasts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
