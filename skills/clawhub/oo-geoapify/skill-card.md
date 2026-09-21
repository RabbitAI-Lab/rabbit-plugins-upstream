## Description:

Geoapify (geoapify.com) supports searching and reading Geoapify location data through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Geoapify through OOMOL for address autocomplete, forward and reverse geocoding, route calculation, and travel matrix requests without handling raw Geoapify API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote oo CLI installer scripts directly in a shell.

Mitigation: Review the installer manually, prefer official installation documentation with verification steps, and only run setup commands when the connector is needed and OOMOL is trusted.

Risk: Geoapify actions depend on an authenticated OOMOL connection and may fail when credentials, scopes, or billing state are unavailable.

Mitigation: Use the documented setup and billing checks only after an action fails with the matching authentication, connection, scope, credential, app, or credit error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-geoapify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Geoapify homepage](https://www.geoapify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Geoapify action responses are returned by the connector as JSON data with execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
