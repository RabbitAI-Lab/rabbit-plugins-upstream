## Description:

微信公众号文章订阅 - 每天 6 点，盯梢竞对、同类、关注账号，一份你订阅的公众号文章推送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as competitive monitors, content creators, and researchers use this skill to subscribe to WeChat public accounts, fetch daily posts, and generate terminal or HTML reports with titles, summaries, reads, likes, and article links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RedFoxHub receives the public-account names or IDs being monitored.

Mitigation: Use the skill only when sharing those monitored account names or IDs with RedFoxHub is acceptable.

Risk: Scheduled mode creates persistent local execution and may leave scheduler entries behind.

Mitigation: Avoid enabling --subscribe until the scheduler code is hardened; if used, inspect LaunchAgents or crontab afterward and remove entries that are no longer needed.

Risk: API keys can be exposed when passed on the command line or written into scheduled task configuration.

Mitigation: Prefer REDFOX_API_KEY from the environment, avoid command-line API keys, and check macOS plist files for plaintext key material after enabling scheduled mode.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/gzh-subscribe)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFoxHub](https://redfox.hk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated reports are HTML files and terminal tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local subscription JSON, HTML reports, and optional scheduled jobs.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
