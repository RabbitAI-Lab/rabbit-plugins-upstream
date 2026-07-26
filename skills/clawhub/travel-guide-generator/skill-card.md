## Description: <br>
Travel Guide Generator creates responsive, multilingual travel-guide HTML files and companion text itineraries for leisure travel requests, with optional AMap route calculations and fallback estimates when live data is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gmmg55](https://clawhub.ai/user/gmmg55) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel planners use this skill to turn destination, trip length, departure city, and style preferences into an HTML travel guide plus a readable itinerary summary. It is aimed at leisure travel such as romantic, weekend, family, self-drive, and casual city trips, not booking, visa, business-travel, or payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documentation asks users to paste an AMap API key into chat and have the agent persist it, which could expose credentials. <br>
Mitigation: Configure AMAP_KEY directly through the shell, operating system environment settings, or a secret manager; avoid pasting secrets into chat and rotate any key that was exposed. <br>
Risk: Travel routes, prices, restaurants, hotel areas, and transport details may be estimated or based on general travel knowledge when live lookup fails. <br>
Mitigation: Keep estimate and verification labels visible in the generated guide, and confirm bookings, prices, schedules, local conditions, and safety details with authoritative sources before travel. <br>


## Reference(s): <br>
- [Daily Itinerary HTML Specification](references/daily-itinerary-spec.md) <br>
- [Travel Guide HTML Design Specification](references/design-spec.md) <br>
- [AMap Open Platform](https://lbs.amap.com/) <br>
- [AMap Geocoding API](https://restapi.amap.com/v3/geocode/geo) <br>
- [AMap Driving Direction API](https://restapi.amap.com/v3/direction/driving) <br>
- [AMap Distance API](https://restapi.amap.com/v3/distance) <br>
- [AMap POI Search API](https://restapi.amap.com/v3/place/text) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Responsive HTML file plus Markdown-style itinerary summary and optional JSON route/search helper output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated travel details may include live AMap route data when AMAP_KEY is configured, or clearly labeled estimates and general travel knowledge when API or search data is unavailable.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and metadata.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
