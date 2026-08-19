## Description: <br>
Notion CLI for creating and managing pages, databases, and blocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[willykinfoussia](https://clawhub.ai/user/willykinfoussia) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to guide agents in searching, reading, creating, updating, and querying Notion pages, databases, and blocks through notion-cli and direct Notion API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Notion integration token can expose or modify workspace content available to that integration. <br>
Mitigation: Use a dedicated least-privilege Notion integration, share only required pages or databases, and store the token with restrictive permissions or a secret manager. <br>
Risk: Create and update operations can change live Notion workspace data. <br>
Mitigation: Review any generated command or API payload before execution, especially requests that create pages or update database properties. <br>


## Reference(s): <br>
- [Notion Manager on ClawHub](https://clawhub.ai/willykinfoussia/skills/notion-cli) <br>
- [notion-cli GitHub repository](https://github.com/litencatt/notion-cli) <br>
- [Notion API documentation](https://developers.notion.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with inline shell commands, curl examples, and JSON property examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided NOTION_TOKEN for authenticated Notion operations.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
