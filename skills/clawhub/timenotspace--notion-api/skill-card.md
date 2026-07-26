## Description: <br>
Generic Notion API CLI for search, querying data sources and databases, creating pages, and reading or editing block content with a configured Notion integration token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timenotspace](https://clawhub.ai/user/timenotspace) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search Notion, query data sources or databases, inspect or edit block content, and create pages from a command line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Notion integration token can read or change workspace content that has been shared with the integration. <br>
Mitigation: Use a dedicated least-privilege integration, share only the pages or databases needed, and keep the token out of the repository. <br>
Risk: Write commands such as create-page, append-blocks, and update-block can modify Notion workspace content. <br>
Mitigation: Review the command and any JSON request body before execution, especially for page creation or block updates. <br>


## Reference(s): <br>
- [Notion API Tools on ClawHub](https://clawhub.ai/timenotspace/skills/notion-api) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions] <br>
**Output Format:** [JSON printed to stdout from Node CLI commands, with Markdown command examples in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Notion integration token via NOTION_KEY or a local key file; command effects depend on the pages and databases shared with that integration.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
