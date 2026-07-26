## Description: <br>
Provides Amazon Store Customer Feedback insights through LinkFox-mediated SP-API Customer Feedback v2024-06-01 calls for item review topics, item browse nodes, review trends, browse node review topics, browse node review trends, return topics, and return trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, ecommerce analysts, and agent operators use this skill to retrieve customer feedback, review trend, browse node, and return-topic data for ASINs or browse nodes through LinkFox-authenticated Amazon SP-API workflows. <br>

### Deployment Geography for Use: <br>
Global, subject to Amazon SP-API marketplace, role, and account availability. <br>

## Known Risks and Mitigations: <br>
Risk: Amazon seller feedback data is sent through LinkFox and full API responses are saved locally. <br>
Mitigation: Run the skill only with intended seller accounts and avoid synced, shared, or repository directories unless saved linkfox data can be managed or deleted. <br>
Risk: The security review reports contradictory credit-cost guidance in the artifact. <br>
Mitigation: Treat calls as potentially billable until the publisher resolves the credit guidance, and confirm expected cost before repeated or exploratory calls. <br>
Risk: The security verdict is suspicious because of local data persistence and cost-guidance ambiguity. <br>
Mitigation: Review the security summary and guidance before deployment, then restrict use to environments where local response files and credentials are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-customer-feedback) <br>
- [Local API reference](references/api.md) <br>
- [Amazon Customer Feedback API use case guide](https://developer-docs.amazon.com/sp-api/docs/customer-feedback-api-v2024-06-01-use-case-guide) <br>
- [getItemReviewTopics](https://developer-docs.amazon.com/sp-api/reference/getitemreviewtopics) <br>
- [getItemBrowseNode](https://developer-docs.amazon.com/sp-api/reference/getitembrowsenode) <br>
- [getBrowseNodeReviewTopics](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereviewtopics) <br>
- [getItemReviewTrends](https://developer-docs.amazon.com/sp-api/reference/getitemreviewtrends) <br>
- [getBrowseNodeReviewTrends](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereviewtrends) <br>
- [getBrowseNodeReturnTopics](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereturntopics) <br>
- [getBrowseNodeReturnTrends](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereturntrends) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; scripts write JSON response files and print JSON or summaries to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API key environment configuration and the companion linkfox-amazon-store-auth skill; full API responses are saved under a local linkfox data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
