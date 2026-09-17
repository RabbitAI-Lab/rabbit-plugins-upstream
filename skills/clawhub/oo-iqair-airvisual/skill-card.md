## Description:

Connects an agent to IQAir AirVisual through OOMOL for current air quality, weather, and supported-location lookup requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current IQAir AirVisual air quality and weather data, find nearest supported city data, and list supported countries, states, and cities through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad oo CLI execution authority rather than a narrow allowlist for IQAir AirVisual actions.

Mitigation: Review intended commands before installation and restrict use to the documented IQAir AirVisual schema and run commands where the host environment supports command-level controls.

Risk: The first-time setup section includes pipe-to-shell installer commands.

Mitigation: Independently verify the OOMOL CLI installer source and installation instructions before running those commands.

Risk: Connector action schemas may change over time.

Mitigation: Fetch the live connector schema before constructing each payload, as the skill instructs.

## Reference(s):

- [IQAir AirVisual homepage](https://www.iqair.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-iqair-airvisual)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to inspect live connector schemas before running read-only IQAir AirVisual actions.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
