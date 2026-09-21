## Description:

Researches software/SaaS products, business reputation, and crowdfunding campaigns via the Crawlora API, covering Product Hunt, Trustpilot, TrustMRR, Capterra, BBB, and Kickstarter, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill for product, vendor, local-business, startup-revenue, software-review, and crowdfunding due diligence across public review and listing sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Crawlora API keys and business, product, vendor, or campaign search queries to a third-party API.

Mitigation: Use only approved Crawlora API credentials, keep the key in CRAWLORA_API_KEY, and avoid confidential company names or vendor information unless that third-party API use is acceptable.

Risk: Bulk paging or review collection can create rate-limit or terms-of-use concerns.

Mitigation: Limit pagination to the user need, respect Crawlora and upstream platform terms, and avoid broad collection where a focused lookup is sufficient.

Risk: Business ratings, reviews, complaints, revenue, and campaign data may be incomplete, stale, or source-biased.

Mitigation: Treat API results as research inputs and cross-check material decisions against primary business, platform, or contractual sources.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends public business, product, review, and campaign queries to the Crawlora API.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
