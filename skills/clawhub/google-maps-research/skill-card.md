## Description:

Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API for current place lookups and comparisons involving addresses, ratings, review themes, and business information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to search Google Maps through Crawlora, refresh place details, and compare businesses or places using addresses, ratings, review counts, review samples, photos, source URLs, and clearly marked unknowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send a Crawlora API key and arbitrary requests outside the documented Google Maps scope.

Mitigation: Use a scoped, revocable Crawlora API key and restrict use to the documented Google Maps endpoints.

Risk: Changing CRAWLORA_API_BASE can direct requests and credentials to an untrusted destination.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is fully trusted and intentionally approved.

Risk: Prompts or request bodies may contain private or internal data that would be sent to the Crawlora service.

Mitigation: Avoid submitting private, confidential, or internal data through skill prompts or API request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with tables and inline shell commands; API helper responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include retrieval time, source URLs, ratings with review counts, attributed review observations, and unknown fields when data is unavailable.]

## Skill Version(s):

1.0.1 (source: server release metadata, created 2026-09-08T04:31:49Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
