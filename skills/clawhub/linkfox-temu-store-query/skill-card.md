## Description:

Filters and analyzes Temu stores by name or ID, country site, category, fulfillment mode, sales, revenue, rating, reviews, followers, product count, opening date, and sorting options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce analysts, and developers use this skill to query and compare Temu store performance through LinkFox using filters for sales, revenue, ratings, categories, fulfillment mode, and listing dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Temu query data and API-key-authenticated requests to LinkFox services.

Mitigation: Install only if you trust LinkFox, use the default LinkFox endpoints, and avoid custom LINKFOX_* endpoint variables unless you control the destination.

Risk: Onboarding can collect a Chinese phone number and SMS code, issue an API key, and create payment orders when a plan is selected.

Mitigation: Use onboarding only when needed, review the LinkFox agreements and pricing first, and confirm the plan and payment method before creating an order.

Risk: Full query results may be saved locally.

Mitigation: Run the skill in an appropriate workspace and review or remove saved JSON files when results may contain sensitive business data.

## Reference(s):

- [Temu store query API reference](references/api.md)
- [Authentication and billing onboarding guide](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-store-query)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON results with Markdown guidance and optional shell commands; large responses are summarized and saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; full query responses are saved locally and larger responses are summarized in stdout.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
