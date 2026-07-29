## Description: <br>
Route-aware weather forecasts for alpine climbs. Terrain-adjusted timing, multi-day camp-to-summit itineraries, three-source verification, descent conditions, and pace calibration that learns your speed over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External alpinists, guides, and agents use this skill to turn a named route, GPX track, or simple elevation profile into terrain-adjusted mountain weather guidance with summit timing, descent conditions, confidence level, and source verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Route or summit coordinates are sent to external weather services, and calibration can save trip timing locally. <br>
Mitigation: Use the skill only for routes whose coordinates are acceptable to share with forecast providers; avoid calibration on shared machines or delete the local alpinist profile after use. <br>
Risk: Mountain forecasts can be uncertain, especially for longer lead times, summit winds, sparse GPX tracks, non-US NOAA coverage, or scraped Mountain-Forecast.com pages. <br>
Mitigation: Treat the output as planning support, keep the displayed confidence level with the forecast, cross-check available sources, and recheck conditions closer to the climb. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/alpinist-route-forecast) <br>
- [Open-Meteo forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [NOAA/NWS API](https://api.weather.gov) <br>
- [Mountain-Forecast.com](https://www.mountain-forecast.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON forecast summaries with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hourly route conditions, confidence levels, warnings, itinerary timing, verification from weather sources, and local pace-calibration updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
