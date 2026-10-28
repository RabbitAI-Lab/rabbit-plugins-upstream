## Description:

Turn a cover photo, a barcode, an ISBN or a whole Goodreads export into clean Obsidian book notes with covers and summaries, plus a library dashboard. Quota-safe: Open Library first, cached lookups, Google Books only to fill gaps. Use when the user wants to catalogue, log or import books into Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Obsidian users use this skill to capture individual books or import Goodreads libraries into consistent vault notes and a library dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imports and reruns can rewrite generated sections in vault notes.

Mitigation: Back up the vault, inspect a dry run, start with a small import, and keep personal writing under User Notes.

Risk: Online enrichment sends book identifiers or titles and authors to metadata providers.

Mitigation: Use --no-enrich for a local-only Goodreads import.

## Reference(s):

- [Project homepage](https://github.com/Ricardodpalmeida/book-capture-obsidian-skill)
- [ClawHub skill listing](https://clawhub.ai/ricardodpalmeida/skills/book-capture-obsidian)
- [Configuration](artifact/references/configuration.md)
- [Data contracts](artifact/references/data-contracts.md)
- [Goodreads migration runbook](artifact/references/migration-runbook.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files]

**Output Format:** [Obsidian Markdown book notes and library dashboard; JSON metadata and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates a user-selected vault and preserves personal content under the User Notes section.]

## Skill Version(s):

1.3.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
