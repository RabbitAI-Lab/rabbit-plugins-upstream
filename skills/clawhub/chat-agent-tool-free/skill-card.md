## Description: <br>
Chat Agent Tool Free provides a temporary password-protected real-time chat room for agent-to-agent and human-agent collaboration through a CLI, browser UI, SSE streaming, and optional cloudflared or ngrok tunnels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to start a short-lived room where multiple agents and human collaborators can exchange task status, debug coordination, and hand off work through CLI or browser access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public tunnels can expose an active chat room to unintended participants. <br>
Mitigation: Use strong one-time passwords, share room URLs only with trusted participants, and stop the service immediately after the collaboration ends. <br>
Risk: Mismatched trigger text could cause an agent to invoke the skill for file conversion or content extraction tasks outside its purpose. <br>
Mitigation: Use the skill only for temporary chat-room coordination; route file conversion, document processing, and extraction work to dedicated tools. <br>
Risk: Live room messages may contain sensitive task context while the service is running. <br>
Mitigation: Avoid secrets and sensitive data in rooms, especially when using public tunnels or the free edition's limited authentication and no message persistence controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chat-agent-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and short configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to start a local chat service, connect clients, or expose a temporary tunnel when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
