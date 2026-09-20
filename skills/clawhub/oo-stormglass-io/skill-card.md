## Description:

Stormglass lets an agent retrieve tide and point weather data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Stormglass action schemas and retrieve high and low tide extremes, hourly tide sea-level data, and forecast weather for coordinates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that can execute code on the user's machine.

Mitigation: Review oo CLI installation steps manually and prefer official, versioned, checksum- or signature-verified installation before use; do not let an agent run remote installers automatically.

Risk: Stormglass access depends on OOMOL credentials, connection status, and billing state.

Mitigation: Keep credentials scoped to the intended read-only weather and tide use, and resolve authentication, connection, or billing failures with user confirmation.

## Reference(s):

- [Stormglass homepage](https://stormglass.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stormglass-io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Stormglass connector actions with live schema inspection before payload construction.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
