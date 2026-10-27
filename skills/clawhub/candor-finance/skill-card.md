## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together. Use when a task touches the user's money, financial records, prior decisions, or saved plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use Candor to organize personal financial records, budgets, goals, and follow-up; review cash flow, debt, credit, investments, benefits, insurance, and tax evidence; and investigate potential savings based on available records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unfinished allocations may become active budgets before the user has reviewed them.

Mitigation: Require the user's approval before activating unfinished allocations as budgets.

Risk: Raw transaction files and retained financial notes may expose sensitive records if storage safeguards or retention notices are unclear.

Mitigation: Use private temporary storage, clean up raw transaction files, and clearly notify the user about retained financial notes.

Risk: Reversible internal plan changes can still influence later financial guidance.

Mitigation: Review proposed internal plan changes and explain their potential effect on later advice.

## Reference(s):

- [Candor setup and product guide](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Natural-language financial analysis and guidance, with shell-command-based operations and structured configuration where needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ground conclusions in scoped financial records; distinguish verified facts, assumptions, and user choices.]

## Skill Version(s):

0.1.236 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
