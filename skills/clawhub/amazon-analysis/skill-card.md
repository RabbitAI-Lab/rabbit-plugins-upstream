## Description: <br>
Amazon Analysis supports Amazon product, market, competitor, ASIN, pricing, category, and seller-intelligence research through ZooData-powered workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Amazon marketplace research, compare products and competitors, evaluate ASINs, explore pricing bands, and generate seller-oriented analysis reports from ZooData API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon research inputs such as keywords, categories, ASINs, dates, and filters are sent to ZooData. <br>
Mitigation: Avoid confidential product ideas unless third-party data sharing with ZooData is acceptable. <br>
Risk: ZooData API calls consume account credits, especially broad or composite research workflows. <br>
Mitigation: Use explicit Amazon, FBA, or product-research prompts and confirm expected credit cost before multi-call scans. <br>
Risk: Generated marketplace analysis may be incomplete or misleading if used as the sole basis for business decisions. <br>
Mitigation: Treat reports as reference material and validate important decisions with additional data sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API field reference](references/reference.md) <br>
- [Execution guide](references/execution-guide.md) <br>
- [ZooData CLI contract](references/cli-contract.md) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData pricing](https://zoodata.ai/en/pricing) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API base](https://api.zoodata.ai/openapi/v2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis reports with API usage tables, data provenance notes, confidence labels, and optional shell command snippets for setup or diagnostics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; broad or composite workflows consume ZooData API credits and may share Amazon research inputs with ZooData.] <br>

## Skill Version(s): <br>
1.1.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
