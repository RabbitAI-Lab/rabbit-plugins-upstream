## Description:

Researches homes and used cars via the Crawlora API -- Zillow and Redfin property search, estimates, and market trends, plus CarMax, Autotrader, Cars.com, and Rightmove listing research -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to search public home and vehicle listings, compare properties or cars, retrieve listing and dealer details, and check market or valuation signals through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and listing identifiers are sent to Crawlora with the user's Crawlora API key.

Mitigation: Use only intended search terms and listing identifiers, keep CRAWLORA_API_KEY in the environment, and do not hardcode, commit, or place the key in command arguments.

Risk: The packaged endpoint reference includes Rightmove routes that are not named in the main description.

Mitigation: Review Rightmove endpoint behavior in reference/endpoints.md before using those routes.

Risk: Real-estate estimates, market trends, and vehicle listing data may be incomplete, stale, or unsuitable as professional advice.

Mitigation: Treat returned public listing data as research input and verify important financial, real-estate, vehicle-history, or purchasing decisions through authoritative sources and qualified professionals.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)
- [Skill release page](https://clawhub.ai/crawlora-org/skills/real-estate-autos-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from Crawlora API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment; helper requests are limited to documented GET routes.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
