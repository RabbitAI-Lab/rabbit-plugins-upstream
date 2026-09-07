## Description:

Quickstart for AI orchestrators driving @dlazy/cli through install, authentication, capability discovery, cloud and local tool invocation, async polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI orchestrator users use this skill to operate @dlazy/cli for discovering available media and text tools, invoking cloud or local commands, polling asynchronous jobs, and recovering from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run mutable external CLI tooling.

Mitigation: Install @dlazy/cli only from trusted package sources, review the publisher before use, and run it in an environment appropriate for external tooling.

Risk: The CLI may handle API keys, local configuration, generated media, downloads, and remote service calls.

Mitigation: Use least-privileged API keys, avoid exposing ~/.dlazy/config.json, and review commands before they access local files or make paid calls.

Risk: The downloader recovery path may use browser session cookies.

Mitigation: Use cookie-based download inputs only with explicit approval, preferably from a dedicated browser profile or narrowly scoped cookie source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source link from metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command examples and JSON input conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and may involve @dlazy/cli authentication, API keys, local runtime installers, downloads, and paid remote tool calls.]

## Skill Version(s):

2.0.14 (source: server release metadata; artifact frontmatter lists 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
