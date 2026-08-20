## Description:

Researches video games via the Crawlora API - Steam store pages, pricing, reviews, player counts, charts, tags, and achievements, plus PlayStation Store products, categories, and deals - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and gaming-focused agents use this skill to look up game listings, prices, reviews, player counts, charts, tags, achievements, and current deals across Steam and PlayStation Store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use the user's Crawlora API key to call unrelated Crawlora routes beyond the Steam and PlayStation routes described by the skill.

Mitigation: Review commands before execution, restrict or replace the helper so it only calls Steam and PlayStation routes, avoid sending sensitive local data in request bodies, and monitor Crawlora key usage or credits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tonywangcn/skills/gaming-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a CRAWLORA_API_KEY environment variable and produces normalized public Steam and PlayStation Store data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
