## Description:

A quickstart for AI orchestrators using @dlazy/cli to authenticate, discover tools, invoke cloud and local tools, track asynchronous tasks, and recover from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users of AI orchestrators can use this guide to set up @dlazy/cli, inspect available tools and costs, invoke cloud or local tools, poll asynchronous jobs, and troubleshoot common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags browser-cookie access through the documented downloader option without an in-skill warning.

Mitigation: Only enable browser-cookie access when needed and explicitly intended; understand the session access involved.

Risk: The security scan flags an unpinned install command that can run changing package versions.

Mitigation: Review the package version before running the install or npx command.

Risk: The security scan was partial because some local references could not be resolved.

Mitigation: Resolve and review the missing references, then complete a full security review before deployment.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-start)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quickstart instructions for CLI setup, discovery, invocation, asynchronous task polling, and troubleshooting.]

## Skill Version(s):

2.0.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
