## Description:

圖書館管家 Plus：ISBN 多源掃描 + 借還追蹤與到期提醒 + Notion 同步 + 書庫統計與匯出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to manage a personal or small shared library through an agent, including ISBN lookup, Notion-backed catalog updates, lending and return tracking, overdue reminders, reading progress, exports, and health reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Notion pages through a Notion integration token.

Mitigation: Use a token shared only with the intended library database and review write operations before running import, lending, return, or update workflows.

Risk: Scheduled reminders may expose credentials or notify an unintended audience if cron messages or platform logs include secrets.

Mitigation: Avoid embedding long-lived secrets in cron messages, confirm the reminder schedule and recipients, and prefer environment variables or scoped secret storage.

Risk: Exports and reports can contain personal library, borrower, or reading-progress information.

Mitigation: Review exported CSV, Markdown, JSON, and HTML reports before sharing them outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/bookshelf-plus)
- [Notion integrations](https://www.notion.so/my-integrations)
- [Notion API pages endpoint](https://api.notion.com/v1/pages)
- [Open Library Books API](https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data)
- [Google Books Volumes API](https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn})

## Skill Output:

**Output Type(s):** [text, markdown, JSON, CSV, HTML, shell commands, configuration, guidance]

**Output Format:** [Text, Markdown, JSON, CSV, HTML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update Notion pages and local reading-log or report files when the included scripts are run.]

## Skill Version(s):

1.0.1 (source: server release metadata, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
