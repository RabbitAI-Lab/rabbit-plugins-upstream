## Description:

Researches Sam's Club catalog data across departments, category product grids, product details, related-item shelves, and curated content pages through the Crawlora API, returning clean JSON instead of scraping samsclub.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when a user needs Sam's Club department browsing, category product listings, product price, availability, ratings, related items, or curated content page data. It is intended for public catalog research through Crawlora rather than direct HTML scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper is broader than the stated Sam's Club research purpose and can send arbitrary requests to Crawlora.

Mitigation: Use only the documented /samsclub GET endpoints or a constrained wrapper, and avoid passing secrets, personal data, or unrelated requests through the helper.

Risk: Using the skill sends Sam's Club lookup IDs or URLs to Crawlora with the user's API key.

Mitigation: Install only if that third-party service use is acceptable, keep the API key in CRAWLORA_API_KEY, and do not hardcode, commit, or place the key in query parameters.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/samsclub-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented Sam's Club GET endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
