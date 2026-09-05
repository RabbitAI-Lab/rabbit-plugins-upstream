## Description:

Quickstart for AI orchestrators driving @dlazy/cli through installation, authentication, capability discovery, cloud and local tool invocation, async task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI orchestrator users use this skill to operate @dlazy/cli from an agent environment, including installing the CLI, authenticating, discovering available tools, invoking cloud or local tools, polling long-running tasks, and recovering from common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can access configured API keys, cloud endpoints, and local media files.

Mitigation: Install only in environments where that access is acceptable, prefer device login or scoped environment/config credentials, and avoid passing API keys directly on the command line.

Risk: Using browser cookies for downloads can expose browser session credentials to the tool.

Mitigation: Avoid cookies_from_browser unless intentionally needed; prefer a dedicated browser profile or scoped exported cookies.

Risk: Some CLI tools may invoke paid cloud generation or long-running external services.

Mitigation: Discover tool schemas and cost shape with dlazy tools list and dlazy tools describe before invocation, and use dry runs where supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command examples for installation, authentication, tool discovery, CLI invocation, async polling, dry runs, and recovery guidance.]

## Skill Version(s):

2.0.13 (source: server release metadata; artifact frontmatter reports 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
