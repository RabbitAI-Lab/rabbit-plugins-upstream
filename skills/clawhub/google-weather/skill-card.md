## Description: <br>
Google Weather provides current conditions, temperature, humidity, wind, and forecasts for worldwide locations using Google's Weather API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer weather requests, fetch current conditions or 24-hour forecasts, and return formatted summaries or raw JSON for a requested location. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends requested locations to Google Weather and Geocoding services and uses a Google API key. <br>
Mitigation: Use a restricted API key limited to the needed Weather and Geocoding APIs, and avoid entering precise private addresses unless necessary. <br>
Risk: Weather and geocoding results depend on Google API availability, permissions, quota, and returned data. <br>
Mitigation: Enable the required APIs, configure the expected key environment variable, and review API errors before relying on the output. <br>


## Reference(s): <br>
- [ClawHub Google Weather skill page](https://clawhub.ai/shaharsha/skills/google-weather) <br>
- [Google Weather API](https://console.cloud.google.com/apis/library/weather.googleapis.com) <br>
- [Google Geocoding API](https://console.cloud.google.com/apis/library/geocoding-backend.googleapis.com) <br>
- [Google Cloud Console](https://console.cloud.google.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Plain text or Markdown weather summaries, with optional pretty-printed JSON for raw data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports metric or imperial units through GOOGLE_WEATHER_UNITS and requires a Google API key.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
