## Description:

Stormglass (stormglass.io) supports Stormglass data requests such as tide extremes, tide sea level, and point weather forecasts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Stormglass marine and weather data through the OOMOL oo CLI after the user has connected a Stormglass account. It supports coordinate-based tide extremes, hourly tide sea-level data, and weather forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI from a trusted, reviewed source with version pinning and checksum or signature verification where possible.

Risk: Stormglass access depends on a connected OOMOL account and server-side credentials.

Mitigation: Connect Stormglass deliberately through the user's OOMOL account and retry setup only after explicit authentication or connection errors.

## Reference(s):

- [Stormglass homepage](https://stormglass.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stormglass-io)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include connector data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
