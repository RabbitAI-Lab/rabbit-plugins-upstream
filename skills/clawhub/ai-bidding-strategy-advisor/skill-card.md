## Description:

帮助用户基于知了标讯历史招中标数据，为具体招标项目制定投标决策、报价策略、竞争预测、采购方画像、风险清单和行动建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and business users use this skill to evaluate whether to pursue a specific tender, how to price competitively, and which competitors are likely to participate. The skill produces a data-backed decision report with confidence, risks, pricing guidance, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports and links containing sk or auto-login sid parameters may grant access without a normal login if shared broadly.

Mitigation: Treat generated HTML reports and signed links as sensitive, and share them only with intended recipients.

Risk: The vendor receives bid and project search terms, optional device-registration data, and may store a local API key for continued use.

Mitigation: Install only if this data sharing is acceptable, and prefer a preconfigured ZLBX_API_KEY when controlled credential management is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor)
- [API quick reference](references/api-quick.md)
- [Five-step analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Account registration and recharge](https://ai.zhiliaobiaoxun.com/?ch=s74)
- [Bailian bid-document product](https://biaoshu.zhiliaobiaoxun.com/)
- [Zhiliaobiaoxun business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown decision report in the agent response, with optional self-contained HTML report file generated from JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete analysis normally uses 12-25 vendor API calls; quick analysis uses 5-8 calls. Reports may include data citations and vendor-provided signed links.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
