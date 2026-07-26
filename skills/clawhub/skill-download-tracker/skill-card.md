## Description: <br>
Monitor download counts for your ClawHub-published skills. Track changes over time, generate daily/weekly/monthly reports, and push notifications via Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsag1](https://clawhub.ai/user/tsag1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
ClawHub skill publishers use this skill to monitor skill-level download counts, keep local history, and generate daily, weekly, or monthly trend reports. It is useful when periodic snapshots and optional Feishu notifications are sufficient, rather than real-time analytics or individual-user tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feishu notifications can include monitored skill slugs, notes, download counts, deltas, and report text. <br>
Mitigation: Use Feishu only when needed, keep the local .env file private, and avoid putting sensitive information in monitored skill notes. <br>
Risk: Local history files and reports can reveal publisher activity or skill performance trends. <br>
Mitigation: Store the tracker data directory with appropriate local file permissions and review generated CSV, JSON, log, and Markdown files before sharing them. <br>
Risk: Scheduled runs execute local Python and shell scripts and call the ClawHub CLI for each monitored slug. <br>
Mitigation: Install only in environments where python3 and clawhub are expected, keep the monitor list to trusted slugs, and rely on the built-in slug validation and file locking behavior. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/tsag1/skills/skill-download-tracker) <br>
- [README](README.md) <br>
- [README.zh](README.zh.md) <br>
- [ClawHub](https://clawhub.com/skills/clawhub-download-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Console text, Markdown reports, CSV history, JSON state, and Feishu text notifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores local history under ~/.openclaw/workspace/data/clawhub-tracker and uses optional Feishu credentials from environment variables or a local .env file.] <br>

## Skill Version(s): <br>
1.584.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
