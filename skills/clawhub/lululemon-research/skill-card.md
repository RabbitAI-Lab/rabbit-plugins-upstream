## Description:

Researches Lululemon's catalog, product details, outfit recommendations, reviews, and store directory through the Crawlora API and returns normalized JSON instead of scraping shop.lululemon.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse Lululemon categories, inspect product pricing, sizes, colors, reviews, and sale status, retrieve curated outfit recommendations, and locate stores through Crawlora's Lululemon endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the bundled helper can send the Crawlora API key to an overridden API base or unrelated Crawlora routes.

Mitigation: Keep the environment controlled, remove or lock down CRAWLORA_API_BASE before use, and restrict calls to the documented /lululemon endpoints.

Risk: The skill requires a Crawlora API key for all requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [lululemon-research endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/lululemon-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests and returns normalized public catalog, review, outfit, and store data.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
