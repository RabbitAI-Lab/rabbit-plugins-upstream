## Description: <br>
Fetches aviation weather data, including METAR, TAF, and PIREPs, from aviationweather.gov for pilot weather checks and flight-planning workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dimitryvin](https://clawhub.ai/user/dimitryvin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Pilots, dispatchers, aviation developers, and flight-planning agents use this skill to retrieve airport observations, terminal forecasts, and nearby pilot reports for weather awareness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Airport codes and PIREP latitude/longitude search areas are sent to aviationweather.gov. <br>
Mitigation: Use the skill only when sharing those weather-query inputs with aviationweather.gov is acceptable. <br>
Risk: Weather output may be incomplete, unavailable, delayed, or inappropriate as the sole basis for flight-critical decisions. <br>
Mitigation: Verify results through official aviation briefing channels before operational use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dimitryvin/skills/aviation-weather) <br>
- [Aviation Weather Center API](https://aviationweather.gov/api/data) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown-formatted weather summaries or raw JSON from a Python CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches METAR, TAF, and PIREP data from aviationweather.gov; PIREP searches can include latitude and longitude.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
