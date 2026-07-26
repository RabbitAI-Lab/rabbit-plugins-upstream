## Description: <br>
AI视频号信息源 scans AI-related WeChat Video content, ranks posts by engagement, clusters them by topic, and generates an HTML daily report with cover images, metrics, and optional daily subscription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content operators, AI creators, and industry analysts use this skill to track AI trends on WeChat Video, compare popular content, and generate daily or historical trend reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subscription mode creates persistent scheduled tasks and may store REDFOX_API_KEY in a local scheduler file. <br>
Mitigation: Use one-time report generation unless daily automation is required; if subscription mode has stored the key, rotate it and remove the scheduler entry when no longer needed. <br>
Risk: Generated HTML reports may open automatically and render report content from fetched data. <br>
Mitigation: Run with --no-open and inspect generated HTML only when the report data source is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-channels-ai-feed) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands, Configuration] <br>
**Output Format:** [Terminal text plus generated HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; reports are written locally, normally under ~/Downloads/QoderReports/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
