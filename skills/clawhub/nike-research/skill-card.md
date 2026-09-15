## Description:

Researches Nike's catalog, including categories, search, product detail, colorways, reviews, and nearby stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce agents use this skill to research public Nike catalog data, compare products and colorways, summarize reviews, and locate nearby Nike stores without scraping nike.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nike search terms, product identifiers, review queries, and store-location coordinates are sent to Crawlora under the user's API key.

Mitigation: Install only when this data sharing is acceptable, and avoid sending unrelated or sensitive data through the helper.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in unsafe contexts.

Mitigation: Keep CRAWLORA_API_KEY private and provide it only through the environment as documented.

## Reference(s):

- [Nike endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/nike-research)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends Nike research requests to Crawlora.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
