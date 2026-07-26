## Description: <br>
文旅抖音信息源 searches Douyin for popular cultural tourism posts, ranks them by likes, clusters them by topic, and generates an HTML report with summary statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, tourism professionals, scenic spot marketers, and researchers use this skill to track high-engagement Douyin cultural tourism content, compare recent trends, and generate daily visual reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a third-party RedFox API key and service. <br>
Mitigation: Verify the key source, scope, expiration, and revocation path before use, and avoid exposing the key in prompts, logs, code, or report output. <br>
Risk: The optional daily subscription feature creates persistent scheduled tasks. <br>
Mitigation: Avoid subscription mode unless needed; if enabled, inspect the generated LaunchAgent or crontab entry and confirm how to remove it. <br>
Risk: Subscription mode may place API credentials into scheduled-task configuration. <br>
Mitigation: Prefer environment-based credentials, inspect generated scheduler files before loading them, and rotate the API key if it may have been exposed. <br>
Risk: The skill writes local HTML reports and may open them in a browser. <br>
Mitigation: Use a trusted output directory, review generated files before sharing, and run in an environment where browser opening is expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/cultural-tourism-douyin-feed) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [README.en.md](artifact/README.en.md) <br>
- [README.md](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, HTML files, API calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown-style category summary plus a generated HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; can write local report files, open the report in a browser, and optionally configure a daily scheduled report.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
