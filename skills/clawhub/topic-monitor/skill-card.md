## Description: <br>
Topic Monitor helps agents monitor configured web searches, RSS/Atom feeds, and GitHub releases, then prioritize alerts and digest items with filtering, importance scoring, sentiment labels, and local state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use Topic Monitor to configure recurring checks for product releases, news topics, technology updates, RSS/Atom feeds, GitHub releases, and other subjects that need proactive alerting or weekly digests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured search queries, feed URLs, and alert contents may be used in external checks or notifications. <br>
Mitigation: Review config.json before use, avoid sensitive topics in externally delivered alerts, and choose trusted search and notification providers. <br>
Risk: Recurring monitoring can create local state and findings over time. <br>
Mitigation: Keep TOPIC_MONITOR_DATA_DIR in a private location and test with dry runs before enabling cron. <br>
Risk: A configured WEB_SEARCH_PLUS_PATH controls which search script is executed. <br>
Mitigation: Set WEB_SEARCH_PLUS_PATH only to a trusted web-search-plus script that has been reviewed for the intended environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/robbyczgw-cla/skills/topic-monitor) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/robbyczgw-cla) <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>
- [DigitalOcean OpenClaw Skills Guide](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; runtime scripts emit text, JSON alert lines, and digest summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3. Optional environment variables configure Telegram chat ID, local data directory, and a trusted web-search-plus path.] <br>

## Skill Version(s): <br>
1.5.2 (source: frontmatter, package.json, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
