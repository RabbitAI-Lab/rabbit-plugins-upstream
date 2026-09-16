## Description:

Fixer (fixer.io) connector skill for retrieving latest rates, historical rates, and supported currency symbols through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Fixer exchange-rate data through an OOMOL-connected account, including latest rates, historical rates, and supported currency symbols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands pipe downloaded scripts directly into a shell during first-time setup.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI through a trusted process with version pinning and integrity verification where possible.

Risk: Connector actions depend on live Fixer connection, authentication, and billing state.

Mitigation: Run setup or account-recovery commands only after an action fails with the matching authentication, connection, scope, credential, app, or billing error.

## Reference(s):

- [Fixer homepage](https://fixer.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fixer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; action responses are JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
