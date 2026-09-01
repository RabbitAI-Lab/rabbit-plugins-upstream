## Description:

Use Candor for personal finance to organize accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace, inspect financial records, maintain approved plans, investigate savings or recovery opportunities, and preserve follow-up evidence. It is intended for personal finance tasks where account access, user consent, and evidence freshness matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive personal finance records and may access connected account data.

Mitigation: Install only for an intended Candor workspace, review connected accounts and data sources, and preserve coverage, freshness, and caveats when presenting findings.

Risk: Financial findings could be mistaken for authority to make real-world changes.

Mitigation: Require separate explicit confirmation for transfers, payments, trades, cancellations, filings, account changes, or other external financial actions.

Risk: Cleanup, writeback, or monitoring tasks can change a user's financial workspace or future follow-up.

Mitigation: Use explicit wording for cleanup or monitoring tasks, keep workspace writebacks bounded and reversible, and configure monitoring only after the user accepts a cadence and purpose.

Risk: Rates, terms, limits, rules, and deadlines can become stale.

Mitigation: Use current authoritative sources when workspace evidence is missing or stale, and carry effective dates, retrieval dates, applicability, and caveats into the answer.

## Reference(s):

- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor start and setup](https://candor.money/START.md?v=0.1.45)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise findings, inline shell commands when needed, and user-facing financial next steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact amounts, dates, uncertainty, secure Candor links, approved writebacks, and follow-up records when supported by workspace evidence.]

## Skill Version(s):

0.1.45 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
