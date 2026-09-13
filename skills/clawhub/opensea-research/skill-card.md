## Description:

Researches OpenSea NFT collections, items, marketplace activity, listings, offers, traits, categories, chains, and creator profiles via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and market researchers use this skill to inspect public OpenSea collection, item, activity, listing, offer, trait, category, chain, and creator-profile data through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a real Crawlora API key and may query wallet, profile, collection, or marketplace identifiers.

Mitigation: Review planned requests before execution, avoid unnecessary identifiers, and use an appropriately scoped Crawlora API key.

Risk: Server security evidence says the helper can send authenticated requests to broader Crawlora paths and methods than the documented endpoint catalog describes.

Mitigation: Restrict use to documented OpenSea endpoint shapes and HTTP methods, and review the helper before using it in sensitive or untrusted-agent workflows.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora account and API key](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for authenticated Crawlora API requests.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
