## Description:

Researches Bonhams auctions and lots via the Crawlora API for upcoming and past sales, lot search, estimates, realized prices, departments, and auction detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and auction-market analysts use this skill to search Bonhams sale calendars and historical lots, compare public estimates and realized prices, and retrieve normalized auction or lot facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API helper may use a user's Crawlora key for broader Bonhams API requests than the documentation describes.

Mitigation: Review the helper before installing, use a limited Crawlora API key, and restrict execution to the documented Bonhams GET route forms.

Risk: Auction research queries may include confidential client or business terms.

Mitigation: Avoid sending confidential terms in queries and treat returned auction and lot data as public research context requiring user review.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Bonhams auction and lot endpoints.]

## Skill Version(s):

1.0.8 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
