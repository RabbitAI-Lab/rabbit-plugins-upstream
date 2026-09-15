## Description:

API Ninjas connector for searching and reading air quality, weather, geocoding, reverse geocoding, timezone, and forecast data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query API Ninjas data through the OOMOL `oo` CLI after their account and API Ninjas connection are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing code on the user's machine.

Mitigation: Review the setup path before installing; prefer an official package-manager or checksum/signature-verified oo CLI installation and avoid pipe-to-shell commands.

Risk: The skill sends API request payloads through OOMOL to API Ninjas.

Mitigation: Treat request payloads as data shared with those services and avoid sending sensitive information unless that data flow is acceptable.

Risk: Authentication and connection setup can affect the user's OOMOL account and API Ninjas access.

Mitigation: Authenticate and connect API Ninjas manually, and do not run setup or installer commands with administrator privileges unless clearly required.

## Reference(s):

- [API Ninjas homepage](https://api-ninjas.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before API requests and returns API results as JSON from the `oo` CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
