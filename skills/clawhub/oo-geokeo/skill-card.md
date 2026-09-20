## Description:

Geokeo (geokeo.com). Use this skill for ANY Geokeo request: searching and reading data through the OOMOL-connected Geokeo connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to run Geokeo forward and reverse geocoding through an OOMOL-connected account. It helps agents inspect the live connector schema, build valid JSON payloads, and run read-oriented geocoding actions with the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Confirm trust in OOMOL and Geokeo, and prefer the official oo CLI installation guide or a verifiable release before running installer commands.

Risk: Geocoding lookups use the user's OOMOL-connected Geokeo account and may submit address or coordinate data to the service.

Mitigation: Confirm the user intends to use the connected Geokeo account and avoid submitting sensitive location data unless authorized.

## Reference(s):

- [Geokeo homepage](https://geokeo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-geokeo)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; credentials are handled through the connected OOMOL account.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
