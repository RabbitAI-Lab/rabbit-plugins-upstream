## Description:

Geoapify helps agents run address autocomplete, geocoding, routing, and route matrix actions through an OOMOL-connected Geoapify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Geoapify location services through an OOMOL-connected account for address lookup, geocoding, routing, and matrix calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions execute remote installer scripts directly, and the security verdict flags this as suspicious.

Mitigation: Review the installer path before use; prefer a verified package or signed release, or download and inspect the installer before execution.

Risk: The forward_geocode action is marked as write even though its description is lookup-style, which can make its effect ambiguous.

Mitigation: Confirm the exact payload and expected effect with the user before running any action marked write.

## Reference(s):

- [ClawHub Geoapify Skill](https://clawhub.ai/oomol/skills/oo-geoapify)
- [Geoapify Homepage](https://www.geoapify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns command responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
