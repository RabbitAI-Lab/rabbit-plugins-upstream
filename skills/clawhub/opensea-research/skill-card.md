## Description:

Researches OpenSea NFT collections, items, marketplace activity, listings, offers, traits, categories, chains, and creator profiles via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and analysts use this skill to query public OpenSea marketplace data through Crawlora for collection and item discovery, marketplace activity comparison, listings, offers, sales analysis, and creator research without scraping pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can make broad authenticated Crawlora requests beyond the OpenSea endpoints described by the skill.

Mitigation: Review commands before execution and prefer limiting helper usage to /opensea paths.

Risk: The helper supports overriding the API base, which could send the Crawlora API key to an unintended endpoint.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is explicitly trusted.

Risk: Requests require a Crawlora API key and send query inputs to an external API.

Mitigation: Avoid sending secrets or private wallet research inputs, and confirm external data handling requirements before use.

## Reference(s):

- [OpenSea endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY. The bundled helper sends authenticated Crawlora API requests and prints raw JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
