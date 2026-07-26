## Description: <br>
Manage a personal travel Markdown database for food finds, places, guides, screenshots, preferences, Notion synchronization, and trip planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jichengkai](https://clawhub.ai/user/jichengkai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and agents use this skill to save, validate, search, and organize personal travel knowledge in a local Markdown database. It also supports dry-run-first Notion synchronization and travel recommendations grounded in the user's stored records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel records can contain sensitive itinerary details, preferences, reservation notes, screenshots, or personal location history. <br>
Mitigation: Keep the local database private, avoid storing sensitive reservation details unless needed, and review records before sharing or syncing them. <br>
Risk: Optional enrichment and Notion sync can send place queries or selected records to external search, map, or Notion services. <br>
Mitigation: Use dry-run sync plans first, keep API tokens in local environment files rather than chat, and apply only the records the user intends to send. <br>


## Reference(s): <br>
- [Travel Database Schema](references/database-schema.md) <br>
- [Ingestion Workflow](references/ingestion-workflow.md) <br>
- [Recommendation Workflow](references/recommendation-workflow.md) <br>
- [Notion Integration Guide](references/notion-integration.md) <br>
- [Notion Sync Schema](references/notion-sync-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown records, concise guidance, and command-line instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses dry-run previews for sync and migration workflows before applying local or Notion changes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
