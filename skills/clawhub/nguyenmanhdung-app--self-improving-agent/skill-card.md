## Description: <br>
Captures learnings, errors, corrections, and feature requests so coding agents can improve recurring workflows over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nguyenmanhdung-app](https://clawhub.ai/user/nguyenmanhdung-app) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to record command failures, user corrections, knowledge gaps, feature requests, and recurring improvements as structured markdown entries. The logged entries can later be reviewed and promoted into project or workspace memory files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad prompt hooks may run in more sessions or prompts than intended. <br>
Mitigation: Prefer project-level hook configuration, use narrower matchers where possible, and review the hook scripts before enabling them. <br>
Risk: Persistent learning logs and promoted memory files can influence future agent behavior. <br>
Mitigation: Require human approval before writing lessons into AGENTS.md, SOUL.md, TOOLS.md, CLAUDE.md, or other prompt-injected files. <br>
Risk: Logs may accidentally capture sensitive details from errors, command output, or user corrections. <br>
Mitigation: Redact secrets, tokens, private keys, environment variables, and full source or configuration files unless the user explicitly approves that level of detail. <br>


## Reference(s): <br>
- [Self Improving Agent on ClawHub](https://clawhub.ai/nguyenmanhdung-app/skills/self-improving-agent) <br>
- [nguyenmanhdung-app Publisher Profile](https://clawhub.ai/user/nguyenmanhdung-app) <br>
- [Entry Examples](references/examples.md) <br>
- [Hook Setup Guide](references/hooks-setup.md) <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes or updates structured markdown learning logs when the agent follows the workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
