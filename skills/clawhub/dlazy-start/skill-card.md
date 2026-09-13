## Description:

Quickstart for AI orchestrators driving @dlazy/cli, covering installation, authentication, capability discovery, cloud and local tool invocation, asynchronous task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to install and authenticate @dlazy/cli, discover registered tools, invoke cloud or local commands, poll asynchronous jobs, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned global installer commands can install a changed package version or affect the user's wider environment.

Mitigation: Prefer a pinned or local @dlazy/cli install, review the package before use, and avoid elevated privileges for installer commands.

Risk: Browser cookie access can expose sensitive session data.

Mitigation: Allow browser cookie access only with explicit user approval, preferably from a dedicated browser profile containing only the target-site session.

Risk: The skill invokes cloud and local tools that may consume credits, contact external endpoints, or modify local files.

Mitigation: Discover tool schemas and cost shapes first, use dry-run validation where available, and confirm provider, model, cost, and output path before paid or file-writing operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command examples and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands that require npm/npx, API credentials, network access, and optional local runtimes.]

## Skill Version(s):

2.0.16 (source: server release metadata; artifact frontmatter is 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
