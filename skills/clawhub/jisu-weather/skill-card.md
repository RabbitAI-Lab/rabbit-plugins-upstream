## Description:

查询实时天气、7 天预报、24 小时逐时、空气质量与生活指数，可查城市列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current weather, seven-day forecasts, hourly forecasts, air quality, lifestyle indices, and supported city data through JisuAPI. It is intended for weather-answering workflows where the agent turns a user's city, city ID, city code, coordinates, or IP input into a weather lookup and natural-language response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather query details and JISU_API_KEY are sent to JisuAPI.

Mitigation: Use only if JisuAPI is acceptable for the deployment; prefer city-based lookup when precise location or IP lookup is unnecessary.

Risk: Coordinate or IP-based lookups can disclose more specific location information than a city name.

Mitigation: Ask for the least precise location input needed to answer the weather request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/jisu-weather)
- [JisuAPI homepage](https://www.jisuapi.com/)
- [JisuAPI weather API documentation](https://www.jisuapi.com/api/weather/)
- [JisuAPI weather query endpoint](https://api.jisuapi.com/weather/query)
- [JisuAPI weather city endpoint](https://api.jisuapi.com/weather/city)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; sends weather lookup parameters and the API key to JisuAPI.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
