## Description:

Search Google Maps for local businesses and places, fetch full place details, read place reviews, and run a local-SEO geo-grid to track where a business ranks across an NxN lattice of points, as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to search for local places, enrich place records with details and reviews, and measure local Maps ranking across a geographic grid. It is suited for lead discovery, local search analysis, and local-SEO workflows that need structured Google Maps-style data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Scavio as a third-party API provider for Google Maps-style data.

Mitigation: Install only when that provider relationship is acceptable for the intended data and workflow.

Risk: SCAVIO_API_KEY could be exposed if copied into source files, logs, or shared transcripts.

Mitigation: Store the key in an environment variable or secret store and do not commit it.

Risk: Pagination and geo-grid searches can consume paid credits quickly, especially because geo-grid cost scales by grid point.

Mitigation: Confirm credit costs before paginating heavily or running large geo-grid searches.

## Reference(s):

- [Scavio Google Maps API documentation](https://scavio.dev/docs/google-maps?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-maps-api)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses may include place data, reviews, pagination, credits used, credits remaining, and cache status.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
