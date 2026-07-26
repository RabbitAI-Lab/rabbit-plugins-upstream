## Description: <br>
Analyze bank transactions, categorize spending, track monthly budgets, detect overspending and anomalies. Outputs interactive HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreolf](https://clawhub.ai/user/andreolf) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Individuals and finance-focused agent workflows use this skill to parse bank transaction exports, classify spending, compare activity against monthly budgets, and generate local spending reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated financial reports load Google Fonts despite the skill's local-only and no-network claims. <br>
Mitigation: Review or remove the external font request before using the report in strict local-only privacy environments. <br>
Risk: Transaction reports and saved state may remain under ~/.watch_my_money/ until deleted or reset. <br>
Mitigation: Use the reset workflow or manually delete stored reports and state when financial data should no longer be retained. <br>
Risk: The privacy blur is a display feature and should not be treated as redaction for shared reports. <br>
Mitigation: Remove or redact sensitive transaction data before sharing reports outside the local environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andreolf/skills/watch-my-money) <br>
- [Budget Templates](references/budget-templates.md) <br>
- [Common Merchant Mappings](references/common-merchants.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands plus local HTML and JSON report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist budgets, merchant overrides, monthly JSON data, and HTML reports under ~/.watch_my_money/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
