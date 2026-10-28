## Description:

Quickstart for AI orchestrators using @dlazy/cli to authenticate, discover tools, invoke cloud and local tools, poll asynchronous tasks, and recover from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI orchestrators use this guide to install and authenticate @dlazy/cli, inspect available tool schemas and costs, run local or cloud media tools, and track asynchronous jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A troubleshooting example suggests accessing browser cookies to handle a video platform login challenge, which can expose an authenticated session.

Mitigation: Require explicit user approval, use a dedicated browser profile containing only the needed account, and keep cookies out of logs and unrelated services.

Risk: Cloud media calls can send input files to providers and may incur usage costs.

Mitigation: Before invoking a cloud tool, confirm the provider, model, input data, and expected cost; pin a reviewed CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy CLI homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (not verified as release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON examples]

**Output Format:** [Markdown with shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
