## Description:

A股公众号大V工具，输入日期获取A股领域公众号大V账号30个及账号数据（平均阅读、红狐指数等），同时获取每个账号最新一篇文章及文章数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External users, investors, content operators, financial professionals, and data analysts use this skill to query A-share WeChat official account rankings, latest article metrics, and subscription updates from RedFox data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key, and command-line or plaintext config usage can expose credentials.

Mitigation: Prefer REDFOX_API_KEY in the environment, avoid passing keys with --api-key, and restrict any local config file to owner-only permissions.

Risk: Subscription management can persistently add, remove, or clear followed accounts.

Mitigation: Confirm account additions, removals, and clear actions before letting an agent run subscription commands.

Risk: Ranking and engagement data are not real time and reflect RedFox ingestion timing.

Mitigation: Show the requested date and data freshness notes with results, especially for daily market-monitoring workflows.

## Reference(s):

- [A股公众号大V API guide](references/api_guide.md)
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/gzh-astock-top)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and concise text derived from JSON helper-script results, with inline shell commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; subscription actions may update local subscription state.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
