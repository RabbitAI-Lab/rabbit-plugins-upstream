## Description: <br>
Reconcile bank accounts against QuickBooks Online (QBO) for monthly close, discrepancy investigation, or audit workpapers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samledger67-dotcom](https://clawhub.ai/user/samledger67-dotcom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Accounting teams, finance operators, and agents supporting monthly close use this skill to compare QBO general ledger activity with bank statement CSVs, identify unmatched transactions, and produce reconciliation workpapers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles sensitive bank statement and QuickBooks Online data and may leave generated workbooks or cache files on local storage. <br>
Mitigation: Use approved private storage, restrict access to generated workbooks and .cache files, and avoid shared or synced Desktop locations unless they meet the organization's data-handling requirements. <br>
Risk: Running against the wrong QuickBooks client slug or overly broad QBO access can expose or reconcile the wrong company data. <br>
Mitigation: Confirm the client slug before running and use the least-privilege QuickBooks access needed for reconciliation. <br>
Risk: Suggested adjusting entries and unmatched transaction classifications can affect financial close decisions if accepted without review. <br>
Mitigation: Review the reconciliation summary, unmatched tabs, and suggested journal entries before posting entries or relying on the workbook for audit support. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samledger67-dotcom/bank-reconciliation) <br>
- [Source skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with bash command examples and reconciliation workflow details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides creation of an Excel reconciliation workbook and a local change-tracking cache.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
