## Description: <br>
Integrate with Notion API v1 to search, read, create, update, comment on, and archive pages and databases within a Notion workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to automate Notion workspace tasks such as finding content, reading pages, creating pages or databases, updating database entries, adding comments, and archiving pages through the official Notion API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify, comment on, create, and archive Notion workspace content. <br>
Mitigation: Require manual confirmation before updates, comments, database creation, or archive/delete actions. <br>
Risk: A broad Notion integration token may expose more workspace content than the user intended. <br>
Mitigation: Use a Notion integration with access only to the pages or databases that should be automated. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/gaolfun/skills/notion-integration) <br>
- [Notion Integrations](https://www.notion.so/profile/integrations) <br>
- [Notion API v1](https://api.notion.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON request examples, shell configuration snippets, and concise success or error summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Notion API operation names, page or database IDs, URLs, timestamps, error codes, and suggested remediation steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
