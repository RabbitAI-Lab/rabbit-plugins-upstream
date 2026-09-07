## Description:

信创与IT信息化投标决策分析助手，基于知了标讯招中标历史数据，为具体IT招标项目生成投标建议、竞争预测、报价参考和风险评估。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and bid teams use this skill to assess whether to pursue a specific IT or Xinchuang procurement opportunity and prepare a data-grounded bid decision report. It analyzes buyer history, likely competitors, comparable pricing, qualification risks, and optional fit against the user's company.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the vendor's cloud service for bid analysis and sends project names, company names, and related query terms to that service.

Mitigation: Use the skill only when that vendor service is acceptable for the project; avoid submitting confidential bid material beyond the terms needed for lookup.

Risk: Automatic trial registration can transmit a hashed device identifier and create a local account key.

Mitigation: Prefer a user-provided ZLBX_API_KEY to bypass automatic registration; if no key exists, obtain user consent before registration.

Risk: A reusable API key may be stored in a plaintext local configuration file.

Mitigation: Prefer environment-based credential configuration where possible and restrict access to local configuration files.

Risk: Full analysis consumes account credits and may write HTML report files by default.

Mitigation: Tell users the expected call or credit cost before analysis, pause before exceeding the documented budget, and disclose the full report output path.

Risk: Generated reports can contain signed source links and business-sensitive competitive analysis.

Mitigation: Review generated HTML links and report contents before sharing externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/xinchuang-it-bid-decision)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Auto-registration guide](references/auto-register.md)
- [Report template](references/report-template.md)
- [知了标讯 API v2](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [知了标讯 AI skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include cited bid/company records when available, cost-unit notes, data gaps, and a disclaimer.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
