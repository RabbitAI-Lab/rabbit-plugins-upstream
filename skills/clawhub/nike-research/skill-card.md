## Description:

Researches Nike's catalog, including categories, search results, product detail, colorways, reviews, and nearby stores, through the Crawlora API and returns normalized JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Nike catalog questions, compare products and colorways, summarize reviews, and locate nearby Nike stores without scraping Nike pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nike search terms, product identifiers, and store-location coordinates are sent to Crawlora.

Mitigation: Use the skill only when sharing those queries with Crawlora is acceptable, and avoid unnecessary sensitive inputs.

Risk: The helper script can send the API key to a destination selected through CRAWLORA_API_BASE.

Mitigation: Leave CRAWLORA_API_BASE unset unless the alternate destination is intentionally trusted.

Risk: The helper script can call non-Nike Crawlora paths even though the skill purpose is Nike catalog research.

Mitigation: Limit execution to the documented /nike endpoints and review generated shell commands before running them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/nike-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
