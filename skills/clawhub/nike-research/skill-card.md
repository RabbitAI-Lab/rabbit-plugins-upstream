## Description:

Researches Nike catalog categories, search results, product details, colorways, reviews, and nearby stores through the Crawlora API and returns clean JSON for product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Nike catalog data, compare product options, summarize product reviews, and find nearby stores without scraping Nike pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send arbitrary paths and data through Crawlora rather than being limited to documented Nike endpoints.

Mitigation: Review command paths before execution and restrict use to the documented /nike endpoints until the script is narrowed.

Risk: Nike search terms, product identifiers, and store lookup coordinates are sent to Crawlora.

Mitigation: Avoid secrets, unrelated personal data, and sensitive locations in queries; use only data that is appropriate to disclose to Crawlora.

Risk: CRAWLORA_API_BASE can redirect requests away from the documented API base.

Mitigation: Validate or remove CRAWLORA_API_BASE before treating the skill as tightly scoped to Nike research.

## Reference(s):

- [nike-research endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/nike-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests; Nike search, product, review, and store results are paginated where documented.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
