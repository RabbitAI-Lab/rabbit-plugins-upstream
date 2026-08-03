## Description: <br>
tax-vat-law helps agents answer Chinese VAT implementation and compliance questions, including taxable transaction classification, input credit checks, deemed taxable transactions, mixed sales, excess input VAT refund controls, taxpayer registration thresholds, and structured self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and compliance teams use this skill to ask VAT law implementation questions, run structured compliance self-checks, identify VAT risk areas, and draft checklist or report-style guidance. It does not replace filing, tax agency, legal due diligence, or final determinations by tax authorities or courts. <br>

### Deployment Geography for Use: <br>
Global, with substantive coverage focused on mainland China VAT compliance scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, calculations, and web self-check metrics can be sent to mcp.aitaxs.top for cloud processing. <br>
Mitigation: Review data handling before installation and do not submit sensitive taxpayer, invoice, contract, or financial details unless that cloud processing model is acceptable. <br>
Risk: The skill can create persistent API credentials and client identifiers locally. <br>
Mitigation: Inspect local credential storage, rotate or remove credentials when no longer needed, and restrict access to the user profile where the client data is stored. <br>
Risk: Some setup modes can modify MCP client configuration files. <br>
Mitigation: Run setup in dry-run or review mode first, inspect configuration changes before enabling them, and keep backups of MCP client configuration files. <br>
Risk: VAT compliance outputs may be incomplete or unsuitable for a specific filing, audit, or dispute posture. <br>
Mitigation: Validate conclusions against current official guidance and qualified tax or legal professionals before filing, claiming refunds, or taking a position in a dispute. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-vat-law) <br>
- [VAT law workflow](https://mcp.aitaxs.top/web/topic_workflow_vat_law.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related digital invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional code, shell command, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service and local offline fallback; users should avoid sensitive taxpayer, invoice, contract, or financial details unless they accept that processing and credential persistence model.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
