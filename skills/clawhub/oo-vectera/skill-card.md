## Description:

Vectera (go.vectera.com). Use this skill for Vectera requests involving reading, creating, and updating data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Vectera meeting rooms through an OOMOL-connected account, including listing, retrieving, creating, updating, and configuring rooms and room permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Vectera meeting rooms, permissions, or settings.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write or destructive.

Risk: Setup and connection commands can alter local authentication or account connection state.

Mitigation: Run first-time setup, login, or connection steps only after an oo CLI command fails with the matching auth, connection, or missing-command error.

Risk: Incorrect JSON payloads could run the wrong connector action or use invalid fields.

Mitigation: Fetch the live connector schema before constructing payloads and validate the JSON against that schema.

## Reference(s):

- [Vectera homepage](https://go.vectera.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vectera)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and JSON payloads validated against the live connector schema.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
