## Description:

OpenCage (opencagedata.com). Use this skill for OpenCage geocoding requests, including forward geocoding, reverse geocoding, and GeoJSON geocoding output through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve addresses or place names into OpenCage geocoding results, reverse geocode latitude and longitude coordinates, and request GeoJSON FeatureCollection output through an OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands and the security summary warns that connector action labels may overstate or mislabel effects.

Mitigation: Install the oo CLI only from a trusted, verified source; review installer contents before execution; inspect the live connector schema before each action; and confirm any action whose schema indicates create, update, write, or destructive effects.

## Reference(s):

- [OpenCage homepage](https://opencagedata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub OpenCage skill page](https://clawhub.ai/oomol/skills/oo-opencage)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
