## Description:

使用曼格云 API 监控微信公众号文章，采集新增内容，并生成 AI 分析、每日简报、HTML 分析面板和 Excel 导出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户、运营分析人员和开发者使用该技能监控授权范围内的微信公众号，增量采集公开文章，分析竞品和行业动态，并导出本地报告供核验和复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring or exporting public-account data without proper authorization could violate user or organizational requirements.

Mitigation: Confirm authorization for the selected public accounts and exported data before installation and use.

Risk: API credentials could be exposed if users place the Mangyun key in files, logs, prompts, or screenshots.

Mitigation: Set MANGYUN_API_KEY only in the environment and avoid writing the key to configuration, SQLite data, outputs, logs, prompts, or screenshots.

Risk: Scan and content-fetch commands can incur paid API usage.

Mitigation: Review budget settings, run estimates before collection, and require explicit approval before exceeding configured per-run budgets.

Risk: Changing the API endpoint could send account or article requests to an untrusted service.

Mitigation: Keep the API endpoint on the trusted Mangyun host unless a reviewer intentionally approves a controlled test endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-intelligence)
- [分析结果导入规范](artifact/references/analysis-schema.md)
- [曼格云 API 调用规范](artifact/references/api-contract.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Files]

**Output Format:** [Chinese Markdown guidance with shell commands, structured JSON analysis records, local HTML dashboards, and Excel workbook exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs local workspace paths, preserves source article links for verification, and reports API consumption from responses.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
