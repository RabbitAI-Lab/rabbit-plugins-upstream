## Description:

Helps an agent use Candor to organize personal financial records, investigate savings, review investments, and keep supported decisions and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People using a Candor-connected agent can review their accounts, spending, budgets, debts, investments, and financial goals; the agent can investigate records, explain findings, and make authorized workspace changes or set requested follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access sensitive financial records and make internal organizational changes.

Mitigation: Limit access and changes to the user's task; confirm scope before changes and verify the resulting records.

Risk: Saved notes and scheduled monitoring can persist financial context or run later without sufficiently clear user-facing consent.

Mitigation: Confirm what will be retained and the purpose, cadence, and notification settings of any requested monitoring before saving it.

Risk: Property estimates can contact an external provider and may expose an address or financial details.

Mitigation: Before requesting estimates, tell the user what may be shared with the provider and obtain explicit confirmation.

Risk: Financial guidance could be mistaken for permission to make payments, trades, filings, cancellations, or provider changes.

Mitigation: Require separate clear confirmation before taking any such external action.

## Reference(s):

- [Candor setup and documentation](https://candor.money/START.md)
- [Setup and access](references/setup.md)
- [Evidence handling](references/evidence.md)
- [Continuity](references/continuity.md)
- [Scheduled monitoring](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with financial findings, record links, assumptions, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record authorized workspace changes, saved notes, and requested follow-up.]

## Skill Version(s):

0.1.145 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
