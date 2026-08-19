## Description:

Filters and queries Etsy stores by sales, favorites, reviews, opening date, country, category, and Raving or star status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce analysts, and developers use this skill to find Etsy stores that match commercial filters and compare store performance signals. It also guides users through LinkFox API-key and credit setup when authentication or billing blocks a query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Etsy store-query parameters and an API key to LinkFox’s external service.

Mitigation: Install and run it only when use of LinkFox’s external service and API-key sharing are acceptable for the task.

Risk: The onboarding flow can request phone/SMS login details and generate an API token.

Mitigation: Prefer self-service setup on the official LinkFox site and avoid giving SMS codes to an agent unless the flow is understood and approved.

Risk: The billing flow can list paid plans and create unpaid payment orders for credits.

Mitigation: Require explicit user confirmation before selecting a plan or creating an order, and verify any payment QR code or URL before payment.

Risk: The service charges credits dynamically based on returned store count, so broad queries can consume more credits than expected.

Mitigation: Confirm filters, page size, and expected cost before running broad or paginated searches.

Risk: Full responses, cached responses, or QR images may be written to a local linkfox output/cache directory.

Mitigation: Review and delete local linkfox output or cache files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-store-query)
- [Etsy store query API reference](artifact/references/api.md)
- [Authentication and credits onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save full API responses, cached responses, or payment QR images under a local linkfox session directory; large responses may be summarized in the agent output.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
