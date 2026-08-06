## Description: <br>
Route-aware weather forecasts for alpine climbs. Terrain-adjusted timing, multi-day camp-to-summit itineraries, three-source verification, descent conditions, and pace calibration that learns your speed over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sundiraman](https://clawhub.ai/user/sundiraman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External climbers and assisting agents use this skill to generate route-aware alpine weather forecasts, timing windows, and descent-condition guidance for named routes, GPX tracks, or simple elevation profiles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forecasts and timing guidance may be wrong or overconfident for real alpine decisions. <br>
Mitigation: Treat outputs as planning aids only and verify conditions with authoritative local forecasts, guide reports, avalanche bulletins, and on-route judgment before climbing. <br>
Risk: GPX files, coordinates, route names, and calibration history can reveal sensitive activity patterns. <br>
Mitigation: Avoid sharing sensitive tracks or route details unnecessarily and review or delete the locally stored alpinist profile when privacy matters. <br>
Risk: External weather sources may be unavailable, limited by geography or forecast range, or change format. <br>
Mitigation: Check source confidence, rerun forecasts closer to the climb date, and cross-check against multiple current sources before relying on the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sundiraman/skills/alpinist-route-forecast) <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [NOAA/NWS API](https://api.weather.gov) <br>
- [Mountain-Forecast](https://www.mountain-forecast.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown narrative with command snippets and optional JSON from the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Forecast quality depends on route data, GPX density, weather-source availability, and the date range supported by each provider.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
