## Description:

Split group expenses fairly (equal or weighted shares) and compute the minimum number of money transfers to settle up. Reads a simple ledger of who paid for what, handles non-even splits, weights, and shared vs personal items, then produces an optimal settlement plan (who pays whom, how much) plus a fairness audit. Use when settling trip costs with friends, splitting rent and utilities among roommates, or running any shared-expense pool without a dedicated app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to settle shared expenses for trips, roommates, clubs, and similar groups from a local ledger. It computes fair shares, weighted splits, minimum settlement transfers, audit tables, and optional JSON output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger details and audit output may reveal personal spending behavior.

Mitigation: Review the ledger before sharing output and share only settlement lines when detailed item history is sensitive.

Risk: Settlement results are only as accurate as the ledger amounts, participants, currency assumptions, and weights provided.

Mitigation: Audit inputs with the per-item view before relying on the settlement plan.

## Reference(s):

- [Fair Splitting & Minimum-Transfer Settlement Reference](references/settlement-theory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands, tabular audit text, settlement lines, and optional JSON export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally from ledger input and uses integer cents for settlement calculations.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
