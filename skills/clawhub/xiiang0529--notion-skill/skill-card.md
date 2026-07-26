## Description: <br>
Work with Notion pages and databases via the official Notion API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other agent users use this skill to read, create, update, and query Notion pages and databases through a local Notion CLI connected to the official Notion API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Notion integration token can grant access to shared pages and databases. <br>
Mitigation: Treat NOTION_API_KEY as a secret and share the integration only with pages or databases the agent should access. <br>
Risk: Create, update, append, and schema-change commands can alter Notion content or database structure. <br>
Mitigation: Review proposed writes and schema diffs before execution, and require explicit confirmation before applying schema changes. <br>
Risk: Large or repeated Notion operations can hit API rate limits. <br>
Mitigation: Batch carefully and prefer scoped updates over broad rewrites. <br>


## Reference(s): <br>
- [Notion API documentation](https://developers.notion.com) <br>
- [Notion integrations](https://www.notion.so/my-integrations) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documents Notion CLI commands and required environment variables; API calls are performed by a local CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
