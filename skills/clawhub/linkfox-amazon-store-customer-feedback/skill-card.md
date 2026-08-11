## Description:

Helps agents retrieve Amazon SP-API Customer Feedback review topics, review trends, browse-node mappings, and return feedback insights for Amazon store items and browse nodes through LinkFox scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators, and analysts use this skill to inspect customer feedback topics, review trends, browse-node context, and return feedback for selected ASINs or browse nodes. It depends on the companion LinkFox Amazon store auth skill for store selection and authenticated access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon seller feedback data, LinkFox API keys, phone-based account onboarding, and API-key issuance.

Mitigation: Install only in trusted environments, keep API keys private, avoid sharing stdout logs that may contain keys, and protect or delete saved LinkFox response files that contain sensitive business data.

Risk: Billing remediation can list paid plans and create payment orders through LinkFox.

Mitigation: Confirm the real billing behavior and get explicit user approval before order creation or payment actions.

Risk: API base URL environment variables can redirect LinkFox gateway, login, or agent-user requests.

Mitigation: Leave base URL override variables unset unless intentionally testing in a controlled environment.

Risk: The skill depends on a separate LinkFox auth skill and Amazon role or marketplace support; repeated failed or empty calls may create avoidable operational cost.

Mitigation: Verify the auth dependency, seller role, marketplace support, and request parameters before retrying or expanding calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-customer-feedback)
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Local API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Amazon SP-API Customer Feedback API guide](https://developer-docs.amazon.com/sp-api/docs/customer-feedback-api-v2024-06-01-use-case-guide)
- [Amazon getItemReviewTopics reference](https://developer-docs.amazon.com/sp-api/reference/getitemreviewtopics)
- [Amazon getItemBrowseNode reference](https://developer-docs.amazon.com/sp-api/reference/getitembrowsenode)
- [Amazon getBrowseNodeReviewTopics reference](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereviewtopics)
- [Amazon getItemReviewTrends reference](https://developer-docs.amazon.com/sp-api/reference/getitemreviewtrends)
- [Amazon getBrowseNodeReviewTrends reference](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereviewtrends)
- [Amazon getBrowseNodeReturnTopics reference](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereturntopics)
- [Amazon getBrowseNodeReturnTrends reference](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereturntrends)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON responses saved to local files with stdout summaries or full inline JSON, plus Markdown-style guidance for authentication and billing setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under linkfox/<date>/<session>/data; responses up to 8 KB are printed in full, larger responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
