## Description:

Amazon-domain general analysis and multi-endpoint research engine for broad or composite Amazon market and product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and developers use this skill to run Amazon market, product, competitor, pricing, review, and category research through ZooData-backed workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a ZooData API key and paid API calls, so broad or ambiguous requests may spend credits unintentionally.

Mitigation: Use explicit Amazon, ASIN, category, or marketplace context and confirm estimated credit cost before multi-call scans.

Risk: Persistent credential storage can increase exposure if the local environment is shared or compromised.

Mitigation: Prefer ZOODATA_API_KEY in the environment over a home-directory config, and rely on the skill's trusted-host checks before sending credentials.

Risk: Sampled marketplace data and broad routing can produce incomplete or misleading seller guidance if treated as definitive.

Mitigation: Keep the required data-source, API-usage, and confidence-label sections in reports, and validate business decisions with additional sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-analysis)
- [ZooData-Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData](https://zoodata.ai)
- [ZooData OpenAPI reference](https://api.zoodata.ai/openapi/v2)
- [ZooData CLI Contract](references/cli-contract.md)
- [Execution Guide](references/execution-guide.md)
- [ZooData API Field Reference](references/reference.md)
- [Amazon Seller Comprehensive Analysis & Case Studies](references/scenarios-composite.md)
- [Amazon Product Evaluation & Risk Assessment](references/scenarios-eval.md)
- [Amazon Product Expansion & Market Trends](references/scenarios-expand.md)
- [Amazon Listing Optimization & Content Creation](references/scenarios-listing.md)
- [Amazon Seller Daily Operations & Monitoring](references/scenarios-ops.md)
- [Amazon Pricing Strategy & Profit Estimation](references/scenarios-pricing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with data-source, API-usage, confidence-label, and recommendation sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tables; requires ZOODATA_API_KEY and consumes ZooData credits.]

## Skill Version(s):

1.1.13 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
