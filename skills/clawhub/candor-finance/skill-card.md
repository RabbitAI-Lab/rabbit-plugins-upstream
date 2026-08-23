## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace for account organization, spending review, budgeting, savings investigations, investment-cost review, evidence capture, and financial follow-through.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates on sensitive personal-finance records in an authenticated Candor workspace.

Mitigation: Install only when comfortable granting Candor and its CLI access to the financial workspace, and keep user-facing answers focused on supported amounts, dates, uncertainty, and next steps.

Risk: Routine workspace maintenance can create or update internal financial records and follow-up notes.

Mitigation: Keep changes bounded, reversible, evidence-linked, and aligned with the user's request; confirm goals, priorities, risk tolerance, and other preference-bearing choices before recording them as approved.

Risk: External financial actions such as payments, transfers, cancellations, filings, trades, account connections, credential handling, subscription changes, and professional engagements could materially affect the user.

Mitigation: Treat those as separate consent moments and direct account, credential, subscription, and payment changes through secure Candor pages or other authorized external flows.

Risk: Financial records, imported documents, merchant text, rates, terms, rules, and deadlines may be incomplete, stale, ambiguous, or jurisdiction-specific.

Mitigation: Check coverage, freshness, provenance, exact currency units, and current authoritative sources when needed; state evidence gaps rather than turning them into conclusions.

Risk: Background monitoring could be mistaken for standing authority to act.

Mitigation: Configure monitoring only after the user explicitly chooses a cadence and purpose; use one durable recurrence and contact the user only when follow-up merits attention or needs their authority.

## Reference(s):

- [Candor Finance ClawHub page](https://clawhub.ai/candor/skills/candor-finance)
- [Candor OpenClaw start page](https://candor.money/START.md?v=0.1.30)
- [Monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline shell commands and structured financial-record updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI access; outputs may include bounded reversible workspace writebacks, linked notes, and user-facing financial summaries.]

## Skill Version(s):

0.1.30 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
