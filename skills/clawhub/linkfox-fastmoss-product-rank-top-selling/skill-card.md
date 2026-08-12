## Description:

Queries FastMoss data for TikTok Shop top-selling product rankings across supported global markets, with daily, weekly, monthly, and category-level views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and market analysts use this skill to retrieve TikTok Shop best-seller rankings from FastMoss for product scouting, trend monitoring, and category-level competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles FastMoss queries, API keys, phone-based onboarding data, and billing actions through LinkFox services.

Mitigation: Install and use it only after confirming the user trusts LinkFox for these data flows and explicitly approves onboarding or billing steps.

Risk: Environment variables can redirect LinkFox endpoint hosts.

Mitigation: Verify endpoint-related environment variables resolve to legitimate LinkFox hosts before running API, onboarding, or billing commands.

Risk: API responses and cache files are persisted locally under a linkfox directory.

Mitigation: Treat saved response, cache, and shell-profile API key files as sensitive data and avoid sharing or committing them.

Risk: The artifact includes automatic feedback-reporting behavior.

Mitigation: Submit feedback only with the user's explicit consent and avoid including sensitive query details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-rank-top-selling)
- [FastMoss top-selling API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox tool gateway endpoint](https://tool-gateway.linkfox.com/fastmoss/productRankTopSelling)

## Skill Output:

**Output Type(s):** [API Calls, Files, Shell commands, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query/result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses and cache files under a local linkfox directory; prints full JSON for small responses or summaries for larger responses unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
