## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Yelp-ranked local businesses, retrieve full business records, and page through review text for lead generation, reputation monitoring, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Scavio API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and avoid hard-coding it in source files.

Risk: Yelp endpoint calls spend paid Scavio credits, including duplicate or unnecessary review paging.

Mitigation: Budget calls before use, rely on the business endpoint for the first review page, and start additional review paging at page 2.

Risk: A Yelp search without location can return metro-specific results based on the request exit location.

Mitigation: Provide a term and explicit location, or use a full Yelp search URL, before reporting search results.

## Reference(s):

- [Scavio Yelp Search Documentation](https://scavio.dev/docs/yelp-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/yelp-business-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio Yelp endpoints and interpret structured JSON responses.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
