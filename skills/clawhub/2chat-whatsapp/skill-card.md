## Description: <br>
Connects an OpenClaw agent to 2Chat's remote MCP server to send and receive WhatsApp and SMS messages, manage WhatsApp Business channels and templates, work with contacts, groups, catalogs, and statuses, and view voice call records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2chat](https://clawhub.ai/user/2chat) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an OpenClaw agent to an authorized 2Chat account for WhatsApp, SMS, contact, channel, group, status, catalog, and call-record workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can send WhatsApp or SMS messages and publish WhatsApp statuses that reach real people and may incur account charges. <br>
Mitigation: Confirm the recipient, channel, and exact message or status content before execution; check WhatsApp reachability and template cost when appropriate. <br>
Risk: The skill grants sensitive third-party account access, including the ability to read messages, manage contacts and groups, and view call records through 2Chat. <br>
Mitigation: Install it only for authorized 2Chat accounts and connected channels, and review requests that expose personal, contact, conversation, or call-record data. <br>
Risk: Some actions have durable effects, including deleting contacts or connecting and disconnecting WhatsApp channels. <br>
Mitigation: Require explicit confirmation of the contact UUID or channel before deletion or channel-management commands. <br>


## Reference(s): <br>
- [2Chat ClawHub listing](https://clawhub.ai/2chat/skills/2chat-whatsapp) <br>
- [2Chat homepage](https://2chat.co) <br>
- [2Chat MCP setup documentation](https://developers.2chat.co/docs/MCP/setup) <br>
- [2Chat MCP server endpoint](https://mcp.2chat.io/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OpenClaw and OAuth sign-in to an authorized 2Chat account; actions that send messages, publish statuses, delete contacts, or change channels should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
