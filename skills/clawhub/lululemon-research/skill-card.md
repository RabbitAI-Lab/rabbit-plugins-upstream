## Description:

Researches Lululemon's catalog — category navigation, category listings, product detail with pricing/sizes/reviews, curated outfit recommendations, and the physical store directory — using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to browse Lululemon categories, inspect product price, size, color, availability, review, outfit, and store data, and return normalized JSON through Crawlora instead of scraping Lululemon pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lululemon lookup parameters, including possible latitude and longitude for store searches, are sent to Crawlora.

Mitigation: Avoid submitting sensitive or unnecessarily precise location data, and use the skill only when sending those lookup parameters to Crawlora is acceptable.

Risk: The helper script can send the Crawlora API key to an API host selected through CRAWLORA_API_BASE.

Mitigation: Leave CRAWLORA_API_BASE unset or set it only to https://api.crawlora.net/api/v1 before running the helper.

Risk: The helper script is broader than the documented Lululemon workflow and can be used with arbitrary paths or POST bodies.

Mitigation: Use the documented Lululemon endpoints and review any path or request body before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/lululemon-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Lululemon catalog, outfit, review, availability, and store data from Crawlora endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
