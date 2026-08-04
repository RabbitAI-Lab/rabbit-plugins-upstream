## Description: <br>
Provides China VAT-law implementation guidance for tax compliance, including taxable transaction classification, input VAT deductions, deemed taxable transactions, mixed sales, retained-credit refunds, taxpayer registration, and structured self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, compliance, and advisory users can use this skill to triage VAT-law implementation questions, run structured VAT compliance self-checks, identify risk areas, and produce practical remediation guidance for review against official tax authority positions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions and related context to mcp.aitaxs.top for cloud processing. <br>
Mitigation: Do not provide confidential company, invoice, contract, or taxpayer details unless cloud processing is approved for that data. <br>
Risk: The skill stores API-key material under ~/.tax-policy-client and may use public search fallback when remote service calls fail. <br>
Mitigation: Review local credential storage and fallback behavior before installation, and use an environment where such storage and network access are acceptable. <br>
Risk: The skill can modify local agent MCP configuration when setup is explicitly enabled. <br>
Mitigation: Prefer manual setup and do not enable TAX_ENABLE_AUTOSETUP until the exact configuration changes have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-vat-law) <br>
- [VAT-law compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_vat_law.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text guidance with structured checklists, risk summaries, remediation steps, and optional MCP or web workflow links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote tax-policy MCP services, use offline fallback checks, and present outputs that should be reviewed against current official tax authority guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
