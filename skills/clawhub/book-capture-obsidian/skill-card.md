## Description:

Catalogues photos, barcodes, ISBNs, titles and Goodreads exports as Obsidian book notes with covers, summaries and a library dashboard. Supports Google Books only, Open Library only, or both in either order. Use when the user wants to log or import books into Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Obsidian users can use this skill to capture individual books from photos, ISBNs, or titles, migrate Goodreads CSV exports, and maintain a library dashboard in their vault.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk imports can create or update many notes in the vault.

Mitigation: Back up the vault and review the migration dry-run results before importing.

Risk: Selected metadata providers receive ISBN, title, and author queries; Google API keys are sent to Google, and local caching can retain lookup history.

Mitigation: Choose the provider order deliberately, keep API keys private, and disable caching if lookup history should not be retained locally.

Risk: Obsidian may fetch remote book-cover images when displaying notes.

Mitigation: Review cover links in generated notes and account for remote image fetching in the vault's privacy expectations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ricardodpalmeida/skills/book-capture-obsidian)
- [Project homepage](https://github.com/Ricardodpalmeida/book-capture-obsidian-skill)
- [Configuration](references/configuration.md)
- [Data contracts](references/data-contracts.md)
- [Goodreads migration runbook](references/migration-runbook.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [Obsidian Markdown book notes and dashboards, JSON operation reports, and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes generated or updated notes and dashboards within the selected Obsidian vault; operation reports include counts, errors, and warnings.]

## Skill Version(s):

1.4.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
