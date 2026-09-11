## Description:

Process bank transaction CSV exports (Nordea, ICA), auto-categorize transactions using configurable rules, manage transaction links, and generate analytical database views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to manage local personal finance workflows: importing bank CSV exports, categorizing transactions, linking transfers or reimbursements, and producing SQLite-backed financial summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can change a selected local SQLite finance database, including cleanup, auto-linking, recurring discovery, and delete operations.

Mitigation: Back up the database before imports or destructive operations, use dry-run previews where available, and bypass confirmation prompts only after reviewing the planned changes.

Risk: Untrusted CSV exports or shared regex rules can distort transaction categorization and financial summaries.

Mitigation: Use bank exports from trusted sources, preview match behavior before adding rules, and avoid rules from untrusted people or shared databases until regex validation is hardened.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/financial-categorizer)
- [README](README.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May change a user-selected local SQLite finance database when the suggested CLI commands are run.]

## Skill Version(s):

1.15.0 (source: server release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
