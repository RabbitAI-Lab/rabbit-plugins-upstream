## Description:

Researches public video game store data through the Crawlora API, including Steam pricing, reviews, player counts, charts, tags, achievements, PlayStation Store products and deals, and public Roblox lookup endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer game research questions such as current prices, review summaries, player counts, trending titles, store listings, and sale availability from public storefront data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API keys and game lookup parameters are sent to Crawlora.

Mitigation: Store the API key only in CRAWLORA_API_KEY, avoid committing it, and review whether lookup terms are appropriate to share with the API provider.

Risk: The top-level description emphasizes Steam and PlayStation, while the bundled endpoint set also includes public Roblox lookups.

Mitigation: Review the endpoint reference before use and align user-facing descriptions with the full platform scope.

Risk: Steam pricing and availability can vary by storefront region and language.

Mitigation: Pass supported country and language parameters when results need to match a specific storefront.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/gaming-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API key signup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; responses contain public game store data and may vary by country and language parameters.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
