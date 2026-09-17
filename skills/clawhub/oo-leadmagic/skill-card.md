## Description:

LeadMagic (leadmagic.io) helps agents search and read lead intelligence data through OOMOL's oo CLI instead of calling the LeadMagic API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales operations teams, and developers use this skill to run LeadMagic connector actions for company enrichment, professional profile enrichment, mobile lookup, work email lookup, credit checks, and email validation through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review the installer path before use and prefer an official, version-pinned, signed, or checksum-verified installer.

Risk: Lead enrichment requests may submit personal or business identifiers to OOMOL and LeadMagic and may consume LeadMagic credits.

Mitigation: Confirm that submitted identifiers are appropriate to share with those services and check credit impact before running lookups at scale.

## Reference(s):

- [LeadMagic homepage](https://leadmagic.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [LeadMagic skill page](https://clawhub.ai/oomol/skills/oo-leadmagic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs LeadMagic connector actions through the oo CLI and returns action data with execution metadata when JSON output is requested.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
