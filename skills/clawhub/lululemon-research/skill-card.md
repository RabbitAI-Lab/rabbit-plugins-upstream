## Description:

Researches Lululemon's catalog - category navigation, category listings, product detail with pricing/sizes/reviews, curated outfit recommendations, and the physical store directory - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Lululemon categories, inspect product price, size, color, availability, and review data, retrieve curated outfit recommendations, and locate nearby Lululemon stores through Crawlora's documented Lululemon endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call paths beyond the stated Lululemon research scope.

Mitigation: Use only the documented /lululemon endpoints or restrict the helper with an allowlist before installation.

Risk: The skill requires a Crawlora API key.

Mitigation: Provide the key through CRAWLORA_API_KEY only, avoid query parameters or committed credentials, and rotate the key if exposure is suspected.

Risk: The security verdict is suspicious because the API script is broader than the skill's Lululemon purpose.

Mitigation: Review before installing and confirm agents are configured to call only the five documented Lululemon routes.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and documented Crawlora /lululemon endpoints.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
