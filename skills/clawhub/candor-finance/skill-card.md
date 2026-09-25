## Description:

Helps users organize personal finances in Candor, review accounts and investments, investigate savings, and maintain evidence-backed budgets, goals, and follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their assistants use this skill to review financial records, evaluate spending and planning options, and maintain approved financial context in a Candor workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests to organize, maintain, schedule, or import evidence may create durable changes in the user's Candor workspace.

Mitigation: Confirm the scope of the user's request, stay within their authority, and verify any workspace changes.

Risk: Financial records may be incomplete or stale, leading to unsupported conclusions or recommendations.

Mitigation: Check record coverage and dates, distinguish assumptions from observed facts, and disclose uncertainty.

Risk: Workspace access could be mistaken for permission to make real-world financial or provider-facing decisions.

Mitigation: Require separate explicit authority for payments, trades, cancellations, filings, credential entry, and merchant or provider contact.

## Reference(s):

- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor setup and access](https://candor.money/START.md)
- [Evidence and record-reading guidance](references/evidence.md)
- [Scheduling guidance](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language financial analysis and recommendations, with commands or workspace links when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and compatible Candor CLI; authorized tasks may update internal financial records and follow-up.]

## Skill Version(s):

0.1.140 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
