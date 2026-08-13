## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search eBay listings, inspect item details, and review public seller reputation or shop data through Crawlora instead of scraping eBay pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can call arbitrary Crawlora API paths, not only the documented eBay endpoints.

Mitigation: Review the helper before installation and restrict calls to the documented /ebay endpoints when broader Crawlora access is not intended.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Provide CRAWLORA_API_KEY through the environment only, and do not hardcode, commit, or pass the key in URLs.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled helper prints raw JSON from Crawlora endpoints and expects CRAWLORA_API_KEY to be supplied through the environment.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
