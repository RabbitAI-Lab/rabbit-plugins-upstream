## Description:

ShipBob (shipbob.com). Use this skill for ANY ShipBob request — searching and reading data. Whenever a task involves ShipBob, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query ShipBob inventory, product, channel, and fulfillment-location data through an OOMOL-connected ShipBob account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Use a verified, pinned, or package-manager installation path where available, and only run the remote installer after deciding that OOMOL's installer source is trusted.

Risk: Connector actions depend on a live ShipBob account connection and action schema.

Mitigation: Inspect the live action schema before submitting a payload and avoid proactive sign-in or connection setup unless a command fails for that reason.

## Reference(s):

- [ShipBob homepage](https://www.shipbob.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ship-bob)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
