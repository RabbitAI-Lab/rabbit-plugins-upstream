## Description:

Search Google Maps for local businesses and places, fetch full place details, read place reviews, and run a local-SEO geo-grid to track where a business ranks across an NxN lattice of points, as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Google Maps, enrich places with details and reviews, and run local-SEO geo-grid rank checks through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Map searches, locations, place IDs, and business names are sent to Scavio's API.

Mitigation: Install only when use of Scavio as the data provider is acceptable for the intended data.

Risk: Geo-grid requests can consume more credits because costs scale with the number of grid points.

Mitigation: Check credit usage before paginating many pages or running larger geo-grid searches.

## Reference(s):

- [Scavio Google Maps documentation](https://scavio.dev/docs/google-maps?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-maps-api)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and example code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends map searches, locations, place IDs, and business names to Scavio.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
