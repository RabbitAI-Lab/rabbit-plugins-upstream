## Description:

Helps users maintain local Chinese personal ledgers, track assets and credit cards, analyze wishlists, and generate monthly spending reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikhayeeer](https://clawhub.ai/user/mikhayeeer)

### License/Terms of Use:

MIT

## Use Case:

People managing Chinese personal finances use this skill to import and validate local transaction files, record spending and repayments, track assets and planned purchases, and review monthly totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Re-importing with --overwrite can replace an existing ledger shard and remove records absent from the new bill.

Mitigation: Back up data/ first, confirm the intended replacement, and review and validate the resulting ledger.

Risk: The agent reads and updates sensitive personal financial files.

Mitigation: Grant access only to intended local ledger paths and review file changes.

Risk: Unpinned npx installation can fetch code that has not been reviewed.

Mitigation: Prefer a pinned or otherwise trusted installation path.

## Reference(s):

- [Skill homepage (publisher-provided)](https://github.com/MikhayEeer/mikhay-accounting-skill)
- [Ledger schema](schema.md)
- [Import rules](import_rules.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON files, CSV files]

**Output Format:** [Markdown guidance and reports; local JSON and CSV ledger files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use script-calculated CNY totals and identify warnings.]

## Skill Version(s):

0.2.2 (source: frontmatter and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
