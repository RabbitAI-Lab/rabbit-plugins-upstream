## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Yelp business listings, retrieve structured business profiles, and page through reviews for local lead lists, reputation monitoring, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Yelp lookup queries to a third-party Scavio API using SCAVIO_API_KEY.

Mitigation: Store the API key in environment or secret management, keep it out of source control, and review whether submitted queries are appropriate for the deployment.

Risk: Each Yelp endpoint call spends credits, and repeated review paging or duplicate page-one review requests can create avoidable cost.

Mitigation: Budget requests before paging, use the business endpoint for the first review page, and start additional review paging at page 2.

Risk: Yelp business and review data can be incomplete, filtered, or time-sensitive.

Mitigation: Return the Yelp business URL with important results and verify business names, ratings, addresses, hours, and review details before relying on them.

Risk: Searches without a location can produce unstable metro-specific results.

Mitigation: Provide a location for term-based searches or use a full Yelp search URL.

## Reference(s):

- [Scavio Yelp Search Documentation](https://scavio.dev/docs/yelp-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/yelp-business-data)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with JSON-oriented API guidance and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns structured JSON from Scavio API calls.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
