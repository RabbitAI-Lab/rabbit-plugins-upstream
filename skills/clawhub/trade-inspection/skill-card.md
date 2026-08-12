## Description: <br>
外贸出口检测与单证合规助手 helps exporters draft and review export inspection, trade-document, HS-code, and market-access compliance materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lzh1998-ui](https://clawhub.ai/user/lzh1998-ui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, manufacturers, and exporters use this skill to perform preliminary export inspection review, document consistency checks, HS-code triage, market certification screening, and draft trade-compliance letters or inspection reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade-compliance guidance may be incomplete, outdated, or unsuitable for a specific shipment, market, or controlled item. <br>
Mitigation: Treat outputs as preliminary drafts and verify regulations with official sources, qualified customs brokers, compliance professionals, or counsel before shipment. <br>
Risk: The HS-code helper may send product or shipment search terms to an external placeholder API when online lookup is enabled. <br>
Mitigation: Use local lookup for sensitive descriptions, avoid entering confidential shipment details, and configure only approved external endpoints before enabling online queries. <br>
Risk: Generated inspection reports and compliance letters can look formal while missing real-world evidence such as photos, signatures, lab reports, or authorized approvals. <br>
Mitigation: Require human completion and approval of factual fields, attachments, signatures, and supporting evidence before using generated documents externally. <br>


## Reference(s): <br>
- [主流出口市场检测标准对照表](references/standards.md) <br>
- [单证审核逐项清单](references/document_checklist.md) <br>
- [常见出口品类 HS 编码参考与风险提示](references/hs_codes.md) <br>
- [主要出口目的国禁限运清单摘要](references/export_restrictions.md) <br>
- [英文合规说明函可填充模板](references/compliance_letters.md) <br>
- [出口验货报告模板](assets/inspection_report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports, tables, checklists, draft letters, and optional helper-script command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are preliminary drafts and review aids; final trade, customs, legal, and regulatory decisions require qualified human review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
