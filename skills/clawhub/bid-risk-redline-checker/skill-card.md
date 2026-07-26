## Description: <br>
面向招投标决策场景，识别废标风险、控标信号、限制性条款、采购方历史供应商格局、竞争开放度和报价参考，并输出投标决策分析报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and sales teams use this skill to evaluate a specific bidding opportunity before deciding whether and how to bid. It compares public bidding records, buyer history, likely competitors, restrictive signals, and price anchors to produce a risk-aware decision report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist an API key locally for the vendor service. <br>
Mitigation: Use a pre-provisioned ZLBX_API_KEY when possible, review local credential storage before installation, and rotate or revoke the key if the workstation is shared. <br>
Risk: The auto-registration flow sends a MAC-derived device hash to the vendor service after user consent. <br>
Mitigation: Require explicit user approval before auto-registration and skip the flow by configuring ZLBX_API_KEY or ~/.zlbx/config.json in advance. <br>
Risk: Generated HTML reports may contain signed links that grant access to source bidding records. <br>
Mitigation: Share exported reports only with trusted recipients and remove sensitive signed links before broader distribution. <br>
Risk: Bid-risk conclusions can affect commercial decisions and may involve real companies or public agencies. <br>
Mitigation: Treat outputs as decision support, keep factual evidence separate from inferred signals, and independently review material recommendations before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker) <br>
- [API quick reference](references/api-quick.md) <br>
- [Analysis workflow](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration workflow](references/auto-register.md) <br>
- [Zhiliaobiaoxun API endpoint family](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Manual account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s80) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision report in chat, with optional self-contained HTML report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cited bidding records and signed source-record links returned by the API; complete analysis normally uses about 12-25 API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
