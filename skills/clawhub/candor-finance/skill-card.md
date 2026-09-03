## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor finance workspace: reviewing accounts, spending, budgets, goals, investments, recurring bills, evidence, and approved plans while preserving consent boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a high-trust personal-finance integration that can read sensitive financial records and make reversible internal workspace updates.

Mitigation: Install it only for users comfortable with authenticated Candor workspace access, keep investigations bounded, and review broad cleanup or record-maintenance requests carefully.

Risk: Financial guidance can become incorrect if source coverage, freshness, provenance, or missing records are overlooked.

Mitigation: State coverage limits, freshness, uncertainty, and the evidence behind material claims; avoid turning data gaps into conclusions.

Risk: External money movement, filings, account changes, cancellations, provider contact, and similar actions could affect the user's finances outside Candor.

Mitigation: Require explicit user approval or recoverable prior authority before any external financial action, and ask the user to complete secure controls only they can operate.

Risk: Background monitoring could exceed the user's intended scope if enabled without clear consent.

Mitigation: Configure monitoring only after the user explicitly accepts a cadence and purpose, use one stable recurrence, and contact the user only when attention is warranted.

## Reference(s):

- [Candor Finance skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Candor Start](https://candor.money/START.md?v=0.1.48)
- [Quiet monitoring recipes](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)
- [Money recovery method](methods/candor-money-recovery/METHOD.md)
- [Evidence capture method](methods/candor-evidence-capture/METHOD.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and concise finance findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference authenticated Candor workspace records, exact amounts, dates, evidence, uncertainty, and follow-up actions when supported by the user's data.]

## Skill Version(s):

0.1.48 (source: ClawHub release evidence, released 2026-09-02T16:05:50Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
