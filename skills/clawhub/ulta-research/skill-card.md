## Description:

Researches Ulta Beauty's catalog, including categories, products, shades, questions, reviews, and nearby stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and retail research agents use this skill to search and browse public Ulta Beauty catalog data, inspect product details, summarize customer Q&A and reviews, compare shades, and find nearby stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use CRAWLORA_API_KEY for broader requests than the Ulta-only purpose describes.

Mitigation: Audit helper invocations, keep requests pinned to https://api.crawlora.net/api/v1, and restrict routine use to /ulta/ endpoints.

Risk: Setting CRAWLORA_API_BASE can direct authenticated requests to a destination outside the documented Crawlora API base.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is fully trusted, and rotate the Crawlora key if it may have been sent to an untrusted host.

Risk: The skill depends on a user-provided Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY; do not hardcode it, pass it in query parameters, or commit it.

## Reference(s):

- [Ulta Research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ulta-research)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Ulta Beauty data returned by Crawlora.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
