## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to search eBay listings, inspect item details, and review public seller reputation or shop listings through Crawlora instead of scraping eBay pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths beyond the documented eBay endpoints, creating overbroad external access.

Mitigation: Review the script before installation, restrict use to documented /ebay endpoints, and avoid sending secrets, private business data, or unrelated prompts to Crawlora.

## Reference(s):

- [eBay endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ebay-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized public eBay listing, item, seller, feedback, shop, and live stream data.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
