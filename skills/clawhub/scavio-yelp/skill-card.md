## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Yelp local business listings, retrieve full business records, and page through reviews for lead generation, reputation monitoring, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Yelp lookup requests are sent through Scavio using SCAVIO_API_KEY.

Mitigation: Install only when that data flow is acceptable, keep the API key in a secret store or environment variable, and do not commit credentials.

Risk: Returned reviews and author or profile fields can contain third-party personal data.

Mitigation: Retain or republish only the fields needed for the user's task and avoid exposing unnecessary review or profile details.

Risk: Paging or invalid requests can consume credits without useful new data.

Mitigation: Start review paging at page 2 after fetching a business, stop when has_next_page is false, include location on searches, and use documented sort values.

Risk: Yelp may hide some reviews or omit popular item details, so returned data can be incomplete.

Mitigation: Report only data returned by the API, include the business URL for verification, and avoid claiming review or item lists are complete when omission flags or counts indicate otherwise.

## Reference(s):

- [Scavio Yelp Search documentation](https://scavio.dev/docs/yelp-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-yelp)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scavio Yelp API responses are structured JSON; each Yelp endpoint costs 2 credits.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
