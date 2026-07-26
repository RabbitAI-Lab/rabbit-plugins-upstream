## Description: <br>
Install and configure the ClawGuard security plugin, an LLM-as-a-Judge guardrail that detects and blocks risky tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lidan-capsule](https://clawhub.ai/user/lidan-capsule) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to install ClawGuard in OpenClaw, configure tool-call security checks, choose blocking or log-only behavior, and troubleshoot gateway setup issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tool-call logging can expose sensitive tool inputs or context in gateway logs. <br>
Mitigation: Disable full tool-call logging in sensitive environments and restrict log access before production use. <br>
Risk: Security evaluation sends tool context to the configured LLM provider. <br>
Mitigation: Confirm which provider receives evaluation context and avoid sending secrets or regulated data through tool calls. <br>
Risk: Anonymous metrics collection is enabled by default. <br>
Mitigation: Disable metrics collection when telemetry is not acceptable for the deployment. <br>
Risk: Troubleshooting output may reveal gateway tokens. <br>
Mitigation: Redact tokens and configuration secrets before sharing logs, command output, or support details. <br>


## Reference(s): <br>
- [ClawGuard GitHub repository](https://github.com/capsulesecurity/clawguard) <br>
- [ClawGuard npm package](https://www.npmjs.com/package/@capsulesecurity/clawguard) <br>
- [ClawGuard on ClawHub](https://clawhub.ai/lidan-capsule/skills/clawguard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes OpenClaw and Docker installation commands, configuration options, verification steps, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
