## Description: <br>
Access Apple WeatherKit REST API for detailed weather forecasts using JWT authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimmcq](https://clawhub.ai/user/jimmcq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to fetch current Apple WeatherKit weather data and detailed forecasts for specified coordinates, date ranges, time zones, data sets, and country codes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a WeatherKit-specific Apple private key. <br>
Mitigation: Keep the .p8 key outside shared folders with restricted file permissions, and rotate or revoke it if disclosure is suspected. <br>
Risk: Requested latitude and longitude values are sent to Apple and may appear in logs along with raw API responses. <br>
Mitigation: Avoid exposing stderr logs for sensitive locations and review log handling before use in shared environments. <br>


## Reference(s): <br>
- [ClawHub WeatherKit skill page](https://clawhub.ai/jimmcq/skills/weatherkit) <br>
- [Apple WeatherKit REST API documentation](https://developer.apple.com/documentation/weatherkitrestapi/) <br>
- [Apple WeatherKit REST API endpoint](https://weatherkit.apple.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [Pretty-printed JSON forecast data with stderr diagnostic and error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Apple WeatherKit credentials through APPLE_TEAM_ID, APPLE_KEY_ID, APPLE_WEATHERKIT_KEY_PATH, and APPLE_SERVICE_ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
