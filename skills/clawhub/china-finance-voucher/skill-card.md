## Description: <br>
Generate import-ready Chinese finance workbooks from monthly input VAT invoice exports or bank statement exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khanabdullha258974-dot](https://clawhub.ai/user/khanabdullha258974-dot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance operators, accountants, and agent users use this skill to convert monthly Chinese input VAT invoice exports or bank statement exports into accounting-review-ready Excel workbooks for financial-system import. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated voucher rows, account mappings, bank-fee aggregation, or finance assumptions may be incorrect for a specific company or accounting period. <br>
Mitigation: Require qualified finance review of mappings, voucher balances, reconciliations, and recorded assumptions before importing the workbook into a financial system. <br>
Risk: Missing or mismatched bank statement rows can create misleading totals or balance continuity. <br>
Mitigation: Record visible totals, source totals, differences, affected dates, and rows requiring finance judgment instead of inferring missing fee rows by default. <br>


## Reference(s): <br>
- [Finance Voucher Workbook Workflow](references/workflow.md) <br>
- [Bank Statement Workbook Workflow](references/bank_statement.md) <br>
- [ClawHub skill page](https://clawhub.ai/khanabdullha258974-dot/skills/china-finance-voucher) <br>
- [Publisher profile](https://clawhub.ai/user/khanabdullha258974-dot) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Excel workbook files with concise audit notes and supporting implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces import-ready finance workbooks with stable sheets, typed identifiers, balanced voucher rows, account-code mapping, and review notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
