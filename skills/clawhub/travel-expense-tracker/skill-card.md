## Description:

多币种记录旅行消费、汇率自动换算、分类统计与预算管理，旅行花钱心里有数。暑期旅行开销记录，AA记账轻松分摊

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to record trip expenses in multiple currencies, summarize spending by category, date, or currency, and check spending against trip budgets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trip names, dates, amounts, descriptions, and budgets are stored in local JSON files.

Mitigation: Use the skill only where local storage of travel expense data is acceptable, and protect or delete the local travel_expenses/ files according to the user's data-retention needs.

Risk: The documented frontmatter tool name differs from the script tool names used by the artifact.

Mitigation: Invoke the script-supported tools add_expense, expense_summary, and budget_check until the publisher aligns the metadata.

Risk: Currency conversion uses built-in reference rates rather than live rates.

Mitigation: Treat converted CNY totals as estimates and verify exchange rates separately for financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-expense-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Natural-language guidance with JSON-backed local expense records and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local JSON files under travel_expenses/ and built-in reference exchange rates.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
