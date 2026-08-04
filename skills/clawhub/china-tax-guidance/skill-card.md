## Description: <br>
China Tax Guidance helps users navigate Chinese electronic tax bureau workflows, filing paths, invoice handling, tax deregistration, credit repair, tax calendars, forms, and common compliance questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business tax staff, finance teams, and individual taxpayers use this skill to get procedural guidance, document checklists, and self-check steps for China tax filings and electronic tax bureau tasks. It is intended as guidance that users should confirm against local tax authority requirements and qualified professional advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions may be sent to mcp.aitaxs.top or, during fallback, public search engines. <br>
Mitigation: Avoid entering taxpayer IDs, credentials, invoice details, payroll data, bank information, or confidential business facts unless the remote service is trusted and the user has explicitly consented. <br>
Risk: The skill can store credentials and logs locally and can modify MCP client configuration when autosetup is enabled. <br>
Mitigation: Review ~/.tax-policy-client and Claude, Cursor, or Cline MCP configuration files after testing, and only enable TAX_ENABLE_AUTOSETUP when configuration changes are intended. <br>
Risk: Tax guidance can be incomplete, outdated, or vary by local tax authority. <br>
Mitigation: Confirm filing deadlines, forms, and eligibility requirements with the relevant tax authority or qualified tax professional before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Tax compliance path self-check page](https://mcp.aitaxs.top/web/topic_workflow_china_tax_guidance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related tax invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Related VAT law skill](https://skillhub.cn/skills/tax-vat-law) <br>
- [Related tax judicial cases skill](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Related social insurance tax skill](https://skillhub.cn/skills/tax-social-insurance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown text with procedural steps, checklists, risk self-check results, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services for tax policy questions, risk checks, tax calculations, and knowledge-base metadata; offline scripts provide limited reference guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
