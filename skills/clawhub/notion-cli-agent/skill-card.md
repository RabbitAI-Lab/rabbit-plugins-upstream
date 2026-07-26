## Description: <br>
Provides command-line access for agents to search, create, update, and manage Notion pages, databases, blocks, users, and comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[froemic](https://clawhub.ai/user/froemic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to give an agent structured command-line guidance for working with a Notion workspace through notion-cli and the Notion API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can read and change Notion pages, databases, blocks, users, and comments that are shared with the configured integration. <br>
Mitigation: Use a dedicated Notion integration, share only required pages or databases, and require explicit confirmation before update, archive, delete, append, or comment commands. <br>
Risk: The Notion API key grants access to the content available to the integration. <br>
Mitigation: Protect the API key, rotate it if exposed, and avoid verbose debug logging when sensitive workspace content may appear in requests or responses. <br>
Risk: The release depends on an external repository and npm dependencies. <br>
Mitigation: Review the external repository and dependency set before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/froemic/skills/notion-cli-agent) <br>
- [Notion integrations](https://www.notion.so/profile/integrations) <br>
- [Notion API endpoint](https://api.notion.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include commands that read or modify Notion content shared with the configured integration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
