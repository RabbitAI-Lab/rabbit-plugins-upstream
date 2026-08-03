## Description: <br>
Provides China tax filing and compliance guidance for electronic tax bureau workflows, tax registration, invoice handling, tax declarations, export tax rebate steps, tax deregistration, incentives, credit repair, forms, filing calendars, and common tax questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax operators, and developers use this skill to obtain structured China tax procedure guidance, risk self-checks, tax calculations, policy Q&A, and checklist-style support before completing official filings themselves. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and risk scenarios may be sent to the third-party cloud service mcp.aitaxs.top. <br>
Mitigation: Use only non-confidential scenarios unless the provider's privacy terms, retention practices, and data-handling controls are acceptable. <br>
Risk: Fallback behavior may query public search engines for tax information. <br>
Mitigation: Avoid entering identity numbers, client names, bank details, invoice data, or confidential business facts when using the skill. <br>
Risk: The setup path can modify local MCP or editor configuration when write mode is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled and do not run setup in write mode unless local configuration changes are intended and reviewed. <br>
Risk: Tax guidance can become outdated or differ by locality. <br>
Mitigation: Confirm deadlines, forms, and filing positions against official tax authority sources or a qualified tax professional before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Tax compliance path self-check](https://mcp.aitaxs.top/web/topic_workflow_china_tax_guidance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [MCP tax policy service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge) <br>
- [Related skill: tax policy knowledge](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related skill: tax invoice compliance](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Related skill: tax VAT law](https://skillhub.cn/skills/tax-vat-law) <br>
- [Related skill: tax judicial cases](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Related skill: social insurance tax compliance](https://skillhub.cn/skills/tax-social-insurance) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown text, structured JSON-like tool results, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a third-party cloud MCP service for tax policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline fallbacks provide local checklist and keyword-reference guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
