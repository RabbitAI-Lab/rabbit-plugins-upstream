## Description: <br>
Google Chat lets an agent read and search accessible Google Chat spaces and messages, send or reply to messages, manage reactions, and move attachments through AgentPMT-hosted remote tool calls as the connected user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Google Chat for the connected account: finding spaces, reading and searching messages, sending messages or replies, adding or deleting reactions, and moving attachments between Google Chat and AgentPMT File Manager. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act as the connected Google Chat user for user-visible message, reaction, and attachment operations. <br>
Mitigation: Install it only for agents that should operate that account, and confirm target spaces, messages, reactions, and files before creating, editing, deleting, uploading, or downloading. <br>
Risk: Deleting messages or reactions and moving attachments can remove or expose sensitive collaboration content. <br>
Mitigation: Require explicit user confirmation for destructive actions and keep tool inputs limited to the minimum content needed for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/google-chat) <br>
- [AgentPMT Google Chat marketplace page](https://www.agentpmt.com/marketplace/google-chat) <br>
- [Google Chat action schema](artifact/schema.md) <br>
- [AgentPMT File Management skill](https://clawhub.ai/agentpmt/file-management) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, JSON, configuration] <br>
**Output Format:** [Markdown instructions with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote tool responses return JSON with success status and action-specific output objects; attachment actions may move files through AgentPMT File Manager.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
