## Description:

Process bank transaction CSV exports (Nordea, ICA), auto-categorize transactions using configurable rules, manage transaction links, and generate analytical database views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to manage local personal-finance transaction data, import bank CSV exports, apply categorization rules, link transfers and reimbursements, and generate SQLite-backed financial summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool can modify a local personal-finance SQLite database, including cleanup, linking, deletion, and recurring-payment discovery workflows.

Mitigation: Keep database backups, use dry-run modes for auto-linking and recurring discovery, review proposed changes, and pass --yes only when intentionally bypassing confirmation prompts.

Risk: Automated categorization, recurring-payment detection, and salary-period configuration can produce misleading financial summaries if rules or boundaries are wrong.

Mitigation: Preview matches where supported, review categorization rules and adjusted amounts, and recalculate or inspect summary views after material changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/financial-categorizer)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide local CLI workflows that may read from or modify a user-selected SQLite database.]

## Skill Version(s):

1.13.0 (source: server release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
