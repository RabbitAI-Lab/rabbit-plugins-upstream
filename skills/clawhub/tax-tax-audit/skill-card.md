## Description: <br>
面向企业、机构和审计人员的财税合规审计助手，提供税务审计程序、内控测试、涉税舞弊识别、关键审计事项披露和合规自检报告指导。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax professionals, auditors, and compliance teams use this skill to structure Chinese enterprise tax-audit and fiscal-compliance reviews, including control testing, fraud red-flag review, disclosure drafting, risk self-checks, and report preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax/audit prompts and self-check content may be sent to mcp.aitaxs.top. <br>
Mitigation: Review the service's data-handling terms before use and avoid entering confidential client, company, invoice, fraud, or audit details unless approved. <br>
Risk: Fallback search can send query text to public search engines. <br>
Mitigation: Use nonsensitive queries for fallback mode, disable or avoid fallback searches for confidential matters, and verify results against official sources or qualified professionals. <br>
Risk: The client may store local configuration, logs, identifiers, or API-key metadata under the user's home directory. <br>
Mitigation: Inspect and clear ~/.tax-policy-client after testing with sensitive data, and manage API keys according to local credential-handling policy. <br>
Risk: Optional auto-setup can alter local AI-client MCP configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional, and review generated backups and MCP entries before continued use. <br>
Risk: Tax calculations, policy summaries, and risk ratings may be incomplete or outdated for specific facts, regions, or filing periods. <br>
Mitigation: Treat outputs as preliminary guidance only and confirm material tax, audit, legal, or filing decisions with official authorities or licensed professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-audit) <br>
- [Tax audit self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_tax_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code snippets, shell commands, configuration examples, structured risk-check results, and generated report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, use local offline fallback workflows, open an interactive self-check page, and generate copyable compliance report text.] <br>

## Skill Version(s): <br>
3.15.6 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
