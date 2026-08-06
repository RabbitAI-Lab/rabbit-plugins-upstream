## Description:

Bookshelf Plus helps an agent manage a personal library with multi-source ISBN lookup, barcode scanning, lending and return tracking, overdue reminders, Notion synchronization, reading progress tracking, reports, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to maintain a Notion-backed personal or small library catalog, look up books by ISBN, track lending status and reading progress, schedule reminders, and generate exports or library health reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notion mutations may affect records outside the intended scope if used with broad credentials or insufficient confirmation.

Mitigation: Use a dedicated Notion integration limited to one library database and add confirmation or database-scoped lookup before archive, borrow, return, or update operations.

Risk: Scheduled reminder examples can run with live credentials and send automated reminders when enabled.

Mitigation: Enable cron examples only when scheduled reminders are intended, and avoid embedding live keys directly in scheduled commands.

Risk: Borrower names and reading activity can be personal data.

Mitigation: Store only necessary borrower and reading-progress information and limit access to the backing Notion database.

Risk: Report export mode is flagged for a hard-coded dynamic import issue.

Mitigation: Avoid report export mode until the import path is fixed and reviewed.

## Reference(s):

- [Server-resolved source repository](https://github.com/xuan905/bookshelf-plus)
- [ClawHub skill page](https://clawhub.ai/xuan905/skills/bookshelf-plus)
- [Publisher profile](https://clawhub.ai/user/xuan905)
- [Notion integrations](https://www.notion.so/my-integrations)
- [Open Library Books API](https://openlibrary.org/api/books)
- [Google Books API](https://www.googleapis.com/books/v1/volumes)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, HTML, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands, JSON responses, CSV or Markdown exports, and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external APIs and write local report or export files when the user runs the provided scripts.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
