## Description:

Provides 17 Gaode Map capabilities, including geocoding, POI search, nearby search, driving, transit, walking, and cycling route planning, weather lookup, and IP location without requiring the user to configure a Gaode API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer location, map search, route planning, weather, administrative district, and IP-location questions through Gaode Map-backed data tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Map searches, addresses, route endpoints, coordinates, weather city names, and possible IP-location requests are sent through the bundled proxy service.

Mitigation: Install only when that data flow is acceptable, avoid submitting highly sensitive locations, and do not set a sensitive PROXY_TOKEN unless it is intended for this proxy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/gaode-map-pro)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, JSON, API calls, guidance]

**Output Format:** [JSON responses with map, route, weather, location, or error data for the selected tool]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invoked as a command-line Python tool with a tool name and JSON parameters; results depend on the bundled proxy service and upstream map data.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
