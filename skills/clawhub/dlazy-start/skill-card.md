## Description:

Guides AI agents through installing, authenticating, discovering, and using dLazy CLI tools, including asynchronous jobs and common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this quickstart to set up dLazy CLI, discover available cloud and local tools, invoke them, and troubleshoot results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-cookie access for video downloads can expose authenticated sessions.

Mitigation: Do not permit automatic browser-cookie access; handle cookie-based workarounds manually for a specific task.

Risk: API keys and saved CLI credentials may be exposed.

Mitigation: Prefer device-code login and protect API keys and ~/.dlazy/config.json.

Risk: Installing the CLI or invoking paid provider tools can introduce package or cost exposure.

Mitigation: Verify or pin the npm package version where practical and review provider costs before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.23 (source: ClawHub release; skill frontmatter lists 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
