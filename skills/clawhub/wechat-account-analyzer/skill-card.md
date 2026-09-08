## Description:

公众号账号诊断工具是对任意公众号账号进行四维度量化评分（内容健康度、用户活跃度、内容核心数据、运营规范性），对标行业平均水平，输出可落地的运营优化建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

公众号号主、新媒体运营、MCN 机构、品牌方和内容创作者 use this skill to diagnose WeChat Official Account health, benchmark performance against similar accounts, and generate operational recommendations. It supports single-account analysis and multi-account comparison based on RedFox API data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a RedFox API key for authenticated requests.

Mitigation: Use a dedicated RedFox API key, avoid pasting secrets into chat, and prefer a secure secret manager or session-scoped environment variable.

Risk: The skill writes raw API data and generated reports locally.

Mitigation: Review generated files before sharing them and delete output/raw_data.json, report_data.json, multi_report_data.json, and HTML reports when they are no longer needed.

Risk: Follow-up syncing or subscription flows may create later account-data retrieval tasks.

Mitigation: Accept sync or scheduled push flows only after confirming which account will be synced, when the task will run, and how it can be cancelled.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/wechat-account-analyzer)
- [RedFox Hub](https://redfox.hk/?source=clawhub)
- [Core Workflow](artifact/references/core_workflow.md)
- [API Guide](artifact/references/api_guide.md)
- [Workflow Guide](artifact/references/workflow_guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown diagnostic reports, structured JSON data files, generated HTML reports, and shell commands for Python execution and API-key configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses RedFox API data, writes raw and structured data under the skill output directory, and may generate single-account or multi-account HTML reports.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
