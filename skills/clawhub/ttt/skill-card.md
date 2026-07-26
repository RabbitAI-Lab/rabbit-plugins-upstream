## Description: <br>
Manage TinyTalkingTodos lists and items via the ttt CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joshuacrowley](https://clawhub.ai/user/joshuacrowley) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to manage TinyTalkingTodos lists and todo items from the command line, including authentication, list management, todo updates, batch operations, undo history, and daemon operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external @ojschwa/ttt-cli package and authenticated access to a TinyTalkingTodos account. <br>
Mitigation: Install only when the publisher and CLI package are trusted, and authenticate intentionally before allowing the agent to manage account data. <br>
Risk: Exported authentication credentials can expose account access if pasted into chat, logs, or shared files. <br>
Mitigation: Avoid ttt auth export unless needed for a script, and do not paste or log exported credentials. <br>
Risk: Delete, force delete, batch add, and batch update commands can change or remove multiple lists or todo items. <br>
Mitigation: Review targets and command intent before running mutating operations, and use ttt undo or history when a mistake needs to be reverted. <br>
Risk: The daemon keeps a background WebSocket connection for faster commands. <br>
Mitigation: Stop the daemon when a persistent background connection is not wanted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/joshuacrowley/skills/ttt) <br>
- [TinyTalkingTodos](https://tinytalkingtodos.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with CLI commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the ttt CLI, an authenticated TinyTalkingTodos account, and may use compact text or JSON CLI output.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
