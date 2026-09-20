## Description:

Researches Bonhams auctions and lots via the Crawlora API, including upcoming and past sales, lot search, estimates, realized prices, departments, and auction detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to query Bonhams public auction and lot data for sale calendars, comparable lots, estimates, realized prices, departments, and auction details through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auction research queries and the Crawlora API key are sent to Crawlora as a third-party API provider.

Mitigation: Treat CRAWLORA_API_KEY as a secret, avoid pasting it into chats or logs, and do not use the skill for confidential or unrelated searches.

Risk: A user may try to call unrelated Crawlora routes or send unsupported request methods through the helper.

Mitigation: Use only the documented Bonhams GET routes; the bundled helper rejects unsupported methods, invalid paths, and routes outside the auction-research catalog.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples; helper responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses fixed Crawlora GET endpoints for Bonhams auction and lot data.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
