## Description:

Researches Old Navy, Gap, Banana Republic, and Athleta catalog data, including categories, products, colors, sizes, pickup availability, stores, and reviews, through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping agents use this skill to search Gap Inc. storefront catalogs, inspect product details and reviews, and check nearby pickup availability through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed catalog and location lookup queries to the third-party Crawlora API.

Mitigation: Use the skill only when Crawlora is an acceptable third-party service for the lookup, and avoid sending precise latitude and longitude unless store or pickup availability requires it.

Risk: The Crawlora API key could be exposed if hardcoded, committed, or passed directly in command-line arguments.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the bundled helper, which keeps the key out of request URLs and command-line arguments.

Risk: Search results can be best-effort and may fall back to recommended results for obscure or invalid keywords.

Mitigation: Treat search results as candidates and verify product identity, color-specific pid, brand, price, availability, and reviews before relying on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment and returns public catalog, review, store, and pickup availability data.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
