## Description:

Helps Chinese-speaking users maintain local personal ledgers, track assets, debts, and wishlists, and validate or summarize financial records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikhayeeer](https://clawhub.ai/user/mikhayeeer)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing Chinese personal finances can import and maintain local ledger files, track asset and debt snapshots and planned purchases, and produce validated daily or monthly summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reimbursement report totals can disagree with daily and category breakdowns.

Mitigation: Reconcile reimbursement reports against the source ledger records before relying on the totals.

Risk: Replacing ledger shards can discard existing records.

Mitigation: Back up the ledger and confirm the intended target files before saving recalculated balances or replacing records.

Risk: The documented installation command is not pinned to a revision.

Mitigation: Choose a reviewed installer and skill revision before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mikhayeeer/skills/mikhay-accounting-skill)
- [Project homepage (Clawdis metadata)](https://github.com/MikhayEeer/mikhay-accounting-skill)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, CSV, Markdown, Guidance]

**Output Format:** [Markdown summaries and JSON or CSV ledger files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ledger data stays local; reported totals should come from the provided validation and reporting workflows.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
