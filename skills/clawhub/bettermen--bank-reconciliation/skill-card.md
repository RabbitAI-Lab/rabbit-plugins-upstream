## Description: <br>
导入银行流水和账面记录，使用精确、模糊和关联匹配自动核销，并生成带待确认异常项的 HTML/JSON 对账结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance teams and agents assisting finance operations use this skill to reconcile bank statement exports against ledger records, review automatically matched transactions, and focus manual attention on unmatched items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bank statement, ledger, JSON result, and HTML report files may contain sensitive financial records. <br>
Mitigation: Choose output locations intentionally, restrict access to generated reports, keep processing local, and delete result files when no longer needed. <br>
Risk: Fuzzy and association matches can produce incorrect transaction pairings when dates, amounts, or descriptions are ambiguous. <br>
Mitigation: Review low-confidence matches and all unmatched items before relying on the reconciliation result. <br>


## Reference(s): <br>
- [Matching rules reference](references/matching_rules.md) <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/bank-reconciliation) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, JSON, HTML report, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, plus local JSON and HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local Excel/CSV inputs and writes reconciliation_result.json and reconciliation_report.html by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
