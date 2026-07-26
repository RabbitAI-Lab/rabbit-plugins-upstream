## Description: <br>
PhoenixClaw Ledger passively detects financial activity in conversations and payment screenshots, records transactions, and produces budget reports, insights, and transaction views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[goforu](https://clawhub.ai/user/goforu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External PhoenixClaw users use this skill to track personal spending and income from conversations and payment screenshots, then review budgets, goals, reports, and transaction history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill passively records sensitive financial activity from conversations, memory, and payment screenshots. <br>
Mitigation: Enable it only after confirming the user wants passive tracking, and verify how to disable auto-recording and review or undo recorded entries. <br>
Risk: Stored receipts, ledgers, reports, and screenshots may expose personal financial information if placed in synced or shared folders. <br>
Mitigation: Keep the finance directory out of shared or synced locations unless the user has explicitly accepted that exposure, and provide a way to delete stored receipts and reports. <br>
Risk: Cross-plugin financial insights may correlate spending with mood, goals, or social data. <br>
Mitigation: Turn off cross-plugin insight sharing when the user does not want financial data correlated with other personal context. <br>


## Reference(s): <br>
- [PhoenixClaw Ledger on ClawHub](https://clawhub.ai/goforu/skills/phoenixclaw-ledger) <br>
- [Expense Detection from Conversations](references/expense-detection.md) <br>
- [Payment Screenshot Recognition](references/payment-screenshot.md) <br>
- [Merchant to Category Mapping](references/merchant-category-map.md) <br>
- [Category Rules and Definitions](references/category-rules.md) <br>
- [Budget Tracking](references/budget-tracking.md) <br>
- [Financial Insights Generation](references/financial-insights.md) <br>
- [Cron Setup for PhoenixClaw Ledger](references/cron-setup.md) <br>
- [Financial Goal Management](references/goal-management.md) <br>
- [Real-time Financial Query Patterns](references/query-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown reports and journal sections with YAML configuration snippets and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local finance ledger, budget, goal, transaction browser, and report files for PhoenixClaw workflows.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
