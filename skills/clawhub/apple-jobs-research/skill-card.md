## Description:

Researches Apple job postings via the Crawlora API, searching jobs.apple.com and pulling full posting detail including description, qualifications, location, and team as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Apple Careers listings, inspect hiring by team or location, and retrieve detailed public posting information for a specific requisition or pipeline role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Apple jobs search requests to Crawlora as a third-party API provider.

Mitigation: Install only when third-party API use is acceptable for the intended workflow.

Risk: Search terms may contain sensitive personal or business information.

Mitigation: Avoid placing sensitive personal data, confidential business plans, or private candidate information in search queries.

Risk: The helper requires a Crawlora API key and successful calls may consume Crawlora credits.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not hardcode or commit it, and monitor credit usage.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses GET requests to documented Crawlora Apple Jobs endpoints.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
