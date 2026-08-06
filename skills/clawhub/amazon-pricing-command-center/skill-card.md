## Description: <br>
Data-driven pricing strategy engine for Amazon sellers that analyzes ASINs, auto-detects product categories, compares pricing signals, and returns RAISE/HOLD/LOWER guidance with profit simulation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to evaluate pricing strategy for one or more ASINs, compare market and competitor data, estimate profit scenarios, and decide whether to raise, hold, or lower prices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and sends Amazon product identifiers and pricing parameters to ZooData. <br>
Mitigation: Install and run it only when that data flow is acceptable, and keep credentials in the supported environment or local credential store. <br>
Risk: ASIN lists, pricing strategy, and cost inputs can be business-sensitive. <br>
Mitigation: Provide only the product and pricing inputs needed for the analysis, and avoid adding unrelated business-sensitive context. <br>
Risk: Broad or batch analyses consume ZooData credits and the bundled CLI includes broader research commands. <br>
Mitigation: Confirm estimated credit cost before broad or batch runs, and use only the commands needed for the pricing workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-pricing-command-center) <br>
- [Publisher Profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData API Field Reference](references/reference.md) <br>
- [ZooData CLI Contract](references/cli-contract.md) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData Pricing](https://zoodata.ai/en/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown pricing analysis with tables, confidence labels, data provenance, API usage, and recommended pricing actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; reports are based on ZooData API sampling and may include credit usage.] <br>

## Skill Version(s): <br>
1.1.7 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
