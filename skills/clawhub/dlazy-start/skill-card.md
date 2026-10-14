## Description:

Guides AI agents through installing and authenticating @dlazy/cli, discovering available tools, invoking cloud and local tools, polling jobs, and recovering from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users of AI coding assistants use this quickstart to guide agents in safely discovering and operating @dlazy/cli tools for media and other cloud or local tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI or optional local runtimes can introduce persistent software into the user's environment.

Mitigation: Install only when the user trusts @dlazy/cli and its npm source; prefer a pinned or project-scoped install.

Risk: Using browser cookies for video downloads can expose an authenticated browsing session to the tool.

Mitigation: Require explicit user approval before allowing browser-cookie access.

Risk: API keys or paid tool calls can expose credentials or incur charges.

Mitigation: Use device-code login or protected environment variables, and disclose provider, model, and expected cost before paid generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes tool discovery, cost checks, asynchronous job polling, and troubleshooting guidance.]

## Skill Version(s):

2.0.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
