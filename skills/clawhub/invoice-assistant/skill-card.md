## Description: <br>
读取并分析本机“小河狸发票助手”中的发票台账、明细、趋势、排行和已归档电子发票附件数据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yk-niu](https://clawhub.ai/user/yk-niu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Finance and operations users use this skill to let an agent query local Little Beaver Invoice Assistant data for invoice ledger summaries, customer and supplier rankings, monthly trends, tax amount summaries, and attachment metadata. It supports read-only analysis and local attachment opening; it does not import, modify, delete, or upload invoice records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive invoice ledger data, tax IDs, amounts, raw invoice JSON, and attachment metadata to the agent. <br>
Mitigation: Install only when this access is intended, keep the endpoint on 127.0.0.1 or localhost, and request only the minimum data needed for the user's question. <br>
Risk: Opening attachments can launch a local PDF, OFD, or XML viewer and reveal local documents on the user's machine. <br>
Mitigation: Call open-attachment only when the user explicitly asks to open a specific archived attachment. <br>
Risk: Invoice ledger calculations can be mistaken for formal tax filing conclusions. <br>
Mitigation: Present results as ledger analysis, include company and date scope, state whether voided invoices are excluded, and avoid describing outputs as final tax declarations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yk-niu/skills/invoice-assistant) <br>
- [Local Skill API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON summaries with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local localhost API responses and should report selected company, date range, and whether voided invoices are excluded.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
