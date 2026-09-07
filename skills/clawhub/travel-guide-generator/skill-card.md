## Description:

旅游攻略生成器 helps an agent create multilingual, structured travel guides with daily itineraries, hotels, food, budgets, safety notes, responsive HTML, and optional Amap route estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmmg55](https://clawhub.ai/user/gmmg55)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to turn a destination, trip length, origin, and preferences into a complete travel guide. It is suited for leisure itineraries, including romantic, weekend, self-driving, family, and multilingual trips, but not booking, visa processing, business travel, or non-tourism routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated guide files may contain detailed trip locations and schedules.

Mitigation: Use a dedicated output folder and review generated files before sharing them with other people.

Risk: When Amap routing is enabled, origin and destination text is sent to Amap for route estimates.

Mitigation: Use routing only when appropriate for the trip data, prefer a temporary AMAP_KEY, and avoid pasting API keys into chat.

## Reference(s):

- [Guide schema](artifact/references/guide-schema.json)
- [Daily itinerary HTML specification](artifact/references/daily-itinerary-spec.md)
- [HTML design specification](artifact/references/design-spec.md)
- [Amap Open Platform](https://lbs.amap.com/)
- [Amap geocoding API](https://restapi.amap.com/v3/geocode/geo)
- [Amap driving route API](https://restapi.amap.com/v3/direction/driving)
- [Amap distance API](https://restapi.amap.com/v3/distance)
- [Amap POI search API](https://restapi.amap.com/v3/place/text)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Structured JSON inputs with generated HTML, Markdown, ICS, GeoJSON, normalized JSON, and conversational travel-guide prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated guide files may include detailed trip locations and schedules; route data may be estimated when Amap is unavailable.]

## Skill Version(s):

2.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
