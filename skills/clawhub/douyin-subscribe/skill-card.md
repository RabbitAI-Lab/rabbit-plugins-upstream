## Description: <br>
抖音账号订阅追踪 lets an agent subscribe to Douyin account IDs, fetch recent works on a daily schedule, and produce Markdown summaries plus local HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, creators, brands, MCNs, and analysts use this skill to monitor selected Douyin accounts, compare recent posts, and receive scheduled reports with engagement metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queried Douyin account IDs and the REDFOX_API_KEY are sent to redfox.hk. <br>
Mitigation: Confirm the API key scope, retention expectations, and revocation process before use; avoid exposing the key in prompts, logs, or generated files. <br>
Risk: The script can persist subscription and failure state under ~/.qoder despite documentation that emphasizes no local storage. <br>
Mitigation: Review and remove ~/.qoder/douyin_subscriptions.json and ~/.qoder/douyin_subscribe_failures.json when disabling or auditing the skill. <br>
Risk: Generated HTML reports are written locally and may auto-open. <br>
Mitigation: Choose an appropriate report path, inspect report contents before sharing, and disable or avoid HTML report generation when local files are not desired. <br>
Risk: Daily automation can silently continue monitoring subscribed accounts. <br>
Mitigation: Confirm scheduled tasks before enabling them and document how to update or delete those tasks when subscriptions change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/douyin-subscribe) <br>
- [RedFoxHub API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>
- [RedFox Douyin Account Works API](https://redfox.hk/story/api/dy/data/listWorkByAccount) <br>
- [API Test Parameters](artifact/references/test_api_params.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown tables and summaries, shell commands, configuration guidance, and generated local HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a REDFOX_API_KEY; fetches account data from redfox.hk and may write reports and subscription/failure state locally.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
