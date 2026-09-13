## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public LinkedIn company, product, and showcase page data by known LinkedIn IDs for company profiling, product audits, showcase checks, and record enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and LinkedIn IDs or request parameters used in each lookup.

Mitigation: Use the skill only for public company, product, and showcase lookups, avoid private or personal-profile data, and keep CRAWLORA_API_KEY in the environment instead of code or command arguments.

Risk: The skill does not discover LinkedIn IDs and does not support personal LinkedIn profiles.

Mitigation: Provide IDs from trusted upstream sources or page URLs, and reject requests that imply personal-profile lookup or unsupported LinkedIn surfaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/linkedin-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known LinkedIn company, product, or showcase ID.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
