## Description:

Use Candor for personal finance to organize accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together when a task touches money, financial records, prior decisions, or approved plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace: inspect financial records, organize spending, preserve approved plans, investigate savings or recovery opportunities, and keep evidence-linked follow-up. It is intended for personal-finance assistance where workspace reads and reversible Candor record updates are useful, while external financial actions remain user-controlled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive financial workspace records and store follow-up notes or approved plans.

Mitigation: Install only for authenticated Candor workspaces where the user is comfortable granting this access, and keep stored continuity tied to explicit evidence, approved context, and useful follow-up.

Risk: The skill can make scoped reversible corrections or imports inside Candor, which could affect later financial analysis if unsupported.

Mitigation: Use bounded, evidence-backed workspace updates; verify coverage, freshness, schema, amounts, dates, and provenance before writing; and keep corrections reversible and reviewable.

Risk: External financial actions such as payments, transfers, trades, filings, cancellations, credential repair, subscription changes, and payment changes are outside the skill's automatic authority.

Mitigation: Require separate user-controlled authorization for each external action and route account access, credentials, source connections, subscription, and payment changes through secure Candor pages.

## Reference(s):

- [Candor OpenClaw materials](https://candor.money/START.md?v=0.1.38)
- [ClawHub candor-finance release](https://clawhub.ai/candor/skills/candor-finance)
- [Candor Finance skill source](artifact/SKILL.md)
- [Financial review method](artifact/methods/candor-financial-review/METHOD.md)
- [Evidence capture method](artifact/methods/candor-evidence-capture/METHOD.md)
- [Quiet monitoring recipes](artifact/references/monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and concise text with inline shell commands when Candor CLI actions are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact amounts, dates, uncertainty, evidence references, follow-up notes, approved plans, or scoped reversible Candor workspace updates.]

## Skill Version(s):

0.1.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
