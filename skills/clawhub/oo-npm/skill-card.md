## Description:

Provides npm registry lookup, package metadata, download analytics, current-user lookup, and security advisory audit workflows through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search npm packages, inspect package and version metadata, review download counts, identify the connected npm user, and audit exact package versions for advisories through an OOMOL-connected npm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote installer commands that execute downloaded scripts directly.

Mitigation: Use a verified installer when available, or inspect and validate the downloaded script before executing it.

Risk: npm connector requests and account connection depend on OOMOL as an intermediary.

Mitigation: Install only when the user accepts OOMOL handling connector requests and server-side account credentials for this workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-npm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [npm homepage](https://www.npmjs.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and execution metadata when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
