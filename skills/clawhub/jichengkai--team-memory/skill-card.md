## Description:

Captures and organizes team conversations, people and company details, events, feedback, judgments, tasks, and summaries, with traceable queries and Notion-based multi-device synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jichengkai](https://clawhub.ai/user/jichengkai)

### License/Terms of Use:

MIT-0

## Use Case:

Managers use this skill to keep an evidence-linked history of relevant team communication and records, then prepare queries, 1:1s, status reports, and review materials. It supports using the same library across devices through Notion synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Team conversations and personnel records are saved and synchronized to Notion.

Mitigation: Use the intended private library, restrict its integration permissions, and keep the Notion token in the environment.

Risk: Deleting a record does not remove its original text or revision history from backups and cloud packages.

Mitigation: Consider retention needs before saving sensitive information, and manage backup and cloud-package access accordingly.

Risk: Background synchronization can keep retrying while work is pending, and the actual Notion permissions were not verified.

Mitigation: Verify the integration’s access to the intended private library and review sync status until pending work is resolved.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jichengkai/skills/team-memory)
- [New device join guide](artifact/references/new-device-join.md)
- [Record format](artifact/references/record-format.md)
- [Management workflows](artifact/references/management-workflows.md)
- [Migration and upgrade guide](artifact/references/migration-and-upgrade.md)
- [Sync protocol](artifact/references/sync-protocol.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)
- [Notion API request limits](https://developers.notion.com/reference/request-limits)
- [Notion Markdown page updates](https://developers.notion.com/reference/update-page-markdown)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, SVG, Shell commands, Configuration guidance]

**Output Format:** [JSON records and status responses; Markdown, JSON, or SVG reports; shell commands and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include record identifiers and source references; SVG summaries show up to 24 recent records.]

## Skill Version(s):

3.0.1 (source: server-resolved release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
