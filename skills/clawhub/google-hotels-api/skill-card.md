## Description:

Search Google Hotels for a destination and stay dates, then retrieve structured property details, nightly rates, ratings, amenities, and booking-site prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare hotels or vacation rentals by destination, stay dates, price, rating, class, and amenities, then inspect detailed booking-source prices for selected properties.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches and stay details are sent to Scavio's API.

Mitigation: Use the skill only with data appropriate for third-party processing and avoid sending unnecessary sensitive details.

Risk: Each endpoint call consumes one Scavio credit.

Mitigation: Run search before detail, use filters and limits, and tell users when additional calls may consume credits.

Risk: API key exposure could allow unauthorized use.

Mitigation: Use a dedicated SCAVIO_API_KEY from the environment or a secret store and keep it out of source code.

## Reference(s):

- [Scavio Google Hotels API documentation](https://scavio.dev/docs/google-hotels?utm_source=clawhub&utm_medium=skill&utm_campaign=google-hotels-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=clawhub&utm_medium=skill&utm_campaign=google-hotels-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-hotels-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON from Scavio API responses, with concise Markdown guidance or summaries when presenting results to users]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search and detail endpoints each cost one credit; search results must provide detail_token before requesting property details.]

## Skill Version(s):

1.0.0 (source: frontmatter, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
