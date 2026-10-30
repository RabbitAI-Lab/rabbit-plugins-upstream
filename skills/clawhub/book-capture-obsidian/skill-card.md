## Description:

Catalogues photos, barcodes, ISBNs, titles and Goodreads exports as Obsidian book notes with covers, summaries and a library dashboard. Supports Google Books only, Open Library only, or both in either order. Use when the user wants to log or import books into Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Obsidian users can capture books from photos, ISBNs, titles, or Goodreads CSV exports, then maintain book notes and a library dashboard in their selected vault.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk imports and reruns can create, update, rename, or refile notes in the selected vault.

Mitigation: Back up the intended vault, inspect the dry-run results, and confirm the vault path before a live import.

Risk: ISBN, title, and author queries are sent to the selected metadata providers.

Mitigation: Choose the provider order deliberately; use --no-enrich for Goodreads imports that should remain local.

Risk: Generated content above ## User Notes is replaced when a note is updated.

Mitigation: Keep personal writing below the ## User Notes heading.

## Reference(s):

- [Configuration](references/configuration.md)
- [Data Contracts](references/data-contracts.md)
- [Goodreads CSV Migration Runbook](references/migration-runbook.md)
- [Troubleshooting](references/troubleshooting.md)
- [Google Books API](https://developers.google.com/books/docs/v1/using#auth)
- [Open Library API](https://openlibrary.org/developers/api)
- [Google Cloud Quotas](https://docs.cloud.google.com/docs/quotas/view-manage)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files]

**Output Format:** [Obsidian Markdown book notes and library dashboard, with JSON results and warnings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated note content above ## User Notes is replaced on reruns; personal content below it is preserved.]

## Skill Version(s):

1.4.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
