## Description:

Use Candor for personal finance tasks that touch the user's money, financial records, prior decisions, or approved plans by organizing accounts and spending, remembering approved budgets and goals, reviewing investments, investigating possible savings, and keeping evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor workspace for personal-finance review, cash-flow analysis, subscriptions, benefits, debt, evidence capture, tax preparation, record organization, and follow-up. It helps the agent inspect financial records, preserve approved decisions, propose bounded next steps, and avoid acting outside the user's authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose an agent to sensitive personal-finance records.

Mitigation: Enable it only for users who accept Candor workspace access, and keep financial claims tied to bounded evidence, coverage, freshness, exact amounts, dates, and uncertainty.

Risk: Persistent notes, impacts, transaction corrections, rules, or background monitoring could continue beyond the immediate conversation.

Mitigation: Confirm how the user can review, edit, and delete those records and configure quiet monitoring only after an explicit opt-in.

Risk: The skill discusses actions involving external accounts, payments, trades, filings, cancellations, messages, and similar high-impact changes.

Mitigation: Require recoverable prior authority or fresh confirmation before any external action, bulk edit, or choice that reflects the user's goals, priorities, or risk tolerance.

## Reference(s):

- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor setup homepage](https://candor.money/START.md)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command recipes for agent use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and candor CLI >=0.3.64 <0.4.0.]

## Skill Version(s):

0.1.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
