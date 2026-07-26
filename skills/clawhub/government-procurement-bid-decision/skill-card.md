## Description: <br>
政府采购投标决策分析助手，基于知了标讯招中标数据帮助评估政采及央国企采购项目是否值得投标、识别限制性信号、预测竞争对手、参考历史成交价并生成决策报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, sales, and bid teams use this skill to evaluate specific Chinese government, public institution, agency, and state-owned enterprise procurement opportunities. It helps decide whether to bid, estimate competition and pricing, identify compliance risks, and produce a traceable decision report. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive bid or project information may be unsuitable for vendor API analysis. <br>
Mitigation: Review before installing when bid data is sensitive and only submit project names, company names, or documents appropriate for external processing. <br>
Risk: The skill can create or reuse persistent credentials through ZLBX_API_KEY or local configuration. <br>
Mitigation: Prefer a user-managed ZLBX_API_KEY and avoid auto-registration if device de-duplication or local credential persistence is undesirable. <br>
Risk: Generated HTML reports and signed sk links may share access to underlying records when forwarded. <br>
Mitigation: Treat generated reports and sk-containing links as sensitive and share them only with intended recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision) <br>
- [Workflow reference](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration reference](references/auto-register.md) <br>
- [知了标讯 API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名}) <br>
- [知了商机大师](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision report plus optional generated HTML report file and file path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; full analysis typically uses 12-25 vendor API calls and may write reports under ~/zlbx-bid-decision-files/.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
