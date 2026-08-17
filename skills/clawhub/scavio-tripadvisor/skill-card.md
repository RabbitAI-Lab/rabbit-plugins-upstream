## Description:

Scavio Tripadvisor resolves place or business names to Tripadvisor IDs and retrieves ranked restaurants, hotels, attractions, location details, and paged review data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query Scavio for Tripadvisor venue discovery, local ranking, location detail, review retrieval, competitive comparison, and reputation monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tripadvisor place queries and related lookup parameters are sent to Scavio using the user's API key.

Mitigation: Use the skill only when the user is comfortable sending those lookup parameters to Scavio, and avoid sending sensitive data in place queries.

Risk: Each documented request consumes credits, including some empty or error responses.

Mitigation: Tell users the expected credit cost before multi-call workflows, resolve IDs before dependent calls, and avoid duplicate or past-last pagination.

Risk: Returned ratings, rankings, and reviews reflect Tripadvisor data selected for display and may not represent a complete market view.

Mitigation: Attribute ratings and rankings to Tripadvisor, preserve returned values, and avoid fabricating or extrapolating venue or review details.

## Reference(s):

- [Scavio Tripadvisor Locations Documentation](https://scavio.dev/docs/tripadvisor-locations)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Tripadvisor endpoints use Scavio credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
