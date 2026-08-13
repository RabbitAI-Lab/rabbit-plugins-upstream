## Description:

Researches software and SaaS products, business reputation, verified startup revenue, and product reviews through Crawlora API endpoints for Product Hunt, Trustpilot, TrustMRR, and Capterra, returning clean JSON for launch history, reviews, alternatives, and vendor due diligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and procurement teams use this skill to query public launch, reputation, revenue, and review data before evaluating, buying, partnering with, or comparing software and SaaS products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send authenticated requests to arbitrary Crawlora API paths or to an overridden API host.

Mitigation: Use a scoped, rotatable Crawlora API key, keep the default Crawlora API host unless reviewed, and restrict use to documented read-only endpoints when strict outbound control is required.

Risk: Business-intelligence queries may disclose sensitive internal project names, vendor lists, or due-diligence targets to the Crawlora API.

Mitigation: Avoid sensitive internal names and confidential vendor lists in queries; sanitize inputs before running API requests.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls; API results are paginated for review and listing endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
