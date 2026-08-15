## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to work with an authenticated Candor personal-finance workspace, inspect accounts and spending, maintain approved budgets and goals, review investments, investigate savings opportunities, and preserve evidence-backed follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill opens an authenticated personal-finance workspace and can access sensitive financial records.

Mitigation: Install only when comfortable granting Candor and its CLI access to that workspace, and require explicit user confirmation for account access, source connections, imports, and choices that encode user values.

Risk: The skill can set up unattended background monitoring.

Mitigation: Keep background monitoring off unless the user opts in, configure only the documented Candor finance pulse, and verify the recurrence once.

Risk: Record-changing actions such as imports, tax-record cleanup, rules, goals, budgets, or other workspace maintenance can affect financial records.

Mitigation: Use task-scoped authority for bounded reversible writebacks only, and require explicit confirmation for broad changes, external actions, filings, trades, transfers, cancellations, payments, or professional engagements.

## Reference(s):

- [Candor getting started](https://candor.money/START.md)
- [Candor application](https://app.candor.money)
- [Monitoring recipes](references/monitoring.md)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Publisher profile](https://clawhub.ai/user/candor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise financial findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bounded Candor CLI operations against an authenticated workspace and may create evidence-linked notes, impacts, rules, goals, budgets, or monitoring configuration when authorized.]

## Skill Version(s):

0.1.20 (source: ClawHub release metadata; skill frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
