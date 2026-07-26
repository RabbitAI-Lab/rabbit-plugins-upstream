## Description: <br>
Accounting assistant for invoice OCR, authenticity verification, reimbursement form filling, and approval-system handoff with enterprise-controlled configuration and local data processing by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, accounting, and operations users use this skill to extract invoice data, check invoice authenticity, populate reimbursement templates, and prepare approval submissions. Developers and administrators configure OCR, verification, template, and approval integrations for their enterprise environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured verification or approval features can send sensitive invoice or reimbursement data to external services. <br>
Mitigation: Keep approval.platform set to none unless an approval provider is intentionally enabled, verify all custom endpoints, and require human confirmation before external verification or approval submission. <br>
Risk: Installer and setup commands may require elevated privileges or change local OCR dependencies. <br>
Mitigation: Inspect installer commands before running them and avoid elevated privileges unless the enterprise administrator has approved the change. <br>
Risk: OCR and invoice checks can produce incorrect or incomplete financial data. <br>
Mitigation: Require human review of low-confidence OCR fields, invoice numbers, amounts, and reimbursement content before recordkeeping or approval submission. <br>


## Reference(s): <br>
- [ClawHub Receipt Compliance Skill Page](https://clawhub.ai/fyniujin/skills/receipt-compliance) <br>
- [Enterprise Setup Guide](artifact/references/setup-guide.md) <br>
- [API Endpoint Notes](artifact/references/api-endpoints.md) <br>
- [Risk Declaration](artifact/references/risk-declaration.md) <br>
- [Tax Rules](artifact/references/tax-rules.md) <br>
- [China Tax Invoice Verification](https://inv-veri.chinatax.gov.cn/) <br>
- [China Electronic Tax Service](https://etax.chinatax.gov.cn/) <br>
- [DingTalk Open Platform](https://open-dev.dingtalk.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands and configuration examples; agent workflows may produce JSON receipt data, Excel reimbursement files, and verification or approval results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes invoice images, PDFs, OFD/XML invoice data, templates, and enterprise configuration; external verification or approval submission should require user confirmation.] <br>

## Skill Version(s): <br>
3.7.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
