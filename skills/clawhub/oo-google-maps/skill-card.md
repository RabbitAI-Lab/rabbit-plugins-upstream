## Description:

Google Maps lets agents search places, retrieve place details, geocode addresses or coordinates, and compute routes through an OOMOL-connected Google Maps account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform Google Maps lookup, geocoding, place search, and route computation tasks through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Maps requests can include addresses, coordinates, routes, and place queries that are routed through OOMOL.

Mitigation: Use the skill only when the user accepts OOMOL as the service path for those payloads, and avoid sending sensitive location data unless the user has approved that exposure.

Risk: First-time setup includes remote installer one-liners for the oo CLI.

Mitigation: Do not run installer commands automatically; prefer reviewed, version-pinned, or signed installation steps.

Risk: Authentication, provider connection, and billing setup steps affect the user's OOMOL account.

Mitigation: Ask the user to approve sign-in, provider connection, and billing actions before opening or running those setup steps.

## Reference(s):

- [ClawHub Google Maps skill](https://clawhub.ai/oomol/skills/oo-google-maps)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Maps Platform](https://mapsplatform.google.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected Google Maps provider before action calls can succeed.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
