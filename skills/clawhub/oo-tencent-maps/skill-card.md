## Description:

Tencent Maps helps agents search, read, geocode, route, and retrieve weather or place data from Tencent Maps through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs Tencent Maps data such as geocoding, reverse geocoding, place search, administrative districts, route planning, distance matrices, IP location, or weather. The skill instructs the agent to inspect live connector schemas before sending requests through the OOMOL-connected Tencent Maps service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that can execute downloaded code.

Mitigation: Review installer commands before running them; prefer official installation documentation, pinned releases, and checksum or signature verification where available.

Risk: Map queries and location data may be sent through OOMOL and Tencent Maps.

Mitigation: Use the skill only when sharing the relevant address, coordinate, route, IP, weather, or place-query data with those services is appropriate.

## Reference(s):

- [Tencent Maps homepage](https://lbs.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tencent-maps)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Tencent Maps icon](https://static.oomol.com/logo/third-party/tencent_maps.png)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides connector calls that return JSON data with a meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
