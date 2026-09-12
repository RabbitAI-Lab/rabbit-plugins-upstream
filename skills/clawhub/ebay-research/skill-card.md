## Description:

Researches eBay listings, items, and sellers using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to search eBay listings, inspect item details, and assess public seller reputation or shop inventory without scraping eBay pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated helper accepts broader Crawlora eBay paths and HTTP method combinations than the documented endpoint catalog.

Mitigation: Use a Crawlora key with limited credits, invoke only documented eBay endpoints, and prefer a hardened helper that binds each endpoint to its exact HTTP method and rejects extra path segments.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/ebay-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized public eBay listing, item, seller, feedback, and shop data.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
