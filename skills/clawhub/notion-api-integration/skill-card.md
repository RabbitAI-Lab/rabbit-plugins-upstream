## Description: <br>
Builds and debugs Notion API integrations across data sources, pages, blocks, properties, filters, files, webhooks, and bulk imports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to build, debug, migrate, and sync Notion API workflows, including access setup, schema-aware queries, page and block updates, file handling, pagination, retries, and bulk data movement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Notion integration token for pages shared with that integration and keeps durable local workspace metadata such as schemas, database names, IDs, mappings, run history, projects, and contacts. <br>
Mitigation: Use least-privilege Notion capabilities, review stored files under ~/Clawic/data/, and keep write_mode at confirm-writes unless direct writes are intentional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/notion-api-integration) <br>
- [Clawic Skill Homepage](https://clawic.com/skills/notion-api-integration) <br>
- [Notion API Endpoint Surface](https://api.notion.com/v1/*) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline JSON, curl, and SDK examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local Notion integration notes under ~/Clawic/data/ and may propose or execute Notion API requests using the user's configured write_mode.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
