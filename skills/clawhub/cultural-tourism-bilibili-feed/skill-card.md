## Description: <br>
文旅B站信息源 searches Bilibili for trending cultural tourism videos, ranks results by engagement, clusters them by topic, and generates a local HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content operators, tourism professionals, and researchers use this skill to monitor Bilibili cultural tourism hotspots, compare engagement across topics, and produce daily or date-filtered reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and sends search queries to redfox.hk. <br>
Mitigation: Use a scoped, revocable key where available, keep it out of prompts and logs, and rotate it if exposure is suspected. <br>
Risk: The subscription feature creates persistent scheduled jobs and may store REDFOX_API_KEY in plaintext on macOS. <br>
Mitigation: Avoid subscription mode unless the generated LaunchAgent or crontab entry has been reviewed; remove the scheduled job when it is no longer needed. <br>
Risk: Non-macOS subscription setup updates crontab through shell commands, which is risky with untrusted keyword input. <br>
Mitigation: Use trusted, simple keyword values, review the generated crontab command, or configure scheduling manually. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/cultural-tourism-bilibili-feed) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, HTML files] <br>
**Output Format:** [Markdown summary with category counts, terminal output, and a local HTML report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and writes reports locally; normal runs may open the generated report in a browser.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
