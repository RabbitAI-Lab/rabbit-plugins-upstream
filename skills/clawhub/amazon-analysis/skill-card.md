## Description: <br>
Amazon-domain general analysis and multi-endpoint research engine for broad or composite Amazon market, product, competitor, pricing, and ASIN research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Amazon seller research workflows, including market analysis, product selection, competitor comparison, ASIN evaluation, pricing reference, and category exploration through ZooData-backed data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon research terms, ASINs, category paths, marketplace and date filters, and numeric filter values to ZooData under the user's API key. <br>
Mitigation: Install only when that data sharing is acceptable, and avoid including sensitive business context beyond the required research inputs. <br>
Risk: The skill requires ZOODATA_API_KEY and can read an optional local ZooData credential store. <br>
Mitigation: Prefer setting ZOODATA_API_KEY as an environment variable or protected secret instead of storing credentials in a local config file. <br>
Risk: Broad or ambiguous scans can consume ZooData account credits. <br>
Mitigation: Review estimated credit costs and confirm before running multi-call scans. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-analysis) <br>
- [Project homepage from artifact metadata](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API Field Reference](references/reference.md) <br>
- [Execution Guide - Complete Protocols](references/execution-guide.md) <br>
- [Amazon Seller Comprehensive Analysis & Case Studies](references/scenarios-composite.md) <br>
- [Amazon Product Evaluation & Risk Assessment](references/scenarios-eval.md) <br>
- [Amazon Pricing Strategy & Profit Estimation](references/scenarios-pricing.md) <br>
- [Amazon Listing Optimization & Content Creation](references/scenarios-listing.md) <br>
- [Amazon Seller Daily Operations & Monitoring](references/scenarios-ops.md) <br>
- [Amazon Product Expansion & Market Trends](references/scenarios-expand.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown reports with data provenance, API usage summaries, confidence labels, and inline shell commands when execution is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; broad scans consume ZooData credits and may require user confirmation before multi-call workflows.] <br>

## Skill Version(s): <br>
1.1.11 (source: server release metadata; artifact metadata reports 1.1.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
