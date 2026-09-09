## Description:

Read, search, export, create, update, monitor, query, inspect, batch-edit, and explicitly archive Notion pages and databases when the user requests Notion content or database operations and a host secret manager can supply NOTION_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robansuini](https://clawhub.ai/user/robansuini)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and workspace operators use Notion Sync to let an agent search, read, export, create, update, monitor, query, inspect, batch-edit, and archive Notion content shared with a configured integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Notion integration token can expose workspace content if it is pasted into chat, source control, command arguments, logs, or committed environment files.

Mitigation: Store NOTION_API_KEY in a secret manager and avoid printing, inspecting, logging, or passing the credential through chat or shell arguments.

Risk: The skill can read, create, update, batch-edit, and archive Notion content shared with the configured integration.

Mitigation: Share only the necessary Notion pages or databases with the integration, prefer host-bound egress to api.notion.com, and review filters before mutating operations.

Risk: Batch updates or archives can change multiple Notion pages when the target set is too broad.

Mitigation: Use dry-run and filter options carefully before batch updates; page archiving requires the explicit --confirm-archive flag.

Risk: Local markdown sync can read or write files selected by the user.

Mitigation: Keep workspace path restrictions enabled and authorize external paths only with exact mode-specific --allow-read-path or --allow-write-path values.

## Reference(s):

- [Notion Sync API Reference](references/API-REFERENCE.md)
- [Migrating notion-sync from v1/v2 to v3](references/MIGRATION-V3.md)
- [Changelog](CHANGELOG.md)
- [ClawHub notion-sync skill page](https://clawhub.ai/robansuini/skills/notion-sync)
- [Notion API outbound host](https://api.notion.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-capable script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and NOTION_API_KEY; local file access outside the workspace requires exact read or write path authorization.]

## Skill Version(s):

3.0.2 (source: changelog and server release metadata, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
