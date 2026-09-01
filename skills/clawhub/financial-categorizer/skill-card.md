## Description:

Process bank transaction CSV exports (Nordea, ICA), auto-categorize transactions using configurable rules, manage transaction links, and generate analytical database views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to import bank CSV exports into a local SQLite finance database, define categorization rules, manage transaction links and recurring payments, and generate budget and cashflow analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a local finance database through user-run CLI commands.

Mitigation: Keep a database backup, use dry-run modes for auto-linking and recurring discovery, and review matches before passing --yes.

Risk: Automated categorization, linking, and recurring-payment discovery can affect finance summaries if matches are wrong.

Mitigation: Preview candidate matches, review rules and linked transactions, and recalculate before relying on generated summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/financial-categorizer)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local files and a user-selected SQLite database; destructive operations require confirmation or an explicit --yes flag as documented.]

## Skill Version(s):

1.12.0 (source: server release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
