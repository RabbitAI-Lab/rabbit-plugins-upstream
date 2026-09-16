## Description:

Comprehensive beach surf conditions via mcporter MCP call. Use when asked about surf, waves, swim conditions, rip currents, or beach safety at any beach worldwide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to retrieve surf, UV, wind, temperature, rip-current, and beach-safety reports for named beaches or coordinates. Outputs should support planning and situational awareness, not replace lifeguards, posted warnings, or official local advisories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce reassuring safety guidance when important hazard data is missing or official alerts are not incorporated.

Mitigation: Treat outputs as informational only and check lifeguards, posted warnings, and official local advisories before entering the water.

Risk: Requested beach names and coordinates are sent to external geocoding and weather providers.

Mitigation: Avoid querying sensitive locations and review relevant provider privacy and usage terms before deployment.

Risk: The overall safety score can understate danger when upstream data sources fail or return incomplete data.

Mitigation: Review raw conditions, unavailable fields, and official alerts instead of relying only on the summarized safety score.

## Reference(s):

- [Nominatim OpenStreetMap search API](https://nominatim.openstreetmap.org/search)
- [Photon geocoder API](https://photon.komoot.io/api/)
- [NOAA National Weather Service API](https://api.weather.gov)
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast)
- [Open-Meteo Marine API](https://marine-api.open-meteo.com/v1/marine)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text reports and structured JSON from MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on external geocoding and weather APIs; outputs are informational and are not official safety determinations.]

## Skill Version(s):

1.1.3 (source: server release metadata; artifact MCP server reports 1.1.3; SKILL.md frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
