## Description:

LiveSession helps agents search and read LiveSession replay data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect LiveSession action schemas and list session replays through the OOMOL LiveSession connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute scripts from the network.

Mitigation: Install the oo CLI only through a trusted, user-reviewed method; verify the installer source, version, and integrity before running setup commands.

Risk: The skill depends on OOMOL account authentication, LiveSession connection state, scopes, and billing status.

Mitigation: Run setup or recovery commands only after matching auth, connection, scope, credential, or billing errors occur, and avoid proactively opening login or connection flows.

## Reference(s):

- [ClawHub LiveSession skill](https://clawhub.ai/oomol/skills/oo-livesession)
- [LiveSession homepage](https://livesession.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payload examples, connector schema inspection commands, and oo CLI action invocations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
