## Description:

Researches OpenSea NFT collections, items, marketplace activity, listings, offers, traits, categories, chains, and creator profiles via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to inspect public OpenSea marketplace data, compare collection activity, research NFT items and traits, and review creator or wallet profile footprints through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenSea lookup terms, collection slugs, contract addresses, token IDs, and wallet or profile identifiers are sent to Crawlora.

Mitigation: Use the skill only when sharing those lookup values with Crawlora is acceptable, and treat wallet or profile lookups as potentially sensitive.

Risk: The helper requires a Crawlora API key.

Mitigation: Provide the key through CRAWLORA_API_KEY, avoid exposing it in prompts or logs, and review generated shell commands before execution.

## Reference(s):

- [OpenSea Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/opensea-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested OpenSea lookup terms, collection slugs, contract addresses, token IDs, and wallet or profile identifiers to Crawlora.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
