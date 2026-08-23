## Description:

Google Maps local business and place data as structured JSON: search places by query and map center, fetch full place detail with address, phone, hours, rating and GPS coordinates, and page reviews with sort.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search local businesses and places, retrieve place details, and fetch paginated reviews from the Scavio Google Maps API. It is suited for local lead generation, business listing enrichment, and place-data lookup workflows that require structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search, place detail, and review requests are sent to Scavio and consume SCAVIO_API_KEY credits.

Mitigation: Keep the API key out of source control and confirm with the user before paginating through many result pages.

Risk: The skill returns place and review data from an external API, so fabricated or unsourced place details would mislead users.

Mitigation: Return only data from API responses and avoid inventing place names, ratings, addresses, or review text.

## Reference(s):

- [Scavio Google Maps API documentation](https://scavio.dev/docs/google-maps?utm_source=clawhub&utm_medium=skill&utm_campaign=google-maps-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=clawhub&utm_medium=skill&utm_campaign=google-maps-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-maps-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint costs 1 credit per request.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
