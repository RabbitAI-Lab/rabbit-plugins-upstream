## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor workspace for personal-finance record review, budgeting, goals, investments, cashflow, subscriptions, recovery opportunities, evidence capture, and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can work with sensitive financial records through an authenticated Candor workspace.

Mitigation: Install it only when the user wants an agent to use that workspace, keep account access and source-connection changes visible to the user, and avoid exposing raw financial records unnecessarily.

Risk: Some plans, follow-ups, and monitoring choices may be saved as durable notes or run on a recurring cadence.

Mitigation: Save only useful, evidence-linked continuity; use background monitoring only with an explicit cadence and purpose the user wants.

Risk: Financial records may have coverage, freshness, or provenance gaps that can make conclusions incomplete.

Mitigation: Inspect coverage and freshness before making claims, state practical limits plainly, and use current authoritative sources for changing rates, limits, terms, rules, deadlines, or benchmarks.

Risk: Personal finance work can imply external actions such as transfers, purchases, cancellations, applications, filings, trades, or account changes.

Mitigation: Treat those actions as separate consent moments and require recoverable or fresh user authority before proceeding.

## Reference(s):

- [Candor Finance skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Candor setup and start guide](https://candor.money/START.md)
- [Quiet monitoring recipes](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)
- [Evidence capture method](methods/candor-evidence-capture/METHOD.md)
- [Transaction organization method](methods/candor-transaction-organization/METHOD.md)
- [Recurring bills method](methods/candor-recurring-bills/METHOD.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured financial review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Candor workspace data; may create durable notes or approved records only within documented consent boundaries.]

## Skill Version(s):

0.1.74 (source: server release metadata, created 2026-09-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
