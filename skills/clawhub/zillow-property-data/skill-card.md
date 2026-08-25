## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured Zillow listing, property, rental-building, and real-estate agent review data through Scavio for property search, comparable analysis, rent-vs-buy analysis, and market monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Zillow search inputs, property IDs or URLs, and agent screen names to Scavio using the user's API key.

Mitigation: Install and use it only when sharing those inputs with Scavio is acceptable, and keep SCAVIO_API_KEY in environment or secret storage.

Risk: Each API request consumes a credit, including empty or invalid-result workflows.

Mitigation: Validate parameters before calling endpoints and avoid retrying unchanged requests when filters are too narrow or identifiers cannot be resolved.

Risk: Returned listing data, Zestimates, and agent reviews can be misread as appraisals, property reviews, or personal profiling material.

Mitigation: Treat results as public real-estate data, label Zestimates as estimates, keep agent reviews separate from property reviews, and avoid occupant profiling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/zillow-property-data)
- [Scavio Zillow Search documentation](https://scavio.dev/docs/zillow-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown with JSON API request examples and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for API calls that return structured JSON; requests require SCAVIO_API_KEY and consume one credit per endpoint call.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
