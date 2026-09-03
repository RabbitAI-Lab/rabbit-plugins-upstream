## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Zillow sale, rental, and sold listings, inspect detailed property records, and retrieve real-estate agent profile reviews through Scavio's Zillow API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zillow-related queries send locations, property identifiers, URLs, or agent screen names to Scavio as a third-party service.

Mitigation: Install and use the skill only when that data sharing is acceptable for the user and use case.

Risk: Each API call consumes Scavio credits, including calls that return empty results.

Mitigation: Confirm filters and identifiers before calling endpoints, and make users aware of credit usage when queries may require retries or pagination.

Risk: The skill requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in environment or secret storage and never hard-code live credentials in shared files.

Risk: Property data could be misused to profile home occupants.

Mitigation: Use returned public listing data for real-estate search and analysis, not occupant profiling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/zillow-property-data)
- [Scavio Zillow API documentation](https://scavio.dev/docs/zillow-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [Scavio sign-up](https://dashboard.scavio.dev/sign-up?utm_source=clawhub&utm_medium=skill&utm_campaign=zillow-property-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for POST requests to Scavio Zillow endpoints and interpretation of returned structured JSON.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
