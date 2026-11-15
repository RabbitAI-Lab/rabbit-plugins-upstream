## Description:

Catalogues photos, barcodes, ISBNs, titles and Goodreads exports as Obsidian book notes with covers, summaries and a library dashboard. Supports Google Books only, Open Library only, or both in either order. Use when the user wants to log or import books into Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to capture books from photos, ISBNs, titles, or Goodreads CSV exports into an Obsidian vault, with metadata lookup and a library dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's tool scope is not fully declared.

Mitigation: Review its requested actions before use and keep execution within the intended book capture or import task.

Risk: Setup may write to the shared pip cache.

Mitigation: Review setup behavior before installing dependencies and use a skill-local Python environment.

## Reference(s):

- [Project homepage](https://github.com/Ricardodpalmeida/book-capture-obsidian-skill)
- [Configuration and metadata providers](references/configuration.md)
- [Book fields and data contracts](references/data-contracts.md)
- [Goodreads migration runbook](references/migration-runbook.md)
- [Troubleshooting](references/troubleshooting.md)
- [Google Books API requirements](https://developers.google.com/books/docs/v1/using#auth)
- [Google Cloud quota guidance](https://docs.cloud.google.com/docs/quotas/view-manage)
- [Open Library API guidance](https://openlibrary.org/developers/api)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Obsidian Markdown book notes and a library dashboard, JSON workflow results, and shell-command usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Book notes are written to the configured Obsidian vault; dashboard tables require the Dataview plugin.]

## Skill Version(s):

1.4.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
