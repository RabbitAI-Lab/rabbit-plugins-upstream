## Description: <br>
Polls Feishu groups and documents, compiles candidate sources, and ingests selected materials into a Research KB through prepare/apply workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-base operators use this skill to turn authorized Feishu group history, attachments, docs, wikis, sheets, and bitables into curated Research KB pages in Gitea. It supports scheduled prepare/apply ingestion while requiring OpenClaw to decide which materials are worth preserving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads authorized Feishu group history, attachments, cloud docs, sheets, and bitables, then writes selected materials to a configured Gitea knowledge-base repository. <br>
Mitigation: Install it only for that workflow, use a dedicated Feishu app, and scope the Gitea bot token to the intended knowledge-base repository. <br>
Risk: Feishu tokens and temporary ingest artifacts are cached under OPENCLAW_SHARED_DIR or the configured shared directory. <br>
Mitigation: Use a dedicated directory with restricted access and retention appropriate for the Feishu content being processed. <br>
Risk: Missing permissions, unsupported Feishu folders, or oversized files can leave materials unprocessed or marked need_authorization, fetch_failed, or unsupported. <br>
Mitigation: Monitor sourceItems statuses after prepare/apply and grant only the specific Feishu permissions needed for the intended chats and documents. <br>
Risk: Low-value or misleading chat fragments could be written into the Research KB if generated pages are not reviewed against source evidence. <br>
Mitigation: Review generated pages and sourceItemKeys before applying them, and preserve message or document provenance for materials that are ingested. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/myd2002/skills/feishu-ingest) <br>
- [Feishu Open APIs](https://open.feishu.cn/open-apis) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Files, Guidance] <br>
**Output Format:** [JSON envelope with Markdown source and page content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prepare emits inputItems and sourceItems; apply emits Research KB page updates, archived source files, catalog/index updates, and sourceItems status records.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
