## Description:

Summarizes SuperBooks financial reports, including profit and loss, spending, balances, burn rate, runway, and top customers, without changing account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners and team members use this skill to understand revenue, expenses, cash position, and customer trends from their SuperBooks reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive financial reports and account summaries could expose more business data than needed.

Mitigation: Limit SuperBooks OAuth grants to read and report scopes where possible, and request only reports needed for the question.

Risk: A financial summary could be mistaken for tax or legal advice or used to justify account changes.

Mitigation: Keep the skill read-only and do not use its summaries for tax or legal advice or write actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/superbooks-reading-financial-reports)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown financial summary with a month-by-month table and brief observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the team's currency and reports only figures returned by SuperBooks.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
