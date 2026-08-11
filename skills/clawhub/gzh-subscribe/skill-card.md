## Description:

Tracks selected WeChat Official Accounts, fetches recent article metadata from RedFox, and produces terminal summaries and HTML daily reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External content, marketing, and research users use this skill to monitor competitor, peer, or followed WeChat Official Accounts, fetch recent article metrics, and generate a daily report for review or archiving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and can read it from the REDFOX_API_KEY environment variable, a command-line argument, or ~/.qoder/apis/redfox.json.

Mitigation: Prefer REDFOX_API_KEY over command-line keys, avoid hardcoding the key, and confirm the key source, scope, expiry, and reset process before use.

Risk: Subscribed account IDs and fetch requests are sent to redfox.hk.

Mitigation: Install only if sending monitored WeChat account IDs to RedFox is acceptable for the intended workflow.

Risk: The skill stores subscription data under ~/.qoder and generates reports in ~/Downloads/QoderGzhReports.

Mitigation: Review local subscription and report files for sensitive account lists or article data, and delete them when they are no longer needed.

Risk: The optional daily push installs a scheduled task through LaunchAgent or crontab.

Mitigation: Enable daily scheduling only when needed and remove the LaunchAgent or crontab entry when the subscription workflow is stopped.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/gzh-subscribe)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox service](https://redfox.hk?source=clawhub)
- [RedFox WeChat article API endpoint](https://redfox.hk/story/api/gzh/data/queryWorkList)

## Skill Output:

**Output Type(s):** [Text, HTML, Files, Shell commands, Configuration]

**Output Format:** [Terminal text plus generated HTML reports and local JSON configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores subscription data under ~/.qoder and reports under ~/Downloads/QoderGzhReports; optional daily scheduling creates a LaunchAgent or crontab entry.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
