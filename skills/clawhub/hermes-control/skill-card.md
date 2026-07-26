## Description: <br>
Hermes Control is a reference skill for using OpenClaw to operate Hermes Agent commands, configuration, toolsets, gateway operations, multi-agent workflows, scheduled tasks, and skill management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[internettrollwatt](https://clawhub.ai/user/internettrollwatt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they need concise command and workflow guidance for automating Hermes Agent through OpenClaw. It supports setup, configuration, tool and skill management, gateways, MCP, webhooks, cron jobs, and multi-agent coordination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad automation control can run Hermes actions through CLI, tools, gateways, scheduled jobs, and background agents. <br>
Mitigation: Install only when that level of control is intended, keep approvals enabled for normal use, and limit unattended operation to isolated or reviewed environments. <br>
Risk: Disabling approvals or using yolo-style modes can allow actions to proceed without interactive confirmation. <br>
Mitigation: Keep approval prompts enabled unless operating in an isolated test environment with clear rollback and monitoring. <br>
Risk: Debug uploads, logs, sessions, and gateway messages may expose sensitive information. <br>
Mitigation: Keep secret and PII redaction enabled where possible and review debug reports, logs, and exported sessions before sharing. <br>
Risk: Webhooks, gateway services, cron jobs, and background agents can continue acting after the original session. <br>
Mitigation: Prefer localhost or authenticated exposure for webhooks, periodically audit active services and scheduled jobs, and stop or remove persistent agents that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/internettrollwatt/skills/hermes-control) <br>
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/) <br>
- [Hermes Agent Source](https://github.com/NousResearch/hermes-agent) <br>
- [Hermes Slash Commands](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) <br>
- [Hermes Tools Reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference) <br>
- [Hermes Configuration Guide](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) <br>
- [Hermes Messaging Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) <br>
- [Hermes MCP Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) <br>
- [Hermes Cron Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Code snippets] <br>
**Output Format:** [Markdown with inline shell, Python, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is command-oriented and may include operational cautions for approvals, secrets, webhooks, background agents, and gateway services.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
