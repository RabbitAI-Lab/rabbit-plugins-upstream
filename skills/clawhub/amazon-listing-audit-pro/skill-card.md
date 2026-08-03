## Description: <br>
Comprehensive listing health check and optimization engine for Amazon sellers that scores listings across 8 dimensions, benchmarks against category leaders, identifies keyword gaps, and generates data-backed improvement recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, agencies, and ecommerce operators use this skill to audit a single ASIN or bulk listing set, compare listings with category leaders, find keyword and content gaps, and prioritize listing improvements. It requires a ZooData API key and produces an analysis report based on ZooData product, market, review, and pricing data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon ASINs, keywords, categories, marketplace and date filters, numeric filters, and review-derived research data to ZooData under the user's API key. <br>
Mitigation: Use it only for product research data the user is comfortable sharing with ZooData, and keep unrelated business-sensitive profile text out of prompts and API inputs. <br>
Risk: Multi-call audits consume ZooData account credits, and the composite listing-audit workflow can use about 15-20 credits for one ASIN. <br>
Mitigation: Estimate credit cost and get confirmation before broad, ambiguous, bulk, or multi-call scans; use granular commands when a credit cap matters. <br>
Risk: The review fallback can create temporary review working files under /tmp and may read an optional local ZooData credential store. <br>
Mitigation: Store the API key in an environment variable or protected home config, and delete temporary review files after use when they are no longer needed. <br>


## Reference(s): <br>
- [Amazon Listing Audit Pro on ClawHub](https://clawhub.ai/apiclaw/skills/amazon-listing-audit-pro) <br>
- [Listing Audit Pro API Field Reference](artifact/references/reference.md) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with scorecards, comparison tables, data provenance, API usage, and inline shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; outputs should match the user's language and include confidence labels, data provenance, API usage, and the required business-decision disclaimer.] <br>

## Skill Version(s): <br>
1.0.6 (source: server evidence release.version and skill metadata version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
