## Description:

Researches Sam's Club's catalog, including departments, category product grids, product detail, related-item shelves, and curated content pages, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to browse Sam's Club departments and categories, inspect product price, availability, ratings, and related items, and retrieve curated Sam's Club content as normalized JSON instead of scraping samsclub.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sam's Club category or product identifiers and related lookup parameters are sent to Crawlora.

Mitigation: Use the skill only when sending those public lookup parameters to Crawlora is acceptable for the user or organization.

Risk: The Crawlora API key can be exposed if it is committed, placed in a URL, or sent to an untrusted custom API base.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not commit it, and set CRAWLORA_API_BASE only for destinations that are intentionally trusted.

Risk: Catalog responses can reflect upstream public-site limitations, including zero-result category responses, 404 content pages, or generic related-item shelves for unknown identifiers.

Mitigation: Verify important price, availability, and recommendation decisions against the current Sam's Club product or category page before acting on them.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/samsclub-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Sam's Club catalog data through Crawlora endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
