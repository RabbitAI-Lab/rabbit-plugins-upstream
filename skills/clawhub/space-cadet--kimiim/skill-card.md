## Description: <br>
Guides agents through Kimi Group Chat and Session workflows, including reading group rules, members, messages, files, workspace memory, and replying in the correct chat context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents working in Kimi group chats use this skill to follow group and thread startup routines, inspect recent context, manage group-scoped memory, and send concise replies or file attachments in the correct chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to read Kimi group rules, member lists, recent messages, shared files, and workspace-scoped memory before acting. <br>
Mitigation: Use it for intended Kimi group or Session workflows and confirm the active group or thread context before reading or responding. <br>
Risk: The skill can guide agents to send group messages or attach files in chat context. <br>
Mitigation: Review the target chat ID, recipient mentions, message text, and file paths before sending; prefer the documented send-message flow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/kimiim) <br>
- [Publisher Profile](https://clawhub.ai/user/space-cadet) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text, Files] <br>
**Output Format:** [Markdown guidance with inline shell command examples and plain-text message patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outgoing group messages should be short plain text; file sharing is routed through send-message with attachments when possible.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
