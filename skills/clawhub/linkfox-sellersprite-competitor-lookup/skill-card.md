## Description:

This skill helps Amazon sellers query SellerSprite competitor data across 12 marketplaces, including sales, BSR, pricing, ratings, and growth trend metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to discover competing products, benchmark ASINs, brands, sellers, and categories, and review market metrics before making commercial decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads API keys from environment variables and sends competitor lookup requests to LinkFox services.

Mitigation: Install only when the user is comfortable with the LinkFox/SellerSprite integration, review environment variables before use, and avoid endpoint overrides unless the endpoint is controlled.

Risk: The skill can write full API responses locally, which may include sensitive business queries or competitive research data.

Mitigation: Review saved response files before sharing a workspace, and avoid sending sensitive business or conversation details through feedback without explicit consent.

Risk: The onboarding flow can help create or retrieve API credentials through SMS login and guide payment order creation for credits.

Mitigation: Prefer self-service account setup on the official site and manually review billing actions before proceeding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-competitor-lookup)
- [SellerSprite Competitor Lookup API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown summaries with saved JSON response files and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries can consume LinkFox credits; full API responses are written under the current workspace and may be summarized on stdout when large.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
