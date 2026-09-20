## Description:

Researches H&M's catalog -- storefront categories, product listings, product detail, free-text search, and nearby physical stores -- using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research public H&M catalog, product-detail, search, and store-location data through Crawlora instead of scraping hm.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: H&M search terms, product IDs, and store-location queries are sent to Crawlora with the user's API key.

Mitigation: Avoid including secrets or unrelated personal data in search parameters, and use the skill only for intended H&M catalog and store research.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or placed in prompts.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the provided helper, which keeps the key out of command-line arguments.

## Reference(s):

- [hm-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/hm-research)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET requests; requires CRAWLORA_API_KEY; results depend on Crawlora API and H&M public data availability.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
