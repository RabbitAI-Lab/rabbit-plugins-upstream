## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use Candor Finance to work with an authenticated Candor financial workspace for personal finance review, record organization, budgeting, goals, investments, savings investigations, and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive personal financial records in an authenticated Candor workspace.

Mitigation: Install only when the user accepts this access, and keep use bounded to finance tasks in that workspace.

Risk: An agent could make persistent internal record updates when asked to organize or fix a finance area.

Mitigation: Limit updates to bounded, reversible Candor records and keep real payments, trades, account changes, filings, cancellations, and credential entry under explicit user control.

Risk: Financial guidance can be misleading when records are stale, incomplete, or outside the workspace's coverage.

Mitigation: Use coverage, freshness, caveats, and authoritative current sources where required, and state practical limits before drawing conclusions.

## Reference(s):

- [Candor start guide](https://candor.money/START.md)
- [Quiet monitoring recipes](references/monitoring.md)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Candor publisher profile](https://clawhub.ai/user/candor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise user-facing prose and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI 0.3.94 or newer.]

## Skill Version(s):

0.1.80 (source: ClawHub release metadata; skill frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
