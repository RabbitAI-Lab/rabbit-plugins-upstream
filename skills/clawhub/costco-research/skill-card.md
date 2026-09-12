## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping researchers use this skill to find Costco products, compare public product details, check US delivery availability, inspect reviews, and locate nearby warehouses through Crawlora instead of scraping Costco.com.

### Deployment Geography for Use:

United States for delivery availability; other public Costco research endpoints are not region-restricted in the artifact.

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends Costco search terms plus any ZIP/state or coordinates supplied by the user to Crawlora.

Mitigation: Use a scoped Crawlora key, keep it in CRAWLORA_API_KEY, avoid hardcoding or committing it, and send only the minimum location or search data needed for the task.

Risk: Evidence.security marks the release suspicious because the helper can make authenticated POST calls and reach broader Costco route patterns than the documented read-only endpoints.

Mitigation: Review the helper before sensitive or automated use and restrict operation to the documented GET endpoints in reference/endpoints.md.

Risk: Costco availability checks are US-only and require a ZIP code plus two-letter state code.

Mitigation: Confirm the user is asking for US delivery availability and avoid presenting availability results as valid for non-US destinations.

## Reference(s):

- [costco-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/costco-research)
- [ClawHub publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; Crawlora responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and may use Costco product IDs, search terms, ZIP/state pairs, or latitude/longitude coordinates.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
