## Description:

Foursquare helps agents use the OOMOL-connected oo CLI to search for places and retrieve place details, photos, and tips without handling raw Foursquare credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search Foursquare Places, retrieve place details, and fetch photos or tips through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute changing code on a user's machine.

Mitigation: Prefer an official, version-pinned oo CLI installer with checksum or signature verification, and run setup only after a missing-command or authentication failure.

## Reference(s):

- [ClawHub Foursquare Skill](https://clawhub.ai/oomol/skills/oo-foursquare)
- [Foursquare Homepage](https://foursquare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown text with oo CLI commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands can return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
