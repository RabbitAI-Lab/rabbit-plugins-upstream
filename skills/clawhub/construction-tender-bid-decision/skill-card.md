## Description:

建筑工程投标决策分析助手，帮助评估施工、市政、装修、园林、公路、房建和基建类项目是否值得投标，并基于招中标历史数据生成决策报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to analyze a specific construction tender, compare purchaser history, likely competitors, historical pricing, qualification barriers, and bid/no-bid risks. It produces a concise decision report and can export a local HTML version for sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can preserve signed report or source-data links that may bypass login.

Mitigation: Review generated Markdown and HTML reports before sharing, especially links containing sk or auto-login-style parameters.

Risk: The skill can create and persist account credentials through an external registration flow.

Mitigation: Prefer a user-managed ZLBX_API_KEY; if auto-registration is used, remove ~/.zlbx credentials when they are no longer needed.

Risk: Bid reports may influence commercial decisions using incomplete or delayed public tender data.

Mitigation: Treat generated reports as decision support, review data gaps and citations, and verify critical bid, pricing, and qualification facts before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Zhiliao Biaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})
- [Zhiliao Biaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s75)
- [Zhiliao business intelligence platform](https://agent.zhiliaobiaoxun.com)
- [Bailian bid document product](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown decision report with optional local HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; complete analysis is documented as approximately 12-25 API calls and quick analysis as approximately 5-8 API calls.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
