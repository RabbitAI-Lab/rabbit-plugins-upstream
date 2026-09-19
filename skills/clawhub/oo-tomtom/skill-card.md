## Description:

Use this skill for TomTom requests involving search, geocoding, nearby place lookup, autocomplete, and reverse geocoding through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve TomTom location data, including address search, geocoding, nearby places, autocomplete suggestions, and reverse geocoding, through an already configured OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes executing remote installer scripts directly in a shell.

Mitigation: Prefer a managed or verified installation source for the oo CLI, and review installer contents before executing remote scripts.

Risk: Connector actions depend on a live OOMOL account connection and may fail when credentials, scopes, app state, or billing are unavailable.

Mitigation: Run setup and account-connection steps only after matching command failures, then retry with the connector schema as the authoritative contract.

## Reference(s):

- [TomTom Developer](https://developer.tomtom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tomtom)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; listed TomTom actions are read-focused.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
