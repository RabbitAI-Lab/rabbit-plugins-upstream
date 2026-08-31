## Description:

AI抖音信息源 scans AI-related Douyin posts, ranks them by engagement, clusters topics, and generates a local HTML daily report with cover images, metrics, and optional daily subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, AI creators, and industry analysts use this skill to track Douyin AI trends, search by keyword or date range, and produce reports for trend monitoring, competitor review, and historical analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search parameters and API-key-authenticated requests are sent to RedFox.

Mitigation: Use a revocable REDFOX_API_KEY only after confirming the key source, scope, validity period, and reset process.

Risk: Subscription mode persists scheduled execution and may write the API key into a plaintext macOS LaunchAgent file.

Mitigation: Avoid subscription mode for valuable keys; review the created LaunchAgent or crontab entry and use --unsubscribe when scheduled reporting is no longer needed.

Risk: Generated local HTML reports may contain unescaped remote content and can be opened automatically.

Mitigation: Treat reports as untrusted external-service content; use --no-open or inspect generated files before opening them in a browser.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-ai-feed)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox service](https://redfox.hk)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Terminal text plus a local HTML report; agent summaries may preserve Markdown links from the script output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; writes reports to ~/Downloads/QoderReports by default and can optionally install a daily 16:00 subscription task.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
