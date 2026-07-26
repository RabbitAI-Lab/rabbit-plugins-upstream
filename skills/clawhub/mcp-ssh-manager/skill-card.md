## Description: <br>
This skill helps agents manage remote SSH servers through MCP ssh-manager workflows for command execution, sessions, file transfer, monitoring, tunneling, backups, and organized workdir persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imaxtomas](https://clawhub.ai/user/imaxtomas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations engineers use this skill to guide agents through remote server administration tasks, including SSH command execution, reusable sessions, deployments, health checks, troubleshooting, file movement, tunnels, and backups. It is intended for trusted hosts where command plans and resulting server data can be reviewed and controlled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad remote administration over SSH, including privileged or destructive operations. <br>
Mitigation: Install it only for trusted hosts, use least-privilege SSH accounts, review commands before execution, and require explicit approval for sudo, sync, restore, tunnel, service restart, session-close-all, and deletion operations. <br>
Risk: Workdir logs and saved command outputs may contain sensitive server data. <br>
Mitigation: Protect ~/.ssh-workdir storage, redact sensitive values before sharing, and clean up retained outputs when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/imaxtomas/skills/mcp-ssh-manager) <br>
- [Session Management Deep Dive](references/sessions.md) <br>
- [Workdir Structure and Usage](references/workspace.md) <br>
- [Historical Data Comparison](references/comparison.md) <br>
- [System Health Check Workflow](examples/system-check.md) <br>
- [Multi-step Deployment Workflow](examples/deployment.md) <br>
- [Troubleshooting Workflow](examples/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command plans, session workflows, workdir paths, status summaries, and file transfer or tunnel instructions.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata; SKILL.md frontmatter lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
