## Description:

Searches 1688 by product image to help cross-border sellers find visually similar supplier listings with sourcing data such as price, minimum order quantity, sales, repurchase rate, trade score, and supplier badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and sourcing agents use this skill to find same-style or visually similar 1688 supplier products from a public image URL, uploaded local image, base64 image, or prior 1688 image ID. It supports filtered and sorted sourcing workflows where the agent returns structured product data and guidance for pagination or authentication issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox may receive image URLs or uploaded images, search parameters, API credentials, and possible onboarding or payment information.

Mitigation: Use the skill only when that data sharing is acceptable; review the configured LinkFox gateway URL and provide phone numbers, SMS codes, or payment actions only when intentionally starting those flows.

Risk: Search responses and cached results may be persisted in local linkfox folders, which can expose sensitive sourcing data on shared machines.

Mitigation: Review and periodically delete local linkfox response and cache folders when the product or supplier data is sensitive.

Risk: The skill consumes credits for 1688 searches and includes onboarding and billing flows.

Mitigation: Confirm the expected credit cost before repeated calls, avoid automatic retry loops, and require user approval before purchase or recharge actions.

## Reference(s):

- [1688-以图搜图 API reference](references/api.md)
- [Authentication and billing onboarding guidance](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-search-by-image)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON product-search results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The search script writes full responses to local JSON files, prints small responses inline, summarizes large responses, and may cache repeated parameter combinations for 24 hours.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
