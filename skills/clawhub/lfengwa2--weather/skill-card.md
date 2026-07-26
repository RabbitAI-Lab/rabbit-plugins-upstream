## Description: <br>
Query current conditions and 1-10 day weather forecasts for cities, counties, districts, or coordinates in China, including temperature, apparent temperature, humidity, precipitation, wind, UV, sunrise, and sunset. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lfengwa2](https://clawhub.ai/user/lfengwa2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer Chinese or English weather questions for locations in mainland China, Hong Kong, Macao, or Taiwan. It resolves place names or coordinates, retrieves Open-Meteo data, and guides the agent to summarize current conditions and requested forecasts without fabricating missing values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queried place names or precise coordinates are sent to Open-Meteo. <br>
Mitigation: Avoid entering highly sensitive exact locations when that privacy tradeoff is not acceptable. <br>
Risk: Forecasts may be mistaken for official safety warnings during severe weather. <br>
Mitigation: Treat results as model forecasts and verify active alerts with the China Meteorological Administration or relevant local authority for safety-critical conditions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lfengwa2/skills/weather) <br>
- [Open-Meteo geocoding API endpoint](https://geocoding-api.open-meteo.com/v1/search) <br>
- [Open-Meteo forecast API endpoint](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; script output is plain text or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Weather summaries include source and retrieval time when returned by the script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
