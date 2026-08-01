## Description: <br>
数电票合规与空壳虚开防范专项助手，帮助用户进行发票生命周期管理、空壳虚开特征识别、受票方防范、四流一致校验、异常凭证应对与善意取得抗辩准备。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, finance, and tax-compliance users use this skill to review digital invoice scenarios, screen supplier and shell-company risks, check four-flow consistency, respond to abnormal invoice credentials, and prepare practical compliance checklists or reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive invoice, supplier, taxpayer, or transaction details may be sent to cloud or search services. <br>
Mitigation: Install only when the mcp.aitaxs.top service is trusted, and redact confidential or identifying details before requesting analysis. <br>
Risk: The skill may persist local state, credentials, raw query logs, or MCP client configuration changes. <br>
Mitigation: Review or disable TAX_ENABLE_AUTOSETUP before use, inspect local MCP configuration changes, and clear ~/.tax-policy-client logs or config when needed. <br>
Risk: Web self-check and exported prompts may contain company-identifying data. <br>
Mitigation: Treat generated prompts and reports as sensitive business material and remove identifiers before sharing outside trusted systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Invoice compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, practical steps, and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-backed tax analysis, offline fallback guidance, and links to web self-check workflows.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
