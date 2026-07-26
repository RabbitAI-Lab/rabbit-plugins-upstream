## Description: <br>
Toolbelt helps agents set up and use a shared MCP workspace for ingesting documents, querying structured and unstructured data, recording findings, and sharing state across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[toolbeltai](https://clawhub.ai/user/toolbeltai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need persistent, shared access to uploaded documents, structured data, knowledge graph relationships, saved findings, or collaboration state through Toolbelt's MCP server. It also guides first-time setup for account provisioning and MCP client configuration with explicit user consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create a Toolbelt account and store a bearer token in an MCP client configuration. <br>
Mitigation: Require explicit user approval before provisioning an account or writing MCP configuration, and disclose the target config path and token purpose before storage. <br>
Risk: Uploaded content and recorded findings can persist in a Toolbelt namespace and become available to future connected agents or teammates. <br>
Mitigation: Upload or record only user-approved, task-relevant data, avoid sensitive material by default, and direct users to Toolbelt controls for deletion or revocation. <br>
Risk: A share URL can grant access to a namespace when paired with its token-bound invitation flow. <br>
Mitigation: Confirm the user's sharing intent and recipient before creating a share link, and share it only through channels the user controls. <br>


## Reference(s): <br>
- [Toolbelt skill page](https://clawhub.ai/toolbeltai/skills/toolbelt) <br>
- [Toolbelt website and pricing](https://toolbelt.ai) <br>
- [Toolbelt documentation](https://toolbelt.ai/docs) <br>
- [Agent-readable Toolbelt docs](https://toolbelt.ai/llms-full.txt) <br>
- [Toolbelt web app](https://app.toolbelt.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP examples, shell commands, JSON configuration snippets, and YAML status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to use Toolbelt MCP tools after setup; user consent is required before account provisioning, config writes, uploads, saved findings, or share links.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
