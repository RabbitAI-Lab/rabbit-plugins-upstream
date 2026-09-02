## Description:

Double-entry, full-cycle accounting suite built for AI agents that converts bank CSVs, OFX, and QBO files into balanced, auditable local SQLite books with balance sheet, income statement, general ledger, and trial balance outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[737999](https://clawhub.ai/user/737999)

### License/Terms of Use:

AGPL-3.0

## Use Case:

External users and their agents use this skill to create and maintain local bookkeeping records, import bank activity, clear suspense items, and produce auditable financial statements and ledgers. The skill is intended for accounting workflows where the operator reviews categorization, destructive changes, extracted journal entries, and final reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles confidential accounting records and can make high-authority local changes to books.

Mitigation: Set GRIDTRX_WORKSPACE narrowly, keep exports inside the client workspace, and require operator review before destructive changes or final reporting.

Risk: The PDF/image/Excel AJE extraction path can send financial documents to Anthropic despite local-only claims elsewhere.

Mitigation: Use that extraction path only with explicit user approval, and review AI-extracted journal entries before posting them.

Risk: Browser workpaper file-open actions and some export paths may reach beyond the intended workspace boundary.

Mitigation: Run the browser UI only on a trusted local machine and treat workpaper open actions as privileged local file operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/737999/skills/gridtrx)
- [Publisher profile](https://clawhub.ai/user/737999)
- [Project homepage](https://github.com/737999/GridTRX)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [Demo video](https://youtu.be/9mmHbgEB3PQ)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May operate on local SQLite books and produce CSV or PDF accounting reports through the bundled application interfaces.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
