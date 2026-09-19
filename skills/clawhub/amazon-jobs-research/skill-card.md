## Description:

Researches Amazon.jobs postings via the Crawlora API by searching public careers data and fetching individual posting details as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Amazon job openings by keyword, category, country, or recency and retrieve full details for a specific Amazon job ID through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and requested job IDs are sent to Crawlora as a third-party service.

Mitigation: Use only non-sensitive search terms and review Crawlora's service terms before use.

Risk: A Crawlora API key is required for requests.

Mitigation: Store CRAWLORA_API_KEY only in the environment; do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [Amazon Jobs endpoint reference](reference/endpoints.md)
- [Crawlora service](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/amazon-jobs-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses GET requests to documented Amazon Jobs endpoints.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
