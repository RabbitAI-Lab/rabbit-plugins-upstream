## Description:

Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API for current place lookups and comparisons, including addresses, ratings, review themes, and business information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research Google Maps places through Crawlora, compare current business details, and summarize addresses, ratings, review themes, photos, source URLs, and unknown fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends Google Maps lookup requests to Crawlora.

Mitigation: Use a dedicated Crawlora key with limited account exposure, keep it in the environment, and revoke or rotate it if the workspace is shared or compromised.

Risk: The helper may allow broader Crawlora API paths or methods than the documented Google Maps workflow needs.

Mitigation: Review requested paths before execution and prefer only the documented Google Maps search, place detail, review, and photo endpoints until the provider tightens endpoint and place_id scoping.

Risk: Google Maps search results, reviews, and photos are snapshots and may be incomplete or non-representative.

Mitigation: Report retrieval time, preserve source URLs, avoid claiming exhaustive coverage, and mark unavailable business fields as unknown.

## Reference(s):

- [Google Maps endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include place names, addresses, source URLs, ratings, review counts, retrieval time, review observations, photo observations, and unavailable fields marked as unknown.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
