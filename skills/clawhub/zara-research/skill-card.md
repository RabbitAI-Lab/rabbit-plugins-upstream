## Description:

Researches Zara's catalog by retrieving category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, shopping assistants, and research agents use this skill to browse Zara categories, search for products, inspect product variants and stock details, and find nearby Zara stores without scraping Zara pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can forward CRAWLORA_API_KEY to a host selected through CRAWLORA_API_BASE.

Mitigation: Run the skill in a clean environment with CRAWLORA_API_BASE unset or pinned to a trusted Crawlora origin, and treat the API key as a real credential.

Risk: The helper accepts broader request paths and methods than the Zara-only purpose requires.

Mitigation: Before broad use, restrict helper calls to the documented Zara GET endpoints or review each command before execution.

## Reference(s):

- [Zara endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zara-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on public Zara catalog and store data returned by Crawlora endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
