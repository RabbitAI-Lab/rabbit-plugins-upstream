## Description:

Builds and qualifies local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build deduplicated local-business lead shortlists or CSVs with contacts, qualification evidence, source URLs, and refresh status for a requested category and geography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can leak the Crawlora API key if CRAWLORA_API_BASE is redirected.

Mitigation: Use the helper only in a trusted shell, keep CRAWLORA_API_BASE unset or verify it is exactly https://api.crawlora.net/api/v1, and rotate the key if the helper ran with an untrusted API base.

Risk: The bundled API helper is broader than the local-business prospecting workflow.

Mitigation: Review commands before execution and restrict use to the endpoints needed for the requested prospecting task.

Risk: Business prospecting may expose private or regulated data if the user supplies it to the helper or scraping endpoints.

Mitigation: Use only publicly published business information and avoid sending private or regulated data through the helper.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table or CSV with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes business names, provider IDs, addresses, public contact fields, ratings, qualification evidence, source URLs, retrieval time, and refresh status when available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
