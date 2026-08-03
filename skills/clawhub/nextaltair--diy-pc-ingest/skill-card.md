## Description: <br>
Ingest pasted PC parts receipts or specs into Notion DIY_PC tables with classification, enrichment, follow-up, and upsert. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to turn pasted PC parts receipts or specification notes into structured Notion DIY_PC records. It supports classification, field extraction, optional product enrichment, follow-up questions for ambiguous records, and JSONL-driven Notion upserts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented preview path may write to Notion instead of performing a dry run. <br>
Mitigation: Treat generated JSONL as a proposal and verify a read-only mode before execution; do not run the apply script against production data for preview unless the behavior has been fixed or independently confirmed. <br>
Risk: Direct page updates, archive requests, overwrite mode, and storage-to-PCConfig mirroring can modify or remove existing Notion records. <br>
Mitigation: Review JSONL for page_id, id, archive, overwrite, and mirror_to_pcconfig before execution, and use a Notion integration scoped only to the intended DIY_PC databases. <br>
Risk: Optional web enrichment may send partial product text to external web providers. <br>
Mitigation: Skip web_search and web_fetch when external enrichment is not needed or when pasted notes contain sensitive information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/diy-pc-ingest) <br>
- [Publisher profile](https://clawhub.ai/user/nextaltair) <br>
- [Notion API](https://api.notion.com/v1) <br>
- [config.example.json](references/config.example.json) <br>
- [notion-ids.md](references/notion-ids.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSONL records and shell commands for Notion ingestion] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposed Notion records and execution guidance; Notion writes require configured IDs, authentication, and user review.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
