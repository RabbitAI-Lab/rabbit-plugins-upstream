## Description:

Search Google Maps for local businesses and places, fetch full place details, read place reviews, and run a local-SEO geo-grid to track where a business ranks across an NxN lattice of points, as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Google Maps, enrich places with details and reviews, and measure local search rank across geographic grids through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key to query Google Maps data.

Mitigation: Provide SCAVIO_API_KEY through the environment or a secret manager, and avoid embedding keys in source files or shared outputs.

Risk: Searches, reviews, place details, and especially geo-grid requests consume Scavio API credits.

Mitigation: Confirm the user wants to spend credits before paginating broadly or running large geo-grid requests.

Risk: Map results, ratings, addresses, reviews, and rank positions can be incomplete, cached, or unavailable from the upstream data provider.

Mitigation: Return only API-provided data, avoid fabricating missing values, and surface empty results or upstream errors clearly.

## Reference(s):

- [Scavio Google Maps documentation](https://scavio.dev/docs/google-maps)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-maps-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell setup, code examples, API calls, and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and consumes Scavio API credits for searches, place details, reviews, and geo-grid rank tracking.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
