## Description:

Ingest pasted PC parts receipts or specs into Notion DIY_PC tables with classification, enrichment, follow-up, and upsert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn pasted PC parts receipts or hardware notes into planned and applied Notion updates for DIY_PC storage, enclosure, PCConfig, and PCInput tables. It supports local extraction, optional web enrichment, duplicate-safe upsert planning, and explicit apply operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, archive, and mirror records in Notion.

Mitigation: Use the default plan mode first, inspect the proposed targets and before/after changes, then run apply only for already authorized changes.

Risk: Credentialed Notion requests are delegated to the notion-api-automation dependency and can be redirected with NOTIONCTL_PATH.

Mitigation: Install the dependency only from a trusted source and set NOTIONCTL_PATH only to a reviewed local helper.

Risk: A broad Notion integration or noisy runtime environment could expose unrelated workspace data or secrets.

Mitigation: Limit the Notion integration to the intended DIY_PC data sources and keep unrelated secrets out of the runtime environment.

Risk: The deprecated Python script remains in the artifact.

Mitigation: Use scripts/notion_apply_records.js for plan and apply operations and do not invoke the deprecated Python script.

Risk: Optional web enrichment may send partial product text to external search or fetch providers.

Mitigation: Skip web_search and web_fetch when the user does not want external enrichment or when pasted records contain sensitive details.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nextaltair/skills/diy-pc-ingest)
- [Notion target IDs](references/notion-ids.md)
- [Example Notion target configuration](references/config.example.json)
- [Notion integrations](https://www.notion.so/my-integrations)
- [Notion API](https://api.notion.com/v1)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON, Code]

**Output Format:** [Markdown guidance with shell commands and JSONL records for a Node-based Notion apply script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plan/apply results for Notion upserts and requires explicit Notion target IDs plus NOTION_API_KEY.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
