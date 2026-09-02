## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to operate an authenticated Candor financial workspace: inspect financial records, preserve approved budgets and goals, investigate savings opportunities, and keep evidence-linked follow-up organized. It is intended for personal-finance stewardship, not for executing external payments, transfers, trades, filings, cancellations, or account changes without separate authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill works with authenticated personal-finance records and may update Candor workspace records.

Mitigation: Install only for users who want an agent to use Candor as an ongoing financial workspace; keep finance instructions narrow and require explicit approval for budgets, goals, broad rules, imports, or monitoring.

Risk: Useful facts and follow-up notes may be remembered across conversations.

Mitigation: Treat durable memory as user-visible financial continuity, record only useful evidence-linked context, and avoid storing unsupported speculation or unconfirmed preferences.

Risk: A financial investigation can imply external actions such as payments, transfers, cancellations, filings, trades, or account changes.

Mitigation: Keep those actions outside the skill unless the agent has separate explicit authority; use secure Candor pages for account access, source connection, subscription, and payment changes.

Risk: Background monitoring could contact the user or run authenticated checks unexpectedly.

Mitigation: Configure monitoring only after the user chooses a cadence, use one durable scheduler job, and notify only when attention is material or user input is needed.

## Reference(s):

- [Candor Start](https://candor.money/START.md?v=0.1.47)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration]

**Output Format:** [Markdown prose with Candor CLI command recipes, checklists, and small structured snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and candor CLI >=0.3.87 <0.4.0. Outputs may include financial findings, bounded next steps, and reversible Candor workspace writebacks when authorized.]

## Skill Version(s):

0.1.47 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
