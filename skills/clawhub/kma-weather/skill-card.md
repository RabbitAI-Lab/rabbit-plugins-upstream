## Description: <br>
Gets weather from the Korea Meteorological Administration, including current conditions, 3-10 day forecasts, precise local forecasts on a 5 km grid, and weather warnings or advisories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steamb23](https://clawhub.ai/user/steamb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve South Korea weather observations, short-term and mid-term forecasts, and active weather warnings from KMA/data.go.kr APIs. It is useful when a task needs Korean local weather data, KMA warning status, or grid-based forecasts rather than broad city-level weather. <br>

### Deployment Geography for Use: <br>
South Korea <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a KMA/data.go.kr service key and sends weather query parameters to KMA API endpoints. <br>
Mitigation: Use a dedicated API key, keep any configuration containing the key private, and rotate or revoke the key if it may have been exposed. <br>
Risk: Several documented KMA endpoints are not implemented, including detailed warning messages, warning lists, and mid-term land, temperature, and sea forecasts. <br>
Mitigation: Check the implementation status before relying on this skill for unsupported KMA endpoints or emergency decision workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/steamb23/skills/kma-weather) <br>
- [KMA short-term forecast API](https://www.data.go.kr/data/15084084/openapi.do) <br>
- [KMA weather warnings API](https://www.data.go.kr/data/15000415/openapi.do) <br>
- [KMA mid-term forecast API](https://www.data.go.kr/data/15059468/openapi.do) <br>
- [Short-term Forecast API Reference](references/api-forecast.md) <br>
- [Weather Warnings API Reference](references/api-warnings.md) <br>
- [Mid-term Forecast API Reference](references/api-midterm.md) <br>
- [KMA Category Codes](references/category-codes.md) <br>
- [Implementation Status](implement-status.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Plain text or JSON weather output, with Markdown guidance and shell command examples in the skill instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and KMA_SERVICE_KEY; forecast scripts call KMA/data.go.kr endpoints and auto-paginate API results.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
