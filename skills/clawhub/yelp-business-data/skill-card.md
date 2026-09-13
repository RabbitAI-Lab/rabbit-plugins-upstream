## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Yelp businesses, retrieve detailed business profiles, and collect review data for local lead generation, reputation monitoring, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Yelp lookup requests and the Scavio API key are sent to Scavio.

Mitigation: Use the documented SCAVIO_API_KEY environment variable, keep the key out of source control, and run in an isolated environment when evaluating the skill.

Risk: Each Yelp endpoint call consumes paid credits, including duplicate or empty requests.

Mitigation: Budget before paging, start review paging at page 2 because the business endpoint includes page 1, and avoid broad or location-less searches.

Risk: Location-less searches can return results based on the proxy exit location, which may be inconsistent across runs.

Mitigation: Provide an explicit location or a full Yelp search URL and verify that reported filters are reflected in the returned data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/yelp-business-data)
- [Scavio Yelp Search documentation](https://scavio.dev/docs/yelp-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=yelp-business-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=yelp-business-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples and inline Python, JavaScript, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to make authenticated HTTPS or SDK calls that return structured JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
