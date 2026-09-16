## Description:

Connects an agent to IQAir AirVisual through the OOMOL iqair_airvisual connector to retrieve current air quality, weather, and supported-location data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for IQAir AirVisual air-quality, weather, and supported-location lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Verify the oo CLI installer source and integrity before running it, or use an approved internal installation process.

Risk: IQAir queries, including possible location-related request data, are routed through OOMOL.

Mitigation: Confirm OOMOL routing is acceptable for the intended environment and avoid submitting sensitive location data unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-iqair-airvisual)
- [IQAir AirVisual homepage](https://www.iqair.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are described as JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
