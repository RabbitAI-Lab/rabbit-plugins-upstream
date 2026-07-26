## Description: <br>
Plans multi-day road trips in mainland China with Amap APIs, generating continuous-route personal map QR codes and daily Markdown itinerary details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onlydreams](https://clawhub.ai/user/onlydreams) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to design mainland China road trip routes, control daily driving time, check supply needs, and produce a shareable Amap route plus a day-by-day itinerary. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Live road, weather, attraction, and holiday information can change after an itinerary is generated. <br>
Mitigation: Verify official traffic, weather, attraction, and holiday sources for the actual departure dates before relying on the route. <br>
Risk: The workflow may use sensitive location, route, and travel-date details with Amap and related live-information sources. <br>
Mitigation: Share only the minimum location details needed for planning and avoid placing real API keys in prompts, source files, or generated documents. <br>
Risk: Missing Amap API credentials or the personal-map dependency can prevent map and QR-code generation. <br>
Mitigation: Run the documented preflight checks first and stop with setup guidance when the dependency or API key is unavailable. <br>


## Reference(s): <br>
- [Source repository](https://github.com/Onlydreams/road-trip-planner) <br>
- [Amap Personal Map dependency](https://clawhub.ai/lbs-amap/personal-map) <br>
- [Amap Open Platform](https://lbs.amap.com/) <br>
- [Amap SDK Skills repository](https://github.com/amap-demo/amap-sdk-skills) <br>
- [Seasonal Checklist](references/seasonal.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, route details, practical guidance, setup snippets, and QR-code image or fallback links when available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Amap API access and the personal-map dependency; QR route output depends on verified poiId values and current service availability.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
