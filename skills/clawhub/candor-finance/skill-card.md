## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor personal-finance workspace: reviewing accounts, spending, budgets, goals, investments, recurring bills, evidence, and follow-up while keeping consent boundaries visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to sensitive personal-finance workspace records, including transactions, accounts, budgets, goals, insurance, tax, benefit, and investment context.

Mitigation: Install and use it only for an authenticated Candor workspace where that access is expected, and keep reads tied to money-related tasks.

Risk: Financial conclusions can be misleading when workspace coverage, freshness, provenance, or currency units are incomplete or stale.

Mitigation: Check coverage, freshness, caveats, provenance, and units before making claims, and state practical limits instead of treating data gaps as conclusions.

Risk: Agents may appear to have authority to move money, file documents, apply for products, cancel services, trade, change accounts, or handle credentials.

Mitigation: Keep those actions explicit and user-controlled; this skill alone does not authorize external financial actions or credential changes.

Risk: Internal notes or corrections can affect future financial context if recorded without clear support.

Mitigation: Store only bounded notes, corrections, or follow-up records that are supported by evidence and task-scoped user authority.

## Reference(s):

- [Candor setup and OpenClaw materials](https://candor.money/START.md?v=0.1.49)
- [ClawHub candor-finance skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)
- [Evidence capture method](methods/candor-evidence-capture/METHOD.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and structured financial findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded internal Candor notes, corrections, or follow-up records when supported by evidence and user authority.]

## Skill Version(s):

0.1.49 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
