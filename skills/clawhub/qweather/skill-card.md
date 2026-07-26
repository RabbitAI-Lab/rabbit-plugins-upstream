## Description: <br>
天气查询：使用和风天气（JWT+Host）获取实时天气与未来预报；支持城市名/LocationID/经纬度；缺省地点可用 QWEATHER_DEFAULT_LOCATION。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[murphys7017](https://clawhub.ai/user/murphys7017) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer weather questions with current conditions and forecasts for a requested city, LocationID, or latitude/longitude. It is intended for weather lookups that should use QWeather or configured fallback weather services instead of general web search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires locally configured QWeather credentials and placeholder key material appears in the artifact. <br>
Mitigation: Replace placeholder configuration and key material with local secrets, keep private keys out of shared logs and repositories, and verify QWeather credential paths before use. <br>
Risk: Location queries are sent to external weather services, including an Open-Meteo fallback that is under-disclosed in the skill summary. <br>
Mitigation: Inform users when fallback providers are used and avoid submitting sensitive or unnecessary location details. <br>
Risk: The JWT helper can print token and payload details when used for debugging. <br>
Mitigation: Avoid sharing logs from token generation or debug sessions and rotate credentials if token material is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/murphys7017/skills/qweather) <br>
- [QWeather GeoAPI city lookup endpoint](https://geoapi.qweather.com/v2/city/lookup) <br>
- [QWeather current weather endpoint](https://devapi.qweather.com/v7/weather/now) <br>
- [Open-Meteo geocoding endpoint](https://geocoding-api.open-meteo.com/v1/search) <br>
- [Open-Meteo forecast endpoint](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, configuration guidance] <br>
**Output Format:** [Structured weather results and concise natural-language guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses requested or default location input and may return current conditions, daily forecasts, hourly forecasts, warnings, precipitation, and actionable API error guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
