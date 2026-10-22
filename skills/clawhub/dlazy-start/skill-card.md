## Description:

A quickstart for AI orchestrators using @dlazy/cli to authenticate, discover available tools, invoke cloud and local tools, monitor asynchronous jobs, and troubleshoot common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Claude Code, Cursor, Codex, or Copilot use this guide to set up @dlazy/cli, inspect available capabilities, run cloud or local tools, and monitor asynchronous tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting guidance may lead an agent to access browser login cookies without clearly bounded user permission.

Mitigation: Ask the user before accessing cookies; prefer downloads without login, and if authentication is necessary use a dedicated browser profile and keep session data out of logs and cloud inputs.

Risk: Using cloud media tools may involve uploads and announced costs.

Mitigation: Pin a reviewed CLI version and review media uploads and announced costs before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration examples]

**Output Format:** [Markdown with inline shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
