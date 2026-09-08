## Description:

Search Google Maps to discover places, businesses, or map results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to turn Google Maps search requests into Dataify Scraper API calls and receive compact place, business, map-result, or explicitly requested raw response output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Maps search terms, place identifiers, and location anchors are sent to Dataify using the user's API token.

Mitigation: Use only queries intended for the external API and avoid sensitive personal locations unless that submission is acceptable.

Risk: External API calls require a Dataify token and may consume account credits, especially for high-volume or multi-page requests.

Mitigation: Verify token presence without exposing its value and confirm requests when scope or credit impact is material.

Risk: Minor documentation inconsistencies could cause parameter confusion.

Mitigation: Use the bundled API reference and script validation for required queries, documented defaults, and mutually exclusive Maps fields.

## Reference(s):

- [Dataify Google Maps API Reference](references/google_maps_api.md)
- [Dataify Google Maps ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-maps)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional shell commands and raw JSON or HTML when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses documented Google Maps search parameters and returns compact user-facing results by default.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
