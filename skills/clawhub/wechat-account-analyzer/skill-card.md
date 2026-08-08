## Description:

公众号账号诊断工具是对任意公众号账号进行四维度量化评分（内容健康度、用户活跃度、内容核心数据、运营规范性），对标行业平均水平，输出可落地的运营优化建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as WeChat account owners, social media operators, MCN agencies, brands, and content creators use this skill to query RedFox data and produce account health diagnostics, industry benchmarking, and optimization suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a RedFox API key and may guide users toward persistent REDFOX_API_KEY configuration.

Mitigation: Review before installing; set REDFOX_API_KEY only for the current session or with a secret manager, and avoid automatic edits to shell profile files.

Risk: Reports and raw API data may persist locally in output files and include queried account identifiers or API-derived account metrics.

Mitigation: Review and delete generated output files when reports or raw API data should not remain on disk.

Risk: Diagnostics depend on RedFox API data availability, freshness, and account lookup accuracy.

Mitigation: Treat findings as API-derived analysis, confirm questionable results with RedFox or source account data, and do not generate estimates when an account is not found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-account-analyzer)
- [RedFox Hub](https://redfox.hk/)
- [Core workflow](artifact/references/core_workflow.md)
- [API guide](artifact/references/api_guide.md)
- [Workflow guide](artifact/references/workflow_guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration guidance]

**Output Format:** [Markdown diagnostic reports, JSON status/data files, and optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses REDFOX_API_KEY for RedFox API access; output may include queried account identifiers and API-derived account metrics.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
