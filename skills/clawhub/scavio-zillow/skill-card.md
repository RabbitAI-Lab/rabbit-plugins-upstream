## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search Zillow listings, inspect detailed property records, retrieve rental-building details, and read agent profile reviews through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scavio API keys and Zillow lookup inputs are sent to Scavio's external API.

Mitigation: Use an appropriately scoped SCAVIO_API_KEY, avoid sending unnecessary sensitive lookup context, and confirm external API use is acceptable for the deployment.

Risk: Each endpoint call consumes credits, including empty or invalid-result workflows.

Mitigation: Validate required parameters before calling endpoints and relax filters instead of repeating searches that returned valid empty results.

Risk: Zillow-specific behaviors can make results misleading, such as filtered ZIP searches resolving to another city or unrecognized days_on_zillow values returning unfiltered data.

Mitigation: Use city names when combining filters or sorting, restrict days_on_zillow to documented values, and label Zestimate values as estimates rather than appraisals or sale prices.

Risk: The reviews endpoint returns agent reviews, not property reviews.

Mitigation: Present /zillow/reviews output only as agent profile and review data, and never describe it as feedback about a home.

## Reference(s):

- [Scavio Zillow Search Documentation](https://scavio.dev/docs/zillow-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-zillow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with inline JSON, code, and shell command examples; API responses use structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio Zillow endpoint calls consume credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
