## Description:

Researches video games via the Crawlora API - Steam store pages, pricing, reviews, player counts, charts, tags, achievements, and PlayStation Store products, categories, and deals - returning clean JSON for game research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research video game listings, prices, reviews, player counts, trending titles, deals, tags, and platform-specific store metadata from public Steam, PlayStation Store, and Roblox surfaces exposed through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated helper calls can send arbitrary POST bodies to Crawlora.

Mitigation: Review POST bodies before execution and use a Crawlora API key suitable for the account sensitivity and expected usage.

Risk: The endpoint surface includes Roblox lookups that are not prominent in the main skill description.

Mitigation: Check the endpoint reference before use and limit calls to the public game-research routes needed for the task.

Risk: A Crawlora API key is required for all helper calls.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid committing it, and rotate the key if it may have been exposed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Steam pricing and availability can vary by country code and language parameters.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
