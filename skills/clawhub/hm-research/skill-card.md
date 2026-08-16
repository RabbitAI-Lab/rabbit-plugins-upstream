## Description:

Researches H&M catalog categories, listings, product details, free-text search results, and nearby physical stores through the Crawlora API, returning normalized JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping agents use this skill to browse or search H&M products, compare product detail and reviews, and find nearby H&M stores without scraping hm.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call unrelated Crawlora endpoints with arbitrary methods and request bodies.

Mitigation: Use the skill only for non-sensitive H&M research, keep the API key in the environment, and restrict helper usage to the documented H&M GET endpoints before deployment.

## Reference(s):

- [hm-research endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/hm-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Normalized JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses public H&M product, category, review, and store data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
