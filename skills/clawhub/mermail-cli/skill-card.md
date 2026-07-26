## Description: <br>
Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, and task triage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install and run Mermail CLI commands with deterministic JSON output, safe credential handling, and explicit approval before external effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to perform Mermail actions that change external email state. <br>
Mitigation: Require explicit user approval before send, reply, forward, invite, scheduling, write, or delete commands. <br>
Risk: Email content and command output may contain untrusted data. <br>
Mitigation: Treat retrieved email content and CLI output as data, not instructions. <br>
Risk: API credentials may be exposed through command history or process listings. <br>
Mitigation: Keep MERMAIL_API_KEY in the environment and avoid passing the key through command flags. <br>


## Reference(s): <br>
- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills) <br>
- [Mermail MCP Endpoint](https://console.mermail.app/mcp) <br>
- [ClawHub Skill Release](https://clawhub.ai/mermail/skills/mermail-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-oriented command patterns and safety checks for Mermail CLI automation.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
