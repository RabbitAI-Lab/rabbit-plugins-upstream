## Description: <br>
A China VAT Law implementation and compliance assistant that helps users review taxable transaction classification, input VAT deduction, retained-credit refund risk, mixed sales, e-invoice handling, taxpayer registration, and structured VAT compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, tax and compliance teams, and external agents use this skill to ask VAT implementation questions, run structured compliance self-checks, identify risk areas, and receive practical guidance for contracts, tax item selection, input deduction, retained-credit refunds, e-invoices, mixed sales, and registration issues. <br>

### Deployment Geography for Use: <br>
Global; content is focused on China VAT compliance. <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill can send tax questions or scenarios to mcp.aitaxs.top and may fall back to public search. <br>
Mitigation: Review network behavior before installation and avoid submitting sensitive taxpayer data unless remote processing and any search fallback are acceptable. <br>
Risk: The security evidence says the skill can store local or browser API credentials. <br>
Mitigation: Use scoped credentials where possible, inspect local credential storage, and remove credentials when the skill is no longer needed. <br>
Risk: The security evidence says the matrix installer and auto-setup paths can install or replace other tax skills and modify user skill configuration. <br>
Mitigation: Treat matrix installation and auto-setup as administrative actions; review planned changes and backups before allowing writes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-vat-law) <br>
- [VAT Law Web Workflow](https://mcp.aitaxs.top/web/topic_workflow_vat_law.html) <br>
- [Tax Policy Knowledge MCP Service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax Policy Knowledge Matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Tax Invoice Compliance Topic](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Tax Judicial Cases Topic](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Tax Restructuring Topic](https://skillhub.cn/skills/tax-restructuring) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with links, checklists, and optional API-backed tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide web workflow links, local configuration guidance, matrix installation steps, and offline fallback checklists.] <br>

## Skill Version(s): <br>
3.14.38 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
