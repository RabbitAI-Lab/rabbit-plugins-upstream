## Description: <br>
Provides Notion API guidance for creating, moving, updating, locking, and managing pages, data sources, templates, and blocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dongkukim](https://clawhub.ai/user/dongkukim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and workspace operators use this skill to draft Notion API requests for page, data source, block, template, and locking workflows in their own Notion workspaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored Notion API tokens can expose workspace access if mishandled. <br>
Mitigation: Protect ~/.config/notion/api_key and share the Notion integration only with pages or databases it needs. <br>
Risk: Move, lock, update, and erase-content examples can change or remove live Notion page content. <br>
Mitigation: Require explicit confirmation and verify target page, data source, and template IDs before running destructive or state-changing requests. <br>


## Reference(s): <br>
- [Notion API Documentation](https://developers.notion.com) <br>
- [Notion Integrations](https://notion.so/my-integrations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration guidance] <br>
**Output Format:** [Markdown guidance with cURL commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces request examples and operational guidance; it does not execute Notion API calls on its own.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
