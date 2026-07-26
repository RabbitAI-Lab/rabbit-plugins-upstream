## Description: <br>
AI抖音信息源 scans AI-related Douyin posts, filters high-engagement content, clusters topics, and generates a local HTML daily report with cover images, metrics, direct links, and optional daily subscription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content operators, AI creators, and industry observers use this skill to monitor AI trends on Douyin, review high-engagement posts, and generate archived visual reports for daily tracking or historical analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional subscription mode installs a persistent scheduled job and may store REDFOX_API_KEY on disk on macOS. <br>
Mitigation: Prefer manual report generation with --no-open unless daily automation is required; inspect LaunchAgents or crontab entries and remove the subscription when no longer needed. <br>
Risk: The skill requires a RedFox API key and sends query requests to redfox.hk. <br>
Mitigation: Confirm the key source, scope, validity period, and revocation path before use, and keep the key out of code, prompts, logs, and shared output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-ai-feed) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox API service](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal status text and tables, plus generated local HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY, writes reports under ~/Downloads/QoderReports by default, and can optionally install or remove a daily scheduled job.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
