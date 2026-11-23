## Description:

A quickstart for AI orchestrators using @dlazy/cli to install and authenticate, discover tools, invoke cloud and local capabilities, poll asynchronous jobs, and recover from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

AGPL-3.0-or-later

## Use Case:

Developers and AI orchestrators such as Claude Code, Cursor, Codex, and Copilot use this guide to set up @dlazy/cli, discover available tools, invoke cloud or local capabilities, track asynchronous jobs, and troubleshoot common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The guide includes an example that can access browser cookies without a sensitive-data warning.

Mitigation: Review the session-data implications and enable browser-cookie access only when it is needed.

Risk: The CLI install command does not pin a package version, and the security scan left two local references unresolved.

Mitigation: Review the package and version before installing, and resolve the remaining references before relying on the guidance.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [Project URL listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quickstart guidance for command-line setup, tool discovery, invocation, and troubleshooting.]

## Skill Version(s):

2.0.44 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
