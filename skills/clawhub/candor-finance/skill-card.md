## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace, inspect money-related records, preserve approved plans, investigate savings or recovery opportunities, and keep follow-up evidence organized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read sensitive account, transaction, budget, goal, investment, benefits, and tax-adjacent records.

Mitigation: Install it only for users who want an agent to work with their Candor financial workspace, and keep analysis bounded to user-authorized financial tasks.

Risk: The skill may store internal follow-up notes or approved organization changes in the workspace.

Mitigation: Use writebacks only for disclosed, purpose-aligned continuity and preserve evidence, dates, caveats, and user authority with the stored records.

Risk: Financial actions such as payments, transfers, cancellations, filings, trades, account changes, or merchant contact could affect the user outside Candor.

Mitigation: Require separate user authority before any external financial action and keep routine Candor workspace reads or reversible organization separate from those actions.

Risk: Background monitoring may run without the user actively watching the session.

Mitigation: Configure monitoring only after opt-in, make the cadence explicit, and contact the user only when follow-up merits attention or a scheduled run fails.

## Reference(s):

- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor Start](https://candor.money/START.md?v=0.1.55)
- [Quiet monitoring recipes](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and concise financial findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact amounts, dates, uncertainty, evidence references, follow-up notes, and bounded Candor workspace updates when authorized.]

## Skill Version(s):

0.1.55 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
