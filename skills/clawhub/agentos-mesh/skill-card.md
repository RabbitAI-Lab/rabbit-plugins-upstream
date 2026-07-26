## Description: <br>
Enables AI agents to communicate in real time over the AgentOS Mesh network for sending messages, tasks, and status updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentossoftware](https://clawhub.ai/user/agentossoftware) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agent operators use this skill to install and configure a local mesh CLI so agents can send messages, create tasks, poll inboxes, and process pending work through an AgentOS Mesh API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mesh API credentials and status details may be exposed through local configuration, plaintext endpoints, or shared status output. <br>
Mitigation: Use an explicit trusted HTTPS API URL, keep API keys narrowly scoped, protect ~/.agentos-mesh.json with restrictive permissions, and avoid sharing mesh status output. <br>
Risk: Automated polling or heartbeat workflows can process and clear queued messages from mesh participants. <br>
Mitigation: Enable cron or heartbeat polling only for trusted mesh participants and after accepting the queue-clearing behavior. <br>


## Reference(s): <br>
- [AgentOS Mesh ClawHub listing](https://clawhub.ai/agentossoftware/skills/agentos-mesh) <br>
- [AgentOS account portal](https://brain.agentos.software) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with shell command examples and CLI text or JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Installs and documents a local mesh CLI for sending messages, creating tasks, polling inboxes, listing agents, and processing a pending-message queue.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
