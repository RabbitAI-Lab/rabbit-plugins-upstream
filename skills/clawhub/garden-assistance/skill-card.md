## Description: <br>
Manage a climate-generalizable raised-bed garden with planted crops, Open-Meteo weekly forecasts, sowing recommendations, watering-week plans, reminders, harvest windows, and garden memory files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiaswestholm](https://clawhub.ai/user/tobiaswestholm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External gardeners use this skill to manage a raised-bed allotment: configure local climate and bed size, track plantings and harvests, plan watering and sowing, and receive reminders or weekly garden reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local garden memory and crop knowledge files. <br>
Mitigation: Review proposed state-changing actions before use and keep backups of the local data directory. <br>
Risk: The skill sends configured coordinates to Open-Meteo for weather data. <br>
Mitigation: Confirm the location-sharing behavior is acceptable before configuring a profile or updating forecasts. <br>
Risk: The weekly report path can broadcast garden reports to configured Telegram recipients. <br>
Mitigation: Review or disable weekly report delivery unless the recipients and schedule are intentional. <br>
Risk: The unknown-crop flow can add generated crop knowledge automatically. <br>
Mitigation: Review generated crop knowledge before relying on recommendations for newly added crops. <br>


## Reference(s): <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>
- [ClawHub skill page](https://clawhub.ai/tobiaswestholm/skills/garden-assistance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Plain-language gardening guidance with deterministic CLI-backed JSON operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local garden memory files and may send weekly reports to configured Telegram recipients when explicitly used.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
