## Description: <br>
Provides tailored sowing, watering, harvesting advice, reminders, and weather-aware guidance for raised-bed allotment gardening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiaswestholm](https://clawhub.ai/user/tobiaswestholm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External gardeners and allotment owners use this skill to manage planted crops, reminders, sowing recommendations, harvest tracking, and weather-aware watering plans for a configured raised-bed garden. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists local garden records and uses configured coordinates for Open-Meteo forecasts. <br>
Mitigation: Install only if local garden records and coordinate-based weather lookups are acceptable, and review stored profile data before use. <br>
Risk: Weekly reports can be delivered through Telegram to configured recipients. <br>
Mitigation: Verify Telegram recipients and any weekly scheduled task before enabling report delivery. <br>
Risk: The unknown-crop flow can add new crop knowledge without a preview. <br>
Mitigation: Review or change the flow so new crop knowledge is previewed and approved before saving. <br>


## Reference(s): <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Concise natural-language guidance with command-backed garden status, recommendations, reminders, and reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local garden records, use configured coordinates for forecasts, and optionally send weekly Telegram reports.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
