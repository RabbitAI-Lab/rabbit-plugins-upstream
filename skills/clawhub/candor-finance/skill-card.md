## Description:

Candor Finance helps agents use an authenticated Candor workspace to organize accounts and spending, preserve approved budgets and goals, review investments, investigate possible savings, and keep financial evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill for personal-finance work in Candor, including account and spending review, budgeting, cash-flow projection, investment and fee review, recurring-bill investigation, evidence capture, and follow-up tracking. It is intended for authenticated Candor workspaces and keeps recommendations grounded in scoped financial records, approved user decisions, and current authoritative sources when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive financial records through Candor CLI access and saved JSON review pages.

Mitigation: Install only when the user trusts Candor, run review workflows in a private temporary directory, keep saved result pages bounded, and clean them up after use.

Risk: The skill can submit sanitized vendor telemetry without a separate user approval step.

Mitigation: Require a consent control or local review policy before unattended telemetry, and strip account numbers, balances, amounts, merchants, institutions, people, and other personal data before any report.

Risk: Personal-finance recommendations can be misleading when based on stale terms, incomplete account coverage, or unsupported tax, legal, medical, insurance, or investment assumptions.

Mitigation: Use Candor's scoped records and server calculations, preserve uncertainty, verify material rates, terms, benefits, and tax rules from authoritative sources, and stop before external payments, trades, filings, claims, enrollments, or account changes without explicit authority.

## Reference(s):

- [Candor Start](https://candor.money/START.md)
- [Setup, access and openings](references/setup.md)
- [Read and present evidence](references/evidence.md)
- [Useful financial continuity](references/continuity.md)
- [Scheduled work](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI access; financial answers should include scoped evidence, dates, amounts, assumptions, and uncertainty.]

## Skill Version(s):

0.1.106 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
