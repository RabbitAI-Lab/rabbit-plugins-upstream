## Description:

Researches Lululemon catalog navigation, category listings, product details, reviews, outfit recommendations, and store locations through the Crawlora API, returning normalized JSON instead of scraped HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to browse Lululemon categories, inspect product prices, sizes, colors, availability, and reviews, retrieve styled outfit recommendations, and locate nearby stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Lululemon lookup requests to Crawlora as a third-party API provider.

Mitigation: Install only when that third-party API use is acceptable for the intended workflow, and avoid sending secrets or unrelated personal data in requests.

Risk: The helper requires a Crawlora API key.

Mitigation: Set CRAWLORA_API_KEY in the environment and do not hardcode, commit, or pass the key in query parameters.

Risk: The security guidance notes least-privilege cleanup that may be advisable in stricter environments.

Mitigation: Consider restricting the helper to GET-only and adding curl -q before use where stricter curl configuration isolation is required.

## Reference(s):

- [lululemon-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/lululemon-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; helper output is raw JSON suitable for jq or downstream agent processing.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
