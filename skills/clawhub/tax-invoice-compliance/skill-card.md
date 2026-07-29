## Description: <br>
Tax Invoice Compliance helps users assess digital invoice compliance, shell-company false-invoice indicators, recipient due diligence, four-flow consistency, abnormal voucher response, and good-faith defense evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, finance staff, and developers use this skill to perform invoice compliance self-checks, screen supplier and transaction risks, and generate structured guidance for remediation workflows. It is informational and does not replace official tax authority determinations or licensed professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, risk scenarios, self-check metrics, supplier identities, invoice numbers, or transaction details may be sent to the cloud service. <br>
Mitigation: Use anonymized or redacted scenarios unless the organization has approved sharing the real data with mcp.aitaxs.top. <br>
Risk: Local API keys, anonymous client IDs, cache, and logs may be stored by the client or browser workflow. <br>
Mitigation: Use trusted devices, review local storage locations before deployment, and clear stored keys or logs when the skill is no longer needed. <br>
Risk: Automatic setup can modify local MCP client configuration when explicitly enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless configuration changes are intended, and review generated MCP config entries before using them. <br>
Risk: Tax rules and enforcement posture can change, and the skill cannot determine final tax authority or court outcomes. <br>
Mitigation: Verify material decisions against official tax authority guidance or qualified professional advice before filing, remediating, or relying on a defense position. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Invoice compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown or plain text guidance, JSON-like tool results, shell command snippets, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-backed workflows may send tax questions, risk scenarios, and self-check metrics to mcp.aitaxs.top; local client data may include API keys, anonymous client IDs, cache, and logs.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
