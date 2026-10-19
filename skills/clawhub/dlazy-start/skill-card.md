## Description:

A quickstart for AI agents using the dLazy CLI to discover and invoke cloud and local tools, manage authentication, monitor jobs, and troubleshoot failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this guide to install and authenticate the dLazy CLI, inspect available tools and costs, run cloud or local tasks, and recover from common errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using personal browser cookies for video downloads may expose sensitive account sessions.

Mitigation: Require explicit consent before using cookies_from_browser; prefer a dedicated browser profile and avoid profiles with sensitive sessions.

Risk: Installing the CLI or optional local runtimes may run unreviewed dependencies.

Mitigation: Approve installation steps and pin the CLI version where possible.

Risk: Cloud tool calls may incur charges, and saved assets may land in unsafe locations.

Mitigation: Confirm tool costs before paid calls and choose safe output paths for --save.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy website](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides tool discovery, invocation, asynchronous job polling, and troubleshooting.]

## Skill Version(s):

2.0.32 (source: ClawHub release metadata; bundled guide says 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
