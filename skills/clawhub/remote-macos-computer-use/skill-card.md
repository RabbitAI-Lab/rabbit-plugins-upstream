## Description:

Set up cua-driver MCP, macOS permissions, SSH reverse tunneling, persistent LaunchAgents, health checks, and bounded-mode safety so a remote agent can operate a Mac desktop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dont-see-big-shark](https://clawhub.ai/user/dont-see-big-shark)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to onboard a trusted Mac as a remotely reachable desktop target for MCP-capable agents such as Hermes, Claude Code, Codex, Cursor, and OpenCode. It is intended for setup guidance, health checks, troubleshooting, and generation of per-agent MCP configuration for a reverse-SSH bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables persistent remote desktop and SSH access to an unlocked Mac.

Mitigation: Install only on trusted Macs and servers, prefer a dedicated low-privilege macOS account, and maintain a clear process to unload LaunchAgents and disable sshd.

Risk: The security evidence reports weak default guardrails for persistent SSH and desktop access.

Mitigation: Use key-only SSH with tight authorized_keys restrictions, keep the reverse listener bound to localhost, and avoid personal or sensitive Macs unless remote agent visibility and control are acceptable.

Risk: Remote GUI control can perform destructive actions in real applications.

Mitigation: Use cua-driver bounded mode with a reviewed capability manifest and require approval for destructive operations.

## Reference(s):

- [Server-resolved source repository](https://github.com/dont-see-big-shark/remote-macos-computer-use)
- [ClawHub skill page](https://clawhub.ai/dont-see-big-shark/skills/remote-macos-computer-use)
- [cua-driver](https://cua.ai)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, YAML-style MCP configuration, and setup/troubleshooting instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-specific setup commands and configuration fragments based on supplied Mac, server, SSH, and MCP server settings.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
