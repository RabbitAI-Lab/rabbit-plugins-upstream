## Description: <br>
Screen Activity Tracker helps an agent start, stop, summarize, and search background macOS screen activity logs created from periodic screenshots and vision-model analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeject](https://clawhub.ai/user/zeject) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to schedule macOS screen-activity capture, generate daily activity summaries, and search prior local or SiYuan activity logs. It is intended for personal activity tracking where the user controls screenshot capture, retention, and analysis endpoint configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Background full-screen screenshots and searchable local history can expose sensitive screen content. <br>
Mitigation: Use only with informed user consent, verify sensitive-app exclusions before enabling tracking, limit retention, and purge stored screenshots and logs when no longer needed. <br>
Risk: Screenshots may be sent to the configured MLX-compatible analysis service. <br>
Mitigation: Set mlx_url only to a trusted local or controlled endpoint, and disable or stop tracking before handling confidential content if the endpoint cannot be trusted. <br>
Risk: config.json may contain a SiYuan API token and notebook identifiers. <br>
Mitigation: Restrict file permissions on config.json, avoid committing it, and rotate the token if the file is exposed. <br>
Risk: A cron job can continue collecting activity after the user forgets it is enabled. <br>
Mitigation: Confirm the cron job can be listed, disabled, and removed, and document the retention and purge path for local output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zeject/skills/screen-activity-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, search results, cron tool calls, and local Markdown logs with screenshot links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, Screen Recording permission, peekaboo, python3, and a configured vision-model endpoint; can create background cron jobs and local or SiYuan activity logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
