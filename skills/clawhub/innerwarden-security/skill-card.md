## Description:

Install, verify and run InnerWarden on the machine this OpenClaw agent runs on. InnerWarden Community (free, 1.6.11 or newer) screens this agent's own exec, process, write, edit and apply_patch calls before they run, through its innerwarden-guard plugin on OpenClaw's before_tool_call hook (OpenClaw 2026.9.7 or newer), and the calls it makes to its MCP servers through the proxy. Monitor first; enforce is the owner's choice. InnerWarden Pro (paid, Linux) adds the host layer with the kernel Execution Gate. Use when your owner asks to install InnerWarden, check what it protects here, see what it refused, ask whether a command is safe to run, turn on enforce, upgrade it, or remove it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maiconburn](https://clawhub.ai/user/maiconburn)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw owners and developers use this skill to install and verify InnerWarden, inspect what it screens, review command verdicts, and manage monitor or enforce mode. It also guides upgrades and removal while keeping security-sensitive changes under the owner's control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's downloaded installer changes the local machine.

Mitigation: Review the installer before execution and start in monitor mode.

Risk: Optional conversation observation accesses conversation content.

Mitigation: Explain the allowConversationAccess permission and get the owner's agreement before enabling observation.

Risk: Removing InnerWarden in the wrong order can leave its plugin installed and block tool calls.

Mitigation: Disconnect the integration before uninstalling the binary, then restart OpenClaw as instructed.

## Reference(s):

- [InnerWarden skill documentation](https://github.com/InnerWarden/innerwarden-skill)
- [InnerWarden Pro server setup](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/pro-on-a-server.md)
- [Managing InnerWarden Pro](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/managing-pro.md)
- [InnerWarden Pro pricing](https://innerwarden.com/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and setup guidance depend on the installed InnerWarden and OpenClaw versions.]

## Skill Version(s):

1.0.7 (source: ClawHub server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
