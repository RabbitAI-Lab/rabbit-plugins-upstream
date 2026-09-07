## Description:

Researches Bonhams auctions and lots via the Crawlora API — upcoming and past sales, lot search, estimates, realized prices, departments, and auction detail — returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and auction-market analysts use this skill to find Bonhams auctions, compare lots, inspect estimates and realized prices, and retrieve normalized sale and lot facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send authenticated Crawlora API requests beyond the Bonhams endpoints described by the skill.

Mitigation: Review requested paths before running the helper and use the skill only with Crawlora API access you are comfortable delegating.

Risk: Changing CRAWLORA_API_BASE can redirect the API key to a different destination.

Mitigation: Leave CRAWLORA_API_BASE unset unless the replacement endpoint is deliberately trusted.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/auction-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for authenticated Crawlora API calls.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
