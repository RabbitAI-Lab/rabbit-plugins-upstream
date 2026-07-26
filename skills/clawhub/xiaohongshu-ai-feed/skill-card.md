## Description: <br>
AI Xiaohongshu Feed scans AI-related Xiaohongshu posts, ranks popular content by engagement, clusters topics, and generates local HTML daily reports with metrics, cover images, direct links, and optional daily subscription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as content operators, Xiaohongshu creators, and industry analysts use this skill to monitor AI-related Xiaohongshu trends, review high-engagement posts, and generate dated local reports for daily tracking or historical analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and contacts redfox.hk to fetch Xiaohongshu AI content. <br>
Mitigation: Use a revocable key from the RedFox account settings, provide it through the environment when possible, and avoid placing it in prompts, logs, or generated files. <br>
Risk: The --subscribe option creates a persistent scheduled job and, on macOS, may store REDFOX_API_KEY in a LaunchAgent plist file. <br>
Mitigation: Avoid --subscribe unless the scheduled job behavior has been reviewed; inspect LaunchAgents or crontab entries after installation and use --unsubscribe when no longer needed. <br>
Risk: Generated HTML reports may contain untrusted remote content such as links and images from fetched Xiaohongshu data. <br>
Mitigation: Review generated reports before sharing, treat external links and images as untrusted, and open reports in an environment appropriate for untrusted web content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/xiaohongshu-ai-feed) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox website](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, HTML files, shell commands, configuration guidance] <br>
**Output Format:** [Terminal text and local HTML reports, with Markdown usage guidance and shell command examples in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [HTML reports are written under ~/Downloads/QoderReports by default and may be opened automatically unless --no-open is used.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
