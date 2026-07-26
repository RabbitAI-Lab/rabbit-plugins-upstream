## Description: <br>
Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed write operations against selected Notion resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect an agent to a Notion workspace through Maton OAuth, search and read Notion content, and make explicit user-approved changes to pages, blocks, databases, or data sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Maton-mediated Notion access can expose workspace pages, databases, blocks, users, and search results through the selected connection. <br>
Mitigation: Use the least-privileged Notion connection available and install only when Maton-mediated access to the selected workspace is acceptable. <br>
Risk: Write operations can create, update, archive, or delete Notion resources, including shared workspace content. <br>
Mitigation: Confirm the exact page, database, block, or data source and the intended connection before executing any write operation. <br>
Risk: Bulk updates or changes to shared pages can disrupt team workflows. <br>
Mitigation: Require explicit approval for each batch and use extra caution for shared or destructive changes. <br>


## Reference(s): <br>
- [ClawHub Notion Skill](https://clawhub.ai/byungkyu/skills/notion-api-skill) <br>
- [Maton](https://maton.ai) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [Notion API Introduction](https://developers.notion.com/reference/intro) <br>
- [Notion LLM Reference](https://developers.notion.com/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI, HTTP, Python, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, a valid Notion OAuth connection, and explicit confirmation before write operations.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter metadata.version is 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
