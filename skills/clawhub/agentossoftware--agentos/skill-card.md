## Description:

AgentOS SDK for Clawdbot enables context syncing, memory persistence, project tracking, mesh messaging, and dashboard access for Clawdbot agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentossoftware](https://clawhub.ai/user/agentossoftware)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to connect Clawdbot agents to AgentOS for persistent memory, dashboard visibility, project synchronization, mesh messaging, and API-backed operational workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill syncs conversation state, memory files, project notes, and heartbeat status to an external AgentOS service.

Mitigation: Use only when external upload of that data is intended; avoid sensitive work unless the service, tenant controls, API keys, and transport security have been reviewed.

Risk: The skill encourages ongoing sync through heartbeats, cron, and daemon workflows, which can continue sending updates after initial setup.

Mitigation: Before installation, decide whether continuous sync is acceptable and disable heartbeat, cron, or daemon workflows where persistent external sync is not desired.

Risk: Security evidence warns that the CLI implementation needs audit coverage before sensitive use.

Mitigation: Audit the installed CLI and helper scripts before using the skill with sensitive agent memory or production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentossoftware/skills/agentos)
- [AgentOS dashboard](https://brain.agentos.software)
- [AgentOS documentation](https://agentos.software/docs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup, heartbeat sync, context restoration, mesh messaging, daemon, API, and troubleshooting guidance.]

## Skill Version(s):

1.4.4 (source: server release evidence and artifact documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
