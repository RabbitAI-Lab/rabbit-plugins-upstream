## Description: <br>
Works with Notion pages and databases through the official Notion API, including page and database operations, content block editing, and Markdown conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation builders use this skill to create, query, update, and organize Notion pages, databases, and content blocks from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and local file read/write capabilities that are not clearly scoped to Notion automation. <br>
Mitigation: Install and use it only for explicit Notion tasks, keep execution sandboxed where possible, and review any command or file operation before allowing it to run. <br>
Risk: Notion update, delete, import, and bulk actions can modify workspace content. <br>
Mitigation: Confirm target page or database IDs, integration permissions, and action intent before permitting write, delete, import, or bulk operations. <br>
Risk: A Notion API key grants access according to the integration's workspace permissions. <br>
Mitigation: Store the token in an environment variable, avoid logging or committing it, rotate it when needed, and grant the integration only the pages or databases required. <br>


## Reference(s): <br>
- [Notion Integrations](https://www.notion.so/my-integrations) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell commands; Notion API operation results are represented as JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Notion API key and a Notion integration shared with target pages or databases.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
