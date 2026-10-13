## Description:

Guides AI agents through installing, authenticating, discovering, and using dLazy CLI media tools, including asynchronous tasks and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this quickstart to discover available dLazy CLI tools, authenticate, run local and cloud media tasks, check costs, and monitor or troubleshoot results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a mutable global npm package may run unreviewed code.

Mitigation: Install only if you trust @dlazy/cli; review and pin the package version where possible.

Risk: Cloud media tools may incur charges and send supplied content to external services.

Mitigation: Confirm the provider, estimated cost, and content-sharing implications before paid calls; use dry-run validation when appropriate.

Risk: Browser cookies used for video downloads can expose account credentials.

Mitigation: Require explicit approval before using cookies_from_browser; treat extracted cookies as credentials and never log or share them.

Risk: Saving generated assets writes files to local disk.

Mitigation: Confirm the destination and review resulting files before further use or sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project repository (not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability and costs should be checked before invocation.]

## Skill Version(s):

2.0.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
