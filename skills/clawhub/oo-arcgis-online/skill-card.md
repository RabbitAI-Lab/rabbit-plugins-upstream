## Description:

Use this skill for ArcGIS Online requests involving searching and reading data through ArcGIS Online rather than calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to perform ArcGIS Online lookup workflows through an OOMOL-connected account, including address candidate search, reverse geocoding, and address or place suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute immediately on the user's machine.

Mitigation: Review the skill before installing and inspect or independently trust the OOMOL CLI installation path before running installer commands.

Risk: Address and coordinate lookup requests may contain sensitive location data.

Mitigation: Send only addresses or coordinates that are appropriate to process through OOMOL's connector service.

Risk: Authentication, connection, or billing failures can block ArcGIS Online connector actions.

Mitigation: Use the skill only for the listed lookup actions and follow the documented recovery steps when a command returns an auth, connection, scope, or billing error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-arcgis-online)
- [ArcGIS Online homepage](https://www.arcgis.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting ArcGIS Online action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
