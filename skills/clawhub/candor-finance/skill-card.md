## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace, investigate money-related questions, organize records, model plans, and preserve approved decisions with supporting evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill works with sensitive personal financial records in an authenticated Candor workspace.

Mitigation: Install it only for users who intend Candor CLI access to that workspace, and keep account connections, credential repair, subscription changes, and payment details in Candor's secure flows.

Risk: Financial conclusions can be wrong when records, coverage, rates, terms, benefits, or tax rules are incomplete or stale.

Mitigation: Ground answers in scoped workspace evidence, use authoritative current sources when the workspace lacks material terms, and label assumptions and uncertainty.

Risk: Internal updates such as categorization, imports, notes, budgets, goals, or follow-up checks can misrepresent user intent if authority is unclear.

Mitigation: Make only bounded, reversible internal changes authorized by the user, verify the result after writing, and require explicit approval before saving preferences, budgets, goals, priorities, or decisions.

Risk: External money movement, filings, benefit elections, cancellations, messages, applications, or account connection changes could exceed the skill's proper authority.

Mitigation: Keep those actions under explicit user control through Candor or the provider's secure flow, and never request pasted credentials or codes.

## Reference(s):

- [Candor Start](https://candor.money/START.md)
- [Setup and access](references/setup.md)
- [Evidence handling](references/evidence.md)
- [Continuity](references/continuity.md)
- [Monitoring](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with executed Candor CLI command recipes and structured financial notes when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify supporting records, dates, amounts, assumptions, uncertainty, and authorized changes.]

## Skill Version(s):

0.1.98 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
