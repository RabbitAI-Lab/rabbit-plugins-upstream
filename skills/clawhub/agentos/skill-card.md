## Description: <br>
AgentOS SDK for Clawdbot helps an agent sync conversation context, project memory, mesh messages, and dashboard status with AgentOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentossoftware](https://clawhub.ai/user/agentossoftware) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to connect Clawdbot-style agents to AgentOS for memory persistence, project tracking, semantic search, mesh messaging, and dashboard visibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation, note, project, and memory data may be uploaded and reused through AgentOS sync workflows. <br>
Mitigation: Install only when this ongoing data sync is intended, confirm API key scope and deletion controls, and avoid syncing sensitive data unless the service is approved for that data. <br>
Risk: The artifact describes cron, daemon, and mesh wake workflows that can create background sync or wake behavior. <br>
Mitigation: Do not enable cron jobs, daemon mode, or mesh wakeups unless persistent background activity is acceptable for the deployment. <br>
Risk: The default API endpoint shown in the artifact uses a raw HTTP IP address. <br>
Mitigation: Inspect the generated configuration before use and prefer a trusted HTTPS endpoint where available. <br>
Risk: The setup script expects an aos CLI file that is not present in the provided artifact evidence. <br>
Mitigation: Verify the complete installer contents or obtain the missing CLI before running setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentossoftware/skills/agentos) <br>
- [AgentOS dashboard](https://brain.agentos.software) <br>
- [AgentOS documentation](https://agentos.software/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AgentOS API key and may configure recurring sync or wake behavior when the user enables those workflows.] <br>

## Skill Version(s): <br>
1.4.4 (source: server release evidence and artifact/SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
