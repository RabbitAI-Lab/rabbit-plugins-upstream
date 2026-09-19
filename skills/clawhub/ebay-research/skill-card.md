## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search eBay listings, inspect item details, and evaluate public seller profiles, feedback, and shop listings through Crawlora instead of scraping eBay pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and the eBay search terms, item IDs, seller names, and request bodies submitted through this skill.

Mitigation: Install only if Crawlora is an acceptable third-party API provider and avoid sending unrelated private data in requests.

Risk: API keys can be exposed if copied into prompts, URLs, command histories, or committed files.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, commit, or pass it as a query parameter.

Risk: Seller feedback and shop results are paginated, so single-page requests may omit relevant public eBay data.

Mitigation: Use the documented page and per_page parameters when broader feedback or shop coverage is needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/ebay-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested eBay lookup inputs to Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
