## Description:

A quickstart for AI orchestrators using @dlazy/cli to authenticate, discover tools, invoke cloud and local tools, poll asynchronous jobs, and recover from common errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

AGPL-3.0-or-later

## Use Case:

External developers and teams use this guide to connect AI orchestrators to @dlazy/cli, discover available tools, run cloud or local tasks, and troubleshoot results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The quickstart describes using browser-session cookies for a downloader and does not explain their access implications.

Mitigation: Review cookie scope and exposure before enabling browser-cookie access.

Risk: The guide covers sending inputs to cloud tools without describing data-sharing implications.

Mitigation: Review what data each cloud tool receives before sending user or sensitive content.

Risk: The installation guidance does not pin the CLI package version, and scanning did not fully resolve referenced items.

Mitigation: Review or pin the CLI version and inspect linked references before running the quickstart.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown quickstart with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands vary with the tools registered in the CLI; some operations use cloud services or optional local runtimes.]

## Skill Version(s):

2.0.41 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
