## Description: <br>
办税合规智能指引 helps users navigate China e-tax bureau workflows, tax registration, invoice setup, recurring filings, export rebates, tax deregistration, credit repair, forms, calendars, and common compliance questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and operations users can use this skill to get structured China tax filing guidance, electronic tax bureau navigation, document checklists, deadline reminders, and compliance-oriented next steps. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a cloud-backed MCP integration and may process taxpayer, company, invoice, or financial context through remote services. <br>
Mitigation: Review deployment settings before installation and avoid entering sensitive taxpayer or financial data unless remote processing is approved. <br>
Risk: The security evidence reports stored local credentials, raw local logs, and possible client configuration changes. <br>
Mitigation: Inspect the local data paths and MCP client configuration before use, and enable automatic setup only when configuration changes are approved. <br>
Risk: Fallback behavior may search third-party services when cloud access is unavailable. <br>
Mitigation: Disable or avoid fallback workflows in restricted environments and rely on approved tax authority or internal reference sources. <br>
Risk: Tax procedures and electronic tax bureau interfaces vary by locality and can change over time. <br>
Mitigation: Verify final filing actions, deadlines, and required materials against the applicable local tax authority or qualified tax professional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Tax compliance path self-check page](https://mcp.aitaxs.top/web/topic_workflow_china_tax_guidance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-backed MCP responses may be used when available, with offline workflow fallbacks described in the artifact.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
