## Description:

政府采购投标决策分析助手：基于知了标讯招中标历史数据，对具体政采类招标项目输出是否参与、报价参考、竞争预测、限制性信号、废标红线与合规风险评估。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to evaluate whether to bid on a specific Chinese government procurement project. It produces a decision report covering buyer history, likely competitors, historical price anchors, bid/no-bid rationale, compliance risks, and recommended next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement search terms, project names, and company names are sent to Zhiliaobiaoxun APIs during analysis.

Mitigation: Use the skill only for data that may be shared with Zhiliaobiaoxun, and avoid entering confidential bid strategy beyond what is needed for the analysis.

Risk: Trial auto-registration sends a persistent device-derived identifier for deduplication.

Mitigation: Decline auto-registration and configure an existing ZLBX_API_KEY when device-derived registration is not acceptable.

Risk: The local ~/.zlbx/config.json file stores the API credential.

Mitigation: Protect the file as a credential, avoid sharing it, and remove or rotate the key if it may have been exposed.

Risk: Generated reports may include signed links and business-sensitive procurement analysis.

Mitigation: Review reports before sharing, limit redistribution of signed links, and treat links in generated HTML cautiously.

Risk: The skill can create local HTML report files under the user's home directory.

Mitigation: Review generated files before distributing them and delete reports that should not persist locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [workflow.md](references/workflow.md)
- [api-quick.md](references/api-quick.md)
- [report-template.md](references/report-template.md)
- [auto-register.md](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report, optional local HTML report, and concise user guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or a local ~/.zlbx/config.json credential; full reports typically consume 12-25 API calls and quick checks typically consume 5-8 API calls.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
