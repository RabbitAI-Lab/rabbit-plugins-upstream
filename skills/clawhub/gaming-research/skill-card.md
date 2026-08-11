## Description:

Researches video games via the Crawlora API, covering Steam store pages, pricing, reviews, player counts, charts, tags, achievements, and PlayStation Store products, categories, and deals as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research games, compare pricing and discounts, check Steam reviews and current player counts, and browse Steam or PlayStation Store listings through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora paths and send request bodies beyond the gaming endpoints described by the skill.

Mitigation: Review calls before execution and restrict use to the documented /steam and /playstation endpoints when a narrow gaming lookup tool is required.

Risk: Requests require a Crawlora API key and may send user-provided query terms or request bodies to the Crawlora API.

Mitigation: Keep CRAWLORA_API_KEY in the environment, never commit or pass it in URLs, and avoid sending private or sensitive data through API requests.

Risk: Steam price and availability data can vary by storefront region and language.

Mitigation: Pass country and language parameters where supported when results need to match a specific storefront.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/gaming-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Steam pricing and availability can vary by country and language parameters.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
