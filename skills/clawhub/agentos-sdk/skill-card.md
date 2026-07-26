## Description: <br>
AgentOS SDK provides APIs and shell tools for persistent agent memory, project and task management, activity logging, mesh communication, and self-evolution workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentossoftware](https://clawhub.ai/user/agentossoftware) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to connect agents to AgentOS for persistent memory, semantic recall, project workflows, activity logging, cross-agent messaging, and session continuity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to persist broad operating context to cloud memory, which can include sensitive or regulated information if users are not careful. <br>
Mitigation: Use least-privilege API keys, define retention and deletion rules, and do not store credentials, private conversations, customer data, regulated data, or detailed relationship profiles. <br>
Risk: The evidence security summary reports default sensitive traffic to insecure raw-IP HTTP and WebSocket endpoints. <br>
Mitigation: Configure only a trusted HTTPS/WSS AgentOS endpoint and avoid the raw-IP HTTP default before using the skill with real agent data. <br>
Risk: Heartbeat and cloud sync behavior can persist data repeatedly without explicit review of each item. <br>
Mitigation: Disable or tightly limit heartbeat and cloud sync unless users approve what will be stored and where it will be sent. <br>


## Reference(s): <br>
- [AgentOS SDK ClawHub Page](https://clawhub.ai/agentossoftware/skills/agentos-sdk) <br>
- [agentossoftware Publisher Profile](https://clawhub.ai/user/agentossoftware) <br>
- [AgentOS Website](https://agentos.software) <br>
- [AgentOS SDK Documentation](artifact/DOCS.md) <br>
- [AgentOS Agent Operations Guide](artifact/AGENT-OPS.md) <br>
- [AgentOS Self-Evolution Framework](artifact/SELF-EVOLUTION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing operational guidance and command examples; API responses shown by the SDK are typically JSON.] <br>

## Skill Version(s): <br>
3.7.0 (source: server release metadata and artifact/skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
