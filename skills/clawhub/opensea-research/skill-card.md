## Description:

Researches OpenSea NFT collections, items, marketplace activity, listings, offers, traits, categories, chains, and creator profiles via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect public OpenSea marketplace data, compare NFT collection activity, resolve valid filters, and retrieve collection, item, listing, offer, sales, trait, chain, category, and creator profile data as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make authenticated Crawlora API calls beyond the advertised OpenSea research scope.

Mitigation: Constrain calls to documented OpenSea endpoints unless the user and publisher explicitly authorize broader Crawlora API use.

Risk: The skill requires a Crawlora API key and may submit wallet, ENS, OpenSea username, collection, contract, or token identifiers to the Crawlora API.

Mitigation: Use only an API key suitable for this helper and avoid submitting sensitive wallet or profile identifiers unless they are necessary for the task.

## Reference(s):

- [OpenSea endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; API responses are raw JSON printed to stdout.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
