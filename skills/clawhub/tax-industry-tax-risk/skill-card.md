## Description: <br>
Provides industry-focused tax risk guidance for fuel retail, network freight platforms, logistics companies, bulk commodity trading, and tax-incentive zone compliance, including risk patterns, evidence checks, monitoring indicators, and remediation paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, compliance, and advisory users use this skill to identify industry-specific tax risks, check supporting evidence across contracts, invoices, payments, logistics, and inventory records, and prepare self-check or remediation guidance. It is not a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global, with tax guidance focused on China-specific compliance scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top/tax-policy-knowledge. <br>
Mitigation: Review the service's privacy and retention terms before use, and avoid submitting confidential tax, employee, invoice, or investigation details unless approved. <br>
Risk: The skill creates persistent local credentials and logs. <br>
Mitigation: Protect the local credential and log storage, include it in data handling review, and remove credentials or logs when they are no longer needed. <br>
Risk: Auto-setup behavior can modify Claude, Cursor, or Cline MCP configuration files when write mode is enabled. <br>
Mitigation: Keep setup in dry-run mode unless approved, review planned configuration changes and backups, and enable write mode only in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [Industry tax risk self-check page](https://mcp.aitaxs.top/web/topic_workflow_industry_tax_risk.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown or structured text guidance, with optional configuration instructions for supported agent clients] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use external cloud MCP service responses and local offline fallback guidance depending on availability.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
