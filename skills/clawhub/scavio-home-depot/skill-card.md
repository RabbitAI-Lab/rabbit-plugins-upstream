## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON. 3 endpoints for retail price monitoring, catalog enrichment and review mining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Home Depot products, retrieve item details, and page through reviews for retail price monitoring, catalog enrichment, and review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home Depot queries, item IDs, and product URLs are sent to Scavio.

Mitigation: Avoid sending sensitive or unnecessary query data, and disclose the third-party API use before running lookups.

Risk: Each API request consumes credits, including paginated searches and reviews.

Mitigation: Set an explicit page or credit budget before looping through search results or reviews.

Risk: SCAVIO_API_KEY is required for API access.

Mitigation: Store the key in an environment variable or secret store and keep it out of source control and shared logs.

## Reference(s):

- [Scavio Home Depot Search Documentation](https://scavio.dev/docs/home-depot-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes structured JSON responses, fixed pagination sizes, billed API calls, and SCAVIO_API_KEY setup.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
