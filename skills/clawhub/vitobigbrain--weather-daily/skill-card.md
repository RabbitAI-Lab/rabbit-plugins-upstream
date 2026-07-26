## Description: <br>
Fetches current weather for a configured location and writes a daily briefing markdown entry into an Obsidian daily-note directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vitobigbrain](https://clawhub.ai/user/vitobigbrain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to add today's weather conditions and temperature to an Obsidian daily note for a requested or default location. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an OpenWeatherMap API key, and security evidence notes that the implementation passes the key as a curl argument/query parameter. <br>
Mitigation: Use a limited-purpose weather API key, avoid sharing command logs, and rotate the key if exposure is suspected. <br>
Risk: The skill appends markdown files under the Obsidian daily-note directory or WEATHER_DAILY_OUTPUT_DIR. <br>
Mitigation: Set WEATHER_DAILY_OUTPUT_DIR deliberately and review the destination path before running the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vitobigbrain/skills/weather-daily) <br>
- [Publisher Profile](https://clawhub.ai/user/vitobigbrain) <br>
- [Skill Homepage](https://github.com/beebee-ai/weather-daily) <br>
- [OpenWeatherMap API](https://openweathermap.org/api) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration] <br>
**Output Format:** [Markdown daily briefing appended to a local note, with a terminal status line] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENWEATHER_API_KEY and curl; WEATHER_DAILY_OUTPUT_DIR optionally changes the destination directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
