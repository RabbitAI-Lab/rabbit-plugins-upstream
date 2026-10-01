## Description:

A quickstart for AI agents using the dLazy CLI to install and authenticate, discover tools, invoke local and cloud capabilities, monitor long-running tasks, and troubleshoot failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to set up dLazy CLI, discover available tools and their costs, run local or cloud tasks, and handle asynchronous results and common errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-cookie reuse for video downloads can expose sensitive logged-in sessions.

Mitigation: Do not enable cookies_from_browser without explicit user consent; prefer device login or narrowly scoped credentials.

Risk: Stored authentication credentials may be exposed if the local configuration is mishandled.

Mitigation: Protect ~/.dlazy/config.json and avoid sharing API keys.

Risk: Cloud generation may incur charges or vary with installed CLI versions.

Mitigation: Confirm tool costs before generation and pin the npm package version for repeatable installs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes tool-discovery, invocation, status-polling, and troubleshooting guidance.]

## Skill Version(s):

2.0.24 (source: server-resolved release; included skill frontmatter states 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
