## Description:

Researches public Apple job postings through the Crawlora API, including search results and full posting details such as description, qualifications, location, and team, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Apple's public careers listings, inspect hiring by role, team, or location, and retrieve full posting details for a specific Apple requisition or pipeline role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apple job search terms, job IDs, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only if that data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and do not hardcode, commit, or pass the key in query parameters.

Risk: The helper is intended only for public Apple Careers listings.

Mitigation: Use only the documented Apple Jobs routes and avoid submitting unrelated or sensitive data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; intended for public Apple Careers listings.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
