## Description:

Mapbox (mapbox.com). Use this skill for ANY Mapbox request: reading, creating, and updating data through an OOMOL-connected Mapbox account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to geocode addresses, reverse geocode coordinates, compute directions, and calculate travel-time or distance matrices through Mapbox via the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mapbox request payloads, including addresses, coordinates, and route details, are routed through OOMOL.

Mitigation: Use the skill only when that data flow is acceptable for the task and organization.

Risk: First-time setup includes shell installer commands that pipe remote scripts directly to an interpreter.

Mitigation: Prefer a reviewed, signed, or package-manager installation path, and do not run installer commands blindly.

Risk: Some actions can change Mapbox state.

Mitigation: Inspect the live action schema first and confirm the exact payload and expected effect before executing write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mapbox)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Mapbox homepage](https://www.mapbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Mapbox connector JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
