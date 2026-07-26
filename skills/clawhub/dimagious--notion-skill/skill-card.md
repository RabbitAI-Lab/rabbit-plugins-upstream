## Description: <br>
Work with Notion pages and databases via the official Notion API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dimagious](https://clawhub.ai/user/dimagious) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to guide agents that read, create, and update Notion pages and databases through a local Notion CLI backed by the official Notion API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Notion integration token can expose any pages or databases shared with that integration. <br>
Mitigation: Use a dedicated integration token and share it only with the specific Notion pages or databases needed for the task. <br>
Risk: The NOTION_API_KEY secret could be exposed through logs, commits, or copied configuration. <br>
Mitigation: Keep NOTION_API_KEY in the environment or a secure secret store and do not include it in prompts, logs, or repository files. <br>
Risk: Write operations or database schema changes can alter Notion content unexpectedly. <br>
Mitigation: Review proposed updates and schema diffs before allowing the agent to run write or schema-change commands. <br>


## Reference(s): <br>
- [Notion API Documentation](https://developers.notion.com) <br>
- [Notion Integrations](https://www.notion.so/my-integrations) <br>
- [ClawHub Skill Page](https://clawhub.ai/dimagious/skills/notion-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NOTION_API_KEY and a local notion-cli or notion-cli-py installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
