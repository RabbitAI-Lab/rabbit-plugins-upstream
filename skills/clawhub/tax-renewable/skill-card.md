## Description: <br>
再生资源/资源回收/废旧物资企业财税政策、反向开票（自然人出售者）、资源综合利用即征即退、简易计税、风险指标、真实案例、报告模板与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax-compliance practitioners use this skill for renewable-resource and waste-material business tax guidance, including reverse invoicing, VAT refund eligibility, simplified taxation, risk self-checks, case analysis, and report or checklist drafting. It is advisory support and does not replace tax filing, legal representation, audit, or professional tax advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Remote processing may expose sensitive taxpayer, invoice, bank, investigation, or trade-secret details to the service endpoint. <br>
Mitigation: Avoid entering sensitive details unless remote processing is acceptable; redact or generalize case facts before using remote policy, risk, or calculation tools. <br>
Risk: The skill can store API keys, logs, and health state in a local tax-policy client directory. <br>
Mitigation: Review local storage before deployment, restrict file access where appropriate, and clear stored keys and logs when uninstalling or rotating access. <br>
Risk: Auto-setup behavior can persist MCP configuration when explicitly enabled. <br>
Mitigation: Administrators should inspect auto-setup paths and avoid setting TAX_ENABLE_AUTOSETUP unless persistent MCP configuration changes are intended. <br>
Risk: Tax guidance, calculations, and risk scores may be incomplete or outdated for a specific business, region, or filing position. <br>
Mitigation: Treat outputs as advisory drafts; verify policy basis, calculations, and filing decisions with official tax authority materials or qualified tax professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Renewable-resource compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with optional structured checklists, report templates, JSON-like tool results, and local configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools for policy questions, risk checks, tax calculations, and knowledge-base metadata; offline workflows provide limited reference guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
