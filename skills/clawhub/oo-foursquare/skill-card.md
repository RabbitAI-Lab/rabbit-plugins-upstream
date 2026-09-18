## Description:

Search and read Foursquare place data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search nearby places, retrieve place details, photos, and tips from Foursquare through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts executed directly in a shell.

Mitigation: Review the installer before running it; prefer an official package manager or a version-pinned download with a published checksum or signature, and avoid elevated privileges unless verified as required.

Risk: Foursquare searches and place lookups may include location or place identifiers sent through the connected service.

Mitigation: Send only the location and place details needed for the user's request, and confirm before including sensitive or unnecessary personal context.

## Reference(s):

- [ClawHub Foursquare Skill](https://clawhub.ai/oomol/skills/oo-foursquare)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Foursquare Homepage](https://foursquare.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
