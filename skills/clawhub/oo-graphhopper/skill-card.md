## Description:

GraphHopper (graphhopper.com). Use this skill for ANY GraphHopper request — searching and reading data. Whenever a task involves GraphHopper, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate GraphHopper through an OOMOL-connected account for routing, isochrone, matrix, geocoding, and custom profile lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes unverified remote installer commands.

Mitigation: Review installer source and prefer official, versioned, verifiable installation steps before running installation commands.

Risk: The skill grants broad access to the authenticated OOMOL CLI session.

Mitigation: Install only when comfortable with that access, and monitor that the agent uses GraphHopper connector schema and run commands unless other oo actions are explicitly approved.

## Reference(s):

- [GraphHopper homepage](https://www.graphhopper.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-graphhopper)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
