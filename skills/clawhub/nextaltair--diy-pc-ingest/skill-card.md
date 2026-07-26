## Description: <br>
Ingests pasted PC parts purchase logs and spec notes, optionally enriches product details, and prepares or upserts records into Notion DIY_PC tables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and personal automation users use this skill to turn messy PC parts receipts or configuration notes into structured Notion records for PCConfig, storage, enclosure, and PCInput tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update or archive live Notion pages, and the documented preview step is not guaranteed to be read-only. <br>
Mitigation: Use a backup or sandbox Notion workspace first, review all generated JSONL before execution, and do not treat preview output as a dry run unless the script adds an explicit dry-run mode. <br>
Risk: A broad Notion integration token could expose or modify more workspace content than intended. <br>
Mitigation: Use a minimally scoped Notion integration connected only to the intended DIY_PC databases and store the token in environment variables or a secret manager. <br>
Risk: Optional web enrichment may send partial product text to external web providers. <br>
Mitigation: Skip web search or fetch enrichment when inputs contain sensitive purchase details or when the user requests local-only extraction. <br>
Risk: Control fields such as page_id, overwrite, archive, archived, relation, and mirror_to_pcconfig can cause direct updates, archiving, or linked-row changes. <br>
Mitigation: Manually review and confirm records containing these fields before running the Notion apply script. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/diy-pc-ingest) <br>
- [Publisher profile](https://clawhub.ai/user/nextaltair) <br>
- [Notion integrations](https://www.notion.so/my-integrations) <br>
- [Example configuration](artifact/references/config.example.json) <br>
- [Notion ID setup notes](artifact/references/notion-ids.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSONL examples, shell commands, and Notion record updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a Notion API key; may call the Notion API and optional web search or fetch tools for enrichment.] <br>

## Skill Version(s): <br>
2.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
