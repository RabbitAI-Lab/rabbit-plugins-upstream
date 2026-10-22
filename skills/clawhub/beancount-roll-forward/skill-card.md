## Description:

Explains how one Beancount balance-sheet account moved over a period using read-only opening, signed-movement, and independently computed closing queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users and finance professionals use this skill to explain a selected local Beancount account's balance-sheet movement for a specified period, with a query-backed tie-out and any unexplained difference left visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive financial records, and an ambiguous ledger selection could produce a misleading explanation.

Mitigation: Confirm the intended local ledger when discovery is ambiguous before running queries.

Risk: Shared import or editing examples could be mistaken for permission to change the ledger.

Mitigation: Keep this workflow read-only; handle ledger modifications only as a separately requested task.

## Reference(s):

- [Roll-forward calculation](references/roll-forward.md)
- [bea command recipes](references/bea-cli.md)
- [Compatibility paths](references/compatibility.md)
- [Project homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-roll-forward)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands]

**Output Format:** [Markdown with a balance tie-out and reproducible bea query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only explanation based on ledger query results; financial records may be sensitive, and no ledger files are modified.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
